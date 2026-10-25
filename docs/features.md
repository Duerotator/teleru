# функции tele

every tele patch, grouped by the settings page that holds its switch. [releases](releases.md) has the same rows by the release that brought them.

everything tele adds lives in settings → tele, right below the language row, grouped into pages. the search at the top of the page, and the main settings search, find every tele setting. right-click any of them to copy a link that opens it.

резервное копирование экспортирует настройки tele в файл, которым можно поделиться, и импортирует их с наглядным предпросмотром изменений. оно охватывает переключатели и списки tele, но не затрагивает системные параметры самого telegram (например, масштаб интерфейса) или данные конкретных аккаунтов (локальные закрепления, наборы, закладки, локальные папки). чтобы перенести абсолютно всё на другой ПК, просто скопируйте всю папку `tdata` рядом с исполняемым файлом tele.

"toggle" is where the switch is and its default. `always on` has no switch, `with N` follows the switch of patch N.

more about some of them: [title bar template](title-template.md), [link cleaner](link-cleaner.md), [launch flags](launch-flags.md), [tele server](server.md).

<a id="interface"></a>
## интерфейс

настройки → tele → интерфейс.

| # | what it does | toggle |
|---|---|---|
| [10](../patches/tdesktop/0010-feat-make-the-title-bar-label-a-live-template.patch) | тихая отправка всех сообщений по умолчанию с возможностью исключений для выбранных чатов | tele → интерфейс |
| [22](../patches/tdesktop/0022-feat-lowercase-every-interface-text.patch) | переводит весь интерфейс в нижний регистр. сообщения и имена остаются без изменений | tele → interface, off, требуется перезапуск |
| [30](../patches/tdesktop/0030-feat-hide-the-all-chats-folder.patch) | скрывает папку «Все чаты», если настроены другие папки; список сразу открывается на первой папке | tele → интерфейс, выкл. |
| [35](../patches/tdesktop/0035-feat-lowercase-tele-s-own-texts-too.patch) | нижний регистр применяется также к собственным текстам tele и окну отчета о сбоях | вместе с 22 |
| [37](../patches/tdesktop/0037-feat-turn-off-animated-userpics.patch) | возможность сделать анимированные аватары статичными: раздельно для списка чатов и внутри чатов/профилей | tele → interface, off, in chats and profiles: tele → chats, off |
| [40](../patches/tdesktop/0040-feat-customize-the-window-title-and-format-template-.patch) | заголовок окна ОС (панель задач, Alt+Tab, рамка окна) также поддерживает шаблоны или синхронизацию с панелью. переменные принимают модификаторы вроде `{weekday | tele → интерфейс |
| [81](../patches/tdesktop/0081-feat-move-chats-instantly-in-the-chat-list.patch) | чаты мгновенно перемещаются на новую позицию в списке без задержки при наведении курсора мыши | tele → интерфейс, выкл. |
| [83](../patches/tdesktop/0083-feat-set-your-own-app-and-tray-icons.patch) | установка собственных иконок приложения и трея из любого изображения; иконка в трее может следовать за иконкой приложения | tele → interface → app icon |
| [96](../patches/tdesktop/0096-feat-redesign-the-title-template-editor.patch) | обновленный редактор шаблона заголовка: переменные в виде чипов, палитра модификаторов и готовые пресеты | вместе с 10 |
| [116](../patches/tdesktop/0116-feat-hide-communities.patch) | скрытие сообществ (community): входящие в них чаты остаются в общем списке как обычные чаты | tele → интерфейс, выкл. |
| [122](../patches/tdesktop/0122-feat-pin-chats-past-the-limit.patch) | закрепление большего числа чатов, чем разрешает telegram: дополнительные закрепления сохраняются локально, помечаются контурным значком булавки и свободно перемещаются среди серверных | tele → интерфейс, выкл. |
| [123](../patches/tdesktop/0123-feat-folders-past-the-limit.patch) | больше папок и больше чатов в каждой папке, чем разрешает telegram: превышающие лимит сохраняются локально на этом устройстве | tele → интерфейс, выкл. |
| [128](../patches/tdesktop/0128-feat-hide-message-previews-in-the-chat-list.patch) | скрытие превью текста сообщений в списке чатов с компактной высотой строк | tele → интерфейс, выкл. |
| [149](../patches/tdesktop/0149-feat-make-build-the-bare-build-number.patch) | переменная `{build}` возвращает чистый номер сборки, стандартный заголовок — TELE #{build}, пользовательские шаблоны обновляются автоматически | вместе с 10 |
| [151](../patches/tdesktop/0151-feat-interface-scale-in-1-steps.patch) | ползунок масштабирования интерфейса перемещается с шагом в 1% | tele → интерфейс, выкл. |
| [153](../patches/tdesktop/0153-feat-reduce-motion.patch) | режим уменьшения движения: отключение всех анимаций (кроме звонков), зацикливания стикеров, всплесков реакций и эффектов сообщений | tele → интерфейс, выкл. |
| [161](../patches/tdesktop/0161-feat-unsorted-folder.patch) | папка «Без папки» со всеми чатами, не распределенными по другим папкам (кроме архива). чаты с непрочитанными сообщениями остаются в ней | tele → интерфейс, выкл. |
| [164](../patches/tdesktop/0164-feat-select-several-chats-in-the-list.patch) | Alt+клик выбирает несколько чатов, Shift+клик — диапазон. общая панель позволяет пометить прочитанными, архивировать, заглушить, добавить в папку или покинуть | tele → интерфейс, выкл. |
| [180](../patches/tdesktop/0180-feat-preview-chats-in-the-chat-area.patch) | Alt+клик или удержание аватара открывает чат в режиме только для чтения прямо в основной области, не помечая сообщения прочитанными | tele → интерфейс, выкл. |
| [190](../patches/tdesktop/0190-feat-page-keys-in-lists-and-safer-box-edges.patch) | клавиши Page Up, Page Down, Home и End прокручивают списки и диалоги; случайный клик вблизи границы модального окна больше не закрывает его | tele → интерфейс, выкл. |
| [191](../patches/tdesktop/0191-feat-search-filter-and-export-star-transactions.patch) | поиск, фильтрация, подсчет суммы и экспорт транзакций Звёзд и TON в формат CSV | tele → интерфейс, выкл. |
| [192](../patches/tdesktop/0192-feat-filter-long-lists-by-date.patch) | фильтрация транзакций Звёзд и TON, общих медиа и подарков профиля по конкретному дню или диапазону дат | tele → интерфейс, выкл. |
| [257](../patches/tdesktop/0257-feat-lowercase-the-default-title-bar-label.patch) | текст в заголовке панели по умолчанию выводится в нижнем регистре `tele #N` вместо `TELE #N` | вместе с 10 |
| [263](../patches/tdesktop/0263-feat-smaller-minimum-window-size.patch) | минимальный размер окна программы уменьшен до 256x256 вместо 380x480 | tele → интерфейс, выкл. |
| [274](../patches/tdesktop/0274-feat-smooth-wheel-scrolling.patch) | приблизительная дата регистрации аккаунта на основе диапазона ID | tele → интерфейс, выкл. |
| [299](../patches/tdesktop/0299-feat-compact-icon-only-folders.patch) | папки, отображаемые только значками, получают более компактные иконки и кнопки на боковой панели и во вкладках над списком чатов | tele → интерфейс, выкл. |
| [303](../patches/tdesktop/0303-feat-scroll-to-zoom-in-the-media-viewer.patch) | масштабирование колесиком мыши во встроенном просмотрщике медиа. удержание Ctrl или Cmd при прокрутке переключает фото | tele → интерфейс, выкл. |
| [304](../patches/tdesktop/0304-feat-smoother-wheel-glides-in-chats.patch) | прокрутка с частотой обновления вашего монитора, кеширование кадра чата во время скольжения, приостановка анимаций стикеров и GIF до завершения прокрутки | вместе с 274 |
| [318](../patches/tdesktop/0318-feat-close-the-media-viewer-with-mouse-back.patch) | кнопка «Назад» на мыши (Mouse 4) закрывает просмотрщик медиа: фото, видео, оконный просмотрщик и истории | tele → интерфейс, выкл. |
| [333](../patches/tdesktop/0333-fix-smooth-scrolling-no-longer-leaves-blank-areas.patch) | список чатов и чат больше не становятся пустыми или чёрными местами, пока другой плавно прокручивается: они продолжают отрисовку во время скольжения | вместе с 304 |
| [1004](../patches/Telegram/lib_ui/0004-feat-ease-mouse-wheel-steps-in-scroll-areas.patch) | компонент плавного скроллинга колесиком мыши на уровне областей прокрутки библиотеки UI | вместе с 274 |
| [1007](../patches/Telegram/lib_ui/0007-feat-glide-at-the-screen-refresh-rate.patch) | синхронизация плавного скольжения с частотой обновления монитора в библиотеке UI | вместе с 274 |

<a id="chats"></a><a id="gift-studio"></a>
## чаты

настройки → tele → чаты.

