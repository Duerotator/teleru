# функции tele

каждый патч tele, сгруппированный по страницам настроек. [релизы](releases.md) содержит те же пункты, разбитые по релизам.

всё, что добавляет tele, находится в: **настройки → tele**, прямо под выбором языка, сгруппированное по вкладкам. строка поиска вверху и глобальный поиск по настройкам находят любую опцию tele. клик правой кнопкой мыши по любой настройке копирует прямую ссылку на неё.

резервное копирование экспортирует настройки tele в файл, которым можно поделиться, и импортирует их с наглядным предпросмотром изменений. оно охватывает переключатели и списки tele, но не затрагивает системные параметры самого telegram (например, масштаб интерфейса) или данные конкретных аккаунтов (локальные закрепления, наборы, закладки, локальные папки). чтобы перенести абсолютно всё на другой ПК, просто скопируйте всю папку `tdata` рядом с исполняемым файлом tele.

«тумблер» указывает, где находится переключатель и его состояние по умолчанию. `всегда вкл` не имеет тумблера, `вместе с N` активируется переключателем патча N.

подробнее о некоторых функциях: [шаблоны заголовка окна](title-template.md), [очистка ссылок](link-cleaner.md), [флаги запуска](launch-flags.md), [сервер tele](server.md).

<a id="interface"></a>
## интерфейс

настройки → tele → интерфейс.

| # | что делает | тумблер |
|---|---|---|
| [10](../patches/tdesktop/0010-feat-make-the-title-bar-label-a-live-template.patch) | текст в заголовке панели поддерживает шаблон с живыми переменными, см. [шаблоны заголовка окна](title-template.md) | tele → интерфейс |
| [22](../patches/tdesktop/0022-feat-lowercase-every-interface-text.patch) | переводит весь интерфейс в нижний регистр. сообщения и имена остаются без изменений | tele → интерфейс, выкл., требуется перезапуск |
| [30](../patches/tdesktop/0030-feat-hide-the-all-chats-folder.patch) | скрывает папку «Все чаты», если настроены другие папки; список сразу открывается на первой папке | tele → интерфейс, выкл. |
| [35](../patches/tdesktop/0035-feat-lowercase-tele-s-own-texts-too.patch) | нижний регистр применяется также к собственным текстам tele и окну отчета о сбоях | вместе с 22 |
| [38](../patches/tdesktop/0038-feat-turn-off-animated-userpics.patch) | возможность сделать анимированные аватары статичными: раздельно для списка чатов и внутри чатов/профилей | tele → интерфейс, выкл., в чатах и профилях: tele → чаты, выкл. |
| [41](../patches/tdesktop/0041-feat-customize-the-window-title-and-format-template-.patch) | заголовок окна ОС (панель задач, Alt+Tab, рамка окна) также поддерживает шаблоны или синхронизацию с панелью. переменные принимают модификаторы вроде `{weekday|short|lower}` или `{chat|max:20}` | tele → интерфейс |
| [82](../patches/tdesktop/0082-feat-move-chats-instantly-in-the-chat-list.patch) | чаты мгновенно перемещаются на новую позицию в списке без задержки при наведении курсора мыши | tele → интерфейс, выкл. |
| [84](../patches/tdesktop/0084-feat-set-your-own-app-and-tray-icons.patch) | установка собственных иконок приложения и трея из любого изображения; иконка в трее может следовать за иконкой приложения | tele → интерфейс → значок приложения |
| [97](../patches/tdesktop/0097-feat-redesign-the-title-template-editor.patch) | обновленный редактор шаблона заголовка: переменные в виде чипов, палитра модификаторов и готовые пресеты | вместе с 10 |
| [117](../patches/tdesktop/0117-feat-hide-communities.patch) | скрытие сообществ (community): входящие в них чаты остаются в общем списке как обычные чаты | tele → интерфейс, выкл. |
| [123](../patches/tdesktop/0123-feat-pin-chats-past-the-limit.patch) | закрепление большего числа чатов, чем разрешает telegram: дополнительные закрепления сохраняются локально, помечаются контурным значком булавки и свободно перемещаются среди серверных | tele → интерфейс, выкл. |
| [124](../patches/tdesktop/0124-feat-folders-past-the-limit.patch) | больше папок и больше чатов в каждой папке, чем разрешает telegram: превышающие лимит сохраняются локально на этом устройстве | tele → интерфейс, выкл. |
| [129](../patches/tdesktop/0129-feat-hide-message-previews-in-the-chat-list.patch) | скрытие превью текста сообщений в списке чатов с компактной высотой строк | tele → интерфейс, выкл. |
| [150](../patches/tdesktop/0150-feat-make-build-the-bare-build-number.patch) | переменная `{build}` возвращает чистый номер сборки, стандартный заголовок — TELE #{build}, пользовательские шаблоны обновляются автоматически | вместе с 10 |
| [152](../patches/tdesktop/0152-feat-interface-scale-in-1-steps.patch) | ползунок масштабирования интерфейса перемещается с шагом в 1% | tele → интерфейс, выкл. |
| [154](../patches/tdesktop/0154-feat-reduce-motion.patch) | режим уменьшения движения: отключение всех анимаций (кроме звонков), зацикливания стикеров, всплесков реакций и эффектов сообщений | tele → интерфейс, выкл. |
| [162](../patches/tdesktop/0162-feat-unsorted-folder.patch) | папка «Без папки» со всеми чатами, не распределенными по другим папкам (кроме архива). чаты с непрочитанными сообщениями остаются в ней | tele → интерфейс, выкл. |
| [165](../patches/tdesktop/0165-feat-select-several-chats-in-the-list.patch) | Alt+клик выбирает несколько чатов, Shift+клик — диапазон. общая панель позволяет пометить прочитанными, архивировать, заглушить, добавить в папку или покинуть | tele → интерфейс, выкл. |
| [181](../patches/tdesktop/0181-feat-preview-chats-in-the-chat-area.patch) | Alt+клик или удержание аватара открывает чат в режиме только для чтения прямо в основной области, не помечая сообщения прочитанными | tele → интерфейс, выкл. |
| [191](../patches/tdesktop/0191-feat-page-keys-in-lists-and-safer-box-edges.patch) | клавиши Page Up, Page Down, Home и End прокручивают списки и диалоги; случайный клик вблизи границы модального окна больше не закрывает его | tele → интерфейс, выкл. |
| [192](../patches/tdesktop/0192-feat-search-filter-and-export-star-transactions.patch) | поиск, фильтрация, подсчет суммы и экспорт транзакций Звёзд и TON в формат CSV | tele → интерфейс, выкл. |
| [193](../patches/tdesktop/0193-feat-filter-long-lists-by-date.patch) | фильтрация транзакций Звёзд и TON, общих медиа и подарков профиля по конкретному дню или диапазону дат | tele → интерфейс, выкл. |
| [258](../patches/tdesktop/0258-feat-lowercase-the-default-title-bar-label.patch) | текст в заголовке панели по умолчанию выводится в нижнем регистре `tele #N` вместо `TELE #N` | вместе с 10 |
| [264](../patches/tdesktop/0264-feat-smaller-minimum-window-size.patch) | минимальный размер окна программы уменьшен до 256x256 вместо 380x480 | tele → интерфейс, выкл. |
| [275](../patches/tdesktop/0275-feat-smooth-wheel-scrolling.patch) | плавный скроллинг колесиком мыши: плавное скольжение вместо резких скачков в чатах, списке диалогов, разделах и настройках. тачпады работают штатно | tele → интерфейс, выкл. |
| [300](../patches/tdesktop/0300-feat-compact-icon-only-folders.patch) | папки, отображаемые только значками, получают более компактные иконки и кнопки на боковой панели и во вкладках над списком чатов | tele → интерфейс, выкл. |
| [304](../patches/tdesktop/0304-feat-scroll-to-zoom-in-the-media-viewer.patch) | масштабирование колесиком мыши во встроенном просмотрщике медиа. удержание Ctrl или Cmd при прокрутке переключает фото | tele → интерфейс, выкл. |
| [306](../patches/tdesktop/0306-feat-smoother-wheel-glides-in-chats.patch) | прокрутка с частотой обновления вашего монитора, кеширование кадра чата во время скольжения, приостановка анимаций стикеров и GIF до завершения прокрутки | вместе с 275 |
| [318](../patches/tdesktop/0318-fix-glides-in-boxes-no-longer-blank-the-chats-under-.patch) | прокрутка в диалогах, настройках или панелях больше не приводит к мерцанию черным списка чатов под ними | вместе с 306 |
| [325](../patches/tdesktop/0325-feat-close-the-media-viewer-with-mouse-back.patch) | кнопка «Назад» на мыши (Mouse 4) закрывает просмотрщик медиа: фото, видео, оконный просмотрщик и истории | tele → интерфейс, выкл. |
| [1005](../patches/Telegram/lib_ui/0005-feat-ease-mouse-wheel-steps-in-scroll-areas.patch) | компонент плавного скроллинга колесиком мыши на уровне областей прокрутки библиотеки UI | вместе с 275 |
| [1008](../patches/Telegram/lib_ui/0008-feat-glide-at-the-screen-refresh-rate.patch) | синхронизация плавного скольжения с частотой обновления монитора в библиотеке UI | вместе с 275 |

