# tele server

tele can pull extra account data, like checkmarks, custom verification, scam / fake marks and support marks, from an optional server (settings → tele → server). it only ever downloads one public list and never tells the server which accounts you look at. the list is hashed, so it can't just be read off as a list of accounts. tele checks it every 10 minutes, and "refresh now" fetches it right away. leave the field empty to turn it off. "clear cached data" drops the list tele saved, so the marks disappear until the next fetch.

the same server takes crash reports. after a crash, tele offers to send the report: a short text with the version, platform and the crash reason, plus a minidump of the crashed process. you can look at it first and untick your username. tele also offers it when there's no dump, when the crash happened in another version, or after a graphics crash. with the server field empty, nothing is offered.

on windows and linux, tele also catches freezes: when the main thread is stuck for 15 seconds, a watchdog writes a minidump. next launch, tele says it froze last time and offers to send that report the same way.

the server can also post notices. they show up in the notification centre (main menu → notifications), and some also as a one-time toast. turn them off with settings → tele → server → notifications from the server. they need the notification centre on.

## running your own server

any server that serves the same format works: point settings → tele → server at it. the list never contains account ids, only keys that can't be turned back into ids without trying them one by one.

tele asks `GET <server>/v1/badges` and expects json like this:

```json
{
  "salt": "AAECAwQFBgcICQoLDA0ODw==",
  "argon2": { "memory": 8192, "passes": 1, "lanes": 1 },
  "peers": {
    "iguxbtP_SnLvK69aBff2OQ": { "checkmark": true, "icon": "5368324170671202286", "description": "official" },
    "w5Zbi-HfwlqkJ6S4wjwqcw": { "scam": true }
  }
}
```

- `salt` is 8 to 64 random bytes in standard base64 with padding.
- `argon2` are the argon2id costs: `memory` in KiB (1024 to 65536), `passes` (1 to 8), `lanes` (1 to 8), and `memory × passes` at most 65536. the official server uses 8192 / 1 / 1.
- each key in `peers` is `base64url` without padding of `argon2id(password, salt)` with those costs, a 16-byte output, version `0x13`, no secret and no associated data.
- the password is the utf-8 string `<scope>:<id>`:
  - `scope` is `prod`, or `test` for accounts on telegram's test servers;
  - `id` is the bot api style id: users as is (`777000`), channels and supergroups as `-100` followed by the channel id (`-1001234567890`). basic groups can't have entries.
- every field of an entry is optional: `checkmark`, `scam`, `fake` and `support` are booleans (false by default), `icon` is a custom emoji document id as a decimal string, `description` is plain text shown under the verification in the profile, and `supportText` (1 to 64 characters, users only) replaces the word "support" under the name of a support account. tele ignores fields it doesn't know, but rejects the whole list when a known field has the wrong type or length.

with the salt above, `prod:777000` gives `iguxbtP_SnLvK69aBff2OQ` and `prod:-1001234567890` gives `w5Zbi-HfwlqkJ6S4wjwqcw`. check your implementation against these two before anything else. in python:

```python
from argon2.low_level import hash_secret_raw, Type
import base64

raw = hash_secret_raw(b"prod:777000", bytes(range(16)), time_cost=1, memory_cost=8192,
                      parallelism=1, hash_len=16, type=Type.ID, version=0x13)
print(base64.urlsafe_b64encode(raw).rstrip(b"=").decode())  # iguxbtP_SnLvK69aBff2OQ
```

the list can also give accounts extra usernames. they're public anyway, so they come as plain text, in an optional `usernames` object next to `peers`:

```json
"usernames": {
  "tele": { "username": "teleAppUpdates", "position": 0 },
  "teleNews": { "username": "teleAppUpdates" }
}
```