| # | what it does | toggle |
|---|---|---|
| [8](../patches/tdesktop/0008-feat-send-quick-replies-in-groups-and-channels.patch) | быстрые ответы Telegram Business в группах и каналах (отправляются как обычные сообщения) | tele → чаты, выкл. |
| [21](../patches/tdesktop/0021-feat-hide-call-buttons.patch) | скрытие кнопок аудио- и видеозвонков в личных чатах и профилях | tele → чаты |
| [24](../patches/tdesktop/0024-feat-hide-sponsored-messages.patch) | блокировка рекламы: отсутствие рекламных сообщений в каналах и ботах, видеорекламы и спонсированных результатов поиска | tele → чаты, выкл. |
| [34](../patches/tdesktop/0034-feat-hide-the-mtproxy-sponsor-channel.patch) | скрытие закрепленного спонсорского канала при подключении через MTProxy | tele → чаты, выкл. |
| [61](../patches/tdesktop/0061-feat-hide-or-confirm-call-and-voice-chat-buttons.patch) | скрытие или подтверждение перед началом звонков и голосовых чатов отдельно для личных чатов, групп и каналов | tele → чаты |
| [67](../patches/tdesktop/0067-feat-set-or-remove-chat-backgrounds-only-for-you.patch) | установка или удаление фона конкретного чата только локально для себя | tele → chats → chat backgrounds |
| [70](../patches/tdesktop/0070-feat-link-usernames-to-profiles-locally.patch) | локальная привязка юзернеймов к профилям пользователей | tele → chats → username aliases |
| [71](../patches/tdesktop/0071-feat-hide-the-mentions-and-reactions-buttons.patch) | скрытие плавающих кнопок перехода к непрочитанным упоминаниям и реакциям внизу чата | tele → чаты, выкл. |
| [75](../patches/tdesktop/0075-feat-open-the-emoji-panel-and-attach-menu-by-click-o.patch) | открытие панели эмодзи и меню прикрепления только по клику, без случайного открытия при наведении курсора | tele → чаты, выкл. |
| [100](../patches/tdesktop/0100-feat-find-chats-by-their-aliases.patch) | поиск чатов и пользователей по вашим локальным псевдонимам | вместе с 70 |
| [120](../patches/tdesktop/0120-feat-use-aliases-for-inline-bots.patch) | классические отступы пузырей сообщений без лишних пустых полей | вместе с 70 |
| [121](../patches/tdesktop/0121-feat-hide-mention-and-reaction-badges-in-the-chat-li.patch) | скрытие значков упоминаний и реакций в строках чатов в списке диалогов | вместе с 71 |
| [126](../patches/tdesktop/0126-feat-pin-sticker-and-emoji-sets.patch) | скрытие кнопки отправки подарка со звездочкой внутри поля набора текста | tele → чаты, выкл. |
| [130](../patches/tdesktop/0130-feat-turn-off-touchpad-gestures.patch) | скрытие блока рекомендаций похожих каналов при подписке и в профилях каналов | tele → чаты, выкл. |
| [131](../patches/tdesktop/0131-feat-hide-similar-channels.patch) | раздельное скрытие счетчиков непрочитанных сообщений в папках, чатах, трее и панели задач | tele → чаты, выкл. |
| [133](../patches/tdesktop/0133-feat-hide-and-show-the-pinned-bar-from-the-chat-menu.patch) | отключение случайных жестов смахивания тачпада при наборе текста | tele → chats, on |
| [136](../patches/tdesktop/0136-feat-turn-off-ai-features.patch) | запись голосовых сообщений без затухания и обрезки фоновых частот | tele → чаты, выкл. |
| [163](../patches/tdesktop/0163-feat-keep-saved-gifs-and-stickers-past-the-limit.patch) | сохранение GIF и стикеров сверх лимита Telegram локально на этом устройстве | tele → чаты, выкл. |
| [167](../patches/tdesktop/0167-feat-regex-search-in-loaded-history.patch) | полнотекстовый поиск по загруженной истории сообщений чата с поддержкой регулярных выражений | tele → чаты, выкл. |
| [174](../patches/tdesktop/0174-feat-sticker-captions.patch) | настройка отображения имен авторов в цитатах удаленных сохраненных сообщений | tele → чаты, выкл. |
| [178](../patches/tdesktop/0178-feat-copy-or-delete-aliases-from-their-menu.patch) | правый клик по алиасу (псевдониму) в профиле или сообщении для его копирования, удаления или перехода в профиль | вместе с 70 |
| [234](../patches/tdesktop/0234-feat-your-own-reaction-strip.patch) | настройка количества и порядка быстрых реакций над меню сообщения: клик в предпросмотре закрепляет реакцию, перетаскивание меняет порядок | tele → чаты, выкл. |
| [253](../patches/tdesktop/0253-feat-send-quick-replies-by-their-exact-name.patch) | сообщение, состоящее ровно из /имя, отправляет ваш быстрый ответ с этим именем вместо текста команды, и этот быстрый ответ предлагается первым в подсказках | tele → чаты, выкл. |
| [267](../patches/tdesktop/0267-feat-show-online-members-in-big-groups.patch) | копирование чистого числового ID поста в каналах | tele → чаты, выкл. |
| [268](../patches/tdesktop/0268-feat-select-more-than-100-messages.patch) | копирование ID создателя набора стикеров | tele → чаты, выкл. |
| [278](../patches/tdesktop/0278-feat-hide-birthday-banners-and-effects.patch) | скрытие праздничных баннеров, конфетти в профиле, торта и кнопки подарка в поле ввода | tele → чаты, выкл. |
| [280](../patches/tdesktop/0280-feat-filter-chat-search-by-message-type.patch) | инспектор кнопок меню ботов с копированием payload в JSON | tele → чаты, выкл. |
| [287](../patches/tdesktop/0287-feat-turn-off-money.patch) | полное скрытие сообщений заблокированных пользователей в общих группах | tele → chats, off, требуется перезапуск |
| [309](../patches/tdesktop/0309-feat-hide-the-other-balances-above-the-money-card.patch) | скрытие второстепенных балансов над картой Money для приватности | tele → чаты, выкл. |
| [314](../patches/tdesktop/0314-feat-filter-stickers-and-emoji-by-format.patch) | симуляция различных сетевых состояний (ожидание сети, обновление, переподключение) | tele → чаты, выкл. |
| [323](../patches/tdesktop/0323-feat-open-json-code-text-and-csv-files-in-tele.patch) | встроенный быстрый просмотрщик файлов JSON, исходного кода, TXT и CSV прямо внутри tele | tele → chats, on |

<a id="messages"></a>
## сообщения

настройки → tele → сообщения.

| # | what it does | toggle |
|---|---|---|
| [17](../patches/tdesktop/0017-feat-show-seconds-in-message-times.patch) | отображение секунд в метках времени сообщений и на сервисных сообщениях | tele → сообщения, выкл. |
| [18](../patches/tdesktop/0018-feat-keep-the-edit-history-of-messages.patch) | сохранение полной истории правок отредактированных сообщений с возможностью просмотра исходных версий | tele → сообщения, выкл. |
| [19](../patches/tdesktop/0019-feat-keep-deleted-messages.patch) | сохранение удаленных собеседником сообщений в чате с отметкой значком корзины или полупрозрачностью | tele → сообщения, выкл. |
| [25](../patches/tdesktop/0025-feat-open-links-without-confirmation.patch) | открытие внешних ссылок сразу в браузере без окна запроса подтверждения | tele → сообщения, выкл. |
| [26](../patches/tdesktop/0026-feat-open-disappearing-media-without-burning-it.patch) | открытие самоуничтожающихся фото и видео без запуска таймера сгорания | tele → сообщения, выкл. |
| [50](../patches/tdesktop/0050-feat-open-links-in-their-desktop-apps.patch) | отправка текстовых сообщений вслед за выгружаемым медиа без сбоев порядка сообщений | tele → сообщения → открывать ссылки в приложениях |
| [51](../patches/tdesktop/0051-feat-clean-tracking-parameters-from-links.patch) | автоматическое удаление UTM-меток и трекинговых параметров из входящих и отправляемых ссылок | tele → сообщения, выкл. |
| [52](../patches/tdesktop/0052-feat-reveal-spoilers-automatically.patch) | автоматическое отображение текста и медиа под спойлерами без необходимости кликать по ним | tele → сообщения, выкл. |
| [57](../patches/tdesktop/0057-feat-keep-messages-you-delete-yourself.patch) | сообщения, удаленные вами лично, также сохраняются, а не только удаленные собеседниками | вместе с 19 |
| [60](../patches/tdesktop/0060-feat-show-edit-history-as-a-chat.patch) | адрес сервера tele, статус подключения и кнопка ручного обновления списка меток | вместе с 18 |
| [68](../patches/tdesktop/0068-feat-skip-or-quote-deleted-messages-when-replying.patch) | возможность цитировать или отвечать на удаленные сохраненные сообщения | tele → сообщения |
| [76](../patches/tdesktop/0076-feat-rewrite-pasted-links-with-your-own-rules.patch) | замена доменов и параметров вставляемых ссылок по собственным правилам (например, Twitter в vxtwitter) | tele → messages → link rewrites |
| [84](../patches/tdesktop/0084-feat-choose-when-links-get-previews-and-set-your-own.patch) | выбор предпросмотра ссылок: для всех, кроме вставленных, или только добавленных вручную; добавление предпросмотра любой ссылки к любому сообщению | tele → сообщения |
| [103](../patches/tdesktop/0103-feat-choose-which-app-opens-each-service.patch) | выбор приложения для открытия внешних сервисов: официальное приложение, альтернативный клиент (например, Spotifast), браузер или любая программа | tele → сообщения → открывать ссылки в приложениях |
| [113](../patches/tdesktop/0113-feat-forward-protected-messages-as-copies.patch) | детальная настройка элементов снимка: скрытие имени, времени, заголовка и разделителей | tele → сообщения, выкл. |
| [125](../patches/tdesktop/0125-feat-bookmark-messages-and-return-to-where-you-were-.patch) | закрепление любимых наборов стикеров и эмодзи в нижней панели | tele → сообщения, выкл. |
| [137](../patches/tdesktop/0137-feat-choose-the-map-service-for-locations.patch) | отключение всех встроенных AI-функций и подсказок Telegram | tele → сообщения → открывать ссылки в приложениях |
| [141](../patches/tdesktop/0141-feat-number-the-lines-of-long-code-blocks.patch) | зацикленное воспроизведение видео во встроенном просмотрщике медиа | tele → сообщения, выкл. |
| [143](../patches/tdesktop/0143-feat-rewrite-only-the-link-preview.patch) | нумерация строк в длинных блоках моноширинного исходного кода | вместе с 76 |
| [146](../patches/tdesktop/0146-feat-remember-when-your-messages-were-read.patch) | возможность заменять ссылку только в блоке предпросмотра, оставляя исходный URL в тексте | tele → сообщения, вкл. |
| [150](../patches/tdesktop/0150-feat-choose-which-deleted-messages-to-keep.patch) | выбор, какие удаленные сообщения сохранять: в чатах с ботами, в «Избранном» и удаленные вами лично | вместе с 19 |
| [172](../patches/tdesktop/0172-feat-choose-how-quoted-names-of-deleted-messages-lin.patch) | отображение прикрепленных медиа над полем ввода в виде сетки альбома | вместе с 19 |
| [181](../patches/tdesktop/0181-feat-keep-deleted-messages-and-edit-history-after-a-.patch) | сохраненные удаленные сообщения и история правок сохраняются после перезапуска в зашифрованном виде на 1, 7, 30 дней или бессрочно | вместе с 19 |
| [198](../patches/tdesktop/0198-feat-quote-rich-messages.patch) | выделение части сообщения и выбор «цитировать и ответить»: открывается редактор с цитатой, а цитата без автора больше не исчезает при отправке | tele → сообщения, вкл. |
| [209](../patches/tdesktop/0209-feat-multiple-quotes-in-one-reply.patch) | получение сервисных уведомлений и анонсов от сервера tele | tele → сообщения, вкл. |
| [255](../patches/tdesktop/0255-feat-leave-kept-deleted-messages-out-of-the-chat-lis.patch) | сохраненные удаленные сообщения можно не учитывать в списке чатов и счетчиках непрочитанных: чат показывает последнее неудаленное сообщение, а счетчики, упоминания и уведомления о них убираются | вместе с 19 |
| [266](../patches/tdesktop/0266-feat-hide-bubble-tails.patch) | щадящий алгоритм сжатия фотографий с сохранением максимальной детализации | tele → сообщения, выкл. |
| [269](../patches/tdesktop/0269-feat-no-outline-on-large-emoji.patch) | мгновенная генерация QR-кода на сообщение, чат или медиафайл из контекстного меню | tele → сообщения, выкл. |
| [271](../patches/tdesktop/0271-feat-classic-text-padding-in-bubbles.patch) | автоматическое отключение звуков уведомлений во время голосовых и видеозвонков | вместе с 266 |
| [282](../patches/tdesktop/0282-feat-keep-deleted-chats-and-topics.patch) | одновременная вставка нескольких объектов из буфера обмена | вместе с 19 |
| [313](../patches/tdesktop/0313-feat-recover-deleted-channel-posts-from-forwards.patch) | скрытие плашки «изменено» для сообщений от ботов | вместе с 19 |
| [324](../patches/tdesktop/0324-fix-deleted-chats-with-people-and-bots-stay-writable.patch) | сохранённые чаты с людьми и ботами остаются доступными для ввода: поле ввода, разблокировка и перезапуск бота работают как обычно, а первое новое сообщение превращает чат обратно в обычный. сохранённые группы и каналы остаются только для чтения | вместе с 282 |
| [327](../patches/tdesktop/0327-fix-quote-rich-messages-chooses-tele-s-or-telegram-s.patch) | при включённом цитировании rich-сообщений цитирование части rich-сообщения из его меню или свайпом для ответа помещает его в ваше сообщение как цитату-блокпост, как и раньше. отключите его, чтобы получить собственные rich-цитаты telegram, появившиеся в telegram desktop 7.3.2 | вместе с 198 |
| [330](../patches/tdesktop/0330-fix-deleted-messages-only-lists-messages-deleted-one.patch) | сообщения, сохранённые из-за выхода или удаления всего чата, больше не считаются удалёнными сообщениями: пока чат сохранён, у них нет значка корзины или затухания, а страница удалённых сообщений чата и её счётчик показывают только поштучно удалённые сообщения. когда удалённый чат с человеком или ботом возвращается, его старые сообщения получают отметку, но не попадают на страницу | вместе с 282 |
| [331](../patches/tdesktop/0331-feat-bigger-video-messages-while-playing.patch) | видеосообщения увеличиваются до 400 px во время воспроизведения или паузы, насколько позволяет ширина чата, и уменьшаются обратно при остановке | tele → сообщения, выкл. |
| [332](../patches/tdesktop/0332-feat-seek-anywhere-on-video-messages.patch) | перетаскивание в любой точке видеосообщения, кроме центра, выполняет перемотку, а не только вдоль его края | tele → сообщения, выкл. |