<a id="chats"></a>
## чаты

настройки → tele → чаты.

| # | что делает | тумблер |
|---|---|---|
| [8](../patches/tdesktop/0008-feat-send-quick-replies-in-groups-and-channels.patch) | быстрые ответы Telegram Business в группах и каналах (отправляются как обычные сообщения) | tele → чаты, выкл. |
| [21](../patches/tdesktop/0021-feat-hide-call-buttons.patch) | скрытие кнопок аудио- и видеозвонков в личных чатах и профилях | tele → чаты |
| [24](../patches/tdesktop/0024-feat-hide-sponsored-messages.patch) | блокировка рекламы: отсутствие рекламных сообщений в каналах и ботах, видеорекламы и спонсированных результатов поиска | tele → чаты, выкл. |
| [29](../patches/tdesktop/0029-feat-jump-to-the-first-message-of-a-chat.patch) | переход к самому первому сообщению чата через меню чата | всегда вкл. |
| [62](../patches/tdesktop/0062-feat-hide-or-confirm-call-and-voice-chat-buttons.patch) | скрытие или подтверждение перед началом звонков и голосовых чатов отдельно для личных чатов, групп и каналов | tele → чаты |
| [68](../patches/tdesktop/0068-feat-set-or-remove-chat-backgrounds-only-for-you.patch) | установка или удаление фона конкретного чата только локально для себя | всегда вкл., контекстное меню чата |
| [71](../patches/tdesktop/0071-feat-link-usernames-to-profiles-locally.patch) | локальная привязка юзернеймов к профилям пользователей | tele → чаты |
| [72](../patches/tdesktop/0072-feat-hide-the-mentions-and-reactions-buttons.patch) | скрытие плавающих кнопок перехода к непрочитанным упоминаниям и реакциям внизу чата | tele → чаты, выкл. |
| [76](../patches/tdesktop/0076-feat-open-the-emoji-panel-and-attach-menu-by-click-o.patch) | открытие панели эмодзи и меню прикрепления только по клику, без случайного открытия при наведении курсора | tele → чаты, выкл. |
| [101](../patches/tdesktop/0101-feat-find-chats-by-their-aliases.patch) | поиск чатов и пользователей по вашим локальным псевдонимам | всегда вкл. |
| [121](../patches/tdesktop/0121-feat-use-classic-bubble-padding.patch) | классические отступы пузырей сообщений без лишних пустых полей | tele → чаты, выкл. |
| [122](../patches/tdesktop/0122-feat-hide-mention-and-reaction-badges-in-the-chat-li.patch) | скрытие значков упоминаний и реакций в строках чатов в списке диалогов | tele → чаты, выкл. |
| [126](../patches/tdesktop/0126-feat-pin-sticker-and-emoji-sets.patch) | закрепление любимых наборов стикеров и эмодзи в нижней панели | tele → чаты, выкл. |
| [131](../patches/tdesktop/0131-feat-hide-similar-channels.patch) | скрытие блока рекомендаций похожих каналов при подписке и в профилях каналов | tele → чаты, выкл. |
| [132](../patches/tdesktop/0132-feat-hide-unread-counters.patch) | раздельное скрытие счетчиков непрочитанных сообщений в папках, чатах, трее и панели задач | tele → чаты, выкл. |
| [143](../patches/tdesktop/0143-feat-the-collectible-status-tooltip-in-profiles.patch) | подсказка с подробной информацией о статусе коллекционного подарка в профилях | tele → чаты, выкл. |
| [164](../patches/tdesktop/0164-feat-keep-saved-gifs-and-stickers-past-the-limit.patch) | сохранение GIF и стикеров сверх лимита Telegram локально на этом устройстве | tele → чаты, выкл. |
| [169](../patches/tdesktop/0169-feat-hide-tails-and-bubble-outlines.patch) | скрытие хвостиков у пузырей сообщений и контуров обводки | tele → чаты, выкл. |
| [170](../patches/tdesktop/0170-feat-large-emoji-without-outlines.patch) | отображение больших одиночных эмодзи без белой обводки | tele → чаты, выкл. |
| [174](../patches/tdesktop/0174-feat-sticker-captions.patch) | отправка текстовых подписей вместе со стикерами и показ текста под ними | tele → чаты, выкл. |
| [180](../patches/tdesktop/0180-feat-confirm-sending-reactions.patch) | подтверждение перед установкой реакций в чатах во избежание случайных нажатий | tele → чаты, выкл. |
| [203](../patches/tdesktop/0203-feat-show-who-is-online-in-groups.patch) | отображение списка участников, находящихся сейчас в сети, в заголовке крупных групп | tele → чаты, выкл. |
| [259](../patches/tdesktop/0259-feat-confirm-opening-links.patch) | подтверждение при переходе по внешним ссылкам с показом полного очищенного адреса | tele → чаты, выкл. |
| [271](../patches/tdesktop/0271-feat-choose-double-click-chat-action.patch) | выбор действия по двойному клику на строку чата в списке (открыть, пометить прочитанным, закрепить) | tele → чаты |
| [279](../patches/tdesktop/0279-feat-hide-birthdays.patch) | скрытие праздничных баннеров, конфетти в профиле, торта и кнопки подарка в поле ввода | tele → чаты, выкл. |
| [280](../patches/tdesktop/0280-feat-search-by-message-type.patch) | фильтрация результатов поиска по типу вложений (фото, видео, файлы, музыка, голосовые, кружочки, ссылки) | tele → чаты, выкл. |
| [282](../patches/tdesktop/0282-feat-keep-deleted-chats.patch) | сохранение удаленных собеседником чатов и тем форума в списке с пометкой об удалении | tele → чаты, выкл. |
| [294](../patches/tdesktop/0294-feat-hide-stories-everywhere.patch) | полное скрытие историй (stories) отовсюду: из списка чатов, профилей и медиаленты | tele → чаты, выкл. |
| [295](../patches/tdesktop/0295-feat-show-upload-date-in-media-viewer.patch) | отображение точной даты и времени загрузки файла в окне просмотрщика медиа | tele → чаты, выкл. |
| [298](../patches/tdesktop/0298-feat-save-exact-beginning-of-voice-recordings.patch) | точный захват звука с первой миллисекунды голосовой записи без проглатывания начала | tele → чаты, выкл. |
| [302](../patches/tdesktop/0302-feat-higher-voice-recording-bitrate.patch) | повышенный битрейт записи голосовых сообщений (до 64 кбит/с Opus) для студийного качества | tele → чаты, выкл. |
| [305](../patches/tdesktop/0305-feat-design-the-money-card-with-a-gift.patch) | оформление карты Money в стиле любого из ваших коллекционных подарков со стикерами | tele → чаты, выкл. |
| [328](../patches/tdesktop/0328-feat-restrict-members-from-message-menus-and-find-th.patch) | ограничение прав участников прямо из меню сообщения и быстрый поиск всех сообщений пользователя в группе | tele → чаты, выкл. |

