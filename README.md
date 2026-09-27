# tele

a telegram desktop fork. it isn't a real fork of the code: this repo only holds a queue of patches that get applied on top of every stable [tdesktop](https://github.com/telegramdesktop/tdesktop) release and built here automatically.

## download

grab the latest build from [releases](https://github.com/nitreojs/tele/releases/latest).

- **windows x64**: `tele-<version>-win64.zip`. unpack it anywhere and run `tele.exe`. it keeps its data next to the exe.
- **linux x64**: `tele-<version>-linux64.zip`. unpack it somewhere you can write to (like `~/.local/opt/tele`) and run `./tele`. it keeps its data in `~/.local/share/tele` and adds itself to the app menu.
- **macos** (apple silicon and intel): `tele-<version>-macos.zip`. unpack it, move `tele.app` to applications, then run this once in the terminal, since the build isn't notarized by apple:

  ```
  xattr -dr com.apple.quarantine /Applications/tele.app
  ```

  it keeps its data in `~/Library/Application Support/tele`.

none of them touch an installed telegram or its data.

tele updates itself: it checks these releases every 3 hours, downloads new builds in the background and asks you to restart. the update feed is signed, so a build that isn't from here won't be installed. you can turn it off in settings → tele → updates.

## patches

everything tele adds lives in settings → tele, right below the language row.

| # | what it does | where to toggle |
|---|---|---|
| [1](patches/tdesktop/0001-feat-show-the-tele-build-number-in-the-title-bar.patch) | the title bar shows which tele build you're on | always on, see 10 |
| [2](patches/tdesktop/0002-feat-add-a-tele-section-to-the-settings.patch) | the tele section in settings | always on |
| [3](patches/tdesktop/0003-feat-add-an-option-to-hide-stories-everywhere.patch) | hides stories everywhere: no stories bar, no rings around userpics, no stories in profiles | tele → stories, off, needs a restart |
| [4](patches/tdesktop/0004-feat-add-an-option-to-watch-stories-invisibly.patch) | watch stories without showing up among the viewers. reactions and replies still reveal you | tele → stories, off |
| [5](patches/tdesktop/0005-feat-show-bot-button-payloads-in-tooltips.patch) | hovering a bot button shows what it carries: callback data, links, inline queries, web apps and more | tele → bots, off |
| [6](patches/tdesktop/0006-feat-update-from-the-tele-github-releases.patch) | self-updates from these releases, signed with ed25519 | tele → updates, on |
| [7](patches/tdesktop/0007-feat-rename-the-app-to-tele.patch) | the app is called tele: `tele.exe`, its own taskbar entry, links point here | always on |
| [8](patches/tdesktop/0008-feat-send-quick-replies-in-groups-and-channels.patch) | business quick replies in groups and channels too. telegram only sends them in private chats, so tele posts the messages as ordinary ones (no bot keyboards, via-bot labels or effects) | tele → chats, off |
| [9](patches/tdesktop/0009-feat-apply-verification-from-the-tele-server.patch) | checkmarks and custom verification from the tele server, shown exactly like telegram's own | tele → server, on |
| [10](patches/tdesktop/0010-feat-make-the-title-bar-label-a-live-template.patch) | the title bar label is a template with live variables, see below | tele → title bar |
| [11](patches/tdesktop/0011-feat-remove-the-account-limit.patch) | no account limit (well, 1536) | always on |
| [12](patches/tdesktop/0012-feat-show-checkmarks-and-custom-verification-in-the-.patch) | checkmarks and custom verification in the account list | always on |
| [13](patches/tdesktop/0013-feat-update-linux-and-macos-builds-from-the-tele-rel.patch) | the self-updater works on linux and macos too | tele → updates, on |
| [14](patches/tdesktop/0014-feat-give-linux-and-macos-builds-their-own-identity.patch) | linux and macos builds are their own app, so they don't clash with an installed telegram | always on |
| [15](patches/tdesktop/0015-feat-refresh-the-server-data-on-demand.patch) | fetch the tele server's data right away instead of waiting for the next check | tele → server → refresh now |
| [16](patches/tdesktop/0016-fix-repaint-member-lists-when-server-verification-ar.patch) | member lists show checkmarks and custom verification from the tele server as soon as they arrive | always on |
| [17](patches/tdesktop/0017-feat-show-checkmarks-and-custom-verification-in-the-.patch) | checkmarks and custom verification next to your name in the main menu | always on |
| [18](patches/tdesktop/0018-feat-apply-scam-and-fake-marks-from-the-tele-server.patch) | scam and fake marks from the tele server, shown like telegram's own | always on |
| [19](patches/tdesktop/0019-feat-animate-custom-verification-icons.patch) | custom verification icons animate like any other custom emoji | always on |
| [20](patches/tdesktop/0020-feat-show-checkmarks-and-custom-verification-next-to.patch) | checkmarks and custom verification next to sender names in messages | tele → chats, off |
| [21](patches/tdesktop/0021-feat-show-a-copyable-gift-id-in-the-unique-gift-card.patch) | a copyable gift id at the top of the collectible gift card | tele → gifts, off |
| [22](patches/tdesktop/0022-fix-only-say-a-gift-is-on-the-blockchain-when-it-is.patch) | the gift card only says a gift is on the ton blockchain while it really is there | always on |
| [23](patches/tdesktop/0023-feat-show-the-peer-id-as-its-own-profile-row.patch) | the peer id gets its own profile row instead of trailing the bio | experimental → show peer ids |
| [24](patches/tdesktop/0024-feat-format-peer-ids-without-spaces-or-bot-api-style.patch) | peer ids without spaces, or in bot api style (-100… for channels) | tele → ids, off |
| [25](patches/tdesktop/0025-feat-copy-links-to-tele-settings.patch) | right-click any tele setting to copy a link that opens it | always on |
| [26](patches/tdesktop/0026-feat-ignore-users-by-hiding-or-fading-their-messages.patch) | ignore users from their userpic menu: their messages fade or disappear, the list lives in settings | tele → ignoring |
| [27](patches/tdesktop/0027-feat-show-seconds-in-message-times.patch) | message times show seconds, like 14:03:21 | tele → messages, off |
| [28](patches/tdesktop/0028-feat-keep-the-edit-history-of-messages.patch) | remembers what edited messages looked like while tele runs: right-click an edited message → edit history | tele → messages, off |
| [29](patches/tdesktop/0029-feat-keep-deleted-messages.patch) | messages deleted by others or from your other devices stay in the chat until tele restarts, faded or with a trash icon by the time | tele → messages, off |
| [30](patches/tdesktop/0030-fix-fade-every-unsupported-experimental-option.patch) | experimental options your system doesn't support are faded completely, title included | always on |
| [31](patches/tdesktop/0031-feat-hide-call-buttons.patch) | no call button in private chats and profiles | tele → chats, off |
| [32](patches/tdesktop/0032-feat-lowercase-every-interface-text.patch) | lowercases the whole interface. messages and names stay as they are | tele → interface, off, needs a restart |
| [33](patches/tdesktop/0033-feat-list-deleted-messages-per-chat.patch) | each chat gets a page with its kept deleted messages and a clear all button: chat menu → deleted messages | with 29 |
| [34](patches/tdesktop/0034-feat-show-the-data-center-in-profiles.patch) | a dc row in profiles: the data center the account or chat lives in | tele → ids, off |
| [35](patches/tdesktop/0035-feat-hide-sponsored-messages.patch) | no ads: no sponsored messages in channels and bots, no video ads, no sponsored search results | tele → chats, off |
| [36](patches/tdesktop/0036-feat-open-links-without-confirmation.patch) | links with custom text open right away, without the confirmation | tele → chats, off |
| [37](patches/tdesktop/0037-feat-open-disappearing-media-without-burning-it.patch) | view-once and timed media open without burning, and the sender still sees them unopened. message menu → mark as viewed burns them | tele → messages, off |
| [38](patches/tdesktop/0038-feat-allow-screenshots-of-disappearing-media.patch) | view-once and timed media can be screenshotted and recorded | tele → messages, off |
| [39](patches/tdesktop/0039-feat-copy-the-callback-data-of-bot-buttons.patch) | right-click over a bot button to copy its callback data, inline query, web app url and so on | always on |
| [40](patches/tdesktop/0040-feat-show-the-message-id-in-the-message-menu.patch) | the message menu starts with the message id, click it to copy | tele → ids, off |
| [41](patches/tdesktop/0041-feat-view-messages-as-tl.patch) | view as tl in the message menu: fetches the message from the server and opens it on [schema.jppgr.am](https://schema.jppgr.am) | tele → ids, off |
| [42](patches/tdesktop/0042-feat-hide-the-all-chats-folder.patch) | hides the all chats folder when you have other folders, the list opens on your first one | tele → chats, off |
| [43](patches/tdesktop/0043-feat-jump-to-the-first-message-of-a-chat.patch) | jump to the first message, in the chat menu | tele → chats, off |
| [44](patches/tdesktop/0044-feat-add-ghost-mode.patch) | ghost mode: no read receipts, typing, online status or story views, each switchable. optionally reads a chat when you reply, and the message menu has mark as read up to here. quick toggle in the side menu | tele → ghost mode, off |
| [45](patches/tdesktop/0045-feat-override-ghost-mode-per-chat.patch) | ghost mode per chat: always or never, from the chat menu | chat menu → ghost mode in this chat |
| [46](patches/tdesktop/0046-fix-show-checkmarks-next-to-emoji-statuses.patch) | checkmarks show next to emoji statuses instead of being replaced by them | always on |
| [47](patches/tdesktop/0047-feat-view-any-telegram-object-as-tl.patch) | view as tl also for chats, profiles, members, topics, stickers and sets, custom emoji, gifts, stories and folders | with 41 |
| [48](patches/tdesktop/0048-feat-hide-the-mtproxy-sponsor-channel.patch) | no sponsor channel pinned to the chat list when you connect through an mtproxy | tele → chats, off |
| [49](patches/tdesktop/0049-feat-lowercase-tele-s-own-texts-too.patch) | lowercase covers tele's own texts too | with 32 |
| [50](patches/tdesktop/0050-fix-stop-maximized-windows-jittering-on-monitors-wit.patch) | a maximized window no longer jitters on a monitor without a taskbar (windows) | always on |

### title bar template

the default is `TELE {build}`. empty hides the label.

- `{build}`, `{version}`
- `{time}`, `{date}`, `{weekday}`, or any qt format like `{time:HH:mm:ss}` and `{date:dd MMM}`
- `{name}`, `{username}`, `{id}`, `{accounts}`
- `{unread}`, `{chat}`, `{chat_unread}`, `{status}`

`[ … ]` hides its part when a variable inside is empty or 0, so `TELE {build}[ · {unread} unread]` doesn't show "· 0 unread". doubled brackets are literal. account and activity variables stay empty while the app is locked with a passcode.

### tele server

tele can pull extra account data, like checkmarks, custom verification and scam / fake marks, from an optional server (settings → tele → server). it only ever downloads one public list and never tells the server which accounts you look at. the list is hashed, so it can't just be read off as a list of accounts. tele checks it every 10 minutes, and "refresh now" fetches it right away. leave the field empty to turn it off.

## how it works

- `UPSTREAM` holds the tdesktop tag the patches target, `patches/` holds the patches (grouped per repo, so submodules get their own folders), and `tele.py` moves a tdesktop checkout to that tag and applies, continues or exports them.
- every 3 hours [sync](.github/workflows/sync.yml) looks for a new stable tdesktop release. when the patches apply cleanly, it bumps `UPSTREAM` and [build](.github/workflows/build.yml) builds and publishes `<version>-tele.<n>`. when they don't, it opens an issue and the conflict gets fixed by hand.

## building it yourself

clone tdesktop next to this repo (as `../tdesktop`), then:

```
python tele.py checkout
```

that puts tdesktop on the `UPSTREAM` tag with the patches applied as commits. from there, build as upstream's [docs](https://github.com/telegramdesktop/tdesktop/tree/dev/docs) say. builds you make yourself show `TELE DEV` and don't update themselves.

to change a patch, commit inside the tdesktop checkout (or inside the submodule that owns the file) and run `python tele.py export`.