<a id="sending"></a>
## отправка сообщений

настройки → tele → отправка сообщений.

| # | what it does | toggle |
|---|---|---|
| [42](../patches/tdesktop/0042-feat-upload-media-in-several-chats-at-once.patch) | отображение точного времени отправки на сервисных и системных сообщениях чата | tele → отправка, выкл. |
| [44](../patches/tdesktop/0044-feat-compute-messages-starting-with-via-calcmula.patch) | автоматическое вычисление математических выражений, начинающихся со знака `=` (калькулятор Calcmula) | tele → отправка, выкл. |
| [48](../patches/tdesktop/0048-feat-move-late-sent-messages-to-the-bottom.patch) | сообщение, отправка которого заняла длительное время, перемещается в конец чата после успешной доставки | tele → отправка, выкл. |
| [49](../patches/tdesktop/0049-feat-queue-messages-behind-an-uploading-media.patch) | автоматическое перемещение задержавшихся при отправке сообщений в самый низ ленты чата | tele → отправка, выкл. |
| [66](../patches/tdesktop/0066-feat-skip-the-rich-message-prompt-on-paste.patch) | отправка результатов inline-ботов без плашки «через @bot» | tele → отправка, выкл. |
| [79](../patches/tdesktop/0079-feat-preview-calcmula-results-while-typing.patch) | отображение результата вычислений Calcmula во всплывающей подсказке прямо в процессе ввода | tele → отправка, выкл. |
| [92](../patches/tdesktop/0092-feat-send-gifs-as-videos-and-videos-as-gifs.patch) | сопоставление дополнительных коротких юзернеймов с публичного списка сервера | tele → sending, on |
| [94](../patches/tdesktop/0094-feat-send-scheduled-messages-on-time.patch) | компактное отображение ID и номера дата-центра в одну строку в профиле | tele → отправка, выкл. |
| [98](../patches/tdesktop/0098-feat-save-drafts-for-later.patch) | сохраненные черновики: несколько черновиков на чат с медиа и форматированием в виде отдельного раздела; отправка в любой чат и восстановление удаленных | tele → отправка → черновики |
| [99](../patches/tdesktop/0099-feat-send-photos-in-hd-by-default.patch) | менеджер сохраненных черновиков: просмотр и восстановление заготовок сообщений для разных чатов | tele → sending, on |
| [106](../patches/tdesktop/0106-feat-attach-media-above-the-field-beta.patch) | экспорт всех настроек tele в переносимый JSON-файл и импорт с наглядным предпросмотром | tele → отправка, выкл. |
| [117](../patches/tdesktop/0117-feat-send-replies-to-older-messages-past-the-queue.patch) | динамическое скрытие зависимых поднастроек, пока не включен основной родительский тумблер | вместе с 49 |
| [118](../patches/tdesktop/0118-feat-send-right-away-on-double-enter.patch) | отправка ответов на старые сообщения вне очереди выгружаемых тяжелых файлов | вместе с 49 |
| [124](../patches/tdesktop/0124-feat-hide-the-gift-button-in-the-message-field.patch) | скрытие кнопки отправки подарка в поле ввода сообщения | tele → отправка, выкл. |
| [129](../patches/tdesktop/0129-feat-confirm-stickers-gifs-and-voice-messages-before.patch) | стикеры, GIF и голосовые сообщения требуют повторного клика перед отправкой | tele → отправка, выкл. |
| [134](../patches/tdesktop/0134-feat-record-voice-without-fading.patch) | запись голосовых сообщений без затухания в начале с сохранением первых 0.4 секунды, которые срезает официальный Telegram Desktop | tele → отправка, выкл. |
| [147](../patches/tdesktop/0147-feat-calcmula-suggestions-and-sending-without-calcul.patch) | открытие контекстного меню сообщения вплотную к пузырю сообщения, а не под курсором | вместе с 79 |
| [156](../patches/tdesktop/0156-feat-send-an-audio-file-as-a-voice-message.patch) | уведомления о появлении выбранных пользователей в сети (online) | tele → sending, on |
| [157](../patches/tdesktop/0157-feat-download-folders-per-chat.patch) | режим стримера: скрытие личных данных, номеров, текста тостов и приложения от захвата экрана | tele → отправка, выкл. |
| [158](../patches/tdesktop/0158-feat-resize-the-message-field.patch) | перетаскивание верхней границы поля ввода сообщения для настройки его минимальной высоты | tele → отправка, выкл. |
| [160](../patches/tdesktop/0160-feat-translate-your-message-before-sending.patch) | перевод текста сообщения на нужный язык прямо перед отправкой | tele → sending, on |
| [175](../patches/tdesktop/0175-feat-inline-calcmula-results-after.patch) | вставка вычисленного значения Calcmula сразу после знака `=` нажатием Tab или стрелки вправо | вместе с 44 |
| [225](../patches/tdesktop/0225-feat-see-and-release-messages-queued-behind-an-uploa.patch) | сообщения в очереди за загрузкой файла указывают, чего именно они ожидают, и их можно отправить сразу или отменить из меню | вместе с 49 |
| [235](../patches/tdesktop/0235-feat-captioned-stickers-go-to-the-docked-media.patch) | стикеры с подписью прикрепляются к медиапанели над полем ввода, а стикеры и GIF можно добавлять туда прямо из их панелей | вместе с 106 |
| [241](../patches/tdesktop/0241-feat-choose-how-silent-videos-are-sent.patch) | выбор формата отправки видео без звука: как зацикленные GIF или как обычные видеофайлы | tele → отправка |
| [244](../patches/tdesktop/0244-feat-markdown-renders-as-you-type.patch) | рендеринг разметки Markdown прямо при вводе: жирный, курсив, зачеркнутый, спойлеры, код и блоки кода с приглушенными спецсимволами. Строки с > становятся цитатами, а с >! — сворачиваемыми | tele → отправка, выкл. |
| [258](../patches/tdesktop/0258-feat-forward-messages-one-by-one.patch) | подтверждение при переходе по внешним ссылкам с показом полного очищенного адреса | tele → отправка, выкл. |
| [259](../patches/tdesktop/0259-feat-record-voice-in-higher-quality.patch) | выбор позиции всплывающих тостов на экране (любой из четырех углов) | tele → отправка, выкл. |
| [260](../patches/tdesktop/0260-feat-compress-photos-less.patch) | подавление фоновых сетевых пингов при входящих аудио- и видеозвонках | tele → отправка, выкл. |
| [261](../patches/tdesktop/0261-feat-thinner-brush-in-the-photo-editor.patch) | предпросмотр и прослушивание голосовых и видеосообщений (кружочков) перед отправкой | tele → отправка, выкл. |
| [279](../patches/tdesktop/0279-feat-mention-several-people-in-a-row.patch) | фильтрация результатов поиска по типу вложений (фото, видео, файлы, музыка, голосовые, кружочки, ссылки) | tele → отправка, выкл. |
| [312](../patches/tdesktop/0312-fix-confirm-stickers-sent-from-sticker-set-boxes.patch) | просмотр и копирование параметра `start_param` в ссылках на ботов и веб-приложения | вместе с 129 |
| [328](../patches/tdesktop/0328-fix-enter-sends-attached-media-with-an-empty-field-i.patch) | в темах, комментариях и избранном нажатие Enter отправляет прикреплённые над полем медиафайлы даже при пустом поле ввода вместо того, чтобы только отмечать чат прочитанным | вместе с 106 |