<a id="messages"></a>
## сообщения

настройки → tele → сообщения.

| # | что делает | тумблер |
|---|---|---|
| [17](../patches/tdesktop/0017-feat-show-seconds-in-message-times.patch) | отображение секунд в метках времени сообщений и на сервисных сообщениях | tele → сообщения, выкл. |
| [18](../patches/tdesktop/0018-feat-keep-the-edit-history-of-messages.patch) | сохранение полной истории правок отредактированных сообщений с возможностью просмотра исходных версий | tele → сообщения, выкл. |
| [19](../patches/tdesktop/0019-feat-keep-deleted-messages.patch) | сохранение удаленных собеседником сообщений в чате с отметкой значком корзины или полупрозрачностью | tele → сообщения, выкл. |
| [25](../patches/tdesktop/0025-feat-open-links-without-confirmation.patch) | открытие внешних ссылок сразу в браузере без окна запроса подтверждения | tele → сообщения, выкл. |
| [26](../patches/tdesktop/0026-feat-open-disappearing-media-without-burning-it.patch) | открытие самоуничтожающихся фото и видео без запуска таймера сгорания | tele → сообщения, выкл. |
| [27](../patches/tdesktop/0027-feat-allow-screenshots-of-disappearing-media.patch) | снятие запрета на создание снимков экрана при просмотре самоуничтожающегося медиа | tele → сообщения, выкл. |
| [43](../patches/tdesktop/0043-feat-show-times-on-service-messages.patch) | отображение точного времени отправки на сервисных и системных сообщениях чата | вместе с 17 |
| [45](../patches/tdesktop/0045-feat-compute-messages-starting-with-via-calcmula.patch) | автоматическое вычисление математических выражений, начинающихся со знака `=` (калькулятор Calcmula) | tele → сообщения, выкл. |
| [52](../patches/tdesktop/0052-feat-clean-tracking-parameters-from-links.patch) | автоматическое удаление UTM-меток и трекинговых параметров из входящих и отправляемых ссылок | tele → сообщения, выкл. |
| [53](../patches/tdesktop/0053-feat-reveal-spoilers-automatically.patch) | автоматическое отображение текста и медиа под спойлерами без необходимости кликать по ним | tele → сообщения, выкл. |
| [59](../patches/tdesktop/0059-feat-keep-messages-you-delete-yourself.patch) | сохранение в чате сообщений, удаленных вами для всех участников | tele → сообщения, выкл. |
| [69](../patches/tdesktop/0069-feat-skip-or-quote-deleted-messages-when-replying.patch) | возможность цитировать или отвечать на удаленные сохраненные сообщения | tele → сообщения, выкл. |
| [77](../patches/tdesktop/0077-feat-rewrite-pasted-links-with-your-own-rules.patch) | замена доменов и параметров вставляемых ссылок по собственным правилам (например, Twitter в vxtwitter) | tele → сообщения, выкл. |
| [78](../patches/tdesktop/0078-feat-edit-link-rewrite-rules-and-presets.patch) | редактор пользовательских правил замены ссылок с поддержкой регулярных выражений и пресетов | вместе с 77 |
| [80](../patches/tdesktop/0080-feat-preview-calcmula-results-while-typing.patch) | отображение результата вычислений Calcmula во всплывающей подсказке прямо в процессе ввода | вместе с 45 |
| [96](../patches/tdesktop/0096-feat-keep-drafts-on-this-device.patch) | локальное сохранение черновиков сообщений на устройстве с защитой от сброса сервером | tele → сообщения, выкл. |
| [100](../patches/tdesktop/0100-feat-save-drafts-for-later.patch) | менеджер сохраненных черновиков: просмотр и восстановление заготовок сообщений для разных чатов | tele → сообщения, выкл. |
| [115](../patches/tdesktop/0115-feat-forward-protected-messages-as-copies.patch) | пересылка сообщений из каналов и чатов с запретом копирования в виде обычных копий | tele → сообщения, выкл. |
| [128](../patches/tdesktop/0128-feat-bookmark-messages-and-return-to-where-you-were-.patch) | локальные закладки на важные сообщения и возврат к месту чтения после перехода | tele → сообщения, выкл. |
| [141](../patches/tdesktop/0141-feat-copy-messages-as-markdown-or-html.patch) | копирование сообщений с сохранением разметки в формате Markdown или HTML | tele → сообщения, выкл. |
| [142](../patches/tdesktop/0142-feat-loop-videos-in-the-media-viewer.patch) | зацикленное воспроизведение видео во встроенном просмотрщике медиа | tele → сообщения, выкл. |
| [144](../patches/tdesktop/0144-feat-number-the-lines-of-long-code-blocks.patch) | нумерация строк в длинных блоках моноширинного исходного кода | tele → сообщения, выкл. |
| [147](../patches/tdesktop/0147-feat-rewrite-only-the-link-preview.patch) | возможность заменять ссылку только в блоке предпросмотра, оставляя исходный URL в тексте | вместе с 77 |
| [153](../patches/tdesktop/0153-feat-choose-which-deleted-messages-to-keep.patch) | выборочное сохранение удаленных сообщений: только входящие, только исходящие или от всех | tele → сообщения, выкл. |
| [167](../patches/tdesktop/0167-feat-hide-messages-by-keyword-or-regex.patch) | скрытие нежелательных сообщений в чатах по ключевым словам или регулярным выражениям | tele → сообщения, выкл. |
| [168](../patches/tdesktop/0168-feat-regex-search-in-loaded-history.patch) | полнотекстовый поиск по загруженной истории сообщений чата с поддержкой регулярных выражений | tele → сообщения, выкл. |
| [175](../patches/tdesktop/0175-feat-how-quoted-names-of-deleted-messages-lin.patch) | настройка отображения имен авторов в цитатах удаленных сохраненных сообщений | tele → сообщения |
| [176](../patches/tdesktop/0176-feat-inline-calcmula-results-after.patch) | вставка вычисленного значения Calcmula сразу после знака `=` нажатием Tab или стрелки вправо | вместе с 45 |
| [183](../patches/tdesktop/0183-feat-quote-rich-messages.patch) | цитирование части форматированного сообщения с ответом в расширенном редакторе без потери стилей | tele → сообщения, выкл. |
| [184](../patches/tdesktop/0184-feat-add-multiple-quotes-to-one-reply.patch) | добавление нескольких независимых цитат из разных сообщений в один ответ | вместе с 183 |
| [321](../patches/tdesktop/0321-fix-html-cards-no-longer-crash-when-their-message-go.patch) | устранение сбоя при отображении интерактивных HTML-карточек в чате | всегда вкл. |
| [330](../patches/tdesktop/0330-fix-line-numbers-no-longer-freeze-long-code-blocks.patch) | устранение зависания интерфейса при нумерации строк в очень длинных блоках кода | всегда вкл. |
| [332](../patches/tdesktop/0332-feat-open-json-code-text-and-csv-files-in-tele.patch) | встроенный быстрый просмотрщик файлов JSON, исходного кода, TXT и CSV прямо внутри tele | tele → сообщения, выкл. |

