# tele

a telegram desktop fork. it isn't a real fork of the code: this repo only holds a queue of patches that get applied on top of every stable [tdesktop](https://github.com/telegramdesktop/tdesktop) release and built here automatically.

## download

grab the latest build from [releases](https://github.com/nitreojs/tele/releases/latest).

- **windows x64**: `tele-<version>-win64.zip`. unpack it anywhere and run `tele.exe`. it keeps its data next to the exe.
- **linux x64**: `tele-<version>-linux64.zip`. unpack it somewhere you can write to (like `~/.local/opt/tele`) and run `./tele`. it keeps its data in `~/.local/share/tele` and adds itself to the app menu.
- **macos** (apple silicon and intel): `tele-<version>-macos.dmg`. open it, drag tele into applications, then run this once in the terminal, since the build isn't notarized by apple (the `.zip` next to it is what the self-updater downloads):

  ```
  xattr -dr com.apple.quarantine /Applications/tele.app
  ```

  it keeps its data in `~/Library/Application Support/tele`.

none of them touch an installed telegram or its data.

tele updates itself: it checks these releases every 3 hours, downloads new builds in the background and asks you to restart. the update feed is signed, so a build that isn't from here won't be installed. you can turn it off in settings → tele → updates.

## patches

everything tele adds lives in settings → tele, right below the language row, grouped into pages: interface, chats and messages, privacy, profiles and ids, bots, server and updates. the search at the top of the page, and the main settings search, find every tele setting.

<details>
<summary>all 118 patches, newest release first</summary>

### [tele 9](https://github.com/nitreojs/tele/releases/tag/v7.2.9-tele.9)

| # | what it does | where to toggle |
|---|---|---|
| [82](patches/tdesktop/0082-feat-keep-messages-you-delete-yourself.patch) | messages you delete yourself are kept too, not only ones deleted by others | with 29 |
| [83](patches/tdesktop/0083-feat-show-server-and-updates-on-the-tele-settings-pa.patch) | the server and updates rows sit right on the tele settings page | always on |
| [84](patches/tdesktop/0084-feat-pick-brush-colors-from-the-image.patch) | an eyedropper in the photo editor picks the brush color from the image | always on |
| [85](patches/tdesktop/0085-feat-show-edit-history-as-a-chat.patch) | edit history opens as its own chat: every version as a full message with its media and time | with 28 |
| [86](patches/tdesktop/0086-feat-hide-or-confirm-call-and-voice-chat-buttons.patch) | call and voice chat buttons can each be shown, hidden, or ask before calling | tele → interface |
| [87](patches/tdesktop/0087-feat-group-the-tele-interface-settings.patch) | the interface page is split into groups: title bar, chat list, chats and profiles, text | always on |
| [88](patches/tdesktop/0088-feat-hide-ghost-mode-from-the-main-menu-unless-asked.patch) | the ghost mode toggle in the main menu is optional | tele → privacy, off |
| [89](patches/tdesktop/0089-feat-show-ids-on-regular-gifts.patch) | a copyable id on regular gifts too, not only on collectible ones | tele → profiles and ids, off |
| [90](patches/tdesktop/0090-feat-go-offline-right-after-sending-in-ghost-mode.patch) | with the online status hidden in ghost mode, sending a message sets you offline again right away | with 44 |
| [91](patches/tdesktop/0091-feat-send-inline-results-without-via.patch) | inline bot results go out as your own messages, without via @bot | tele → bots, off |
| [92](patches/tdesktop/0092-fix-put-the-checkmark-after-the-emoji-status.patch) | badges go in telegram's order everywhere: custom verification, name, emoji status, checkmark | always on |
| [93](patches/tdesktop/0093-fix-play-reactions-once-in-ghost-mode.patch) | in ghost mode, reaction animations play once instead of over and over | with 44 |
| [94](patches/tdesktop/0094-feat-skip-the-rich-message-prompt-on-paste.patch) | no rich message prompt when you paste formatted text | tele → chats and messages, off |
| [95](patches/tdesktop/0095-feat-group-the-tele-profile-settings.patch) | the profiles and ids page is split into groups: peer ids, profiles, gifts | always on |
| [96](patches/tdesktop/0096-feat-remove-a-chat-s-background-only-for-you.patch) | remove a chat's background only for you, from the chat menu | tele → chats and messages → chat backgrounds |
| [97](patches/tdesktop/0097-feat-set-chat-backgrounds-only-for-you.patch) | set your own background for any chat, only for you | with 96 |
| [98](patches/tdesktop/0098-fix-show-the-premium-star-next-to-checkmarks.patch) | the premium star shows next to checkmarks instead of being hidden by them | always on |
| [99](patches/tdesktop/0099-feat-skip-or-quote-deleted-messages-when-replying.patch) | replying to a message that got deleted meanwhile either drops the reply or quotes the deleted text | tele → chats and messages |
| [100](patches/tdesktop/0100-feat-add-test-server-accounts-with-a-plain-right-cli.patch) | a plain right-click on add account offers the test server | always on |
| [101](patches/tdesktop/0101-feat-link-usernames-to-profiles-locally.patch) | username aliases: your own @alias for any profile, clickable and in autocomplete, only for you | tele → chats and messages → username aliases |
| [102](patches/tdesktop/0102-feat-replace-username-aliases-when-sending.patch) | aliases in sent messages become real mentions, a toast says what changed | with 101 |
| [103](patches/tdesktop/0103-feat-hide-the-mentions-and-reactions-buttons.patch) | the jump to mentions and jump to reactions buttons can be hidden | tele → interface, off |
| [104](patches/tdesktop/0104-feat-pick-ignored-users-and-ghost-chats-like-privacy.patch) | ignored users and ghost chats are picked from a searchable list, like privacy exceptions | tele → privacy |
| [105](patches/tdesktop/0105-feat-show-what-s-new-in-a-local-tele-chat.patch) | what's new comes from a local tele chat with its own profile instead of telegram's service chat | with 55 |
| [106](patches/tdesktop/0106-feat-group-what-s-new-by-settings-category.patch) | what's new is grouped by settings page | with 55 |
| [107](patches/tdesktop/0107-feat-show-what-s-new-once-per-account-when-you-open-.patch) | every account gets what's new once, the first time you open it after an update | with 55 |
| [108](patches/tdesktop/0108-feat-show-names-instead-of-phone-numbers-in-chat-hea.patch) | people who shared their number with you but aren't in your contacts keep their name in the chat header instead of the number | tele → profiles and ids, off |
| [109](patches/tdesktop/0109-feat-allow-any-letters-in-username-aliases.patch) | aliases can use any letters, not only latin ones | with 101 |
| [110](patches/tdesktop/0110-feat-open-the-emoji-panel-by-click-only.patch) | the emoji, sticker and gif panel opens on click only, not on hover | tele → interface, off |
| [111](patches/tdesktop/0111-feat-rewrite-pasted-links-with-your-own-rules.patch) | links you paste are rewritten by your own rules, like x.com to fixupx.com. ctrl+z brings the original back | tele → chats and messages → link rewrites |
| [112](patches/tdesktop/0112-feat-edit-link-rewrite-rules-and-presets.patch) | an editor for link rewrite rules: domains or regex patterns, presets for x, instagram, tiktok, reddit, bluesky and pixiv, and a field to test a link | with 111 |
| [113](patches/tdesktop/0113-feat-name-people-only-for-you.patch) | give people a name only you see, from their chat menu. their profile keeps the real one | tele → profiles and ids → custom names |
| [114](patches/tdesktop/0114-feat-add-launch-flags-to-turn-off-tele-s-own-network.patch) | launch flags that keep tele off the network for one launch, see [below](#launch-flags) | always on |
| [115](patches/tdesktop/0115-feat-preview-calcmula-results-while-typing.patch) | the calcmula result shows above the input field while you type, like an inline bot | tele → chats and messages, off |
| [116](patches/tdesktop/0116-feat-open-the-attach-menu-by-click-only.patch) | the attach menu opens on click only, not on hover | tele → interface, off |
| [117](patches/tdesktop/0117-feat-clear-the-tele-server-s-cached-data.patch) | clear the tele server's saved data, badges included | tele → server → clear cached data |
| [118](patches/tdesktop/0118-fix-stop-calcmula-s-restored-text-from-doubling.patch) | a failed calcmula message goes back into the field once instead of doubling | with 68 |

### [tele 8](https://github.com/nitreojs/tele/releases/tag/v7.2.9-tele.8)

| # | what it does | where to toggle |
|---|---|---|
| [53](patches/tdesktop/0053-feat-apply-support-marks-from-the-tele-server.patch) | the tele server can mark accounts as support, optionally with its own text instead of "support" under the name | always on, with the server |
| [54](patches/tdesktop/0054-feat-turn-off-animated-userpics.patch) | animated userpics can stay still: separately in the chat list and in chats and profiles | tele → interface, off |
| [55](patches/tdesktop/0055-feat-show-what-s-new-in-tele-after-an-update.patch) | after an update, telegram's service chat gets a message with what's new in that tele version, visible only to you | tele → updates, on |
| [56](patches/tdesktop/0056-feat-show-checkmarks-and-custom-verification-in-the-.patch) | checkmarks and custom verification next to your name at the top of settings | always on |
| [57](patches/tdesktop/0057-feat-call-the-app-tele-everywhere.patch) | the app calls itself tele everywhere: tray menu, crash window, system menus and more | always on |
| [58](patches/tdesktop/0058-feat-customize-the-native-window-title.patch) | the window title (taskbar, alt+tab, system window frame) can be a template too, or follow the title bar label | tele → interface |
| [59](patches/tdesktop/0059-feat-lowercase-the-whole-crash-window.patch) | lowercase covers the crash window too | with 32 |
| [60](patches/tdesktop/0060-feat-group-tele-settings-into-categories.patch) | tele settings are grouped into pages like the main settings, and the settings search finds them | always on |
| [61](patches/tdesktop/0061-feat-search-tele-settings.patch) | a search field on the tele settings page | always on |
| [62](patches/tdesktop/0062-refactor-shorten-tele-option-descriptions.patch) | shorter descriptions for every tele setting | always on |
| [63](patches/tdesktop/0063-fix-open-tele-categories-from-old-settings-links-aft.patch) | old links to tele settings open the right page | always on |
| [64](patches/tdesktop/0064-fix-show-the-changelog-to-users-updating-from-builds.patch) | the what's new message shows up on the first update from tele 7 or older too, fresh installs skip it | with 55 |
| [65](patches/tdesktop/0065-feat-show-times-on-service-messages.patch) | service messages like joins and pins show their time too, with seconds | with 27 |
| [66](patches/tdesktop/0066-feat-upload-media-in-several-chats-at-once.patch) | media uploads in several chats at once instead of waiting for each other. files in one chat still go one after another | tele → chats and messages, off |
| [67](patches/tdesktop/0067-feat-reply-timestamps-for-media-in-rich-messages.patch) | time codes like 1:23 in a reply to a rich message link to its video or audio, the first one if there are several | always on |
| [68](patches/tdesktop/0068-feat-compute-messages-starting-with-via-calcmula.patch) | messages and captions starting with `= ` are computed with [calcmula](https://calcmula.app) and sent as the quoted query with `= result` below it. if it fails, nothing is sent and the text goes back into the field | tele → chats and messages, off |
| [69](patches/tdesktop/0069-feat-move-show-peer-ids-into-tele-settings.patch) | show peer ids moved from experimental settings into tele | tele → profiles and ids |
| [70](patches/tdesktop/0070-feat-show-the-tele-build-in-the-main-menu.patch) | the main menu shows the tele build next to the version | always on |
| [71](patches/tdesktop/0071-feat-open-collectible-gifts-in-see.tg.patch) | an open in see.tg link on collectible gift cards | tele → profiles and ids, off |
| [72](patches/tdesktop/0072-feat-move-late-sent-messages-to-the-bottom.patch) | a message that took long to send moves to the bottom of the chat once it's sent, so it's clear when it went out | tele → chats and messages, off |
| [73](patches/tdesktop/0073-feat-queue-messages-behind-an-uploading-media.patch) | messages sent while a media is uploading wait for it and go out after it, in order | tele → chats and messages, off |
| [74](patches/tdesktop/0074-feat-open-links-in-their-desktop-apps.patch) | spotify, steam, discord, zoom, teams, notion, slack and epic links open in their desktop apps when they're installed | tele → chats and messages, off |
| [75](patches/tdesktop/0075-feat-clean-tracking-parameters-from-opened-links.patch) | the SUPER MAGA PALANTIR ICE PETER THIEL AI DATA HARVESTER 9000 remover: opened links lose their tracking parameters (utm, fbclid, si, gclid and [more](#link-cleaner)). when it would change a link, its right-click menu offers open without cleaning | tele → chats and messages, off |
| [76](patches/tdesktop/0076-feat-clean-tracking-parameters-from-sent-links.patch) | the same remover for links in sent messages and captions, the rest of the text stays as it is | tele → chats and messages, off |
| [77](patches/tdesktop/0077-feat-reveal-spoilers-automatically.patch) | text and media spoilers are revealed right away, in chats and the chat list | tele → chats and messages, off |
| [78](patches/tdesktop/0078-feat-move-tele-tools-to-the-bottom-of-the-message-me.patch) | tele's items sit at the bottom of the message menu: view as tl, then the message id | always on |
| [79](patches/tdesktop/0079-feat-copy-custom-emoji-ids-from-the-message-menu.patch) | right-click a custom emoji in a message to copy its id | tele → chats and messages, off |
| [80](patches/tdesktop/0080-fix-change-the-speed-instead-of-moving-the-media-vie.patch) | dragging while holding a video to speed it up changes the speed instead of moving the media viewer window, and the speedup no longer stops by itself | always on |
| [81](patches/tdesktop/0081-feat-reorder-and-hide-message-menu-items.patch) | reorder and hide items of the message menu, items it doesn't know keep their place | tele → chats and messages → message menu |

### [tele 7](https://github.com/nitreojs/tele/releases/tag/v7.2.9-tele.7)

| # | what it does | where to toggle |
|---|---|---|
| [27](patches/tdesktop/0027-feat-show-seconds-in-message-times.patch) | message times show seconds, like 14:03:21 | tele → chats and messages, off |
| [28](patches/tdesktop/0028-feat-keep-the-edit-history-of-messages.patch) | remembers what edited messages looked like while tele runs: right-click an edited message → edit history | tele → chats and messages, off |
| [29](patches/tdesktop/0029-feat-keep-deleted-messages.patch) | messages deleted by others or from your other devices stay in the chat until tele restarts, faded or with a trash icon by the time | tele → chats and messages, off |
| [30](patches/tdesktop/0030-fix-fade-every-unsupported-experimental-option.patch) | experimental options your system doesn't support are faded completely, title included | always on |
| [31](patches/tdesktop/0031-feat-hide-call-buttons.patch) | no call button in private chats and profiles | tele → interface, off |
| [32](patches/tdesktop/0032-feat-lowercase-every-interface-text.patch) | lowercases the whole interface. messages and names stay as they are | tele → interface, off, needs a restart |
| [33](patches/tdesktop/0033-feat-list-deleted-messages-per-chat.patch) | each chat gets a page with its kept deleted messages and a clear all button: chat menu → deleted messages | with 29 |
| [34](patches/tdesktop/0034-feat-show-the-data-center-in-profiles.patch) | a dc row in profiles: the data center the account or chat lives in | tele → profiles and ids, off |
| [35](patches/tdesktop/0035-feat-hide-sponsored-messages.patch) | no ads: no sponsored messages in channels and bots, no video ads, no sponsored search results | tele → chats and messages, off |
| [36](patches/tdesktop/0036-feat-open-links-without-confirmation.patch) | links with custom text open right away, without the confirmation | tele → chats and messages, off |
| [37](patches/tdesktop/0037-feat-open-disappearing-media-without-burning-it.patch) | view-once and timed media open without burning, and the sender still sees them unopened. message menu → mark as viewed burns them | tele → chats and messages, off |
| [38](patches/tdesktop/0038-feat-allow-screenshots-of-disappearing-media.patch) | view-once and timed media can be screenshotted and recorded | tele → chats and messages, off |
| [39](patches/tdesktop/0039-feat-copy-the-callback-data-of-bot-buttons.patch) | right-click over a bot button to copy its callback data, inline query, web app url and so on | always on |
| [40](patches/tdesktop/0040-feat-show-the-message-id-in-the-message-menu.patch) | the message menu ends with the message id, click it to copy | tele → chats and messages, off |
| [41](patches/tdesktop/0041-feat-view-messages-as-tl.patch) | view as tl in the message menu: fetches the message from the server and opens it on [schema.jppgr.am](https://schema.jppgr.am) | tele → chats and messages, off |
| [42](patches/tdesktop/0042-feat-hide-the-all-chats-folder.patch) | hides the all chats folder when you have other folders, the list opens on your first one | tele → interface, off |
| [43](patches/tdesktop/0043-feat-jump-to-the-first-message-of-a-chat.patch) | jump to the first message, in the chat menu | tele → chats and messages, off |
| [44](patches/tdesktop/0044-feat-add-ghost-mode.patch) | ghost mode: no read receipts, typing, online status or story views, each switchable. optionally reads a chat when you reply, and the message menu has mark as read up to here. quick toggle in the side menu | tele → privacy, off |
| [45](patches/tdesktop/0045-feat-override-ghost-mode-per-chat.patch) | ghost mode per chat: always or never, from the chat menu | chat menu → ghost mode in this chat |
| [46](patches/tdesktop/0046-fix-show-checkmarks-next-to-emoji-statuses.patch) | checkmarks show next to emoji statuses instead of being replaced by them | always on |
| [47](patches/tdesktop/0047-feat-view-any-telegram-object-as-tl.patch) | view as tl also for chats, profiles, members, topics, stickers and sets, custom emoji, gifts, stories and folders | with 41 |
| [48](patches/tdesktop/0048-feat-hide-the-mtproxy-sponsor-channel.patch) | no sponsor channel pinned to the chat list when you connect through an mtproxy | tele → chats and messages, off |
| [49](patches/tdesktop/0049-feat-lowercase-tele-s-own-texts-too.patch) | lowercase covers tele's own texts too | with 32 |
| [50](patches/tdesktop/0050-fix-stop-maximized-windows-jittering-on-monitors-wit.patch) | a maximized window no longer jitters on a monitor without a taskbar (windows) | always on |
| [51](patches/tdesktop/0051-feat-send-crash-reports-to-the-tele-server.patch) | when tele crashed, the next start offers to send the crash report to the tele server instead of telegram. nothing leaves without your click | tele → server, on with the server |
| [52](patches/tdesktop/0052-feat-send-messages-as-scheduled-in-ghost-mode.patch) | in ghost mode, messages go out as scheduled a few seconds ahead, so sending doesn't put you online | tele → privacy, off |

### [tele 5](https://github.com/nitreojs/tele/releases/tag/v7.2.9-tele.5)

| # | what it does | where to toggle |
|---|---|---|
| [13](patches/tdesktop/0013-feat-update-linux-and-macos-builds-from-the-tele-rel.patch) | the self-updater works on linux and macos too | tele → updates, on |
| [14](patches/tdesktop/0014-feat-give-linux-and-macos-builds-their-own-identity.patch) | linux and macos builds are their own app, so they don't clash with an installed telegram | always on |
| [15](patches/tdesktop/0015-feat-refresh-the-server-data-on-demand.patch) | fetch the tele server's data right away instead of waiting for the next check | tele → server → refresh now |
| [16](patches/tdesktop/0016-fix-repaint-member-lists-when-server-verification-ar.patch) | member lists show checkmarks and custom verification from the tele server as soon as they arrive | always on |
| [17](patches/tdesktop/0017-feat-show-checkmarks-and-custom-verification-in-the-.patch) | checkmarks and custom verification next to your name in the main menu | always on |
| [18](patches/tdesktop/0018-feat-apply-scam-and-fake-marks-from-the-tele-server.patch) | scam and fake marks from the tele server, shown like telegram's own | always on |
| [19](patches/tdesktop/0019-feat-animate-custom-verification-icons.patch) | custom verification icons animate like any other custom emoji | always on |
| [20](patches/tdesktop/0020-feat-show-checkmarks-and-custom-verification-next-to.patch) | checkmarks and custom verification next to sender names in messages | tele → interface, off |
| [21](patches/tdesktop/0021-feat-show-a-copyable-gift-id-in-the-unique-gift-card.patch) | a copyable gift id at the top of the collectible gift card | tele → profiles and ids, off |
| [22](patches/tdesktop/0022-fix-only-say-a-gift-is-on-the-blockchain-when-it-is.patch) | the gift card only says a gift is on the ton blockchain while it really is there | always on |
| [23](patches/tdesktop/0023-feat-show-the-peer-id-as-its-own-profile-row.patch) | the peer id gets its own profile row instead of trailing the bio | tele → profiles and ids, off (see 69) |
| [24](patches/tdesktop/0024-feat-format-peer-ids-without-spaces-or-bot-api-style.patch) | peer ids without spaces, or in bot api style (-100… for channels) | tele → profiles and ids, off |
| [25](patches/tdesktop/0025-feat-copy-links-to-tele-settings.patch) | right-click any tele setting to copy a link that opens it | always on |
| [26](patches/tdesktop/0026-feat-ignore-users-by-hiding-or-fading-their-messages.patch) | ignore users from their userpic menu: their messages fade or disappear, the list lives in settings | tele → privacy |

### [tele 4](https://github.com/nitreojs/tele/releases/tag/v7.2.9-tele.4)

| # | what it does | where to toggle |
|---|---|---|
| [8](patches/tdesktop/0008-feat-send-quick-replies-in-groups-and-channels.patch) | business quick replies in groups and channels too. telegram only sends them in private chats, so tele posts the messages as ordinary ones (no bot keyboards, via-bot labels or effects) | tele → chats and messages, off |
| [9](patches/tdesktop/0009-feat-apply-verification-from-the-tele-server.patch) | checkmarks and custom verification from the tele server, shown exactly like telegram's own | tele → server, on |
| [10](patches/tdesktop/0010-feat-make-the-title-bar-label-a-live-template.patch) | the title bar label is a template with live variables, see below | tele → interface |
| [11](patches/tdesktop/0011-feat-remove-the-account-limit.patch) | no account limit (well, 1536) | always on |
| [12](patches/tdesktop/0012-feat-show-checkmarks-and-custom-verification-in-the-.patch) | checkmarks and custom verification in the account list | always on |

### [tele 3](https://github.com/nitreojs/tele/releases/tag/v7.2.9-tele.3)

| # | what it does | where to toggle |
|---|---|---|
| [1](patches/tdesktop/0001-feat-show-the-tele-build-number-in-the-title-bar.patch) | the title bar shows which tele build you're on | always on, see 10 |
| [2](patches/tdesktop/0002-feat-add-a-tele-section-to-the-settings.patch) | the tele section in settings | always on |
| [3](patches/tdesktop/0003-feat-add-an-option-to-hide-stories-everywhere.patch) | hides stories everywhere: no stories bar, no rings around userpics, no stories in profiles | tele → privacy, off, needs a restart |
| [4](patches/tdesktop/0004-feat-add-an-option-to-watch-stories-invisibly.patch) | watch stories without showing up among the viewers. reactions and replies still reveal you | tele → privacy, off |
| [5](patches/tdesktop/0005-feat-show-bot-button-payloads-in-tooltips.patch) | hovering a bot button shows what it carries: callback data, links, inline queries, web apps and more | tele → bots, off |
| [6](patches/tdesktop/0006-feat-update-from-the-tele-github-releases.patch) | self-updates from these releases, signed with ed25519 | tele → updates, on |
| [7](patches/tdesktop/0007-feat-rename-the-app-to-tele.patch) | the app is called tele: `tele.exe`, its own taskbar entry, links point here | always on |

</details>

### title bar template

the default is `TELE {build}`. empty hides the label.

- `{build}`, `{version}`
- `{time}`, `{date}`, `{weekday}`, or any qt format like `{time:HH:mm:ss}` and `{date:dd MMM}`
- `{name}`, `{username}`, `{id}`, `{accounts}`
- `{unread}`, `{chat}`, `{chat_unread}`, `{status}`

`[ … ]` hides its part when a variable inside is empty or 0, so `TELE {build}[ · {unread} unread]` doesn't show "· 0 unread". doubled brackets are literal. account and activity variables stay empty while the app is locked with a passcode.

the window title (what the taskbar, alt+tab and the system window frame show) takes the same template, set next to the label. `{label}` puts the rendered label there, so `{label}` alone keeps both in sync. empty keeps telegram's own title, and a template that renders to nothing leaves the title blank.

### link cleaner

on every site: `utm*`, `mtm_*`, `pk_*`, `ga_*`, `_ga`, `_gl`, `gclid`, `gclsrc`, `gbraid`, `wbraid`, `dclid`, `gad_source`, `gad_campaignid`, `fbclid`, `fb_action_*`, `fb_source`, `fb_ref`, `action_*_map`, `msclkid`, `twclid`, `ttclid`, `li_fat_id`, `epik`, `yclid`, `ysclid`, `_openstat`, `mc_cid`, `mc_eid`, `mc_tc`, `ml_subscriber*`, `mkt_tok`, `igshid`, `igsh`, `_hsenc`, `_hsmi`, `__hsfp`, `__hssc`, `__hstc`, `hsctatracking`, `srsltid`, `s_kwcid`, `s_cid`, `oly_*_id`, `rb_clickid`, `vero_*`, `wickedid`, `_kx`, `wt_mc`, `wtrid`, `hmb_*`, `itm_*`, `otm_*`, `cmpid`, `os_ehash`, `__twitter_impression`, `tracking_source`, `echobox`, `spm`, `_branch_match_id`, `_branch_referrer`, `si`. fragments like `#utm_source=…` go too.

per site, on top of that: youtube (`feature`, `pp`, `kw`), spotify (`context`, `nd`, `dl_branch`), twitter / x and fx/vx mirrors (`s`, `t`, `src`, `ref_src`, `ref_url`, `cn`), threads (`xmt`, `slof`), tiktok (`_r`, `_t`, `is_from_webapp`, `sender_device`, `share_*` and more), facebook (`mibextid`, `__tn__`, `__cft__`, `ref*`, `notif_*` and more), reddit (`share_id`, `ref*`, `correlation_id`, `rdt`), amazon (`pd_rd_*`, `qid`, `ref_`, `tag`, `linkCode`, `/ref=…` in the path and more), aliexpress (`aff_*`, `algo_*`, `pvid`, `scm*` and more), vk (`from`, `ref`, `ref_domain`), yandex (`from`, `clid`, `redircnt`), google search (`ved`, `ei`, `sa`, `usg`, `oq`, `aqs`, `gs_*` and more), google docs / drive (`usp`), linkedin (`trk*`, `refId`, `lipi` and more), ebay (`_trk*`, `mk*`, `campid` and more), medium (`source`), github (`email_token`, `email_source`), steam (`snr`), netflix (`trackId`, `tctx`), twitch (`tt_medium`, `tt_content`), imdb (`ref_`, `pf_rd_*`), bing, msn, apple (`itsct`, `itscg`), pinterest, hh.ru, ozon. t.me links are never touched.
### launch flags

start tele with any of these to keep it off the network on its own for that launch. telegram's own connection works as usual, and your settings stay as they are.

- `-noteleserver`: nothing goes to the tele server: no checkmark or other mark updates (the saved ones still show) and no crash reports.
- `-noteleupdate`: no update checks, no downloads, no what's new.
- `-teleoffline`: both of the above, and calcmula is off too.

the flags stay on when tele restarts itself, like after an update. on windows, add them to a shortcut after `tele.exe`; on linux, `./tele -teleoffline`; on macos, `open -a tele --args -teleoffline`. a shortcut with `-noteleserver` keeps even the very first launch away from the tele server. to turn the server off for good, empty its field in settings.

### tele server

tele can pull extra account data, like checkmarks, custom verification, scam / fake marks and support marks, from an optional server (settings → tele → server). it only ever downloads one public list and never tells the server which accounts you look at. the list is hashed, so it can't just be read off as a list of accounts. tele checks it every 10 minutes, and "refresh now" fetches it right away. leave the field empty to turn it off. "clear cached data" drops the list tele saved, so the marks disappear until the next fetch.

the same server takes crash reports. after a crash, tele offers to send the report: a short text with the version, platform and the crash reason, plus a minidump of the crashed process. you can look at it first and untick your username. with the server field empty, nothing is offered.

#### running your own server

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

to keep it that way:

- serve the keys sorted, so their order says nothing about the accounts behind them.
- change the salt from time to time (the official server derives a new one every month), so lists from different times can't be compared key by key. every key has to be recomputed with the new salt.
- keep the costs within the limits above: tele computes one key for every account it shows, and rejects a list that asks for more.

tele also rejects a list over 4 MiB or with more than 100000 entries, and then keeps using the last good one. it sends `If-None-Match` with `"<hex sha256 of the body it has>"`, so answering `304` when that matches the current body saves traffic, and a server can't tag clients with its own etags.

crash reports are optional. tele speaks the same protocol as telegram's own crash server, at `<server>/v1/crash.php`:

- `GET ?act=query_report&apiid=…&version=…&dmp=0|1&platform=…` answers `Report` as plain text when the server wants the report. anything else makes tele say thanks and send nothing.
- `POST ?act=report` is `multipart/form-data` with `platform` (like `Windows64Bit`, `Linux`, `MacOS`), `version` (like `7002009`), `report` (the report text) and, when there is one, `dump` (a zip with one `.dmp` minidump, under 20 MiB). answer `Done`.
- answer `404` to both if you don't collect crashes.