<a id="notifications"></a>
## уведомления

настройки → tele → уведомления.

| # | what it does | toggle |
|---|---|---|
| [127](../patches/tdesktop/0127-feat-send-silently-by-default.patch) | локальные закладки на важные сообщения и возврат к месту чтения после перехода | tele → уведомления, выкл. |
| [132](../patches/tdesktop/0132-feat-hide-unread-counters.patch) | скрытие счётчиков непрочитанных на вкладках папок, панели задач и в трее, исключение архива и аккаунтов из контекстного меню | tele → уведомления, выкл. |
| [154](../patches/tdesktop/0154-feat-notify-when-people-come-online.patch) | удобное разбиение настроек tele на тематические категории с быстрым переключением | tele → уведомления, выкл. |
| [155](../patches/tdesktop/0155-feat-mute-folders-and-silence-chats-completely.patch) | отключение звука для всей папки на этом устройстве и полное заглушение чатов, включая упоминания и ответы | tele → уведомления, вкл. |
| [204](../patches/tdesktop/0204-feat-notification-centre.patch) | центр уведомлений в главном меню: всплывающие уведомления tele, обновления, отчеты о сбоях, алерты онлайна и новости сервера в едином списке с хранением 30 дней на аккаунт. Ограничения частоты (rate limits) показывают обратный отсчет вместо тихого зависания | tele → уведомления, вкл. |
| [211](../patches/tdesktop/0211-fix-rate-limit-notices-for-slowmode-and-download-thr.patch) | настройка звуковых сигналов для собственных уведомлений tele | tele → уведомления, вкл. |
| [231](../patches/tdesktop/0231-feat-mentions-and-replies-in-the-notification-centre.patch) | упоминания и ответы из групп (включая группы без звука) сохраняются в центре уведомлений; клик открывает сообщение | tele → уведомления, вкл. |
| [238](../patches/tdesktop/0238-fix-notification-centre-shows-whole-entries.patch) | центр уведомлений показывает записи целиком, длинные — с кнопкой раскрытия, и поддерживает анимацию нажатия | вместе с 204 |
| [239](../patches/tdesktop/0239-feat-copied-values-in-the-notification-centre.patch) | уведомления о копировании сохраняются в центре уведомлений вместе со скопированным текстом: клик копирует его повторно | tele → уведомления, вкл. |
| [245](../patches/tdesktop/0245-feat-reply-and-mention-badges-in-the-notification-ce.patch) | ответы и упоминания в центре уведомлений помечаются значком стрелки или @ на аватарке отправителя | вместе с 231 |

<a id="menus"></a>
## меню

настройки → tele → меню.

| # | what it does | toggle |
|---|---|---|
| [29](../patches/tdesktop/0029-feat-show-the-message-id-in-the-message-menu.patch) | переход к самому первому сообщению чата через меню чата | tele → меню, выкл. |
| [31](../patches/tdesktop/0031-feat-jump-to-the-first-message-of-a-chat.patch) | просмотр сообщений и структур Telegram в сыром виде TL-схем на schema.jppgr.am | tele → меню, выкл. |
| [33](../patches/tdesktop/0033-feat-view-messages-and-telegram-objects-as-tl.patch) | просмотр в формате TL в контекстных меню сообщений, чатов, профилей, участников, стикеров, подарков, историй и папок через schema.jppgr.am | tele → меню, выкл. |
| [54](../patches/tdesktop/0054-feat-copy-custom-emoji-ids-from-the-message-menu.patch) | копирование ID кастомных эмодзи из контекстного меню сообщения | tele → меню, выкл. |
| [56](../patches/tdesktop/0056-feat-reorder-and-hide-message-menu-items.patch) | редактор структуры контекстного меню сообщений: скрытие и изменение порядка пунктов | tele → меню |
| [86](../patches/tdesktop/0086-feat-save-messages-as-a-picture.patch) | снимок сообщений: сохранение выбранных сообщений как изображения из контекстного меню с фоном чата или без него и датами | tele → меню, выкл. |
| [104](../patches/tdesktop/0104-feat-scale-shots-up-to-4x-and-show-your-messages-as-.patch) | масштабирование снимков сообщений от 1x до 4x с чётким текстом, облачками, аватарками, медиа и эмодзи; показ своих сообщений как входящих | вместе с 86 |
| [111](../patches/tdesktop/0111-feat-choose-what-shots-show.patch) | выбор элементов на снимках сообщений: имена, аватарки, реакции, время и галочки, ответы, пересылки, кнопки и предпросмотр ссылок | вместе с 86 |
| [138](../patches/tdesktop/0138-feat-copy-messages-as-markdown-or-html.patch) | копирование сообщений в формате Markdown или HTML из контекстного меню сообщения | tele → меню, выкл. |
| [144](../patches/tdesktop/0144-feat-open-the-message-menu-next-to-the-bubble.patch) | правый клик рядом с облачком открывает контекстное меню сообщения | tele → меню, выкл. |
| [148](../patches/tdesktop/0148-feat-open-view-as-tl-inside-tele.patch) | просмотр в формате TL открывается внутри tele с заголовком конструктора объекта; с флагом -teleoffline открывается в браузере | вместе с 33 |
| [170](../patches/tdesktop/0170-feat-rearrange-menus-with-groups-and-submenus-in-a-m.patch) | конструктор меню: группировка пунктов в подменю, разделители и визуальный редактор | tele → меню |
| [254](../patches/tdesktop/0254-feat-copy-file-paths-from-the-message-menu.patch) | копирование полного пути к скачанному файлу из контекстного меню сообщения | tele → меню, выкл. |
| [273](../patches/tdesktop/0273-fix-sharp-boost-icons-and-button-emoji-in-scaled-sho.patch) | тонкая настройка параметров аппаратного ускорения видео и графики | вместе с 104 |
| [300](../patches/tdesktop/0300-feat-remove-all-your-messages-from-a-chat.patch) | отправка документов и медиа в виде файлов без сжатия по умолчанию | tele → меню, выкл. |
| [319](../patches/tdesktop/0319-feat-show-skipped-messages-in-shots.patch) | улучшенный рендеринг пропущенных сообщений на снимках высокого разрешения | вместе с 86 |
| [320](../patches/tdesktop/0320-feat-restrict-members-from-message-menus-and-find-th.patch) | ограничение прав участников прямо из меню сообщения и быстрый поиск всех сообщений пользователя в группе | tele → menus, on |
| [1003](../patches/Telegram/lib_ui/0003-fix-icon-emoji-stay-sharp-in-renders-at-a-higher-rat.patch) | иконки-эмодзи внутри текста (например, значок буста) остаются чёткими на снимках повышенного масштаба | вместе с 104 |

<a id="privacy"></a>
## приватность

настройки → tele → приватность.