<a id="sending"></a>
## отправка

настройки → tele → отправка.

| # | что делает | тумблер |
|---|---|---|
| [9](../patches/tdesktop/0009-feat-confirm-chat-stickers-gifs-and-previewed-voice-.patch) | раздельные запросы подтверждения перед отправкой стикеров, GIF и голосовых сообщений | tele → отправка, выкл. |
| [10](../patches/tdesktop/0010-feat-default-outgoing-messages-to-silent-with-chat-s.patch) | тихая отправка всех сообщений по умолчанию с возможностью исключений для выбранных чатов | tele → отправка, выкл. |
| [44](../patches/tdesktop/0044-feat-upload-media-in-several-chats-at-once.patch) | параллельная выгрузка и отправка медиафайлов сразу в несколько чатов одновременно | всегда вкл. |
| [50](../patches/tdesktop/0050-feat-move-late-sent-messages-to-the-bottom.patch) | автоматическое перемещение задержавшихся при отправке сообщений в самый низ ленты чата | tele → отправка, выкл. |
| [51](../patches/tdesktop/0051-feat-queue-messages-behind-an-uploading-media.patch) | отправка текстовых сообщений вслед за выгружаемым медиа без сбоев порядка сообщений | tele → отправка, выкл. |
| [67](../patches/tdesktop/0067-feat-send-inline-results-without-via.patch) | отправка результатов inline-ботов без плашки «через @bot» | tele → отправка, выкл. |
| [70](../patches/tdesktop/0070-feat-skip-the-rich-message-prompt-on-paste.patch) | мгновенная вставка форматированного текста без надоедливого всплывающего запроса | tele → отправка, выкл. |
| [98](../patches/tdesktop/0098-feat-send-scheduled-messages-on-time.patch) | отправка отложенных сообщений секунда в секунду встроенным таймером клиента | tele → отправка, выкл. |
| [102](../patches/tdesktop/0102-feat-send-photos-in-hd-by-default.patch) | отправка фотографий в исходном высоком качестве (HD) по умолчанию без сильного сжатия | tele → отправка, выкл. |
| [108](../patches/tdesktop/0108-feat-attach-media-above-the-field-beta.patch) | компоновка медиафайлов над полем ввода с отдельными подписями к каждому файлу | tele → отправка, выкл. |
| [116](../patches/tdesktop/0116-feat-turn-on-docked-media-and-bring-it-to-parity-wit.patch) | закрепленные медиафайлы над полем ввода: поддержка драг-н-дропа, порядка файлов и альбомов | вместе с 108 |
| [119](../patches/tdesktop/0119-feat-send-replies-to-older-messages-past-the-queue.patch) | отправка ответов на старые сообщения вне очереди выгружаемых тяжелых файлов | tele → отправка, выкл. |
| [120](../patches/tdesktop/0120-feat-send-right-away-on-double-enter.patch) | отправка сообщения мгновенно по двойному нажатию Enter | tele → отправка, выкл. |
| [127](../patches/tdesktop/0127-feat-hide-the-gift-button-in-the-message-field.patch) | скрытие кнопки отправки подарка со звездочкой внутри поля набора текста | tele → отправка, выкл. |
| [134](../patches/tdesktop/0134-feat-turn-off-touchpad-gestures.patch) | отключение случайных жестов смахивания тачпада при наборе текста | tele → отправка, выкл. |
| [137](../patches/tdesktop/0137-feat-record-voice-without-fading.patch) | запись голосовых сообщений без затухания и обрезки фоновых частот | tele → отправка, выкл. |
| [160](../patches/tdesktop/0160-feat-resize-the-message-field.patch) | ручное изменение высоты поля ввода текста перетаскиванием разделителя | tele → отправка, выкл. |
| [161](../patches/tdesktop/0161-feat-translate-your-message-before-sending.patch) | перевод текста сообщения на нужный язык прямо перед отправкой | tele → отправка, выкл. |
| [173](../patches/tdesktop/0173-feat-docked-media-as-album-grid.patch) | отображение прикрепленных медиа над полем ввода в виде сетки альбома | вместе с 108 |
| [185](../patches/tdesktop/0185-feat-send-several-gifts-at-once.patch) | массовая отправка нескольких подарков сразу выбранным получателям | tele → отправка, выкл. |
| [262](../patches/tdesktop/0262-feat-preview-voice-and-video-notes-before-sending.patch) | предпросмотр и прослушивание голосовых и видеосообщений (кружочков) перед отправкой | tele → отправка, выкл. |
| [263](../patches/tdesktop/0263-feat-confirm-sending-files-and-media.patch) | подтверждение перед отправкой любых файлов, фото и видео | tele → отправка, выкл. |
| [265](../patches/tdesktop/0265-feat-thinner-photo-editor-brush.patch) | сверхтонкая кисть в встроенном фоторедакторе для аккуратных пометок | tele → отправка, выкл. |
| [266](../patches/tdesktop/0266-feat-pick-brush-colors-from-the-image.patch) | пипетка для выбора цвета кисти непосредственно с редактируемого изображения | tele → отправка, выкл. |
| [267](../patches/tdesktop/0267-feat-less-photo-compression.patch) | щадящий алгоритм сжатия фотографий с сохранением максимальной детализации | tele → отправка, выкл. |
| [273](../patches/tdesktop/0273-feat-chain-mentions.patch) | последовательное упоминание нескольких человек через ПКМ или Tab в списке подсказок | tele → отправка, выкл. |
| [274](../patches/tdesktop/0274-feat-mention-by-name-via-ctrl-click.patch) | упоминание пользователя по отображаемому имени через Ctrl+клик | вместе с 273 |
| [283](../patches/tdesktop/0283-feat-paste-multiple-clipboard-items.patch) | одновременная вставка нескольких объектов из буфера обмена | tele → отправка, выкл. |
| [284](../patches/tdesktop/0284-feat-paste-images-as-stickers.patch) | вставка скопированных изображений напрямую в виде стикеров | tele → отправка, выкл. |
| [285](../patches/tdesktop/0285-feat-edit-sticker-captions-after-sending.patch) | редактирование текстовых подписей под отправленными стикерами | tele → отправка, выкл. |
| [299](../patches/tdesktop/0299-feat-custom-quick-replies.patch) | шаблоны быстрых ответов с поддержкой переменных и шорткатов | tele → отправка, выкл. |
| [301](../patches/tdesktop/0301-feat-send-as-file-by-default.patch) | отправка документов и медиа в виде файлов без сжатия по умолчанию | tele → отправка, выкл. |

