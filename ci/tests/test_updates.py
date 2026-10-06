import base64
import hashlib
import json
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import update_feed as f
import upstream
from teleru_overlay import replace_constant


class UpdateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.key = Ed25519PrivateKey.generate()
        self.pem = self.key.private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8, serialization.NoEncryption()).decode()
        self.pub = self.root / 'public.pem'
        self.pub.write_bytes(self.key.public_key().public_bytes(serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo))

    def tearDown(self):
        self.temp.cleanup()

    def test_signed_feed_verifies_and_tamper_fails(self):
        envelope = f.sign_feed({'counter': 2}, self.pem, self.pub)
        signature = base64.b64decode(envelope['signature'])
        self.key.public_key().verify(signature, base64.b64decode(envelope['feed']))
        with self.assertRaises(InvalidSignature):
            self.key.public_key().verify(signature, b'{"counter":3}')

    def test_wrong_key_fails(self):
        other = Ed25519PrivateKey.generate().private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8, serialization.NoEncryption()).decode()
        with self.assertRaises(ValueError):
            f.sign_feed({}, other, self.pub)

    def test_archive_hash_and_legacy_migration(self):
        tag = 'v7.2.9-tele.2'
        file = self.root / f'tele-{tag}-win64.zip'
        with zipfile.ZipFile(file, 'w') as archive:
            archive.writestr('tele.exe', b'test executable')
        signer = f.sign_feed
        with patch.object(f, 'sign_feed', side_effect=lambda data, pem: signer(data, pem, self.pub)):
            paths = f.create_feeds(self.root, tag, 7002009, 2, 'Duerotator/teleru', self.pem, ['win64'], True)
        signed, legacy = [json.loads(p.read_text()) for p in paths]
        self.assertTrue(signed['signature'])
        self.assertEqual(legacy['signature'], '')
        self.assertEqual(signed['feed'], legacy['feed'])
        data = json.loads(base64.b64decode(signed['feed']))
        self.assertEqual(data['exe_sha256'], hashlib.sha256(b'test executable').hexdigest())
        self.assertEqual(data['zip_sha256'], hashlib.sha256(file.read_bytes()).hexdigest())
        self.assertIn('github.com/Duerotator/teleru/', data['url'])

    def test_mismatched_tag_counter_rejected(self):
        with self.assertRaises(ValueError):
            f.create_feeds(self.root, 'v7.2.9-tele.2', 7002009, 3, 'Duerotator/teleru', self.pem, ['win64'])

    def test_original_repository_rejected(self):
        with self.assertRaises(ValueError):
            f.create_feeds(self.root, 'v7.2.9-tele.2', 7002009, 2, 'nitreojs/tele', self.pem, ['win64'])

    def test_key_generation_refuses_overwrite(self):
        private = self.root / 'private.pem'
        f.generate(private, self.pub)
        with self.assertRaises(ValueError):
            f.generate(private, self.pub)

    def test_lock_requires_full_commit(self):
        data = dict(repository='nitreojs/tele', tag='v7.2.9-tele.17', commit='abc', tdesktop='v7.2.9')
        path = self.root / 'lock.json'
        path.write_text(json.dumps(data))
        with self.assertRaises(ValueError):
            upstream.read_lock(path)

    def test_current_lock_valid(self):
        data = upstream.read_lock()
        self.assertEqual(data['tag'].split('-tele.')[0], data['tdesktop'])
        self.assertEqual(len(data['commit']), 40)

    def test_metadata_replacement_requires_one_constant(self):
        self.assertEqual(replace_constant('constexpr auto kKey = "abc"\n"def";', 'kKey', 'ru'), 'constexpr auto kKey = "ru";')
        for text in ['', 'constexpr auto kKey="a"; constexpr auto kKey="b";']:
            with self.assertRaises(ValueError):
                replace_constant(text, 'kKey', 'ru')


if __name__ == '__main__':
    unittest.main()