| # | what it does | toggle |
|---|---|---|
| [3](../patches/tdesktop/0003-feat-add-an-option-to-hide-stories-everywhere.patch) | скрытие историй повсюду: убирает панель историй, рамки вокруг аватарок и разделы историй в профилях | tele → приватность, выкл., требуется перезапуск |
| [4](../patches/tdesktop/0004-feat-add-an-option-to-watch-stories-invisibly.patch) | просмотр историй без отображения в списке зрителей (реакции и ответы по-прежнему раскрывают вас) | tele → приватность, выкл. |
| [16](../patches/tdesktop/0016-feat-ignore-users-by-hiding-or-fading-their-messages.patch) | локальное игнорирование пользователей в группах: скрытие или затемнение их сообщений | tele → приватность |
| [27](../patches/tdesktop/0027-feat-allow-screenshots-of-disappearing-media.patch) | снятие запрета на создание снимков экрана при просмотре самоуничтожающегося медиа | tele → приватность, выкл. |
| [32](../patches/tdesktop/0032-feat-add-ghost-mode.patch) | режим призрака: отключение отчетов о прочтении, статуса набора текста, онлайна и просмотра историй с раздельной настройкой для каждого чата; скрытая отправка через отложенные сообщения | tele → приватность, выкл. |
| [63](../patches/tdesktop/0063-feat-more-ghost-mode-options.patch) | расширенные параметры невидимки: выборочное отключение набора текста, чтения реакций и опросов | tele → приватность |
| [72](../patches/tdesktop/0072-feat-pick-ignored-users-and-ghost-chats-like-privacy.patch) | списки исключений для режима невидимки и игнорирования по чатам | tele → приватность |
| [93](../patches/tdesktop/0093-feat-keep-drafts-on-this-device.patch) | черновики хранятся локально на этом устройстве и не синхронизируются с облаком; кнопка очищает сохраненные ранее | tele → приватность, выкл. |
| [110](../patches/tdesktop/0110-feat-never-block-screen-capture.patch) | tele никогда не блокирует создание снимков экрана, запись видео и демонстрацию экрана, включая защищенные чаты и таймерные медиа | tele → приватность, вкл. |
| [159](../patches/tdesktop/0159-feat-streamer-mode.patch) | ручное изменение высоты поля ввода текста перетаскиванием разделителя | tele → приватность, выкл. |
| [165](../patches/tdesktop/0165-feat-hide-messages-by-keyword-or-regex.patch) | скрытие сообщений по ключевым словам или регулярным выражениям повсюду и в отдельных чатах | tele → приватность |
| [186](../patches/tdesktop/0186-feat-local-password-for-stars-and-gift-actions.patch) | локальный пароль (PIN-код) для подтверждения трат Звёзд, передачи и улучшения подарков | tele → приватность |
| [216](../patches/tdesktop/0216-feat-local-password-for-bot-payments-and-paid-messag.patch) | запрос локального пароля можно включить перед платежами ботам, платными сообщениями и предложенными постами | вместе с 186 |
| [226](../patches/tdesktop/0226-feat-show-pending-ghost-scheduled-messages.patch) | сообщения, отложенные режимом призрака, отображаются в чате: правый клик позволяет отправить их немедленно или отменить | tele → приватность, вкл. |
| [227](../patches/tdesktop/0227-feat-ignored-users-and-hidden-words-can-stay-silent.patch) | сообщения от игнорируемых пользователей и со скрытыми словами не присылают уведомлений, не увеличивают счётчик непрочитанных и не показываются в предпросмотре списка чатов | tele → приватность, вкл. |
| [228](../patches/tdesktop/0228-fix-invisible-stories-follow-ghost-settings-and-surv.patch) | анонимный просмотр историй учитывает настройки призрака для конкретного чата, сохраняет просмотренных авторов между перезапусками и предупреждает перед прямыми трансляциями, раскрывающими зрителя | вместе с 4 |
| [292](../patches/tdesktop/0292-fix-closing-the-rich-editor-keeps-drafts-on-this-dev.patch) | скрытие текста и автора уведомлений, если приложение заблокировано локальным паролем | вместе с 93 |

<a id="profiles-and-ids"></a><a id="profiles"></a>
## профили и id

настройки → tele → профили и id.

| # | what it does | toggle |
|---|---|---|
| [13](../patches/tdesktop/0013-feat-show-gift-ids.patch) | режим невидимки (Ghost Mode): чтение без отметок, скрытие статуса «печатает», online и историй | tele → профили и id, выкл. |
| [14](../patches/tdesktop/0014-feat-show-the-peer-id-as-its-own-profile-row.patch) | отображение числового ID чата/пользователя отдельной строкой в профиле с копированием по клику | tele → profiles and ids, off (see 46) |
| [23](../patches/tdesktop/0023-feat-show-the-data-center-in-profiles.patch) | отображение номера дата-центра (DC) аккаунта и аватара в профиле | tele → профили и id, выкл. |
| [45](../patches/tdesktop/0045-feat-move-show-peer-ids-into-tele-settings.patch) | управление отображением ID в профилях перенесено в настройки tele | tele → профили и id |
| [47](../patches/tdesktop/0047-feat-open-collectible-gifts-in-see.tg.patch) | открытие коллекционных подарков во внешнем верификаторе see.tg | tele → профили и id, выкл. |
| [64](../patches/tdesktop/0064-feat-show-ids-on-regular-gifts.patch) | отображение уникальных ID подарков с защитой от отслеживания | tele → профили и id, выкл. |
| [74](../patches/tdesktop/0074-feat-show-names-instead-of-phone-numbers-in-chat-hea.patch) | отображение имен пользователей вместо номеров телефонов в шапке чата | tele → профили и id, выкл. |
| [77](../patches/tdesktop/0077-feat-name-people-only-for-you.patch) | редактор пользовательских правил замены ссылок с поддержкой регулярных выражений и пресетов | tele → profiles and ids → custom names |
| [82](../patches/tdesktop/0082-feat-show-collectible-prices-at-the-purchase-date.patch) | отображение цены покупки и текущей рыночной стоимости подарка в TON | tele → профили и id, выкл. |
| [95](../patches/tdesktop/0095-feat-show-id-and-dc-in-one-row.patch) | локальное сохранение черновиков сообщений на устройстве с защитой от сброса сервером | tele → профили и id, выкл. |
| [142](../patches/tdesktop/0142-feat-hide-the-collectible-status-tooltip-in-profiles.patch) | подсказка с подробной информацией о статусе коллекционного подарка в профилях | tele → профили и id, выкл. |
| [171](../patches/tdesktop/0171-feat-hide-phone-numbers-in-profiles.patch) | скрытие номеров телефонов в чужих и собственном профиле | tele → профили и id, выкл. |
| [183](../patches/tdesktop/0183-feat-send-several-gifts-at-once.patch) | добавление нескольких независимых цитат из разных сообщений в один ответ | tele → профили и id, выкл. |
| [184](../patches/tdesktop/0184-feat-dim-hidden-gifts-and-select-several.patch) | массовая отправка нескольких подарков сразу выбранным получателям | tele → профили и id, выкл. |
| [185](../patches/tdesktop/0185-feat-search-gifts.patch) | визуальное затемнение скрытых подарков и массовый выбор подарков в профиле | tele → профили и id, выкл. |
| [188](../patches/tdesktop/0188-fix-show-a-chat-s-data-center-from-its-first-photo.patch) | копирование стикеров и эмодзи в буфер обмена как растровых изображений PNG | вместе с 23 |
| [189](../patches/tdesktop/0189-feat-more-bulk-gift-actions.patch) | режим массового выбора подарков позволяет продавать, снимать с продажи, переводить в звёзды и добавлять в коллекцию с пояснением ошибок | вместе с 184 |
| [195](../patches/tdesktop/0195-feat-show-the-media-s-data-center-in-the-media-viewe.patch) | просмотрщик медиа показывает дата-центр (DC), на котором хранится открытое фото, видео или файл | вместе с 23 |
| [196](../patches/tdesktop/0196-feat-gift-studio.patch) | студия подарков: сборка любого подарка из реальных деталей (коллекция, модель, фон, символ, номер) на живой обложке в разных макетах; экспорт в PNG, MP4, GIF или валидный TGS-стикер с текстом в кривых. Избранное, развертки, данные с @GiftChanges. TGS-стикеры не содержат личных данных | tele → профили и id, меню подарков |
| [197](../patches/tdesktop/0197-feat-fake-gift-upgrades.patch) | встроенный инспектор сетевых пакетов MTProto и расширенное логирование сессий | tele → profiles and ids, on |
| [203](../patches/tdesktop/0203-feat-gift-grid-builder.patch) | конструктор витрины подарков: поклеточное заполнение сетки коллекционными или обычными подарками, ленты, булавки и скрытые метки, перетаскивание, сохранение сеток и экспорт в PNG, GIF или MP4 с рамкой профиля | tele → профили и id |
| [207](../patches/tdesktop/0207-feat-show-usernames-for-invisible-names.patch) | центр уведомлений: системные тосты tele, обновления, отчеты о сбоях и важные сообщения в едином окне | tele → профили и id, выкл. |
| [208](../patches/tdesktop/0208-feat-show-hidden-characters.patch) | информативные предупреждения о превышении лимитов Telegram (FloodWait) с точным временем ожидания | tele → профили и id, выкл. |
| [212](../patches/tdesktop/0212-fix-gift-batches-survive-flood-waits-and-bad-items.patch) | полное отключение загрузки сторонних галочек верификации с сервера | вместе с 189 |
| [233](../patches/tdesktop/0233-feat-more-gifts-and-models-in-the-gift-studio.patch) | студия подарков открывает случайный подарок, ставит новые коллекции первыми, поддерживает исходную 3D-модель, пользовательские TGS-модели, обычные подарки, коллекцию плюшевых медведей и переименование параметров на карточке | вместе с 196 |
| [246](../patches/tdesktop/0246-feat-open-anyone-s-gifts-in-the-gift-grid.patch) | открытие подарков любого пользователя или его коллекций в витрине подарков, импорт в витрину, прокрутка больших сеток, исключение строк при экспорте и скрытие отдельных подарков | вместе с 203 |
| [247](../patches/tdesktop/0247-feat-rarity-tiers-and-pills-in-the-gift-studio.patch) | созданные модели показывают уровень редкости, а плашки редкости в студии подарков имеют цветные бейджи | вместе с 196 |
| [252](../patches/tdesktop/0252-fix-copy-peer-ids-as-plain-digits.patch) | копирование ID чата или пользователя из строки профиля копирует только чистые цифры, даже если в строке они отображаются с пробелами | вместе с 14 |
| [264](../patches/tdesktop/0264-feat-show-when-media-was-uploaded-in-the-media-viewe.patch) | сверхтонкая кисть в встроенном фоторедакторе для аккуратных пометок | tele → профили и id, выкл. |
| [265](../patches/tdesktop/0265-feat-copy-the-owner-id-of-sticker-sets.patch) | пипетка для выбора цвета кисти непосредственно с редактируемого изображения | tele → профили и id, выкл. |
| [281](../patches/tdesktop/0281-feat-peek-at-a-hidden-last-seen.patch) | плавное изменение размеров окна программы без артефактов перерисовки | tele → профили и id, выкл. |
| [298](../patches/tdesktop/0298-feat-use-the-blurred-profile-photo-as-the-profile-ba.patch) | шаблоны быстрых ответов с поддержкой переменных и шорткатов | tele → профили и id, выкл. |
| [302](../patches/tdesktop/0302-feat-fill-the-whole-profile-with-the-blurred-photo-s.patch) | фоновое заполнение всего окна профиля размытым фото контакта | вместе с 298 |
| [325](../patches/tdesktop/0325-feat-show-the-last-activity-next-to-a-hidden-last-se.patch) | для людей со скрытым онлайном в заголовке чата и профиле отображается время, когда tele в последний раз видел их пишущими, набирающими текст, читающими ваши сообщения или реагирующими: был(а) недавно (14:32). сохраняется между перезапусками | tele → профили и id, выкл. |
| [329](../patches/tdesktop/0329-feat-show-typing-in-the-chat-list-with-a-hidden-last.patch) | в строках списка чатов отображается набор текста, запись и выбор стикера для людей со скрытым онлайном, что telegram показывает только в открытом чате. боты остаются как есть | tele → профили и id, выкл. |