<a id="notifications"></a>
## уведомления

настройки → tele → уведомления.

| # | что делает | тумблер |
|---|---|---|
| [157](../patches/tdesktop/0157-feat-notify-when-people-come-online.patch) | уведомления о появлении выбранных пользователей в сети (online) | tele → уведомления, выкл. |
| [208](../patches/tdesktop/0208-feat-notification-centre.patch) | центр уведомлений: системные тосты tele, обновления, отчеты о сбоях и важные сообщения в едином окне | главное меню → уведомления |
| [209](../patches/tdesktop/0209-feat-rate-limit-notices.patch) | информативные предупреждения о превышении лимитов Telegram (FloodWait) с точным временем ожидания | tele → уведомления, выкл. |
| [210](../patches/tdesktop/0210-feat-server-notices.patch) | получение важных системных новостей и обновлений с сервера tele | tele → сервер |
| [211](../patches/tdesktop/0211-feat-dismiss-all-notices.patch) | кнопка «прочитать все» для быстрой очистки центра уведомлений | в центре уведомлений |
| [212](../patches/tdesktop/0212-feat-sound-for-tele-notifications.patch) | настройка звуковых сигналов для собственных уведомлений tele | tele → уведомления |
| [260](../patches/tdesktop/0260-feat-custom-notification-position.patch) | выбор позиции всплывающих тостов на экране (любой из четырех углов) | tele → уведомления |
| [272](../patches/tdesktop/0272-feat-silent-notifications-during-calls.patch) | автоматическое отключение звуков уведомлений во время голосовых и видеозвонков | tele → уведомления, выкл. |
| [292](../patches/tdesktop/0292-feat-group-notifications-by-chat.patch) | группировка всплывающих системных уведомлений по чатам | tele → уведомления, выкл. |
| [293](../patches/tdesktop/0293-feat-hide-notification-text-when-locked.patch) | скрытие текста и автора уведомлений, если приложение заблокировано локальным паролем | tele → приватность, выкл. |
<a id="menus"></a>
## меню

настройки → tele → меню.

| # | что делает | тумблер |
|---|---|---|
| [14](../patches/tdesktop/0014-feat-show-the-peer-id-as-its-own-profile-row.patch) | отображение числового ID чата/пользователя отдельной строкой в профиле с копированием по клику | tele → меню, выкл. |
| [28](../patches/tdesktop/0028-feat-show-the-message-id-in-the-message-menu.patch) | отображение числового ID сообщения в контекстном меню с копированием по нажатию | tele → меню, выкл. |
| [54](../patches/tdesktop/0054-feat-move-tele-tools-to-the-bottom-of-the-message-me.patch) | перенос пунктов инструментов tele в нижнюю часть контекстного меню сообщений | tele → меню, выкл. |
| [55](../patches/tdesktop/0055-feat-copy-custom-emoji-ids-from-the-message-menu.patch) | копирование ID кастомных эмодзи из контекстного меню сообщения | tele → меню, выкл. |
| [57](../patches/tdesktop/0057-feat-reorder-and-hide-message-menu-items.patch) | редактор структуры контекстного меню сообщений: скрытие и изменение порядка пунктов | tele → меню |
| [89](../patches/tdesktop/0089-feat-save-messages-as-a-picture.patch) | сохранение одного или нескольких сообщений в виде красивой картинки-снимка (Message Shots) | tele → меню, выкл. |
| [103](../patches/tdesktop/0103-feat-shots-up-to-4x-and-show-your-messages-as-.patch) | снимки сообщений в разрешении до 4x, скрытие аватаров, времени и фона чата | вместе с 89 |
| [114](../patches/tdesktop/0114-feat-choose-what-shots-show.patch) | детальная настройка элементов снимка: скрытие имени, времени, заголовка и разделителей | вместе с 89 |
| [148](../patches/tdesktop/0148-feat-open-the-message-menu-next-to-the-bubble.patch) | открытие контекстного меню сообщения вплотную к пузырю сообщения, а не под курсором | tele → меню, выкл. |
| [171](../patches/tdesktop/0171-feat-rearrange-menus-with-groups-and-submenus-in-a-m.patch) | конструктор меню: группировка пунктов в подменю, разделители и визуальный редактор | tele → меню |
| [189](../patches/tdesktop/0189-feat-copy-stickers-and-emojis-as-images.patch) | копирование стикеров и эмодзи в буфер обмена как растровых изображений PNG | tele → меню, выкл. |
| [268](../patches/tdesktop/0268-feat-copy-channel-post-id.patch) | копирование чистого числового ID поста в каналах | tele → меню, выкл. |
| [269](../patches/tdesktop/0269-feat-copy-sticker-pack-owner-id.patch) | копирование ID создателя набора стикеров | tele → меню, выкл. |
| [270](../patches/tdesktop/0270-feat-quick-share-qr-code.patch) | мгновенная генерация QR-кода на сообщение, чат или медиафайл из контекстного меню | tele → меню, выкл. |
| [286](../patches/tdesktop/0286-feat-show-skipped-messages-in-shots.patch) | отображение разрыва цепочки («...») при создании снимка непоследовательных сообщений | вместе с 89 |
| [287](../patches/tdesktop/0287-feat-custom-shot-backgrounds.patch) | выбор пользовательского фонового градиента или монохромной заливки для снимков | вместе с 89 |
| [327](../patches/tdesktop/0327-feat-show-skipped-messages-in-shots.patch) | улучшенный рендеринг пропущенных сообщений на снимках высокого разрешения | вместе с 89 |
| [329](../patches/tdesktop/0329-feat-let-scripts-give-their-menu-items-icons.patch) | поддержка кастомных иконок для пунктов меню, добавляемых пользовательскими скриптами | всегда вкл. |

