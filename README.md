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

### title bar template

the default is `TELE {build}`. empty hides the label.

- `{build}`, `{version}`
- `{time}`, `{date}`, `{weekday}`, or any qt format like `{time:HH:mm:ss}` and `{date:dd MMM}`
- `{name}`, `{username}`, `{id}`, `{accounts}`
- `{unread}`, `{chat}`, `{chat_unread}`, `{status}`

`[ … ]` hides its part when a variable inside is empty or 0, so `TELE {build}[ · {unread} unread]` doesn't show "· 0 unread". doubled brackets are literal. account and activity variables stay empty while the app is locked with a passcode.

### tele server

tele can pull extra account data, like checkmarks and custom verification, from an optional server (settings → tele → server). it only ever downloads one public list and never tells the server which accounts you look at. the list is hashed, so it can't just be read off as a list of accounts. tele checks it every 10 minutes, and "refresh now" fetches it right away. leave the field empty to turn it off.

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