- each key is the extra username, 2 to 32 latin letters, digits and underscores. `username` is the real public username of the account that gets it, 4 to 32 of them. both start with a letter and are compared ignoring case.
- `position` is optional: the place of the extra username among the account's usernames, counting from 0, so 0 makes it the main one in the profile. without it, the username goes after the real ones. a position past the end puts it last.
- tele skips a bad entry on its own and keeps the rest: a wrong name, an extra username equal to its account's username, the same key twice in different case, or a `position` that isn't a whole number from 0 to 1000. only the first 1000 good entries count. `usernames` never makes tele reject the list, and `salt`, `argon2` and `peers` are still required (`peers` can be empty).
- they only apply to accounts on telegram's main servers, not the test ones.

with settings → tele → usernames from the server on (the default), the profile of @teleAppUpdates shows @tele, and `@tele` in messages, `t.me/tele` and `tg://resolve?domain=tele` open @teleAppUpdates, even when someone really owns @tele. the menu on such a link can still open the real one. your own aliases come first. `@tele` in a message you send becomes `@teleAppUpdates`, so other apps see the real username.

to keep it that way:

- serve the keys sorted, so their order says nothing about the accounts behind them.
- change the salt from time to time (the official server derives a new one every month), so lists from different times can't be compared key by key. every key has to be recomputed with the new salt.
- keep the costs within the limits above: tele computes one key for every account it shows, and rejects a list that asks for more.

tele also rejects a list over 4 MiB or with more than 100000 entries, and then keeps using the last good one. it sends `If-None-Match` with `"<hex sha256 of the body it has>"`, so answering `304` when that matches the current body saves traffic, and a server can't tag clients with its own etags.

the same json can carry an optional `notices` array next to `peers`:

```json
"notices": [{
  "id": "tele-14",
  "rev": 0,
  "type": "info",
  "title": "tele 14 is out",
  "text": "update from settings",
  "entities": [{ "type": "bold", "offset": 0, "length": 6 }],
  "photo": { "url": "/v1/notices/tele-14/photo?rev=0", "width": 1280, "height": 720 },
  "buttons": [{ "text": "release notes", "url": "https://github.com/nitreojs/tele/releases" }],
  "toast": true,
  "builds": { "min": 13, "max": null },
  "platforms": ["windows", "linux"],
  "users": null,
  "from": 1791000000,
  "until": 1792000000
}]
```

- `id` is 1 to 64 latin letters, digits and dashes. `rev` is a whole number from 0. bump it when you edit a notice: tele replaces the old entry in the notification centre, but toasts each id only once.
- `type` is `info`, `success`, `warning` or `critical`, and picks the colour of the toast. `toast: true` shows the toast; otherwise the notice only goes to the notification centre.
- `title` or `text` must not be empty. `text` is cut at 4096 characters and `entities` at 256. entities work like the bot api: `offset` and `length` count utf-16 units.
- `photo` is optional. its `url` is relative to the server (`/…`, not `//…`) and serves a jpeg or png up to 1 MB.
- `buttons` are at most 2, and their urls start with `http://`, `https://` or `tg://`.
- `builds`, `platforms`, `users`, `from` and `until` are optional filters. `builds.min` and `builds.max` are tele build numbers, each can be null. `platforms` are `windows`, `linux` and `macos`. `from` and `until` are unix seconds.
- `users` are keys made exactly like the keys in `peers`, with the same salt, costs and scope, so the list doesn't say who a notice is for. null means everyone.
- tele reads at most 64 notices. a notice that leaves the feed stays in the notification centre history.

crash reports are optional. tele speaks the same protocol as telegram's own crash server, at `<server>/v1/crash.php`:

- `GET ?act=query_report&apiid=…&version=…&dmp=0|1&platform=…` answers `Report` as plain text when the server wants the report. anything else makes tele say thanks and send nothing.
- `POST ?act=report` is `multipart/form-data` with `platform` (like `Windows64Bit`, `Linux`, `MacOS`), `version` (like `7002009`), `report` (the report text) and, when there is one, `dump` (a zip with one `.dmp` minidump, under 20 MiB). answer `Done`, or `Done <id>` to have tele show "crash report #id sent".
- when there's no dump, the crash came from another version or the report is a freeze, the report text starts with `Tele-Note: <reason>` lines, like `Tele-Note: freeze 15 s`. freeze reports come through the same endpoint.
- answer `404` to both if you don't collect crashes.