<a id="privacy"></a>
## приватность

настройки → tele → приватность.

| # | что делает | тумблер |
|---|---|---|
| [13](../patches/tdesktop/0013-feat-add-experimental-ghost-controls-with-per-chat-e.patch) | режим невидимки (Ghost Mode): чтение без отметок, скрытие статуса «печатает», online и историй | tele → приватность, выкл. |
| [16](../patches/tdesktop/0016-feat-ignore-users-by-hiding-or-fading-their-messages.patch) | локальное игнорирование пользователей в группах: скрытие или затемнение их сообщений | tele → приватность, выкл. |
| [64](../patches/tdesktop/0064-feat-more-ghost-mode-options.patch) | расширенные параметры невидимки: выборочное отключение набора текста, чтения реакций и опросов | tele → приватность, выкл. |
| [65](../patches/tdesktop/0065-feat-show-ids-on-regular-gifts.patch) | отображение уникальных ID подарков с защитой от отслеживания | tele → приватность, выкл. |
| [73](../patches/tdesktop/0073-feat-pick-ignored-users-and-ghost-chats-like-privacy.patch) | списки исключений для режима невидимки и игнорирования по чатам | tele → приватность |
| [75](../patches/tdesktop/0075-feat-show-names-instead-of-phone-numbers-in-chat-hea.patch) | отображение имен пользователей вместо номеров телефонов в шапке чата | tele → приватность, выкл. |
| [113](../patches/tdesktop/0113-feat-never-block-screen-capture.patch) | снятие системных блокировок захвата экрана и защиты от скриншотов | tele → приватность, выкл. |
| [158](../patches/tdesktop/0158-feat-streamer-mode.patch) | режим стримера: скрытие личных данных, номеров, текста тостов и приложения от захвата экрана | tele → приватность, выкл. |
| [172](../patches/tdesktop/0172-feat-hide-phone-numbers-in-profiles.patch) | скрытие номеров телефонов в чужих и собственном профиле | tele → приватность, выкл. |
| [187](../patches/tdesktop/0187-feat-local-password-for-stars-and-gift-actions.patch) | локальный пароль (PIN-код) для подтверждения трат Звёзд, передачи и улучшения подарков | tele → приватность, выкл. |
| [261](../patches/tdesktop/0261-feat-suppress-audio-video-call-pings.patch) | подавление фоновых сетевых пингов при входящих аудио- и видеозвонках | tele → приватность, выкл. |
| [276](../patches/tdesktop/0276-feat-peek-last-seen.patch) | временный подсмотр скрытого времени последнего захода собеседника (Peek Last Seen) | tele → приватность, выкл. |
| [277](../patches/tdesktop/0277-feat-protect-secret-media-from-caching.patch) | запрет сохранения самоуничтожающихся медиафайлов во временном дисковом кеше системы | tele → приватность, выкл. |
| [278](../patches/tdesktop/0278-feat-secret-chats-prototype.patch) | прототип секретных чатов с локальным паролем, подтверждением ключей и сквозным шифрованием | tele → приватность, выкл. |
| [288](../patches/tdesktop/0288-feat-hide-blocked-users-messages.patch) | полное скрытие сообщений заблокированных пользователей в общих группах | tele → приватность, выкл. |
| [289](../patches/tdesktop/0289-feat-anti-recall-protection.patch) | защита от принудительного удаления сообщений собеседником через серверные отметки | tele → приватность, выкл. |
| [290](../patches/tdesktop/0290-feat-offline-scheduled-send.patch) | отложенная отправка сообщений с автоматическим переходом в offline сразу после передачи | tele → приватность, выкл. |

<a id="profiles-and-ids"></a>
## профили и id

настройки → tele → профили и id.