### gift studio

the gift studio builds any collectible from real parts and exports it, the grid builder lays out a whole profile of gifts, and fake upgrades spin any upgradable gift without spending anything (201, 209 and 202 above). open them from this page or from a gift's menu.

tgs files exported from the gift studio carry an invisible mark that says they were made with tele's gift studio. it holds nothing about you: no user, account, device or time.

## bots

settings → tele → bots.

| # | what it does | toggle |
|---|---|---|
| [5](../patches/tdesktop/0005-feat-show-bot-button-payloads-in-tooltips.patch) | показ callback-данных и URL inline-кнопок ботов во всплывающих подсказках | tele → боты, выкл. |
| [65](../patches/tdesktop/0065-feat-send-inline-results-without-via.patch) | отправка результатов инлайн-ботов как собственных сообщений без подписи «через @bot» | tele → боты, выкл. |
| [230](../patches/tdesktop/0230-feat-show-the-start-parameter-on-the-start-button.patch) | при открытии бота по ссылке параметр запуска отображается прямо на кнопке «Старт» | tele → боты, выкл. |
| [232](../patches/tdesktop/0232-feat-no-edited-mark-on-bot-messages.patch) | сообщения от ботов не показывают значок «изменено», так как боты регулярно редактируют сообщения для обновления информации | tele → боты, выкл. |
| [242](../patches/tdesktop/0242-feat-skip-the-mini-app-terms-box-for-trusted-apps.patch) | ссылки на мини-приложения, которые вы уже открывали, пропускают диалог согласия с условиями | tele → боты, выкл. |
| [248](../patches/tdesktop/0248-feat-never-open-web-apps-in-fullscreen.patch) | мини-приложения всегда открываются в отдельном окне и не переходят в полноэкранный режим | tele → боты, выкл. |

<a id="debug"></a>
## отладка

настройки → tele → отладка.

| # | what it does | toggle |
|---|---|---|
| [87](../patches/tdesktop/0087-feat-debug-logs-and-an-mtproto-inspector.patch) | раздел отладки: переключение логов, открытие папки логов, очистка и инспектор MTProto с фильтрацией запросов, раскрытием объектов и переходом на schema.jppgr.am | tele → отладка |
| [194](../patches/tdesktop/0194-feat-mtproto-console.patch) | консоль MTProto: вызов любых методов API в текущей сессии (текст, JSON или JSON5), автодополнение, подсказки схемы, валидация, дерево результатов и история. Необратимые методы требуют подтверждения, операции со звёздами запрашивают локальный пароль | tele → отладка, ctrl+alt+m |
| [217](../patches/tdesktop/0217-fix-confirm-more-irreversible-methods-in-the-mtproto.patch) | консоль MTProto запрашивает подтверждение перед необратимыми методами API | вместе с 194 |
| [272](../patches/tdesktop/0272-feat-fix-fonts-picked-in-chat-settings.patch) | последовательное упоминание нескольких человек через ПКМ или Tab в списке подсказок | tele → debug, off, требуется перезапуск |
| [277](../patches/tdesktop/0277-feat-turn-on-the-wallet-before-telegram-does.patch) | прототип секретных чатов с локальным паролем, подтверждением ключей и сквозным шифрованием | tele → debug, off, требуется перезапуск |
| [283](../patches/tdesktop/0283-feat-secret-chats-prototype.patch) | вставка скопированных изображений напрямую в виде стикеров | tele → debug, off, требуется перезапуск |
| [284](../patches/tdesktop/0284-feat-update-the-secret-phrase-of-wallets-without-a-b.patch) | принудительная активация интерфейса встроенного кошелька Wallet до его сервера | tele → отладка, выкл. |
| [286](../patches/tdesktop/0286-feat-send-while-an-old-wallet-stays-on-this-device.patch) | выбор пользовательского фонового градиента или монохромной заливки для снимков | tele → отладка, выкл. |
| [297](../patches/tdesktop/0297-feat-open-the-mtproto-inspector-and-console-as-panel.patch) | точный захват звука с первой миллисекунды голосовой записи без проглатывания начала | вместе с 87 |
| [306](../patches/tdesktop/0306-build-take-wallet-engine-from-gettele-money-for-priv.patch) | интеграция криптографического движка gettele money для приватных транзакций | вместе с 307 |
| [307](../patches/tdesktop/0307-feat-import-wallets-from-private-keys.patch) | импорт TON-кошельков напрямую из приватных ключей и сид-фраз | tele → отладка, выкл. |
| [308](../patches/tdesktop/0308-feat-copy-secret-words-without-waiting.patch) | моментальное копирование мнемонической фразы кошелька без искусственных задержек таймера | tele → debug, on |
| [310](../patches/tdesktop/0310-build-fetch-litehtml-for-html-bubbles.patch) | движок litehtml для легковесного отображения форматированных HTML-карточек | вместе с 311 |
| [311](../patches/tdesktop/0311-feat-render-html-cards-with-litehtml-and-run-their-s.patch) | замер и запись плавности прокрутки (FPS и времени кадров) в системный log.txt | tele → отладка, выкл. |
| [1002](../patches/Telegram/lib_ui/0002-feat-let-picked-fonts-use-their-real-metrics-on-wind.patch) | часть исправления выбранного шрифта на уровне библиотеки интерфейса lib_ui | вместе с 272 |

<a id="server"></a>
## сервер tele

настройки → tele → сервер.

| # | what it does | toggle |
|---|---|---|
| [9](../patches/tdesktop/0009-feat-apply-verification-and-marks-from-the-tele-serv.patch) | раздельные запросы подтверждения перед отправкой стикеров, GIF и голосовых сообщений | tele → сервер, вкл. |
| [36](../patches/tdesktop/0036-feat-send-crash-reports-to-the-tele-server.patch) | при падении tele следующий запуск предлагает отправить отчет о сбое на сервер tele вместо Telegram только с вашего согласия | tele → сервер, вкл. with the server |
| [80](../patches/tdesktop/0080-feat-clear-server-data-and-explain-custom-verificati.patch) | кнопка «Очистить кеш данных сервера» и справка по алгоритму хеширования верификаций | tele → сервер → clear cached data |
| [90](../patches/tdesktop/0090-feat-usernames-from-the-tele-server.patch) | автодополнение методов, подсветка синтаксиса и история запросов в консоли MTProto | tele → сервер, вкл. |
| [205](../patches/tdesktop/0205-feat-server-notices.patch) | уведомления от сервера tele в центре уведомлений с возможностью показа однократного цветного тоста | tele → сервер, вкл. |

## backup

settings → tele → backup.

| # | what it does | toggle |
|---|---|---|
| [105](../patches/tdesktop/0105-feat-export-and-import-tele-settings.patch) | экспорт настроек tele в файл или текст и импорт на любом аккаунте, системе или версии с предпросмотром перед применением | tele → резервные копии |
| [262](../patches/tdesktop/0262-feat-bigger-faster-chat-export.patch) | подтверждение перед отправкой любых файлов, фото и видео | tele → резервные копии, off |

<a id="updates"></a>
## обновления

настройки → tele → обновления.

| # | what it does | toggle |
|---|---|---|
| [6](../patches/tdesktop/0006-feat-update-from-the-tele-github-releases.patch) | автоматическая фоновая проверка и загрузка криптографически подписанных обновлений tele | tele → updates, on |
| [38](../patches/tdesktop/0038-feat-show-what-s-new-in-tele-after-an-update.patch) | показ интерактивного окна со списком изменений «Что нового» сразу после обновления | tele → updates, on |
| [73](../patches/tdesktop/0073-feat-show-what-s-new-in-a-local-tele-chat.patch) | локальный чат tele с историей новостей и изменений после обновлений | вместе с 38 |
| [315](../patches/tdesktop/0315-fix-updates-on-macos-keep-the-dock-icon.patch) | сохранение настроенной иконки tele в Dock при фоновом обновлении на macOS | вместе с 6 |

## everywhere

always on, or without a switch of their own.

