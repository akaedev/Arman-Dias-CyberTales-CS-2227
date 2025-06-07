from models import db, QuizQuestion
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

questions = [
    {
        "text_en": "What is the safest way to manage your passwords?",
        "text_ru": "Каков самый безопасный способ управления вашими паролями?",
        "text_kk": "Құпия сөздерді басқарудың ең қауіпсіз әдісі қандай?",
        "options_en": [ "Write them on paper", "Use the same one everywhere", "Use a password manager"],
        "options_ru": [ "Запишите их на бумаге", "Используйте везде одни и те же", "Используйте менеджер паролей"],
        "options_kk": [ "Оларды қағазға жазыңыз", "барлық жерде бірдей қолданыңыз", "құпия сөз менеджерін қолданыңыз"],
        "correct": 2,
        "explanation_en": "Password managers generate and store strong, unique passwords for each account.",
        "explanation_ru": "Менеджеры паролей генерируют и хранят надежные, уникальные пароли для каждой учетной записи.",
        "explanation_kk": "Құпия сөз менеджерлері әрбір тіркелгі үшін күшті, бірегей құпия сөздерді жасайды және сақтайды."
    },
    {
        "text_en": "Why are software updates important?",
        "text_ru": "Почему важны обновления программного обеспечения?",
        "text_kk": "Бағдарламалық жасақтама жаңартулары неге маңызды?",
        "options_en": [ "They add cool new themes", "They fix security issues", "They slow down your device"],
        "options_ru": ["Они добавляют новые интересные темы", "Они устраняют проблемы с безопасностью", "Они замедляют работу вашего устройства"],
        "options_kk": ["Олар жаңа қызықты тақырыптар қосады", "олар қауіпсіздік мәселелерін шешеді", "олар сіздің құрылғыңызды баяулатады"],
        "correct": 1,
        "explanation_en": "Updates often include critical patches for known security vulnerabilities.",
        "explanation_ru": "Обновления часто содержат критические исправления для устранения известных уязвимостей в системе безопасности.",
        "explanation_kk": "Жаңартулар көбінесе белгілі қауіпсіздік осалдықтарын жою үшін маңызды түзетулерді қамтиды."
    },
    {
        "text_en": "Which URL is likely a phishing link?",
        "text_ru": "Какой URL, скорее всего, является фишинговой ссылкой?",
        "text_kk": "Қандай URL фишингтік сілтеме болуы мүмкін?",
        "options_en": [ "https://bank.com/login", "https://secure.bank.com", "https://b4nk-login.secure-fix.ru"],
        "options_ru": [ "https://bank.com/login", "https://secure.bank.com", "https://b4nk-login.secure-fix.ru"],
        "options_kk": [ "https://bank.com/login", "https://secure.bank.com", "https://b4nk-login.secure-fix.ru"],
        "correct": 2,
        "explanation_en": "Phishing URLs often mimic real domains using misspelled names and extra domains.",
        "explanation_ru": "Фишинговые URL-адреса часто имитируют реальные домены, используя имена с ошибками в написании и дополнительные домены.",
        "explanation_kk": "Фишингтік URL мекенжайлары көбінесе қате жазылған атаулар мен қосымша домендерді қолдана отырып, нақты домендерге еліктейді."
    },
    {
        "text_en": "What is a good Wi-Fi security practice?",
        "text_ru": "Как правильно обеспечить безопасность Wi-Fi?",
        "text_kk": "Wi-Fi қауіпсіздігін қалай қамтамасыз етуге болады?",
        "options_en": [ "Use open Wi-Fi without passwords", "Change the default router password", "Share your Wi-Fi with everyone" ],
        "options_ru": [ "Используйте открытый Wi-Fi без паролей", "Измените пароль маршрутизатора по умолчанию", "Поделитесь своим Wi-Fi со всеми" ],
        "options_kk": [ "Құпия сөзсіз ашық Wi-Fi пайдаланыңыз", "маршрутизатордың әдепкі құпия сөзін өзгертіңіз", "Wi-Fi желісін барлығымен бөлісіңіз" ],
        "correct": 1,
        "explanation_en": "Changing the default password protects against unauthorized access to your network.",
        "explanation_ru": "Изменение пароля по умолчанию защищает от несанкционированного доступа к вашей сети.",
        "explanation_kk": "Әдепкі құпия сөзді өзгерту желіге рұқсатсыз кіруден қорғайды."
    },
    {
        "text_en": "What should you do if you receive a suspicious email?",
        "text_ru": "Что вам следует делать, если вы получили подозрительное электронное письмо?",
        "text_kk": "Егер сіз күдікті электрондық поштаны алсаңыз, не істеуіңіз керек?",
        "options_en": [ "Click the link to check", "Reply and ask for details", "Delete or report it"],  
        "options_ru": [ "Нажмите на ссылку, чтобы проверить", "Ответить и запросить подробности", "Удалить или сообщить об этом"],  
        "options_kk": ["Тексеру үшін сілтемені басыңыз", "жауап беру және мәліметтерді сұрау", "жою немесе хабарлау"],
        "correct": 2,
        "explanation_en": "Suspicious emails should never be interacted with. Report and delete them instead.",
        "explanation_ru": "Никогда не просматривайте подозрительные электронные письма. Вместо этого сообщайте о них и удаляйте.",
        "explanation_kk": "Күдікті электрондық хаттарды ешқашан қарауға болмайды. Оның орнына олар туралы хабарлаңыз және жойыңыз."
    },
    {
        "text_en": "How often should you back up your data?",
        "text_ru": "Как часто вам следует создавать резервные копии ваших данных?",
        "text_kk": "Деректердің сақтық көшірмесін қаншалықты жиі жасау керек?",
        "options_en": [ "Only when your device is full", "Regularly, using automated tools", "Once a year"],
        "options_ru": ["Только когда ваше устройство заполнено", "Регулярно, с помощью автоматизированных средств", "Раз в год"],
        "options_kk": ["Құрылғы толған кезде ғана", "жүйелі түрде, автоматтандырылған құралдармен", "жылына бір рет"],
        "correct": 1,
        "explanation_en": "Frequent backups prevent data loss from malware, theft, or accidents.",
        "explanation_ru": "Частое резервное копирование предотвращает потерю данных в результате вредоносных программ, кражи или несчастных случаев.",
        "explanation_kk": "Жиі сақтық көшірме жасау зиянды бағдарламалардан, ұрлықтан немесе жазатайым оқиғалардан деректердің жоғалуына жол бермейді."
    },
    {
        "text_en": "Which of these is a strong password?",
        "text_ru": "Какой из них является надежным паролем?",
        "text_kk": "Қайсысы күшті құпия сөз?",
        "options_en": [ "password123", "Q!7vT@9z#5", "johnsmith" ],
        "options_ru": [ "password123", "Q!7vT@9z#5", "johnsmith" ],
        "options_kk": [ "password123", "Q!7vT@9z#5", "johnsmith" ],
        "correct": 1,
        "explanation_en": "Strong passwords are long, complex, and contain a mix of letters, numbers, and symbols.",
        "explanation_ru": "Надежные пароли - это длинные, сложные пароли, состоящие из букв, цифр и символов.",
        "explanation_kk": "Күшті Құпия сөздер-әріптерден, сандардан және таңбалардан тұратын ұзын, күрделі Құпия сөздер."
    },
    {
        "text_en": "What does 2FA stand for?",
        "text_ru": "Что означает 2FA?",
        "text_kk": "2FA нені білдіреді?",
        "options_en": [ "Two-Factor Authentication", "Two-Firewall Access", "Trusted File Authorization" ],
        "options_ru": [ "Two-Factor Authentication", "Two-Firewall Access", "Trusted File Authorization" ],
        "options_kk": [ "Two-Factor Authentication", "Two-Firewall Access", "Trusted File Authorization" ],
        "correct": 0,
        "explanation_en": "2FA requires two types of credentials to verify identity and improve security.",
        "explanation_ru": "2FA требует два типа учетных данных для проверки личности и повышения безопасности.",
        "explanation_kk": "2FA жеке басын тексеру және қауіпсіздікті жақсарту үшін тіркелгі деректерінің екі түрін қажет етеді."
    },
    {
        "text_en": "When should you update your antivirus software?",
        "text_ru": "Когда вам следует обновить свое антивирусное программное обеспечение?",
        "text_kk": "Антивирустық бағдарламалық жасақтаманы қашан жаңарту керек?",
        "options_en": [ "Once a year", "Only when infected", "Regularly, or set to auto-update" ],
        "options_ru": [ "Раз в год", "Только при заражении", "Регулярно или настроено на автоматическое обновление" ],
        "options_kk": ["Жылына бір рет", "тек жұқтырған кезде", "үнемі немесе автоматты түрде жаңартуға орнатылған" ],
        "correct": 2,
        "explanation_en": "Regular updates ensure your antivirus has the latest virus definitions.",
        "explanation_ru": "Регулярные обновления гарантируют, что ваш антивирус содержит самые последние определения вирусов.",
        "explanation_kk": "Тұрақты жаңартулар сіздің антивирусыңызда вирустың ең соңғы анықтамалары бар екеніне көз жеткізеді."
    },
    {
        "text_en": "What type of file should you avoid opening from unknown senders?",
        "text_ru": "Какой тип файлов вам следует избегать открывать от неизвестных отправителей?",
        "text_kk": "Белгісіз жіберушілерден қандай файл түрін ашудан аулақ болу керек?",
        "options_en": [ ".jpg", ".pdf", ".exe" ],
        "options_ru": [ ".jpg", ".pdf", ".exe" ],
        "options_kk": [ ".jpg", ".pdf", ".exe" ],
        "correct": 2,
        "explanation_en": ".exe files are executable and can install malicious software on your device.",
        "explanation_ru": "exe-файлы являются исполняемыми и могут устанавливать вредоносное программное обеспечение на ваше устройство.",
        "explanation_kk": "exe файлдары орындалады және құрылғыға зиянды бағдарламалық құралды орната алады."
    },
    {
        "text_en": "What is a VPN used for?",
        "text_ru": "Для чего используется VPN?",
        "text_kk": "VPN не үшін қолданылады?",
        "options_en": [ "Speeding up internet", "Securing online activity", "Blocking popups" ],
        "options_ru": [ "Ускорение Интернета", "Защита онлайн-активности", "Блокировка всплывающих окон" ],
        "options_kk": [ "Интернетті жеделдету", "онлайн әрекетті қорғау", "Қалқымалы терезелерді блоктау" ],
        "correct": 1,
        "explanation_en": "A VPN encrypts your traffic and hides your IP address for privacy and safety.",
        "explanation_ru": "VPN шифрует ваш трафик и скрывает ваш IP-адрес для обеспечения конфиденциальности и безопасности.",
        "explanation_kk": "VPN трафикті шифрлайды және құпиялылық пен қауіпсіздік үшін IP мекенжайыңызды жасырады."
    },
    {
        "text_en": "Which of the following is a secure website?",
        "text_ru": "Какой из перечисленных ниже веб-сайтов является безопасным?",
        "text_kk": "Төмендегі веб-сайттардың қайсысы қауіпсіз?",
        "options_en": [ "http://login.com", "https://secure-site.com", "http://bank-site.com" ],
        "options_ru": [ "http://login.com", "https://secure-site.com", "http://bank-site.com" ],
        "options_kk": [ "http://login.com", "https://secure-site.com", "http://bank-site.com" ],
        "correct": 1,
        "explanation_en": "HTTPS encrypts the connection between your browser and the server.",
        "explanation_ru": "HTTPS шифрует соединение между вашим браузером и сервером.",
        "explanation_kk": "HTTPS браузер мен сервер арасындағы байланысты шифрлайды."
    },
    {
        "text_en": "What is social engineering?",
        "text_ru": "Что такое социальная инженерия?",
        "text_kk": "Әлеуметтік инженерия дегеніміз не?",
        "options_en": [ "Coding a website", "Manipulating people to give up info", "Fixing broken software" ],
        "options_ru": ["Кодирование веб-сайта", "Манипулирование людьми, чтобы заставить их отказаться от информации", "Исправление неисправного программного обеспечения" ],
        "options_kk": ["Веб-сайтты кодтау", "адамдарды ақпараттан бас тарту үшін манипуляциялау", "ақаулы бағдарламалық жасақтаманы түзету"],
        "correct": 1,
        "explanation_en": "Social engineering tricks users into revealing sensitive information.",
        "explanation_ru": "Социальная инженерия обманом заставляет пользователей раскрывать конфиденциальную информацию.",
        "explanation_kk": "Әлеуметтік инженерия пайдаланушыларды құпия ақпаратты ашуға алдайды."
    },
    {
        "text_en": "Which practice helps prevent shoulder surfing?",
        "text_ru": "Какая практика помогает предотвратить Плечевой серфинг(shoulder surfing)?",
        "text_kk": "Иық серфингінің(shoulder surfing) алдын алуға қандай тәжірибе көмектеседі?",
        "options_en": [ "Using public computers", "Typing passwords slowly", "Covering the keyboard when typing" ],
        "options_ru": [ "Использование общедоступных компьютеров", "Медленный ввод паролей", "Прикрывание клавиатуры при наборе текста" ],
        "options_kk": ["Жалпыға ортақ компьютерлерді пайдалану", "Парольдерді баяу енгізу", "Теру кезінде пернетақтаны жабу"],
        "correct": 2,
        "explanation_en": "Covering the keyboard prevents others from seeing your password.",
        "explanation_ru": "Закрывая клавиатуру, вы не даете другим пользователям увидеть ваш пароль.",
        "explanation_kk": "Пернетақтаны жабу арқылы сіз басқа пайдаланушыларға құпия сөзіңізді көруге мүмкіндік бермейсіз."
    },
    {
        "text_en": "What should you do before downloading a mobile app?",
        "text_ru": "Что вы должны сделать перед загрузкой мобильного приложения?",
        "text_kk": "Мобильді қосымшаны жүктемес бұрын не істеу керек?",
        "options_en": [ "Install immediately", "Read reviews and permissions", "Ignore source" ],
        "options_ru": [ "Установить немедленно", "Прочитать отзывы и разрешения", "Игнорировать источник" ],
        "options_kk": [ "Дереу орнату", "Пікірлер мен рұқсаттарды оқу", "Дереккөзді елемеу"],
        "correct": 1,
        "explanation_en": "Always verify the app’s source and permissions.",
        "explanation_ru": "Всегда проверяйте источник и права доступа к приложению.",
        "explanation_kk": "Әрқашан дереккөзді және қолданбаға кіру рұқсаттарын тексеріңіз."
    },
    {
        "text_en": "What is ransomware?",
        "text_ru": "Что такое программа-вымогатель(ransomware)?",
        "text_kk": "Төлем бағдарламасы(ransomware) дегеніміз не?",
        "options_en": [ "A type of password", "A scam website", "Malware that locks data for ransom"],
        "options_ru": [ "Тип пароля", "Мошеннический веб-сайт", "Вредоносное ПО, блокирующее данные с целью получения выкупа"],
        "options_kk": [ "Құпия сөз түрі", "алаяқтық веб-сайт", "сатып алу мақсатында деректерді бұғаттайтын зиянды бағдарлама"],
        "correct": 2,
        "explanation_en": "Ransomware encrypts your data and demands payment to unlock it.",
        "explanation_ru": "Программа-вымогатель шифрует ваши данные и требует плату за их разблокировку.",
        "explanation_kk": "Төлем бағдарламасы сіздің деректеріңізді шифрлайды және оны ашу үшін ақы талап етеді."
    },
    {
        "text_en": "Why is using admin accounts daily risky?",
        "text_ru": "Почему ежедневное использование учетных записей администратора сопряжено с риском?",
        "text_kk": "Неліктен Әкімші есептік жазбаларын күнделікті пайдалану қауіпті?",
        "options_en": [ "They are slower", "They can install anything", "They don't work well" ],
        "options_ru": [ "Они работают медленнее", "На них можно установить все, что угодно", "Они плохо работают" ],
        "options_kk": [ "Олар баяу жұмыс істейді", "Оларға кез келген нәрсені орнатуға болады", "Олар жақсы жұмыс істемейді"],
        "correct": 1,
        "explanation_en": "Using admin accounts increases risk of accidental or unauthorized changes.",
        "explanation_ru": "Использование учетных записей администратора увеличивает риск случайных или несанкционированных изменений.",
        "explanation_kk": "Әкімші тіркелгілерін пайдалану кездейсоқ немесе рұқсат етілмеген өзгерістер қаупін арттырады.."
    },
    {
        "text_en": "What is the safest way to connect to public Wi-Fi?",
        "text_ru": "Какой самый безопасный способ подключения к общедоступному Wi-Fi?",
        "text_kk": "Жалпыға Ортақ Wi-Fi желісіне қосылудың ең қауіпсіз жолы қандай?",
        "options_en": [ "Don't connect", "Use a VPN", "Use incognito mode" ],
        "options_ru": [ "Не подключаться", "Использовать VPN", "Использовать режим инкогнито" ],
        "options_kk": [ "Қосылмау", "VPN пайдалану", "Инкогнито режимін пайдалану" ],
        "correct": 1,
        "explanation_en": "A VPN secures your data on public networks.",
        "explanation_ru": "VPN защищает ваши данные в общедоступных сетях.",
        "explanation_kk": "VPN сіздің деректеріңізді жалпыға ортақ желілерде қорғайды."
    },
    {
        "text_en": "Which of the following is a phishing sign?",
        "text_ru": "Что из перечисленного является признаком фишинга?",
        "text_kk": "Төмендегілердің қайсысы фишингтің белгісі?",
        "options_en": [ "Generic greeting", "Secure HTTPS site", "Correct grammar" ],
        "options_ru": [ "Общее приветствие", "Безопасный сайт HTTPS", "Правильная грамматика" ],
        "options_kk": [ "Жалпы сәлемдесу", "HTTPS қауіпсіз сайты", "дұрыс грамматика" ],
        "correct": 0,
        "explanation_en": "Phishing emails often use vague or generic greetings like 'Dear User'.",
        "explanation_ru": "В фишинговых письмах часто используются расплывчатые или общие приветствия типа 'Уважаемый пользователь'.",
        "explanation_kk": "Фишингтік хаттар көбінесе 'Құрметті пайдаланушы' сияқты түсініксіз немесе жалпы сәлемдесулерді пайдаланады."
    },
    {
        "text_en": "What should you do with old USB drives?",
        "text_ru": "Что вам следует делать со старыми USB-накопителями?",
        "text_kk": "Ескі USB дискілерімен не істеу керек?",
        "options_en": [ "Reuse without scanning", "Destroy or securely erase them", "Give them away" ],
        "options_ru": [ "Повторно использовать без сканирования", "Уничтожить или надежно стереть их", "Отдать их" ],
        "options_kk": ["Сканерлеусіз қайта пайдалану", "Оларды жою немесе сенімді түрде өшіру", "Оларды беру"],
        "correct": 1,
        "explanation_en": "Old USBs can carry malware and should be securely wiped or destroyed.",
        "explanation_ru": "Старые USB-накопители могут содержать вредоносное ПО и должны быть надежно стерты или уничтожены.",
        "explanation_kk": "Ескі USB дискілерінде зиянды бағдарлама болуы мүмкін және оларды сенімді түрде өшіру немесе жою қажет."
    },
    {
        "text_en": "What’s a good email hygiene practice?",
        "text_ru": "Как правильно соблюдать правила электронной почты?",
        "text_kk": "Электрондық пошта ережелерін қалай дұрыс сақтау керек?",
        "options_en": [ "Reply to unknown senders", "Click all unsubscribe links", "Verify links before clicking" ],
        "options_ru": [ "Отвечать неизвестным отправителям", "Нажимать на все ссылки для отмены подписки", "Проверять ссылки перед нажатием" ],
        "options_kk": [ "Белгісіз жіберушілерге жауап беру", "Жазылымнан бас тарту үшін барлық сілтемелерді басу", "Басар алдында сілтемелерді тексеру"],
        "correct": 2,
        "explanation_en": "Hover over links to verify before clicking in emails.",
        "explanation_ru": "Наведите курсор на ссылки для проверки, прежде чем переходить по электронным письмам.",
        "explanation_kk": "Электрондық поштаға өтпес бұрын тексеру сілтемелерінің үстіне апарыңыз."
    },
    {
        "text_en": "When should you change passwords?",
        "text_ru": "Когда вам следует сменить пароль?",
        "text_kk": "Құпия сөзді қашан өзгерту керек?",
        "options_en": [ "Only if hacked", "Never", "After breach or regularly" ],
        "options_ru": [ "Только в случае взлома", "Никогда", "После взлома или регулярно" ],
        "options_kk": [ "Тек бұзылған жағдайда", "Ешқашан", "Бұзғаннан кейін немесе үнемі" ],
        "correct": 2,
        "explanation_en": "Regular changes and after security breaches help maintain account safety.",
        "explanation_ru": "Регулярные изменения и устранение нарушений безопасности помогают поддерживать безопасность учетной записи.",
        "explanation_kk": "Қауіпсіздікті үнемі өзгерту және жою есептік жазбаның қауіпсіздігін сақтауға көмектеседі."
    },
    {
        "text_en": "What is multi-factor authentication?",
        "text_ru": "Что такое многофакторная аутентификация?",
        "text_kk": "Көп факторлы аутентификация дегеніміз не?",
        "options_en": [ "Using two passwords", "Multiple logins", "Two or more verification methods" ],
        "options_ru": [ "Использование двух паролей", "Несколько логинов", "Два или более метода проверки" ],
        "options_kk": [ "Екі құпия сөзді пайдалану", "Бірнеше логин", "Екі немесе одан да көп тексеру әдісі"],
        "correct": 2,
        "explanation_en": "MFA combines something you know, have, or are to verify identity.",
        "explanation_ru": "Многофакторная аутентификация объединяет в себе все, что вы знаете, имеете или собираетесь использовать для проверки личности.",
        "explanation_kk": "Көп факторлы аутентификация сіз білетін, бар немесе жеке басын тексеру үшін пайдаланғыңыз келетін барлық нәрсені біріктіреді."
    },
    {
        "text_en": "Where should you store important backups?",
        "text_ru": "Где следует хранить важные резервные копии?",
        "text_kk": "Маңызды сақтық көшірмелерді қайда сақтау керек?",
        "options_en": [ "Same device", "External and cloud storage", "Flash drives only" ],
        "options_ru": [ "На одном устройстве", "Внешнее и облачное хранилище", "Только флэш-накопители" ],
        "options_kk": [ "Бір құрылғыда", "Cыртқы және бұлтты сақтау", "Тек флэш-дискілер"],
        "correct": 1,
        "explanation_en": "Keep backups in different locations in case one is compromised.",
        "explanation_ru": "Храните резервные копии в разных местах на случай, если одна из них будет скомпрометирована.",
        "explanation_kk": "Егер олардың біреуі бұзылған болса, сақтық көшірмелерді әртүрлі жерлерде сақтаңыз."
    },
    {
        "text_en": "Which setting helps reduce device tracking?",
        "text_ru": "Какой параметр помогает уменьшить отслеживание устройств?",
        "text_kk": "Қандай параметр құрылғыны бақылауды азайтуға көмектеседі?",
        "options_en": [ "Enable GPS", "Disable location tracking", "Use social media often" ],
        "options_ru": [ "Включить GPS", "Отключить отслеживание местоположения", "Часто пользоваться социальными сетями" ],
        "options_kk": [ "GPS қосу", "Орынды бақылауды өшіру", "Әлеуметтік медианы жиі пайдалану"],
        "correct": 1,
        "explanation_en": "Turning off location sharing reduces tracking.",
        "explanation_ru": "Отключение общего доступа к местоположению сокращает время отслеживания.",
        "explanation_kk": "Орналасқан жерді бөлісуді өшіру бақылау уақытын қысқартады."
    },
    {
        "text_en": "What is a secure way to dispose of a hard drive?",
        "text_ru": "Каков безопасный способ утилизации жесткого диска?",
        "text_kk": "Қатты дискіні қайта өңдеудің қауіпсіз әдісі қандай?",
        "options_en": [ "Throw it in trash", "Smash it physically", "Recycle unformatted" ],
        "options_ru": [ "Выбросьте это в мусорное ведро", "Разбейте физически", "Утилизируйте неформатированное" ],
        "options_kk": ["Оны қоқыс жәшігіне тастаңыз", "Физикалық түрде сындырыңыз", "Пішімделмеген қоқысқа тастаңыз"],
        "correct": 1,
        "explanation_en": "Physically destroy drives or use secure wipe tools.",
        "explanation_ru": "Физически уничтожьте диски или воспользуйтесь средствами безопасной очистки.",
        "explanation_kk": "Дискілерді физикалық түрде жойыңыз немесе қауіпсіз тазалау құралдарын пайдаланыңыз."
    },
    {
        "text_en": "What is the safest browser behavior?",
        "text_ru": "Какое поведение браузера является наиболее безопасным?",
        "text_kk": "Браузердің ең қауіпсіз әрекеті қандай?",
        "options_en": [ "Allow popups", "Avoid unfamiliar links", "Disable HTTPS" ],
        "options_ru": [ "Разрешить всплывающие окна", "Избегать незнакомых ссылок", "Отключить HTTPS" ],
        "options_kk": ["Қалқымалы терезелерге рұқсат беру", "Бейтаныс сілтемелерден аулақ болу", "HTTPS өшіру"],
        "correct": 1,
        "explanation_en": "Avoid clicking on unknown or suspicious links.",
        "explanation_ru": "Избегайте переходов по неизвестным или подозрительным ссылкам.",
        "explanation_kk": "Белгісіз немесе күдікті сілтемелер арқылы өтуден аулақ болыңыз."
    },
    {
        "text_en": "Why is public charging risky?",
        "text_ru": "Почему публичная зарядки сопряжены риском?",
        "text_kk": "Неліктен қоғамдық зарядтау қауіпті?",
        "options_en": [ "It’s slow", "Can transmit malware", "It doesn’t charge" ],
        "options_ru": [ "Работает медленно", "Может передавать вредоносное ПО", "Не заряжают" ],
        "options_kk": [ "Баяу жұмыс істейді", "Зиянды бағдарламаны жібере алады", "Зарядталмайды"],
        "correct": 1,
        "explanation_en": "Public USB ports can transfer data and potentially malware (juice jacking).",
        "explanation_ru": "Общедоступные USB-порты могут передавать данные и потенциально вредоносное ПО (juice jacking).",
        "explanation_kk": "Жалпыға қол жетімді USB порттары деректерді және ықтимал зиянды бағдарламаны (juice jacking) жібере алады."
    },
    {
        "text_en": "How to recognize fake software updates?",
        "text_ru": "Как распознать поддельные обновления программного обеспечения?",
        "text_kk": "Жалған бағдарламалық жасақтама жаңартуларын қалай тануға болады?",
        "options_en": [ "They prompt from browsers", "They install quickly", "They come from app stores" ],
        "options_ru": [ "Они запрашиваются из браузеров", "Они быстро устанавливаются", "Они поступают из магазинов приложений" ],
        "options_kk": [ "Олар браузерлерден сұралады", "Олар тез орнатылады", "Олар қолданбалар дүкендерінен келеді"],
        "correct": 0,
        "explanation_en": "Fake updates often appear as popups in web browsers.",
        "explanation_ru": "Поддельные обновления часто появляются в виде всплывающих окон в веб-браузерах.",
        "explanation_kk": "Жалған жаңартулар көбінесе веб-шолғыштарда қалқымалы терезелер ретінде пайда болады."
    },
    {
        "text_en": "What’s the first step after detecting a breach?",
        "text_ru": "Каков первый шаг после обнаружения нарушения?",
        "text_kk": "Бұзушылықты анықтағаннан кейінгі алғашқы қадам қандай?",
        "options_en": [ "Ignore it", "Notify IT or security team", "Share online" ],
        "options_ru": [ "Проигнорировать это", "Уведомить ИТ-отдел или службу безопасности", "Поделиться онлайн" ],
        "options_kk": [ "Оны елемеу", "IT бөліміне немесе қауіпсіздік қызметіне хабарлау", "Желіде бөлісу"],
        "correct": 1,
        "explanation_en": "Immediately report breaches to reduce impact and start recovery.",
        "explanation_ru": "Немедленно сообщайте о нарушениях, чтобы уменьшить последствия и начать восстановление.",
        "explanation_kk": "Салдарын азайту және қалпына келтіруді бастау үшін бұзушылықтар туралы дереу хабарлаңыз."
    },
    {
        "text_en": "How should IoT devices be secured?",
        "text_ru": "Как следует защищать устройства Интернета вещей(Iot)?",
        "text_kk": "Интернет заттарының(Iot) құрылғыларын қалай қорғауға болады?",
        "options_en": [ "Use default settings", "Disable updates", "Change default credentials" ],
        "options_ru": [ "Использовать настройки по умолчанию", "Отключить обновления", "Изменить учетные данные по умолчанию" ],
        "options_kk": ["Әдепкі параметрлерді пайдалану", "Жаңартуларды өшіру", "Әдепкі тіркелгі деректерін өзгерту"],
        "correct": 2,
        "explanation_en": "Changing default credentials prevents easy exploitation.",
        "explanation_ru": "Изменение учетных данных по умолчанию препятствует легкому использованию.",
        "explanation_kk": "Әдепкі тіркелгі деректерін өзгерту оңай пайдалануға жол бермейді."
    },
    {
        "text_en": "Which method best protects cloud storage?",
        "text_ru": "Какой метод наилучшим образом защищает облачное хранилище?",
        "text_kk": "Бұлтты сақтауды қандай әдіс жақсы қорғайды?",
        "options_en": [ "Public folders", "MFA and encryption", "Short passwords" ],
        "options_ru": [ "Общие папки", "MFA и шифрование", "Короткие пароли" ],
        "options_kk": [ "Ортақ қалталар", "MFA және шифрлау", "Қысқа парольдер" ],
        "correct": 1,
        "explanation_en": "Use multi-factor authentication and encrypted files.",
        "explanation_ru": "Используйте многофакторную аутентификацию и зашифрованные файлы.",
        "explanation_kk": "Көп факторлы аутентификация мен шифрланған файлдарды пайдаланыңыз."
    },
    {
        "text_en": "Which of the following is an example of safe email behavior?",
        "text_ru": "Что из приведенного ниже является примером безопасного поведения при работе с электронной почтой?",
        "text_kk": "Төмендегілердің қайсысы электрондық поштамен жұмыс істеу кезінде қауіпсіз мінез-құлықтың мысалы болып табылады?",
        "options_en": [ "Clicking unknown links", "Downloading all attachments", "Using work email professionally" ],
        "options_ru": [ "Переход по неизвестным ссылкам", "Загрузка всех вложений", "Профессиональное использование рабочей электронной почты" ],
        "options_kk": [ "Белгісіз сілтемелерге өту", "Барлық тіркемелерді жүктеу", "Жұмыс электрондық поштасын кәсіби пайдалану"],
        "correct": 2,
        "explanation_en": "Keep work email focused on professional, verified communication.",
        "explanation_ru": "Ориентируйте рабочую электронную почту на профессиональное, проверенное общение.",
        "explanation_kk": "Жұмыс электрондық поштасын кәсіби, дәлелденген байланысқа бағыттаңыз."
    },
    {
        "text_en": "What is a botnet?",
        "text_ru": "Что такое ботнет?",
        "text_kk": "Ботнет дегеніміз не?",
        "options_en": [ "A security app", "Network of infected computers", "Firewall system" ],
        "options_ru": [ "Приложение для обеспечения безопасности", "Сеть зараженных компьютеров", "Система брандмауэра" ],
        "options_kk": [ "Қауіпсіздік қолданбасы", "Вирус жұққан Компьютерлер желісі", "Брандмауэр жүйесі"],
        "correct": 1,
        "explanation_en": "A botnet is a group of compromised devices controlled by attackers.",
        "explanation_ru": "Ботнет - это группа скомпрометированных устройств, контролируемых злоумышленниками.",
        "explanation_kk": "Ботнет-зиянкестер басқаратын бұзылған Құрылғылар тобы."
    },
    {
        "text_en": "What is a good policy for mobile device security?",
        "text_ru": "Какова хорошая политика безопасности мобильных устройств?",
        "text_kk": "Мобильді қауіпсіздік саясаты қандай?",
        "options_en": [ "Use auto-login", "Avoid screen lock", "Enable  biometric authentication" ],
        "options_ru": [ "Использовать автоматический вход в систему", "Избегать блокировки экрана", "Включить биометрическую аутентификацию" ],
        "options_kk": ["Автоматты кіруді пайдалану", "Экранды құлыптаудан аулақ болу", "Биометриялық аутентификацияны қосу"],
        "correct": 2,
        "explanation_en": "Biometric methods like fingerprint or face ID help secure mobile devices.",
        "explanation_ru": "Биометрические методы, такие как идентификация по отпечатку пальца или лицу, помогают защитить мобильные устройства.",
        "explanation_kk": "Саусақ ізін немесе бетті анықтау сияқты биометриялық әдістер мобильді құрылғыларды қорғауға көмектеседі."
    },
    {
        "text_en": "What is spear phishing?",
        "text_ru": "Что такое целевой фишинг(spear phishing)?",
        "text_kk": "Мақсатты фишинг(spear phishing) дегеніміз не?",
        "options_en": [ "Mass scam emails", "Targeted phishing attack", "Phone scam" ],
        "options_ru": [ "Массовые мошеннические электронные письма", "Целенаправленная фишинговая атака", "Телефонное мошенничество" ],
        "options_kk": [ "Жаппай алаяқтық хаттар", "Мақсатты фишингтік шабуыл", "Телефондық алаяқтық"],
        "correct": 1,
        "explanation_en": "Spear phishing targets specific individuals using personalized information.",
        "explanation_ru": "Целевой фишинг нацелен на конкретных людей, использующих персонализированную информацию.",
        "explanation_kk": "Мақсатты фишинг жекелендірілген ақпаратты пайдаланатын нақты адамдарға бағытталған."
    },
    {
        "text_en": "What is spyware?",
        "text_ru": "Что такое шпионское ПО?",
        "text_kk": "Шпиондық бағдарлама дегеніміз не?",
        "options_en": [ "Software that protects your device", "Software that tracks user behavior", "A type of firewall" ],
        "options_ru": [ "Программное обеспечение, защищающее ваше устройство", "Программное обеспечение, отслеживающее поведение пользователя", "Тип брандмауэра" ],
        "options_kk": ["Құрылғыны қорғайтын бағдарламалық құрал", "Пайдаланушының әрекетін бақылайтын Бағдарламалық құрал", "Брандмауэр түрі"],
        "correct": 1,
        "explanation_en": "Spyware secretly monitors user activity, often for malicious purposes.",
        "explanation_ru": "Шпионское ПО тайно отслеживает активность пользователей, часто в злонамеренных целях.",
        "explanation_kk": "Шпиондық бағдарлама пайдаланушылардың белсенділігін жасырын түрде бақылайды, көбінесе зиянды мақсаттар үшін."
    },
    {
        "text_en": "What is the safest action if you get a popup saying 'Your computer is infected'?",
        "text_ru": "Что является самым безопасным действием, если вы получаете всплывающее окно с надписью 'Ваш компьютер заражен'?",
        "text_kk": "Егер сіз 'сіздің компьютеріңіз вирус жұқтырған' деген қалқымалы терезені алсаңыз, ең қауіпсіз әрекет қандай?",
        "options_en": [ "Click and follow the instructions", "Ignore and close the browser tab", "Download the recommended software" ],
        "options_ru": [ "Нажмите и следуйте инструкциям", "Проигнорируйте и закройте вкладку браузера", "Загрузите рекомендуемое программное обеспечение" ],
        "options_kk": ["Нұсқауларды нұқыңыз және орындаңыз", "Браузер қойындысын елемеңіз және жабыңыз", "Ұсынылған бағдарламалық жасақтаманы жүктеңіз"],
        "correct": 1,
        "explanation_en": "Such popups are often scams. Close the browser and run a real antivirus scan.",
        "explanation_ru": "Такие всплывающие окна часто являются мошенническими. Закройте браузер и запустите настоящую антивирусную проверку.",
        "explanation_kk": "Мұндай қалқымалы терезелер көбінесе алаяқтық болып табылады. Браузерді жауып, нақты антивирустық тексеруді бастаңыз."
    },
    {
        "text_en": "What is a DDoS attack?",
        "text_ru": "Что такое DDoS-атака?",
        "text_kk": "DDoS шабуылы дегеніміз не?",
        "options_en": [ "An email scam", "Flooding a system with traffic", "A password cracking tool" ],
        "options_ru": [ "Мошенничество с электронной почтой", "Наводнение системы трафиком", "Инструмент для взлома паролей" ],
        "options_kk": ["Электрондық поштаны алдау", "Жүйені трафикпен толтыру", "Құпия сөзді бұзу құралы"],
        "correct": 1,
        "explanation_en": "A DDoS attack overwhelms a server or network with traffic to make it unavailable.",
        "explanation_ru": "DDoS-атака перегружает сервер или сеть трафиком, делая их недоступными.",
        "explanation_kk": "DDoS шабуылы серверді немесе желіні трафикпен шамадан тыс жүктейді, бұл оларды қол жетімсіз етеді."
    },
    {
        "text_en": "Which of the following is best for protecting a home network?",
        "text_ru": "Что из перечисленного лучше всего подходит для защиты домашней сети?",
        "text_kk": "Жоғарыда айтылғандардың қайсысы Үй желісін қорғау үшін жақсы?",
        "options_en": [ "Leaving the router open", "Changing default router settings", "Using old firmware" ],
        "options_ru": [ "Оставить маршрутизатор открытым", "Изменить настройки маршрутизатора по умолчанию", "Использовать старую прошивку" ],
        "options_kk": ["Маршрутизаторды ашық қалдырыңыз", "Маршрутизатордың әдепкі параметрлерін өзгертіңіз", "Ескі микробағдарламаны қолданыңыз"],
        "correct": 1,
        "explanation_en": "Always change default router credentials and keep firmware updated.",
        "explanation_ru": "Всегда меняйте учетные данные маршрутизатора по умолчанию и обновляйте встроенное ПО.",
        "explanation_kk": "Әрқашан маршрутизатордың әдепкі тіркелгі деректерін өзгертіңіз және кірістірілген Бағдарламалық құралды жаңартыңыз."
    }
]

#добавление вопросов
with app.app_context():
    db.create_all()
    for q in questions:
        question = QuizQuestion(
            text_en=q["text_en"],
            text_ru=q["text_ru"],
            text_kk=q["text_kk"],
            options_en=q["options_en"],
            options_ru=q["options_ru"],
            options_kk=q["options_kk"],
            correct=q["correct"],
            explanation_en=q["explanation_en"],
            explanation_ru=q["explanation_ru"],
            explanation_kk=q["explanation_kk"]
        )
        db.session.add(question)
    db.session.commit()
    print("Questions added successfully.")