| # | что делает | тумблер |
|---|---|---|
| [6](../patches/tdesktop/0006-feat-show-peer-ids-in-profiles.patch) | числовой ID пользователя, группы, супергруппы или канала прямо под описанием профиля | tele → профили и id, выкл. |
| [23](../patches/tdesktop/0023-feat-show-the-data-center-in-profiles.patch) | отображение номера дата-центра (DC) аккаунта и аватара в профиле | tele → профили и id, выкл. |
| [46](../patches/tdesktop/0046-feat-move-show-peer-ids-into-tele-settings.patch) | управление отображением ID в профилях перенесено в настройки tele | всегда вкл. |
| [48](../patches/tdesktop/0048-feat-open-collectible-gifts-in-see.tg.patch) | открытие коллекционных подарков во внешнем верификаторе see.tg | tele → профили и id, выкл. |
| [74](../patches/tdesktop/0074-feat-show-what-s-new-in-a-local-tele-chat.patch) | локальный чат tele с историей новостей и изменений после обновлений | tele → профили и id, выкл. |
| [83](../patches/tdesktop/0083-feat-show-collectible-prices-at-the-purchase-date.patch) | отображение цены покупки и текущей рыночной стоимости подарка в TON | tele → профили и id, выкл. |
| [95](../patches/tdesktop/0095-feat-show-id-and-dc-in-one-row.patch) | компактное отображение ID и номера дата-центра в одну строку в профиле | tele → профили и id, выкл. |
| [146](../patches/tdesktop/0146-feat-show-the-media-s-data-center-in-the-media-viewe.patch) | отображение дата-центра (DC) просматриваемого медиафайла в просмотрщике | tele → профили и id, выкл. |
| [186](../patches/tdesktop/0186-feat-dim-hidden-gifts-and-select-several.patch) | визуальное затемнение скрытых подарков и массовый выбор подарков в профиле | tele → профили и id, выкл. |
| [188](../patches/tdesktop/0188-feat-search-gifts.patch) | поиск и мгновенная фильтрация подарков в профиле по названию и атрибутам | tele → профили и id, выкл. |
| [194](../patches/tdesktop/0194-feat-gift-grid-builder.patch) | конструктор сетки витрины профиля: ручная расстановка подарков и выбор рамок | tele → профили и id, выкл. |
| [200](../patches/tdesktop/0200-feat-gift-studio.patch) | Студия Подарков: создание уникальных коллекционных подарков из оригинальных ассетов с экспортом | tele → профили и id |
| [201](../patches/tdesktop/0201-feat-fake-gift-upgrades.patch) | симуляция улучшения подарков (Fake Upgrades) с оригинальной рулеткой без списания Звёзд | tele → профили и id, выкл. |
| [275](../patches/tdesktop/0275-feat-display-registration-date.patch) | приблизительная дата регистрации аккаунта на основе диапазона ID | tele → профили и id, выкл. |
| [291](../patches/tdesktop/0291-feat-bot-api-id-format-toggle.patch) | переключатель формата ID: обычный числовой или формат Bot API с префиксом `-100` | tele → профили и id, выкл. |
| [296](../patches/tdesktop/0296-feat-profile-photo-viewer-zoom.patch) | плавное масштабирование и полноразмерный просмотр любых аватаров профиля | всегда вкл. |
| [297](../patches/tdesktop/0297-feat-copy-clean-raw-id.patch) | копирование чистого числового ID без префиксов по долгому нажатию | всегда вкл. |
| [303](../patches/tdesktop/0303-feat-fill-the-whole-profile-with-the-blurred-photo-s.patch) | фоновое заполнение всего окна профиля размытым фото контакта | tele → профили и id, выкл. |

<a id="gift-studio"></a>
### студия подарков

полноценный конструктор коллекционных предметов: создание уникальных подарков из оригинальных деталей Telegram с выбором моделей, цветовых палитр, фактур и символов. поддержка экспорта в PNG, MP4, GIF и стикеры TGS.

<a id="bots"></a>
## боты

настройки → tele → боты.

| # | что делает | тумблер |
|---|---|---|
| [5](../patches/tdesktop/0005-feat-show-bot-button-payloads-in-tooltips.patch) | показ callback-данных и URL inline-кнопок ботов во всплывающих подсказках | tele → боты, выкл. |
| [202](../patches/tdesktop/0202-feat-turn-off-web-app-confirmations.patch) | открытие проверенных мини-приложений Telegram Mini Apps без повторного окна согласия | tele → боты, выкл. |
| [281](../patches/tdesktop/0281-feat-bot-menu-button-inspector.patch) | инспектор кнопок меню ботов с копированием payload в JSON | tele → боты, выкл. |
| [314](../patches/tdesktop/0314-feat-hide-bot-commands-menu-button.patch) | скрытие кнопки меню команд бота слева от поля ввода | tele → боты, выкл. |
| [315](../patches/tdesktop/0315-feat-inspect-web-app-start-param.patch) | просмотр и копирование параметра `start_param` в ссылках на ботов и веб-приложения | всегда вкл. |
| [316](../patches/tdesktop/0316-feat-hide-bot-edited-mark.patch) | скрытие плашки «изменено» для сообщений от ботов | tele → боты, выкл. |

<a id="debug"></a>
## отладка

настройки → tele → отладка.

| # | что делает | тумблер |
|---|---|---|
| [31](../patches/tdesktop/0031-feat-view-messages-and-telegram-objects-as-tl.patch) | просмотр сообщений и структур Telegram в сыром виде TL-схем на schema.jppgr.am | tele → отладка, выкл. |
| [90](../patches/tdesktop/0090-feat-debug-logs-and-an-mtproto-inspector.patch) | интерактивная консоль MTProto (`Ctrl+Alt+M`): вызов любых API методов Telegram с подсказками схемы | tele → отладка |
| [91](../patches/tdesktop/0091-feat-mtproto-autocomplete-and-history.patch) | автодополнение методов, подсветка синтаксиса и история запросов в консоли MTProto | вместе с 90 |
| [92](../patches/tdesktop/0092-feat-export-mtproto-responses.patch) | экспорт ответов API Telegram в форматы JSON и JSON5 | вместе с 90 |
| [198](../patches/tdesktop/0198-feat-mtproto-console.patch) | встроенный инспектор сетевых пакетов MTProto и расширенное логирование сессий | tele → отладка |
| [285](../patches/tdesktop/0285-feat-force-wallet-enable.patch) | принудительная активация интерфейса встроенного кошелька Wallet до его сервера | tele → отладка, выкл. |
| [313](../patches/tdesktop/0313-feat-log-scroll-frame-rate.patch) | замер и запись плавности прокрутки (FPS и времени кадров) в системный log.txt | tele → отладка, выкл. |
| [317](../patches/tdesktop/0317-feat-simulate-connection-states.patch) | симуляция различных сетевых состояний (ожидание сети, обновление, переподключение) | tele → отладка |
| [320](../patches/tdesktop/0320-fix-listing-accounts-from-a-script-no-longer-crashes.patch) | предотвращение сбоя при получении списка активных аккаунтов через API скриптов | всегда вкл. |
| [323](../patches/tdesktop/0323-fix-passkey-prompts-no-longer-count-as-freezes.patch) | ожидание ответа системного окна Passkey больше не распознается как зависание интерфейса | всегда вкл. |
| [324](../patches/tdesktop/0324-fix-loading-older-messages-no-longer-crashes-on-a-me.patch) | предотвращение падения при быстрой подгрузке старых сообщений в насыщенных медиачатах | всегда вкл. |
| [326](../patches/tdesktop/0326-fix-me-and-other-peer-shortcuts-work-everywhere-in-t.patch) | поддержка шортката `me` и локальных алиасов во всех консольных командах tele | всегда вкл. |

<a id="server"></a>
## сервер

настройки → tele → сервер.

| # | что делает | тумблер |
|---|---|---|
| [61](../patches/tdesktop/0061-feat-server-and-updates-on-the-tele-settings-pa.patch) | адрес сервера tele, статус подключения и кнопка ручного обновления списка меток | tele → сервер |
| [81](../patches/tdesktop/0081-feat-clear-server-data-and-explain-custom-verificati.patch) | кнопка «Очистить кеш данных сервера» и справка по алгоритму хеширования верификаций | tele → сервер |
| [93](../patches/tdesktop/0093-feat-usernames-from-the-tele-server.patch) | сопоставление дополнительных коротких юзернеймов с публичного списка сервера | tele → сервер, выкл. |
| [210](../patches/tdesktop/0210-feat-server-notices.patch) | получение сервисных уведомлений и анонсов от сервера tele | tele → сервер |
| [213](../patches/tdesktop/0213-feat-disable-server-badge-verification.patch) | полное отключение загрузки сторонних галочек верификации с сервера | tele → сервер |