| # | what it does | toggle |
|---|---|---|
| [1](../patches/tdesktop/0001-feat-show-the-tele-build-number-in-the-title-bar.patch) | показ номера сборки tele в заголовке окна | всегда вкл., см. 10 |
| [2](../patches/tdesktop/0002-feat-add-a-tele-section-to-the-settings.patch) | выделенный раздел настроек tele прямо под выбором языка | всегда вкл. |
| [7](../patches/tdesktop/0007-feat-rename-the-app-to-tele.patch) | приложение носит имя tele: исполняемый файл `tele.exe`, отдельная иконка на панели задач, изолированные каталоги данных | всегда вкл. |
| [11](../patches/tdesktop/0011-feat-remove-the-account-limit.patch) | снятие лимита учетных записей (поддержка до 1536 активных аккаунтов) | всегда вкл. |
| [12](../patches/tdesktop/0012-feat-show-checkmarks-and-custom-verification-everywh.patch) | отображение галочек и кастомной верификации в списке аккаунтов, меню, настройках и сообщениях | всегда вкл., in messages: tele → chats, off |
| [15](../patches/tdesktop/0015-feat-copy-links-to-tele-settings.patch) | правый клик по любой настройке tele копирует прямую ссылку для быстрого перехода | всегда вкл. |
| [20](../patches/tdesktop/0020-fix-fade-every-unsupported-experimental-option.patch) | автоматическое затемнение экспериментальных опций, не поддерживаемых текущей версией ОС | всегда вкл. |
| [28](../patches/tdesktop/0028-feat-copy-the-callback-data-of-bot-buttons.patch) | отображение числового ID сообщения в контекстном меню с копированием по нажатию | всегда вкл. |
| [39](../patches/tdesktop/0039-feat-call-the-app-tele-everywhere.patch) | использование имени tele во всех системных уведомлениях, диалогах и окнах | всегда вкл. |
| [41](../patches/tdesktop/0041-feat-group-and-search-tele-settings.patch) | настройки tele сгруппированы по страницам с краткими описаниями и собственным поиском, интегрированным в общий поиск настроек | всегда вкл. |
| [43](../patches/tdesktop/0043-feat-reply-timestamps-for-media-in-rich-messages.patch) | параллельная выгрузка и отправка медиафайлов сразу в несколько чатов одновременно | всегда вкл. |
| [46](../patches/tdesktop/0046-feat-show-the-tele-build-in-the-main-menu.patch) | номер сборки tele отображается в нижней части главного меню приложения | всегда вкл. |
| [53](../patches/tdesktop/0053-feat-move-tele-tools-to-the-bottom-of-the-message-me.patch) | перенос пунктов инструментов tele в нижнюю часть контекстного меню сообщений | всегда вкл. |
| [55](../patches/tdesktop/0055-fix-change-the-speed-instead-of-moving-the-media-vie.patch) | перетаскивание при удержании ускорения видео изменяет скорость вместо перемещения окна просмотрщика | всегда вкл. |
| [58](../patches/tdesktop/0058-feat-show-server-and-updates-on-the-tele-settings-pa.patch) | сохранение в чате сообщений, удаленных вами для всех участников | всегда вкл. |
| [59](../patches/tdesktop/0059-feat-pick-brush-colors-from-the-image.patch) | пипетка в фоторедакторе позволяет брать цвет кисти прямо с изображения | всегда вкл. |
| [62](../patches/tdesktop/0062-feat-group-the-tele-interface-and-profile-settings.patch) | разделы интерфейса, профилей и ID сгруппированы по логическим блокам | всегда вкл. |
| [69](../patches/tdesktop/0069-feat-add-test-server-accounts-with-a-plain-right-cli.patch) | мгновенная вставка форматированного текста без надоедливого всплывающего запроса | всегда вкл. |
| [78](../patches/tdesktop/0078-feat-add-launch-flags-to-turn-off-tele-s-own-network.patch) | флаги запуска для временной изоляции сетевых функций tele на один запуск, см. [флаги запуска](launch-flags.md) | всегда вкл. |
| [85](../patches/tdesktop/0085-feat-turn-username-into-a-t.me-link-in-the-link-box.patch) | поддержка установки произвольных иконок приложения из PNG и ICO | всегда вкл. |
| [88](../patches/tdesktop/0088-feat-new-tele-app-and-tray-icons.patch) | сохранение одного или нескольких сообщений в виде красивой картинки-снимка (Message Shots) | всегда вкл. |
| [89](../patches/tdesktop/0089-fix-name-the-item-Copy-Callback-Data-like-telegram-d.patch) | интерактивная консоль MTProto (`Ctrl+Alt+M`): вызов любых API методов Telegram с подсказками схемы | вместе с 28 |
| [91](../patches/tdesktop/0091-fix-open-custom-emoji-in-rich-and-emoji-only-message.patch) | экспорт ответов API Telegram в форматы JSON и JSON5 | всегда вкл. |
| [97](../patches/tdesktop/0097-fix-ignore-reply-counters-on-scheduled-messages.patch) | отправка отложенных сообщений секунда в секунду встроенным таймером клиента | всегда вкл. |
| [101](../patches/tdesktop/0101-fix-show-seen-and-reacted-counts-separately.patch) | отправка фотографий в исходном высоком качестве (HD) по умолчанию без сильного сжатия | всегда вкл. |
| [102](../patches/tdesktop/0102-feat-send-an-inline-bot-query-as-text.patch) | снимки сообщений в разрешении до 4x, скрытие аватаров, времени и фона чата | всегда вкл. |
| [107](../patches/tdesktop/0107-fix-show-server-badges-on-the-personal-channel-in-pr.patch) | выборочный импорт: возможность применить только выбранные категории настроек из файла | всегда вкл. |
| [108](../patches/tdesktop/0108-fix-explain-a-missing-changelog-instead-of-doing-not.patch) | ассоциация внешних ссылок и сервисов с установленными приложениями системы | всегда вкл. |
| [109](../patches/tdesktop/0109-feat-show-new-settings-after-an-update.patch) | после обновления страница «что нового» показывает добавленные настройки со ссылкой из сервисного сообщения | всегда вкл. |
| [112](../patches/tdesktop/0112-fix-trim-settings-descriptions.patch) | снятие системных блокировок захвата экрана и защиты от скриншотов | всегда вкл. |
| [114](../patches/tdesktop/0114-fix-stop-videos-at-their-end.patch) | пересылка сообщений из каналов и чатов с запретом копирования в виде обычных копий | всегда вкл. |
| [115](../patches/tdesktop/0115-feat-hide-settings-until-their-parent-is-on.patch) | закрепленные медиафайлы над полем ввода: поддержка драг-н-дропа, порядка файлов и альбомов | всегда вкл. |
| [119](../patches/tdesktop/0119-feat-regroup-the-sending-settings.patch) | отправка сообщения мгновенно по двойному нажатию Enter | всегда вкл. |
| [135](../patches/tdesktop/0135-fix-close-the-tele-chat-profile-card-after-a-resize.patch) | карточка профиля чата tele автоматически закрывается при изменении размера окна на macOS | всегда вкл. |
| [139](../patches/tdesktop/0139-feat-loop-videos-in-the-media-viewer.patch) | клавиша R зацикливает воспроизведение видео в просмотрщике медиа | всегда вкл. |
| [140](../patches/tdesktop/0140-fix-count-typed-emoji-in-recent-emoji.patch) | копирование сообщений с сохранением разметки в формате Markdown или HTML | всегда вкл. |
| [145](../patches/tdesktop/0145-fix-taller-shot-box-docked-shot-sending-and-a-center.patch) | отображение дата-центра (DC) просматриваемого медиафайла в просмотрщике | всегда вкл. |
| [152](../patches/tdesktop/0152-fix-send-mkv-files-as-videos.patch) | выборочное сохранение удаленных сообщений: только входящие, только исходящие или от всех | всегда вкл. |
| [162](../patches/tdesktop/0162-fix-gif-frame-timing-and-same-name-downloads.patch) | кадры GIF отображаются с собственной длительностью, а скачиваемые файлы с одинаковыми именами больше не перезаписывают друг друга | всегда вкл. |
| [166](../patches/tdesktop/0166-fix-show-tele-menu-items-only-when-their-feature-is-.patch) | скрытие нежелательных сообщений в чатах по ключевым словам или регулярным выражениям | всегда вкл. |
| [168](../patches/tdesktop/0168-feat-regroup-tele-settings-pages.patch) | скрытие хвостиков у пузырей сообщений и контуров обводки | всегда вкл. |
| [169](../patches/tdesktop/0169-feat-collapsible-sub-toggles-in-tele-settings.patch) | отображение больших одиночных эмодзи без белой обводки | всегда вкл. |
| [173](../patches/tdesktop/0173-fix-land-the-send-animation-where-the-message-really.patch) | отправка текстовых подписей вместе со стикерами и показ текста под ними | всегда вкл. |
| [176](../patches/tdesktop/0176-fix-stop-the-chat-list-repainting-while-idle.patch) | список чатов больше не перерисовывается непрерывно в простое, что приводило к зависанию tele через несколько часов | всегда вкл. |
| [177](../patches/tdesktop/0177-fix-send-large-crash-dumps-zipped.patch) | режим энергосбережения: снижение фоновой сетевой активности при работе от батареи ноутбука | всегда вкл. |
| [179](../patches/tdesktop/0179-fix-userpics-in-compact-chat-list-rows.patch) | подтверждение перед установкой реакций в чатах во избежание случайных нажатий | всегда вкл. |
| [182](../patches/tdesktop/0182-fix-who-reacted-list-matches-the-reaction-count.patch) | цитирование части форматированного сообщения с ответом в расширенном редакторе без потери стилей | всегда вкл. |
| [187](../patches/tdesktop/0187-fix-who-read-list-follows-the-read-state.patch) | поиск и мгновенная фильтрация подарков в профиле по названию и атрибутам | всегда вкл. |
| [193](../patches/tdesktop/0193-fix-show-oversized-stickers-as-files-like-the-server.patch) | конструктор сетки витрины профиля: ручная расстановка подарков и выбор рамок | всегда вкл. |
| [199](../patches/tdesktop/0199-feat-select-service-messages.patch) | Студия Подарков: создание уникальных коллекционных подарков из оригинальных ассетов с экспортом | всегда вкл. |
| [200](../patches/tdesktop/0200-fix-hide-the-upgraded-gift-s-number-and-model-until-.patch) | симуляция улучшения подарков (Fake Upgrades) с оригинальной рулеткой без списания Звёзд | всегда вкл. |
| [201](../patches/tdesktop/0201-feat-send-crash-reports-without-a-dump.patch) | открытие проверенных мини-приложений Telegram Mini Apps без повторного окна согласия | всегда вкл. |
| [202](../patches/tdesktop/0202-feat-report-freezes.patch) | отображение списка участников, находящихся сейчас в сети, в заголовке крупных групп | всегда вкл. |
| [206](../patches/tdesktop/0206-feat-copy-a-gift-collection-s-link.patch) | правый клик по коллекции подарков в профиле для копирования ссылки или отправки в чат | всегда вкл. |
| [210](../patches/tdesktop/0210-feat-quote-voice-message-transcriptions.patch) | кнопка «прочитать все» для быстрой очистки центра уведомлений | всегда вкл. |
| [213](../patches/tdesktop/0213-fix-say-why-a-download-couldn-t-be-saved.patch) | при невозможности сохранить загрузку tele сообщает причину ошибки, а папку загрузок чата можно сбросить, если она была удалена | всегда вкл. |
| [214](../patches/tdesktop/0214-fix-retry-failed-upload-parts.patch) | при ошибке загрузки части файла повторяется отправка только упавшего фрагмента, а не всего файла заново | всегда вкл. |
| [215](../patches/tdesktop/0215-fix-teleoffline-keeps-features-that-only-use-telegra.patch) | с флагом -teleoffline функции, использующие только серверы Telegram (конвертация GIF и видео, предпросмотр ссылок, снимки сообщений), продолжают работать | всегда вкл. |
| [218](../patches/tdesktop/0218-fix-deletions-that-fail-on-the-server-come-back.patch) | сообщения, удаление которых завершилось ошибкой на сервере, восстанавливаются с уведомлением вместо тихого исчезновения | всегда вкл. |
| [219](../patches/tdesktop/0219-feat-retry-failed-messages.patch) | все неотправленные сообщения можно повторно отправить разом из меню любого из них | всегда вкл. |
| [220](../patches/tdesktop/0220-feat-find-any-group-member-when-mentioning.patch) | ввод @ в большой группе ищет любых участников на сервере, а не только уже загруженных в память | всегда вкл. |
| [221](../patches/tdesktop/0221-fix-load-the-call-log-in-the-right-page-sizes.patch) | журнал звонков загружает все свои страницы истории | всегда вкл. |
| [222](../patches/tdesktop/0222-fix-read-archived-stickers-from-cache-for-every-acco.patch) | архивные наборы стикеров отображаются для каждого добавленного аккаунта, а не только для первого | всегда вкл. |
| [223](../patches/tdesktop/0223-fix-retry-loading-gift-collections.patch) | повторная попытка загрузки коллекций подарков при сбое сети | всегда вкл. |
| [224](../patches/tdesktop/0224-fix-shared-media-calendar-follows-the-open-sublist.patch) | календарь медиа переходит к дате внутри того открытого чата избранного, в котором вы находитесь | всегда вкл. |
| [229](../patches/tdesktop/0229-fix-tgs-stickers-telegram-would-reject.patch) | TGS-стикеры с заголовком gzip от утилит Windows исправляются перед отправкой, не превращаясь в файлы, а экспорты из студии подарков всегда открываются как стикеры | всегда вкл. |
| [236](../patches/tdesktop/0236-feat-browse-every-tele-version-s-changes.patch) | просмотр и поиск изменений по всем версиям tele | вместе с 109 |
| [237](../patches/tdesktop/0237-fix-late-sent-messages-show-their-real-sent-time.patch) | задержавшееся при отправке сообщение показывает точное время, когда сервер Telegram фактически его отправил | всегда вкл. |
| [240](../patches/tdesktop/0240-feat-what-s-new-as-a-settings-page-with-live-toggles.patch) | раздел «что нового» выполнен как страница настроек: каждая добавленная опция доступна в виде живого переключателя | вместе с 236 |
| [243](../patches/tdesktop/0243-feat-live-previews-in-settings.patch) | настройки режима призрака, скрытых имен и ID чатов показывают интерактивный предпросмотр изменений | всегда вкл. |
| [249](../patches/tdesktop/0249-fix-unbreakable-characters-no-longer-push-message-te.patch) | длинная последовательность неразрывных символов (например, заполнителей хангыля) больше не вылезает за пределы облачка сообщения и выделения | всегда вкл. |
| [250](../patches/tdesktop/0250-fix-the-failed-send-badge-is-clock-sized-and-no-long.patch) | красный значок ошибки отправки имеет размер часов отправки и больше не перекрывает время сообщения в списке чатов и в облачке | всегда вкл. |
| [251](../patches/tdesktop/0251-fix-messages-with-relative-dates-no-longer-freeze-te.patch) | сообщение с обратным отсчетом или относительной датой (например, «сбросится через 5 минут») больше не приводит к зависанию tele спустя время | всегда вкл. |
| [256](../patches/tdesktop/0256-fix-a-line-under-every-open-group-of-tele-settings.patch) | открытая группа настроек tele заканчивается тонкой линией, наглядно показывая границы группы | вместе с 41 |
| [270](../patches/tdesktop/0270-feat-add-tele-to-the-start-menu.patch) | выбор действия по двойному клику на строку чата в списке (открыть, пометить прочитанным, закрепить) | всегда вкл. |
| [275](../patches/tdesktop/0275-feat-badges-on-forwarded-and-reply-headers.patch) | временный подсмотр скрытого времени последнего захода собеседника (Peek Last Seen) | вместе с 12 |
| [276](../patches/tdesktop/0276-feat-select-table-cells-as-a-range.patch) | запрет сохранения самоуничтожающихся медиафайлов во временном дисковом кеше системы | всегда вкл. |
| [285](../patches/tdesktop/0285-feat-copy-links-to-wallet-transactions.patch) | отображение разрыва цепочки («...») при создании снимка непоследовательных сообщений | всегда вкл. |
| [288](../patches/tdesktop/0288-feat-say-that-the-money-passcode-is-tele-s-passcode.patch) | защита от принудительного удаления сообщений собеседником через серверные отметки | всегда вкл. |
| [289](../patches/tdesktop/0289-feat-dim-every-other-address-group-like-ios.patch) | отложенная отправка сообщений с автоматическим переходом в offline сразу после передачи | всегда вкл. |
| [290](../patches/tdesktop/0290-fix-clicking-another-collage-item-switches-the-open-.patch) | переключатель формата ID: обычный числовой или формат Bot API с префиксом `-100` | всегда вкл. |
| [291](../patches/tdesktop/0291-fix-double-click-selects-words-in-service-messages-a.patch) | группировка всплывающих системных уведомлений по чатам | всегда вкл. |
| [293](../patches/tdesktop/0293-fix-dismissing-the-draft-save-box-no-longer-blocks-c.patch) | полное скрытие историй (stories) отовсюду: из списка чатов, профилей и медиаленты | всегда вкл. |
| [294](../patches/tdesktop/0294-feat-copy-the-text-of-service-messages.patch) | отображение точной даты и времени загрузки файла в окне просмотрщика медиа | всегда вкл. |
| [295](../patches/tdesktop/0295-feat-copy-and-open-transaction-links-from-money-tran.patch) | плавное масштабирование и полноразмерный просмотр любых аватаров профиля | всегда вкл. |
| [296](../patches/tdesktop/0296-feat-resize-the-money-window.patch) | копирование чистого числового ID без префиксов по долгому нажатию | всегда вкл. |
| [305](../patches/tdesktop/0305-fix-quote-the-fee-of-a-wallet-key-update-again.patch) | точный предварительный расчет сетевой комиссии TON при обновлении ключей кошелька | всегда вкл. |
| [317](../patches/tdesktop/0317-fix-gifts-in-money-look-like-gift-cards-instead-of-a.patch) | корректное отображение подарков в кошельке Money в виде подарочных карт | всегда вкл. |
| [322](../patches/tdesktop/0322-fix-code-blocks-keep-the-indent-of-their-first-line.patch) | сохранение исходных отступов первой строки в моноширинных блоках программного кода | всегда вкл. |
| [326](../patches/tdesktop/0326-feat-update-buttons-open-tele-s-updates.patch) | кнопки обновления telegram (неподдерживаемые сообщения, rich-страницы, истории, вход) открывают обновления tele и проверяют новую версию вместо сайта загрузки telegram. сборки без встроенного автообновления открывают gettele.app, как и ссылка в старых неподдерживаемых сообщениях | всегда вкл. |
| [334](../patches/tdesktop/0334-fix-file-pickers-on-macos-no-longer-crash-when-their.patch) | на macOS tele больше не вылетает, когда окно, из которого был открыт выбор файлов, закрывается при открытом диалоге | всегда вкл. |
| [335](../patches/tdesktop/0335-fix-the-telegram-chat-shows-telegram-s-logo.patch) | служебный чат telegram показывает логотип Telegram, пока не загрузится его аватарка, а не значок tele | вместе с 88 |
| [336](../patches/tdesktop/0336-fix-picking-files-on-macos-no-longer-freezes-tele.patch) | на macOS выбор файлов для отправки или открытия и выбор папок открывает модальный лист поверх окна, поэтому tele продолжает работать до его закрытия вместо зависания | всегда вкл. |
| [1001](../patches/Telegram/lib_ui/0001-fix-unbreakable-characters-no-longer-scroll-text-fie.patch) | текстовое поле с длинной цепочкой неразрывных символов больше не скроллится вбок, скрывая остальной интерфейс | всегда вкл. |
| [1005](../patches/Telegram/lib_ui/0005-fix-the-maximize-button-follows-the-real-window-stat.patch) | кнопка развертывания окна корректно отображается и работает после изменения размера или перемещения окна из развернутого или полноэкранного режима | всегда вкл. |

<a id="other"></a>
## другое

everything else.

| # | what it does | toggle |
|---|---|---|
| [301](../patches/tdesktop/0301-feat-scripting-prototype.patch) | повышенный битрейт записи голосовых сообщений (до 64 кбит/с Opus) для студийного качества | tele → scripts β, off |
| [316](../patches/tdesktop/0316-fix-listing-accounts-from-a-script-no-longer-crashes.patch) | предотвращение сбоя при получении списка активных аккаунтов через API скриптов | вместе с 301 |
| [321](../patches/tdesktop/0321-feat-let-scripts-give-their-menu-items-icons.patch) | поддержка кастомных иконок для пунктов меню, добавляемых пользовательскими скриптами | вместе с 301 |
| [1006](../patches/Telegram/lib_ui/0006-feat-let-scripts-swap-label-texts-and-find-full-widt.patch) | текст в окнах tele, измененный скриптом, восстанавливается в точности как был (с форматированием и эмодзи) после остановки скрипта, а строки скрипта в информационных таблицах остаются выше разделительной черты | вместе с 301 |