<a id="backup"></a>
## резервные копии

настройки → tele → резервные копии.

| # | что делает | тумблер |
|---|---|---|
| [107](../patches/tdesktop/0107-feat-export-and-import-tele-settings.patch) | экспорт всех настроек tele в переносимый JSON-файл и импорт с наглядным предпросмотром | tele → резервные копии |
| [108](../patches/tdesktop/0108-feat-selective-backup-restore.patch) | выборочный импорт: возможность применить только выбранные категории настроек из файла | вместе с 107 |

<a id="updates"></a>
## обновления

настройки → tele → обновления.

| # | что делает | тумблер |
|---|---|---|
| [6](../patches/tdesktop/0006-feat-update-from-the-tele-github-releases.patch) | автоматическая фоновая проверка и загрузка криптографически подписанных обновлений tele | tele → обновления |
| [39](../patches/tdesktop/0039-feat-show-what-s-new-in-tele-after-an-update.patch) | показ интерактивного окна со списком изменений «Что нового» сразу после обновления | tele → обновления |
| [319](../patches/tdesktop/0319-fix-updates-on-macos-keep-the-dock-icon.patch) | сохранение настроенной иконки tele в Dock при фоновом обновлении на macOS | всегда вкл. |
| [322](../patches/tdesktop/0322-fix-gifts-in-money-look-like-gift-cards-instead-of-a.patch) | корректное отображение подарков в кошельке Money в виде подарочных карт | всегда вкл. |

<a id="everywhere"></a>
## везде

функции, включенные постоянно или не требующие отдельного переключателя.

| # | что делает | тумблер |
|---|---|---|
| [1](../patches/tdesktop/0001-feat-show-the-tele-build-number-in-the-title-bar.patch) | показ номера сборки tele в заголовке окна | всегда вкл., см. 10 |
| [2](../patches/tdesktop/0002-feat-add-a-tele-section-to-the-settings.patch) | выделенный раздел настроек tele прямо под выбором языка | всегда вкл. |
| [7](../patches/tdesktop/0007-feat-rename-the-app-to-tele.patch) | приложение носит имя tele: исполняемый файл `tele.exe`, отдельная иконка на панели задач, изолированные каталоги данных | всегда вкл. |
| [11](../patches/tdesktop/0011-feat-remove-the-account-limit.patch) | снятие лимита учетных записей (поддержка до 1536 активных аккаунтов) | всегда вкл. |
| [12](../patches/tdesktop/0012-feat-show-checkmarks-and-custom-verification-everywh.patch) | отображение галочек и кастомной верификации в списке аккаунтов, меню, настройках и сообщениях | всегда вкл., в сообщениях: tele → чаты, выкл. |
| [15](../patches/tdesktop/0015-feat-copy-links-to-tele-settings.patch) | правый клик по любой настройке tele копирует прямую ссылку для быстрого перехода | всегда вкл. |
| [20](../patches/tdesktop/0020-fix-fade-every-unsupported-experimental-option.patch) | автоматическое затемнение экспериментальных опций, не поддерживаемых текущей версией ОС | всегда вкл. |
| [40](../patches/tdesktop/0040-feat-call-the-app-tele-everywhere.patch) | использование имени tele во всех системных уведомлениях, диалогах и окнах | всегда вкл. |
| [47](../patches/tdesktop/0047-feat-show-the-tele-build-in-the-main-menu.patch) | номер сборки tele отображается в нижней части главного меню приложения | всегда вкл. |
| [86](../patches/tdesktop/0086-feat-set-your-own-app-and-tray-icons.patch) | поддержка установки произвольных иконок приложения из PNG и ICO | всегда вкл. |
| [109](../patches/tdesktop/0109-feat-choose-which-app-opens-each-service.patch) | ассоциация внешних ссылок и сервисов с установленными приложениями системы | всегда вкл. |
| [118](../patches/tdesktop/0118-feat-hide-settings-until-their-parent-is-on.patch) | динамическое скрытие зависимых поднастроек, пока не включен основной родительский тумблер | всегда вкл. |
| [155](../patches/tdesktop/0155-feat-regroup-tele-settings-pages.patch) | удобное разбиение настроек tele на тематические категории с быстрым переключением | всегда вкл. |
| [307](../patches/tdesktop/0307-fix-quote-the-fee-of-a-wallet-key-update-again.patch) | точный предварительный расчет сетевой комиссии TON при обновлении ключей кошелька | всегда вкл. |
| [308](../patches/tdesktop/0308-build-take-wallet-engine-from-gettele-money-for-priv.patch) | интеграция криптографического движка gettele money для приватных транзакций | всегда вкл. |
| [309](../patches/tdesktop/0309-feat-import-wallets-from-private-keys.patch) | импорт TON-кошельков напрямую из приватных ключей и сид-фраз | tele → кошелек |
| [310](../patches/tdesktop/0310-feat-copy-secret-words-without-waiting.patch) | моментальное копирование мнемонической фразы кошелька без искусственных задержек таймера | всегда вкл. |
| [311](../patches/tdesktop/0311-feat-hide-the-other-balances-above-the-money-card.patch) | скрытие второстепенных балансов над картой Money для приватности | tele → кошелек |
| [312](../patches/tdesktop/0312-build-fetch-litehtml-for-html-bubbles.patch) | движок litehtml для легковесного отображения форматированных HTML-карточек | всегда вкл. |
| [331](../patches/tdesktop/0331-fix-code-blocks-keep-the-indent-of-their-first-line.patch) | сохранение исходных отступов первой строки в моноширинных блоках программного кода | всегда вкл. |

<a id="other"></a>
## прочее

| # | что делает | тумблер |
|---|---|---|
| [138](../patches/tdesktop/0138-feat-turn-off-ai-features.patch) | отключение всех встроенных AI-функций и подсказок Telegram | tele → прочее, выкл. |
| [178](../patches/tdesktop/0178-feat-reduce-network-activity-on-battery.patch) | режим энергосбережения: снижение фоновой сетевой активности при работе от батареи ноутбука | tele → прочее, выкл. |
| [274](../patches/tdesktop/0274-feat-hardware-acceleration-tuning.patch) | тонкая настройка параметров аппаратного ускорения видео и графики | tele → прочее |
| [282](../patches/tdesktop/0282-feat-smooth-resizing.patch) | плавное изменение размеров окна программы без артефактов перерисовки | tele → прочее, выкл. |
