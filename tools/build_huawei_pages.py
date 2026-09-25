"""Generate the Huawei/AppGallery landing page in every language.

    python tools/build_huawei_pages.py

Writes huawei.html plus <lang>/huawei.html. Edit the copy HERE, not in the
generated HTML, or the next run will overwrite it. Every language shares one
template so the pages can't drift apart structurally.

Facts the copy relies on (verified in the AreYouDead app source, 2026-09-25):
- timer choices run 30 min .. 48 h (data/Models.kt)
- huawei flavor: GATEWAY_ENABLED=true -> server backstop fires with phone off
- non-+1 numbers go by WhatsApp; email is REQUIRED for them (ContactsScreen.kt)
- app UI exists only in English + Simplified Chinese (res/values, values-zh)
- AppGallery distribution excludes the US and mainland China
- price differs per country (tax-inclusive tiers) -> never print a number here
"""
import html
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://checkinonme.app"
APPGALLERY = "https://appgallery.huawei.com/app/C117141237"
PLAY = "https://play.google.com/store/apps/details?id=app.safepulse"
APPSTORE = "https://apps.apple.com/app/safepulse-check-in-alert/id6760568365"

LANGS = {}

LANGS["en"] = dict(
    path="/huawei", hreflang="en", og_locale="en_US", label="English", dir="ltr",
    title="SafePulse for Huawei — Safety Check-In App Without Google | Check In On Me",
    desc="SafePulse on Huawei AppGallery: set a check-in timer, and if you don't check in, your chosen contacts get your location by WhatsApp and email, even if your phone is off. Works without Google services.",
    nav=["How it works", "Limits", "FAQ", "Get the app"],
    h1="A safety check-in app that works on Huawei, without Google.",
    tagline="Set a timer before you go out. If you don't check in when it ends, SafePulse alerts the people you chose with your last known location, even if your phone is off, dead, or out of signal.",
    cta=["Get it on AppGallery", "How it works"],
    intro_h="Made for phones without Google Play services",
    intro=["Newer Huawei phones don't include Google Play services, and many safety apps quietly depend on them for location. On those phones the alert still arrives, but without the one thing that matters: where you are.",
           "SafePulse uses the phone's own location system when Google isn't there, so the map link in your alert works on Huawei phones too. The Huawei edition is reviewed and published on AppGallery."],
    how_h="How it works", how_sub="Three steps, and only the first takes any effort.",
    steps=[("Set a timer", "Before a late walk home, a first date, a long drive or a night shift, pick a window from 30 minutes to 48 hours."),
           ("Check in when you're safe", "One tap clears the timer. Nothing is sent and nobody is bothered."),
           ("Or don't, and they're told", "If the timer runs out, your contacts get a message and an email with your last known location. They don't need the app.")],
    feat_h="Why it's built this way",
    feats=[("Location without Google", "The alert includes a map link to your last known position, taken from the phone's own GPS and network location. No Google account or Google services needed."),
           ("Works with the phone off", "Your countdown is also kept on our server. If your phone is switched off, broken, out of battery or taken, the server sends the alert anyway."),
           ("WhatsApp and email", "Outside North America, alerts go by WhatsApp and email. Email is required for every contact, because a WhatsApp message can fail to arrive without any warning."),
           ("Contacts agree first", "Each person you add gets a request and must accept it before they can receive alerts. Nobody gets a surprise emergency message from a stranger.")],
    lim_h="What it is not", lim_sub="Safety tools get oversold. Here are the limits, plainly.",
    lims=[("Not an emergency service.", "SafePulse does not call the police, an ambulance or any emergency number, and nobody monitors it. It tells the people you chose. If you are in danger and can call, call your local emergency number."),
          ("Not a panic button.", "It works the other way round: it goes off when you can't act."),
          ("Not location tracking.", "Nobody can see where you are while a check-in is running normally. Your location is shared only if you miss a check-in."),
          ("Not a guarantee.", "It needs mobile or internet service to reach your contacts. It shortens the time before someone knows something is wrong. It doesn't prevent anything."),
          ("App language.", "The app's screens are in English and Simplified Chinese.")],
    faq_h="Questions",
    faqs=[("Does it need Google Play services?", "No. The Huawei edition works on phones without Google, including newer Huawei models. Location comes from the phone's own GPS and network location."),
          ("Does it track my location all the time?", "No. Location is read for a check-in and shared only if you miss it. Nobody can look up where you are while everything is fine."),
          ("What if my phone is off or taken?", "The alert still goes out. The countdown is kept on a server too, so if your phone never checks in, the server sends the alert itself."),
          ("Do my contacts need the app?", "No. They accept a request once, then receive any alert by WhatsApp and email (or by text message for US and Canadian numbers)."),
          ("How much does it cost?", "SafePulse is a one-time purchase on AppGallery, shown in your local currency. There is no subscription, no ads, and your data is never sold."),
          ("Which countries can get it?", "Most countries where AppGallery operates. It is not offered in the United States or mainland China. In the US, get SafePulse on Google Play or the App Store instead.")],
    dl_h="Get SafePulse on AppGallery",
    dl_sub="Search for SafePulse in AppGallery, or use the button below. The price is shown in your currency.",
    badge=["Explore it on", "AppGallery"],
    other='Not on a Huawei phone? SafePulse is also on <a href="{play}">Google Play</a> and the <a href="{appstore}">App Store</a>.',
    disclaimer="<strong>Please read:</strong> SafePulse is not an emergency service and does not contact police, fire or ambulance services. It notifies contacts you choose and depends on mobile and internet service to deliver alerts. It is not a substitute for calling your local emergency number.",
    foot=["Home", "Privacy Policy", "Terms of Service"],
    lang_nav="Language",
)

LANGS["es"] = dict(
    path="/es/huawei", hreflang="es", og_locale="es_ES", label="Español", dir="ltr",
    title="SafePulse para Huawei: app de seguridad con check-in, sin Google | Check In On Me",
    desc="SafePulse en Huawei AppGallery: pon un temporizador y, si no confirmas que estás bien, tus contactos reciben tu ubicación por WhatsApp y correo electrónico, aunque tu teléfono esté apagado. Funciona sin los servicios de Google.",
    nav=["Cómo funciona", "Límites", "Preguntas", "Descargar"],
    h1="Una app de seguridad que funciona en Huawei, sin Google.",
    tagline="Pon un temporizador antes de salir. Si no confirmas que estás bien cuando termine, SafePulse avisa a las personas que elegiste con tu última ubicación conocida, aunque tu teléfono esté apagado, sin batería o sin señal.",
    cta=["Descárgala en AppGallery", "Cómo funciona"],
    intro_h="Hecha para teléfonos sin servicios de Google",
    intro=["Los teléfonos Huawei más recientes no incluyen los servicios de Google Play, y muchas apps de seguridad dependen de ellos para la ubicación. En esos teléfonos el aviso llega igual, pero sin lo más importante: dónde estás.",
           "SafePulse usa el sistema de ubicación del propio teléfono cuando Google no está, así que el enlace al mapa de tu aviso también funciona en teléfonos Huawei. La edición para Huawei está revisada y publicada en AppGallery."],
    how_h="Cómo funciona", how_sub="Tres pasos, y solo el primero requiere algo de ti.",
    steps=[("Pon un temporizador", "Antes de volver a casa de noche, de una primera cita, de un viaje largo o de un turno de noche, elige un plazo de entre 30 minutos y 48 horas."),
           ("Confirma cuando estés a salvo", "Un toque detiene el temporizador. No se envía nada y no se molesta a nadie."),
           ("Si no lo haces, se les avisa", "Si el tiempo se acaba, tus contactos reciben un mensaje y un correo con tu última ubicación conocida. No necesitan tener la app.")],
    feat_h="Por qué está hecha así",
    feats=[("Ubicación sin Google", "El aviso incluye un enlace al mapa con tu última posición conocida, obtenida del GPS y la red del propio teléfono. No necesitas cuenta ni servicios de Google."),
           ("Funciona con el teléfono apagado", "Tu cuenta atrás también se guarda en nuestro servidor. Si tu teléfono se apaga, se rompe, se queda sin batería o te lo quitan, el servidor envía el aviso de todos modos."),
           ("WhatsApp y correo electrónico", "Fuera de Norteamérica, los avisos se envían por WhatsApp y por correo. El correo es obligatorio para cada contacto, porque un mensaje de WhatsApp puede no llegar sin ninguna advertencia."),
           ("Tus contactos aceptan primero", "Cada persona que añades recibe una solicitud y debe aceptarla antes de poder recibir avisos. Nadie recibe un mensaje de emergencia inesperado de un desconocido.")],
    lim_h="Lo que no es", lim_sub="Las herramientas de seguridad suelen prometer de más. Estos son los límites, sin rodeos.",
    lims=[("No es un servicio de emergencias.", "SafePulse no llama a la policía, a una ambulancia ni a ningún número de emergencias, y nadie lo supervisa. Avisa a las personas que tú eliges. Si estás en peligro y puedes llamar, llama al número de emergencias de tu país."),
          ("No es un botón de pánico.", "Funciona al revés: se activa cuando tú no puedes actuar."),
          ("No es un rastreador.", "Nadie puede ver dónde estás mientras un check-in transcurre con normalidad. Tu ubicación solo se comparte si no confirmas a tiempo."),
          ("No es una garantía.", "Necesita cobertura móvil o internet para llegar a tus contactos. Acorta el tiempo hasta que alguien sabe que algo va mal. No evita nada."),
          ("El idioma de la app.", "La app está en inglés y en chino simplificado. Esta página está traducida, pero la app todavía no está en español.")],
    faq_h="Preguntas frecuentes",
    faqs=[("¿Necesita los servicios de Google Play?", "No. La edición para Huawei funciona en teléfonos sin Google, incluidos los modelos Huawei más recientes. La ubicación se obtiene del GPS y la red del propio teléfono."),
          ("¿Rastrea mi ubicación todo el tiempo?", "No. La ubicación se lee para un check-in y solo se comparte si no confirmas a tiempo. Nadie puede consultar dónde estás mientras todo va bien."),
          ("¿Y si mi teléfono está apagado o me lo quitan?", "El aviso se envía igual. La cuenta atrás también se guarda en un servidor, así que si tu teléfono nunca confirma, el servidor envía el aviso por sí solo."),
          ("¿Mis contactos necesitan la app?", "No. Aceptan una solicitud una vez y después reciben cualquier aviso por WhatsApp y correo electrónico (o por SMS si su número es de EE. UU. o Canadá)."),
          ("¿Cuánto cuesta?", "SafePulse es un pago único en AppGallery, con el precio en tu moneda local. Sin suscripción, sin anuncios, y tus datos nunca se venden."),
          ("¿En qué países está disponible?", "En la mayoría de los países donde opera AppGallery. No se ofrece en Estados Unidos ni en China continental.")],
    dl_h="Descarga SafePulse en AppGallery",
    dl_sub="Busca SafePulse en AppGallery o usa el botón de abajo. El precio aparece en tu moneda.",
    badge=["Explóralo en", "AppGallery"],
    other='¿No tienes un teléfono Huawei? SafePulse también está en <a href="{play}">Google Play</a> y en la <a href="{appstore}">App Store</a>.',
    disclaimer="<strong>Importante:</strong> SafePulse no es un servicio de emergencias y no contacta con la policía, los bomberos ni los servicios médicos. Avisa a los contactos que tú eliges y depende de la cobertura móvil e internet para entregar los avisos. No sustituye a llamar al número de emergencias de tu país.",
    foot=["Inicio", "Privacidad (en inglés)", "Términos (en inglés)"],
    lang_nav="Idioma",
)

LANGS["ar"] = dict(
    path="/ar/huawei", hreflang="ar", og_locale="ar_AR", label="العربية", dir="rtl",
    title="SafePulse لهواتف هواوي — تطبيق أمان يعمل بدون خدمات Google | Check In On Me",
    desc="SafePulse على متجر AppGallery من هواوي: اضبط مؤقتًا، وإذا لم تؤكد أنك بخير، تصل إلى جهات الاتصال التي اخترتها رسالة بموقعك عبر واتساب والبريد الإلكتروني، حتى لو كان هاتفك مغلقًا. يعمل بدون خدمات Google.",
    nav=["كيف يعمل", "حدوده", "الأسئلة", "التحميل"],
    h1="تطبيق أمان يعمل على هواتف هواوي، بدون Google.",
    tagline="اضبط مؤقتًا قبل أن تخرج. إذا لم تؤكد أنك بخير عند انتهائه، ينبّه SafePulse الأشخاص الذين اخترتهم ويرسل إليهم آخر موقع معروف لك، حتى لو كان هاتفك مغلقًا أو فارغ البطارية أو خارج التغطية.",
    cta=["حمّله من AppGallery", "كيف يعمل"],
    intro_h="مصمَّم للهواتف التي لا تحتوي على خدمات Google Play",
    intro=["لا تتضمن هواتف هواوي الأحدث خدمات Google Play، وكثير من تطبيقات الأمان تعتمد عليها لتحديد الموقع. على هذه الهواتف يصل التنبيه، لكن بدون أهم معلومة فيه: أين أنت.",
           "يستخدم SafePulse نظام تحديد الموقع في الهاتف نفسه عندما لا تتوفر خدمات Google، لذلك يعمل رابط الخريطة في التنبيه على هواتف هواوي أيضًا. نسخة هواوي تمت مراجعتها ونشرها على AppGallery."],
    how_h="كيف يعمل", how_sub="ثلاث خطوات، والأولى فقط تحتاج منك جهدًا.",
    steps=[("اضبط المؤقت", "قبل العودة إلى المنزل ليلًا، أو موعد أول، أو رحلة طويلة، أو مناوبة ليلية، اختر مدة بين 30 دقيقة و48 ساعة."),
           ("أكّد عندما تكون بأمان", "لمسة واحدة توقف المؤقت. لا يُرسَل شيء ولا يُزعَج أحد."),
           ("وإن لم تؤكد، يصلهم التنبيه", "إذا انتهى الوقت، تصل إلى جهات اتصالك رسالة وبريد إلكتروني فيهما آخر موقع معروف لك. لا يحتاجون إلى تثبيت التطبيق.")],
    feat_h="لماذا صُمّم بهذه الطريقة",
    feats=[("الموقع بدون Google", "يتضمن التنبيه رابط خريطة لآخر موقع معروف لك، مأخوذًا من GPS وشبكة الهاتف نفسه. لا حاجة إلى حساب Google أو خدماتها."),
           ("يعمل والهاتف مغلق", "يُحفَظ العدّ التنازلي أيضًا على خادمنا. إذا أُغلق هاتفك أو تعطّل أو نفدت بطاريته أو أُخذ منك، يرسل الخادم التنبيه على أي حال."),
           ("واتساب والبريد الإلكتروني", "خارج أمريكا الشمالية، تُرسَل التنبيهات عبر واتساب والبريد الإلكتروني. البريد الإلكتروني إلزامي لكل جهة اتصال، لأن رسالة واتساب قد لا تصل دون أي إشعار."),
           ("جهات الاتصال توافق أولًا", "كل شخص تضيفه يتلقى طلبًا، ويجب أن يوافق عليه قبل أن تصله أي تنبيهات. لا أحد يتلقى رسالة طوارئ مفاجئة من شخص لا يعرفه.")],
    lim_h="ما ليس عليه التطبيق", lim_sub="كثيرًا ما يُبالَغ في وصف أدوات الأمان. هذه حدود التطبيق بوضوح.",
    lims=[("ليس خدمة طوارئ.", "لا يتصل SafePulse بالشرطة أو الإسعاف أو أي رقم طوارئ، ولا توجد جهة تراقبه. إنه ينبّه الأشخاص الذين تختارهم. إذا كنت في خطر وتستطيع الاتصال، فاتصل برقم الطوارئ في بلدك."),
          ("ليس زر استغاثة.", "يعمل بالعكس: ينطلق عندما لا تستطيع أنت التصرف."),
          ("ليس أداة تتبّع.", "لا يستطيع أحد معرفة مكانك أثناء سير المؤقت بشكل طبيعي. لا يُشارَك موقعك إلا إذا لم تؤكد في الوقت المحدد."),
          ("ليس ضمانًا.", "يحتاج إلى شبكة الهاتف أو الإنترنت ليصل إلى جهات اتصالك. إنه يختصر الوقت حتى يعرف أحد أن شيئًا ما حدث، لكنه لا يمنع وقوع أي شيء."),
          ("لغة التطبيق.", "واجهة التطبيق باللغتين الإنجليزية والصينية المبسّطة. هذه الصفحة مترجمة، لكن التطبيق غير متوفر بالعربية بعد.")],
    faq_h="أسئلة شائعة",
    faqs=[("هل يحتاج إلى خدمات Google Play؟", "لا. تعمل نسخة هواوي على الهواتف التي لا تحتوي على Google، بما فيها طرازات هواوي الأحدث. يُحدَّد الموقع من GPS وشبكة الهاتف نفسه."),
          ("هل يتتبّع موقعي طوال الوقت؟", "لا. يُقرأ الموقع لأجل المؤقت، ولا يُشارَك إلا إذا لم تؤكد في الوقت المحدد. لا يستطيع أحد معرفة مكانك ما دام كل شيء على ما يرام."),
          ("ماذا لو كان هاتفي مغلقًا أو أُخذ مني؟", "يُرسَل التنبيه رغم ذلك. العدّ التنازلي محفوظ على خادم أيضًا، فإذا لم يؤكد هاتفك أبدًا، يرسل الخادم التنبيه بنفسه."),
          ("هل تحتاج جهات اتصالي إلى التطبيق؟", "لا. يوافقون على طلب مرة واحدة، ثم يتلقون أي تنبيه عبر واتساب والبريد الإلكتروني (أو برسالة نصية للأرقام الأمريكية والكندية)."),
          ("كم سعره؟", "SafePulse عملية شراء لمرة واحدة على AppGallery، ويظهر السعر بعملتك المحلية. لا اشتراك ولا إعلانات، ولا تُباع بياناتك أبدًا."),
          ("في أي البلدان يتوفر؟", "في معظم البلدان التي يعمل فيها AppGallery. غير متوفر في الولايات المتحدة ولا في البر الرئيسي للصين.")],
    dl_h="حمّل SafePulse من AppGallery",
    dl_sub="ابحث عن SafePulse في AppGallery أو استخدم الزر أدناه. يظهر السعر بعملتك.",
    badge=["اكتشفه على", "AppGallery"],
    other='لا تملك هاتف هواوي؟ SafePulse متوفر أيضًا على <a href="{play}">Google Play</a> و<a href="{appstore}">App Store</a>.',
    disclaimer="<strong>يُرجى القراءة:</strong> SafePulse ليس خدمة طوارئ ولا يتصل بالشرطة أو الدفاع المدني أو الإسعاف. إنه ينبّه جهات الاتصال التي تختارها، ويعتمد على شبكة الهاتف والإنترنت لإيصال التنبيهات. وهو ليس بديلًا عن الاتصال برقم الطوارئ في بلدك.",
    foot=["الرئيسية", "سياسة الخصوصية (بالإنجليزية)", "الشروط (بالإنجليزية)"],
    lang_nav="اللغة",
)

LANGS["ja"] = dict(
    path="/ja/huawei", hreflang="ja", og_locale="ja_JP", label="日本語", dir="ltr",
    title="SafePulse for Huawei｜Googleなしで使える安否確認アプリ | Check In On Me",
    desc="Huawei AppGalleryのSafePulse：タイマーをセットし、時間内にチェックインしなければ、選んだ連絡先にあなたの位置情報がWhatsAppとメールで届きます。スマホの電源が切れていても通知されます。Googleサービス不要。",
    nav=["使い方", "できないこと", "よくある質問", "入手する"],
    h1="Huaweiで使える、Google不要の安否確認アプリ。",
    tagline="出かける前にタイマーをセット。終了までにチェックインしなければ、SafePulseがあなたの選んだ人に、最後に確認された位置情報を知らせます。スマホの電源が切れていても、バッテリーがなくても、圏外でも届きます。",
    cta=["AppGalleryで入手", "使い方"],
    intro_h="Google Playサービスのないスマホのために",
    intro=["新しいHuaweiスマホにはGoogle Playサービスが搭載されておらず、多くの安全アプリは位置情報をそれに頼っています。そうしたスマホでは通知は届いても、いちばん大切な「今どこにいるか」が抜け落ちてしまいます。",
           "SafePulseはGoogleがない場合、スマホ本体の位置情報機能を使うため、通知に含まれる地図リンクはHuaweiスマホでも機能します。Huawei版はAppGalleryの審査を通過し、公開されています。"],
    how_h="使い方", how_sub="手順は3つ。手間がかかるのは最初の1つだけです。",
    steps=[("タイマーをセット", "夜道の帰宅、初めて会う人との約束、長距離の運転、夜勤の前に、30分から48時間の範囲で時間を選びます。"),
           ("無事ならチェックイン", "ワンタップでタイマーが止まります。何も送信されず、誰にも連絡は行きません。"),
           ("チェックインがなければ通知", "時間切れになると、連絡先に最後に確認された位置情報を含むメッセージとメールが届きます。相手はアプリ不要です。")],
    feat_h="この設計にした理由",
    feats=[("Googleなしで位置情報", "通知には、スマホ本体のGPSとネットワークから取得した最終位置の地図リンクが含まれます。Googleアカウントやサービスは必要ありません。"),
           ("電源が切れていても作動", "カウントダウンは当社のサーバーにも保存されます。スマホの電源が切れても、壊れても、電池が切れても、奪われても、サーバーが通知を送ります。"),
           ("WhatsAppとメール", "北米以外では、通知はWhatsAppとメールで送られます。WhatsAppのメッセージは警告なしに届かないことがあるため、すべての連絡先にメールアドレスの登録が必須です。"),
           ("連絡先の同意が先", "追加した相手にはまずリクエストが届き、承認してはじめて通知を受け取れます。知らない人から突然緊急メッセージが届くことはありません。")],
    lim_h="できないこと", lim_sub="安全ツールは過大に宣伝されがちです。限界を正直にお伝えします。",
    lims=[("緊急通報サービスではありません。", "SafePulseは警察・救急などの緊急番号に通報せず、監視センターもありません。知らせるのはあなたが選んだ人だけです。危険が迫っていて電話ができるなら、お住まいの国の緊急番号に電話してください。"),
          ("防犯ブザーではありません。", "逆の仕組みです。あなたが操作できないときに作動します。"),
          ("位置追跡アプリではありません。", "タイマーが通常どおり動いている間、誰もあなたの居場所を見ることはできません。位置情報が共有されるのは、チェックインしなかった場合だけです。"),
          ("保証ではありません。", "連絡先に届くにはモバイル通信またはインターネットが必要です。異変に誰かが気づくまでの時間を短くするものであり、何かを防ぐものではありません。"),
          ("アプリの言語。", "アプリの画面は英語と簡体字中国語です。このページは翻訳されていますが、アプリはまだ日本語に対応していません。")],
    faq_h="よくある質問",
    faqs=[("Google Playサービスは必要ですか？", "いいえ。Huawei版はGoogleのないスマホでも動作し、新しいHuaweiモデルにも対応しています。位置情報はスマホ本体のGPSとネットワークから取得します。"),
          ("常に位置情報を追跡されますか？", "いいえ。位置情報はタイマーのために読み取られ、チェックインしなかった場合にのみ共有されます。何事もなければ、誰もあなたの居場所を調べることはできません。"),
          ("スマホの電源が切れたり、奪われたりしたら？", "それでも通知は送られます。カウントダウンはサーバーにも保存されているため、スマホからチェックインがなければ、サーバーが自動で通知を送ります。"),
          ("連絡先の人もアプリが必要ですか？", "いいえ。一度リクエストを承認すれば、通知はWhatsAppとメールで届きます（米国・カナダの番号にはSMSで届きます）。"),
          ("料金は？", "AppGalleryでの買い切り型で、価格は現地通貨で表示されます。サブスクリプションも広告もなく、データが販売されることもありません。"),
          ("どの国で利用できますか？", "AppGalleryが提供されている多くの国で利用できます。米国と中国本土では提供していません。")],
    dl_h="AppGalleryでSafePulseを入手",
    dl_sub="AppGalleryで「SafePulse」を検索するか、下のボタンをご利用ください。価格は現地通貨で表示されます。",
    badge=["入手はこちら", "AppGallery"],
    other='Huaweiスマホをお使いでない方は、<a href="{play}">Google Play</a>と<a href="{appstore}">App Store</a>でもSafePulseを入手できます。',
    disclaimer="<strong>ご注意：</strong>SafePulseは緊急通報サービスではなく、警察・消防・救急に連絡することはありません。あなたが選んだ連絡先に通知するもので、通知の配信にはモバイル通信とインターネットが必要です。お住まいの国の緊急番号への通報に代わるものではありません。",
    foot=["ホーム", "プライバシーポリシー（英語）", "利用規約（英語）"],
    lang_nav="言語",
)

LANGS["zh-hans"] = dict(
    path="/zh-hans/huawei", hreflang="zh-Hans", og_locale="zh_CN", label="简体中文", dir="ltr",
    title="SafePulse 华为版｜无需谷歌服务的安全签到应用 | Check In On Me",
    desc="华为 AppGallery 上的 SafePulse：设置签到计时器，如果你没有按时签到，你选择的联系人会通过 WhatsApp 和电子邮件收到你的位置，即使手机已关机。无需谷歌服务。",
    nav=["使用方法", "局限", "常见问题", "下载"],
    h1="一款能在华为手机上使用、无需谷歌的安全签到应用。",
    tagline="出门前设置一个计时器。如果计时结束时你还没有签到，SafePulse 会把你最后已知的位置发送给你选择的人。即使手机关机、没电或没有信号，也照样发出。",
    cta=["在 AppGallery 获取", "使用方法"],
    intro_h="专为没有 Google Play 服务的手机打造",
    intro=["较新的华为手机不预装 Google Play 服务，而许多安全应用都依赖它来获取位置。在这些手机上，警报虽然能发出，却缺少最关键的信息：你在哪里。",
           "在没有谷歌服务时，SafePulse 会改用手机自带的定位系统，因此警报中的地图链接在华为手机上同样有效。华为版已通过 AppGallery 审核并正式上架。"],
    how_h="使用方法", how_sub="只需三步，而且只有第一步需要你动手。",
    steps=[("设置计时器", "夜里走路回家、第一次约会、长途驾驶或上夜班之前，选择 30 分钟到 48 小时之间的时长。"),
           ("平安后签到", "轻点一下即可停止计时。不会发送任何信息，也不会打扰任何人。"),
           ("没有签到，就通知他们", "计时结束时，你的联系人会收到一条消息和一封邮件，其中包含你最后已知的位置。他们不需要安装应用。")],
    feat_h="为什么这样设计",
    feats=[("无需谷歌也能定位", "警报中附有地图链接，显示你最后已知的位置，数据来自手机自身的 GPS 和网络定位。不需要谷歌账号或谷歌服务。"),
           ("关机也能发出警报", "倒计时同时保存在我们的服务器上。如果手机关机、损坏、没电或被人拿走，服务器照样会发出警报。"),
           ("WhatsApp 和电子邮件", "在北美以外地区，警报通过 WhatsApp 和电子邮件发送。每位联系人都必须填写电子邮箱，因为 WhatsApp 消息可能在没有任何提示的情况下发送失败。"),
           ("联系人先同意", "你添加的每个人都会先收到一个请求，必须接受后才能收到警报。不会有人突然收到陌生人发来的紧急消息。")],
    lim_h="它不是什么", lim_sub="安全工具常被夸大宣传。以下如实说明它的局限。",
    lims=[("不是紧急救援服务。", "SafePulse 不会拨打报警或急救电话，也没有监控中心。它只通知你选择的人。如果你身处危险且能打电话，请拨打当地的紧急电话。"),
          ("不是紧急求救按钮。", "它的原理正好相反：在你无法操作时才会触发。"),
          ("不是位置追踪工具。", "计时器正常运行期间，没有人能看到你在哪里。只有在你没有按时签到时，你的位置才会被分享。"),
          ("不是万无一失的保证。", "警报需要移动网络或互联网才能送达联系人。它能缩短别人发现异常所需的时间，但不能阻止任何事情发生。"),
          ("应用语言。", "应用界面提供英文和简体中文。")],
    faq_h="常见问题",
    faqs=[("需要 Google Play 服务吗？", "不需要。华为版可在没有谷歌服务的手机上运行，包括较新的华为机型。位置来自手机自身的 GPS 和网络定位。"),
          ("它会一直追踪我的位置吗？", "不会。只在计时签到时读取位置，并且只有在你没有按时签到时才会分享。一切正常时，没有人能查到你在哪里。"),
          ("如果手机关机或被人拿走怎么办？", "警报照样会发出。倒计时同时保存在服务器上，如果你的手机始终没有签到，服务器会自行发送警报。"),
          ("我的联系人需要安装应用吗？", "不需要。他们只需接受一次请求，之后就会通过 WhatsApp 和电子邮件收到警报（美国和加拿大号码则通过短信）。"),
          ("价格是多少？", "SafePulse 在 AppGallery 上一次性购买，价格以你所在地的货币显示。没有订阅，没有广告，也绝不出售你的数据。"),
          ("哪些国家和地区可以下载？", "AppGallery 覆盖的大多数国家和地区均可下载。美国和中国大陆暂不提供。")],
    dl_h="在 AppGallery 下载 SafePulse",
    dl_sub="在 AppGallery 中搜索 SafePulse，或点击下方按钮。价格以你所在地的货币显示。",
    badge=["华为应用市场", "AppGallery"],
    other='不是华为手机？SafePulse 也可在 <a href="{play}">Google Play</a> 和 <a href="{appstore}">App Store</a> 下载。',
    disclaimer="<strong>请注意：</strong>SafePulse 不是紧急救援服务，不会联系警察、消防或急救部门。它只通知你选择的联系人，并依赖移动网络和互联网来发送警报。它不能替代拨打当地的紧急电话。",
    foot=["首页", "隐私政策（英文）", "服务条款（英文）"],
    lang_nav="语言",
)

LANGS["zh-hant"] = dict(
    path="/zh-hant/huawei", hreflang="zh-Hant", og_locale="zh_HK", label="繁體中文", dir="ltr",
    title="SafePulse 華為版｜無需 Google 服務的安全簽到應用程式 | Check In On Me",
    desc="華為 AppGallery 上的 SafePulse：設定簽到計時器，如果你沒有按時簽到，你選擇的聯絡人會透過 WhatsApp 及電子郵件收到你的位置，即使手機已關機。無需 Google 服務。",
    nav=["使用方式", "局限", "常見問題", "下載"],
    h1="一款能在華為手機上使用、無需 Google 的安全簽到應用程式。",
    tagline="出門前設定一個計時器。如果計時結束時你還沒有簽到，SafePulse 會把你最後已知的位置傳送給你選擇的人。即使手機關機、沒電或沒有訊號，也照樣發出。",
    cta=["在 AppGallery 下載", "使用方式"],
    intro_h="專為沒有 Google Play 服務的手機而設",
    intro=["較新的華為手機沒有 Google Play 服務，而許多安全應用程式都依賴它來取得位置。在這些手機上，警報雖然能發出，卻缺少最重要的資訊：你在哪裡。",
           "沒有 Google 服務時，SafePulse 會改用手機內建的定位系統，因此警報中的地圖連結在華為手機上同樣有效。華為版已通過 AppGallery 審核並正式上架。"],
    how_h="使用方式", how_sub="只需三步，而且只有第一步需要你動手。",
    steps=[("設定計時器", "夜晚步行回家、第一次約會、長途駕駛或上夜班之前，選擇 30 分鐘至 48 小時之間的時長。"),
           ("平安後簽到", "輕按一下即可停止計時。不會傳送任何訊息，也不會打擾任何人。"),
           ("沒有簽到，就通知他們", "計時結束時，你的聯絡人會收到一則訊息和一封電子郵件，內含你最後已知的位置。他們不需要安裝應用程式。")],
    feat_h="為什麼這樣設計",
    feats=[("無需 Google 也能定位", "警報附有地圖連結，顯示你最後已知的位置，資料來自手機本身的 GPS 和網絡定位。不需要 Google 帳戶或服務。"),
           ("關機也能發出警報", "倒數計時同時儲存在我們的伺服器上。如果手機關機、損壞、沒電或被人拿走，伺服器照樣會發出警報。"),
           ("WhatsApp 及電子郵件", "在北美以外地區，警報會透過 WhatsApp 及電子郵件傳送。每位聯絡人都必須填寫電子郵件地址，因為 WhatsApp 訊息可能在沒有任何提示的情況下傳送失敗。"),
           ("聯絡人先同意", "你加入的每個人都會先收到一個請求，必須接受後才能收到警報。不會有人突然收到陌生人傳來的緊急訊息。")],
    lim_h="它不能做什麼", lim_sub="安全工具常被誇大宣傳。以下如實說明它的局限。",
    lims=[("不是緊急求助服務。", "SafePulse 不會致電警方、救護車或任何緊急電話，也沒有監控中心。它只會通知你選擇的人。如果你身處危險而且能打電話，請撥打當地的緊急電話。"),
          ("不是求救按鈕。", "它的原理正好相反：在你無法操作時才會觸發。"),
          ("不是位置追蹤工具。", "計時器正常運作期間，沒有人能看到你在哪裡。只有在你沒有按時簽到時，你的位置才會被分享。"),
          ("不是萬無一失的保證。", "警報需要流動網絡或互聯網才能送達聯絡人。它能縮短別人察覺異常所需的時間，但不能阻止任何事情發生。"),
          ("應用程式語言。", "應用程式介面目前提供英文及簡體中文，尚未提供繁體中文。")],
    faq_h="常見問題",
    faqs=[("需要 Google Play 服務嗎？", "不需要。華為版可在沒有 Google 的手機上運作，包括較新的華為型號。位置來自手機本身的 GPS 和網絡定位。"),
          ("它會一直追蹤我的位置嗎？", "不會。只在計時簽到時讀取位置，而且只有在你沒有按時簽到時才會分享。一切正常時，沒有人能查到你在哪裡。"),
          ("如果手機關機或被人拿走怎麼辦？", "警報照樣會發出。倒數計時同時儲存在伺服器上，如果你的手機始終沒有簽到，伺服器會自行傳送警報。"),
          ("我的聯絡人需要安裝應用程式嗎？", "不需要。他們只需接受一次請求，之後就會透過 WhatsApp 及電子郵件收到警報（美國及加拿大號碼則以短訊傳送）。"),
          ("價錢是多少？", "SafePulse 在 AppGallery 上一次性購買，價格以你所在地的貨幣顯示。沒有訂閱，沒有廣告，也絕不出售你的資料。"),
          ("哪些國家和地區可以下載？", "AppGallery 覆蓋的大多數國家和地區均可下載。美國及中國內地暫不提供。")],
    dl_h="在 AppGallery 下載 SafePulse",
    dl_sub="在 AppGallery 搜尋 SafePulse，或按下方按鈕。價格以你所在地的貨幣顯示。",
    badge=["華為應用市場", "AppGallery"],
    other='不是華為手機？SafePulse 亦可在 <a href="{play}">Google Play</a> 及 <a href="{appstore}">App Store</a> 下載。',
    disclaimer="<strong>請注意：</strong>SafePulse 不是緊急求助服務，不會聯絡警方、消防或救護服務。它只會通知你選擇的聯絡人，並依賴流動網絡和互聯網傳送警報。它不能取代撥打當地的緊急電話。",
    foot=["首頁", "私隱政策（英文）", "服務條款（英文）"],
    lang_nav="語言",
)

ICONS = ["&#128752;", "&#128244;", "&#128172;", "&#9989;"]

CSS = """
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            color: #1a1a2e; line-height: 1.6; background-color: #ffffff;
            background-image:
                radial-gradient(1100px 480px at 50% -140px, rgba(76,175,80,0.12), transparent 68%),
                linear-gradient(180deg, #ffffff 0%, #f3f9f4 100%);
            background-attachment: fixed;
        }
        :lang(ja) body, body:lang(ja) { font-family: -apple-system, 'Hiragino Sans', 'Hiragino Kaku Gothic ProN', 'Yu Gothic', Meiryo, 'Noto Sans JP', sans-serif; line-height: 1.8; }
        body:lang(zh-Hans) { font-family: -apple-system, 'PingFang SC', 'Microsoft YaHei', 'Noto Sans SC', 'HarmonyOS Sans SC', sans-serif; line-height: 1.8; }
        body:lang(zh-Hant) { font-family: -apple-system, 'PingFang TC', 'PingFang HK', 'Microsoft JhengHei', 'Noto Sans TC', sans-serif; line-height: 1.8; }
        body:lang(ar) { font-family: 'Segoe UI', Tahoma, 'Geeza Pro', 'Noto Sans Arabic', 'Noto Naskh Arabic', sans-serif; line-height: 1.9; }
        nav {
            position: sticky; top: 0; background: rgba(255,255,255,0.97); backdrop-filter: blur(10px);
            padding: 1rem 2rem; display: flex; justify-content: space-between; align-items: center;
            box-shadow: 0 2px 12px rgba(0,0,0,0.06); z-index: 100;
        }
        .logo { font-size: 1.4rem; font-weight: 800; color: #2e7d32; text-decoration: none; letter-spacing: -0.5px; }
        nav .nav-links { display: flex; gap: 1.5rem; align-items: center; }
        nav .nav-links a { font-size: 0.95rem; color: #000; text-decoration: none; font-weight: 700; }
        nav .nav-links a:hover { color: #2e7d32; }

        .langs { background: #1b5e20; text-align: center; padding: 0.5rem 1rem; font-size: 0.9rem; }
        .langs a { color: #e8f5e9; text-decoration: none; margin: 0 0.55rem; white-space: nowrap; display: inline-block; }
        .langs a:hover { text-decoration: underline; }
        .langs a[aria-current] { color: #fff; font-weight: 700; text-decoration: underline; text-underline-offset: 4px; }

        .hero {
            position: relative; overflow: hidden; padding: 5rem 2rem 5.5rem;
            background: linear-gradient(135deg, #1b5e20 0%, #2e7d32 45%, #4caf50 100%);
            color: #fff; text-align: center;
            clip-path: polygon(0 0, 100% 0, 100% calc(100% - 34px), 0 100%);
        }
        .hero::before, .hero::after { content: ""; position: absolute; border-radius: 50%; pointer-events: none; z-index: 0; }
        .hero::before { width: 460px; height: 460px; top: -160px; left: -120px; background: radial-gradient(circle, rgba(255,255,255,0.22), transparent 62%); }
        .hero::after { width: 520px; height: 520px; bottom: -220px; right: -140px; background: radial-gradient(circle, rgba(129,199,132,0.35), transparent 60%); }
        .hero > * { position: relative; z-index: 1; }
        .hero h1 { font-size: 2.7rem; margin-bottom: 1rem; font-weight: 800; line-height: 1.2; max-width: 800px; margin-left: auto; margin-right: auto; }
        .hero .tagline { font-size: 1.2rem; opacity: 0.95; max-width: 680px; margin: 0 auto 2.25rem; }
        .hero .cta { display: inline-flex; gap: 1rem; flex-wrap: wrap; justify-content: center; }
        .btn {
            display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.9rem 1.75rem; border-radius: 50px;
            text-decoration: none; font-weight: 600; font-size: 1.05rem; transition: transform 0.2s, box-shadow 0.2s;
        }
        .btn:hover { transform: translateY(-2px); box-shadow: 0 8px 22px rgba(0,0,0,0.25); }
        .btn-primary { background: #fff; color: #1b5e20; }
        .btn-ghost { background: rgba(255,255,255,0.15); color: #fff; border: 2px solid rgba(255,255,255,0.4); }

        section { max-width: 960px; margin: 0 auto; padding: 4rem 2rem; }
        h2 { font-size: 2rem; margin-bottom: 1.25rem; color: #1a1a2e; text-align: center; }
        .section-sub { text-align: center; color: #666; max-width: 660px; margin: 0 auto 2.5rem; }
        h3 { font-size: 1.15rem; margin-bottom: 0.5rem; color: #2e7d32; }
        p { margin-bottom: 1rem; color: #444; }
        .prose { max-width: 700px; margin: 0 auto; }
        .prose p:last-child { margin-bottom: 0; }

        .features { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1.5rem; }
        .feature {
            position: relative; overflow: hidden; padding: 1.75rem 1.6rem; background: #fff; border-radius: 16px;
            border: 1px solid rgba(46,125,50,0.10); box-shadow: 0 6px 20px rgba(27,94,32,0.06);
        }
        .feature::before { content: ""; position: absolute; top: 0; left: 0; right: 0; height: 4px; background: linear-gradient(90deg, #2e7d32, #66bb6a); }
        .feature .ico {
            display: inline-flex; align-items: center; justify-content: center; width: 50px; height: 50px; border-radius: 14px;
            background: linear-gradient(135deg, #e8f5e9, #c8e6c9); font-size: 1.55rem; margin-bottom: 0.9rem;
        }
        .feature p:last-child { margin-bottom: 0; }

        .steps { display: flex; justify-content: center; gap: 2.5rem; flex-wrap: wrap; }
        .step { flex: 1; min-width: 220px; max-width: 280px; text-align: center; }
        .step p:last-child { margin-bottom: 0; }
        .step-num {
            width: 58px; height: 58px; border-radius: 50%; background: linear-gradient(135deg, #2e7d32, #66bb6a); color: #fff;
            display: flex; align-items: center; justify-content: center; font-size: 1.45rem; font-weight: 800;
            margin: 0 auto 1rem; box-shadow: 0 10px 22px rgba(46,125,50,0.32);
        }

        .limits { background: #fff; border-radius: 16px; border: 1px solid rgba(46,125,50,0.10); box-shadow: 0 6px 20px rgba(27,94,32,0.06); padding: 2rem 2rem 1.5rem; max-width: 720px; margin: 0 auto; }
        .limits ul { list-style: none; }
        .limits li { position: relative; padding-inline-start: 1.9rem; margin-bottom: 0.9rem; color: #444; }
        .limits li:last-child { margin-bottom: 0; }
        .limits li::before { content: "\\2716"; position: absolute; inset-inline-start: 0; top: 0; color: #c62828; font-weight: 700; }
        .limits li.info::before { content: "\\2139"; color: #2e7d32; }
        .limits strong { color: #1a1a2e; }

        .faq { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.25rem; }
        .faq-item { padding: 1.6rem 1.5rem; background: #fff; border-radius: 16px; border: 1px solid rgba(46,125,50,0.10); box-shadow: 0 6px 20px rgba(27,94,32,0.06); }
        .faq-item h3 { font-size: 1.05rem; color: #1a1a2e; margin-bottom: 0.55rem; line-height: 1.4; }
        .faq-item p { font-size: 0.97rem; margin-bottom: 0; }

        .download { background: linear-gradient(180deg, #f1f8f2, #e8f3ea); text-align: center; border-top: 1px solid rgba(46,125,50,0.08); max-width: none; }
        .download > * { max-width: 960px; margin-left: auto; margin-right: auto; }
        .stores { display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap; margin-top: 1.5rem; }
        .store-badge {
            display: inline-flex; align-items: center; gap: 0.7rem; padding: 0.85rem 1.5rem; background: #1a1a2e; color: #fff;
            text-decoration: none; border-radius: 12px; font-weight: 700; font-size: 1.15rem; text-align: start;
            box-shadow: 0 6px 18px rgba(26,26,46,0.18); transition: transform 0.2s, box-shadow 0.2s;
        }
        .store-badge:hover { transform: translateY(-3px); box-shadow: 0 12px 26px rgba(26,26,46,0.28); }
        .store-badge small { display: block; font-size: 0.7rem; opacity: 0.8; font-weight: 500; }
        .store-badge svg { flex-shrink: 0; }
        .price-note { margin-top: 1.25rem; font-size: 0.95rem; color: #555; }
        .price-note a { color: #2e7d32; font-weight: 600; }

        .disclaimer {
            background: #fff8e1; border-inline-start: 4px solid #f9a825; padding: 1rem 1.25rem; margin: 2rem auto 0;
            max-width: 700px; font-size: 0.95rem; color: #555; border-radius: 8px; text-align: start;
        }
        .disclaimer p { margin-bottom: 0; }

        footer { background: #1a1a2e; color: #aaa; padding: 2rem; text-align: center; font-size: 0.9rem; }
        footer a { color: #81c784; text-decoration: none; }
        footer a:hover { text-decoration: underline; }

        @media (max-width: 600px) {
            .hero { padding: 3.5rem 1.25rem; }
            .hero h1 { font-size: 1.95rem; }
            .hero .tagline { font-size: 1.02rem; }
            section { padding: 3rem 1.25rem; }
            nav { flex-direction: column; gap: 0.5rem; padding: 0.6rem 1rem; }
            nav .logo { font-size: 1.25rem; }
            nav .nav-links { gap: 1.1rem; font-size: 0.9rem; flex-wrap: wrap; justify-content: center; }
            .limits { padding: 1.5rem 1.25rem; }
            .faq { grid-template-columns: 1fr; }
        }
"""

# Generic shopping-bag glyph, not Huawei's trademarked logo.
BAG_SVG = ('<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
           'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 8h14l-1 12H6L5 8z"/>'
           '<path d="M9 8V6a3 3 0 0 1 6 0v2"/></svg>')

e = html.escape


def render(code, L):
    url = BASE + L["path"]
    alternates = "\n".join(
        f'    <link rel="alternate" hreflang="{o["hreflang"]}" href="{BASE}{o["path"]}">' for o in LANGS.values()
    ) + f'\n    <link rel="alternate" hreflang="x-default" href="{BASE}/huawei">'

    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "SoftwareApplication",
                "name": "SafePulse",
                "applicationCategory": "LifestyleApplication",
                "applicationSubCategory": "Personal Safety",
                "operatingSystem": "Android (Huawei EMUI / AppGallery)",
                "inLanguage": L["hreflang"],
                "description": L["desc"],
                "url": url,
                "downloadUrl": APPGALLERY,
                "author": {"@type": "Person", "name": "Frank Nowicki"},
            },
            {
                "@type": "FAQPage",
                "url": url + "#faq",
                "inLanguage": L["hreflang"],
                "mainEntity": [
                    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                    for q, a in L["faqs"]
                ],
            },
        ],
    }

    lang_links = " ".join(
        f'<a href="{o["path"]}" hreflang="{o["hreflang"]}" lang="{o["hreflang"]}"'
        + (' aria-current="page"' if c == code else "")
        + f'>{o["label"]}</a>'
        for c, o in LANGS.items()
    )

    steps = "\n".join(
        f'''        <div class="step">
            <div class="step-num">{i}</div>
            <h3>{e(h)}</h3>
            <p>{e(p)}</p>
        </div>''' for i, (h, p) in enumerate(L["steps"], 1)
    )
    feats = "\n".join(
        f'''        <div class="feature">
            <div class="ico">{ICONS[i]}</div>
            <h3>{e(h)}</h3>
            <p>{e(p)}</p>
        </div>''' for i, (h, p) in enumerate(L["feats"])
    )
    # The last item (app language) is information, not a limit: ℹ instead of ✖.
    info = ' class="info"'
    lims = "\n".join(
        f'            <li{info if i == len(L["lims"]) - 1 else ""}><strong>{e(s)}</strong> {e(t)}</li>'
        for i, (s, t) in enumerate(L["lims"])
    )
    faqs = "\n".join(
        f'''        <div class="faq-item">
            <h3>{e(q)}</h3>
            <p>{e(a)}</p>
        </div>''' for q, a in L["faqs"]
    )
    intro = "\n".join(f"        <p>{e(p)}</p>" for p in L["intro"])
    other = L["other"].format(play=PLAY, appstore=APPSTORE)
    nav = L["nav"]

    return f'''<!DOCTYPE html>
<!-- GENERATED by tools/build_huawei_pages.py - edit the copy there, not here. -->
<html lang="{L["hreflang"]}" dir="{L["dir"]}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="robots" content="index, follow">
    <title>{e(L["title"])}</title>
    <meta name="description" content="{e(L["desc"])}">
    <link rel="canonical" href="{url}">
{alternates}
    <meta property="og:title" content="{e(L["title"])}">
    <meta property="og:description" content="{e(L["desc"])}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="{url}">
    <meta property="og:site_name" content="Check In On Me">
    <meta property="og:locale" content="{L["og_locale"]}">
    <meta property="og:image" content="{BASE}/img/og-image.png">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{e(L["title"])}">
    <meta name="twitter:description" content="{e(L["desc"])}">
    <meta name="twitter:image" content="{BASE}/img/og-image.png">
    <script type="application/ld+json">
{json.dumps(schema, ensure_ascii=False, indent=2)}
    </script>
    <style>{CSS}    </style>
</head>
<body>

<nav>
    <a href="/" class="logo" dir="ltr">Check In On Me</a>
    <div class="nav-links">
        <a href="#how">{e(nav[0])}</a>
        <a href="#limits">{e(nav[1])}</a>
        <a href="#faq">{e(nav[2])}</a>
        <a href="#download">{e(nav[3])}</a>
    </div>
</nav>
<div class="langs" role="navigation" aria-label="{e(L["lang_nav"])}">{lang_links}</div>

<section class="hero">
    <h1>{e(L["h1"])}</h1>
    <p class="tagline">{e(L["tagline"])}</p>
    <div class="cta">
        <a href="{APPGALLERY}" class="btn btn-primary" target="_blank" rel="noopener">{e(L["cta"][0])}</a>
        <a href="#how" class="btn btn-ghost">{e(L["cta"][1])}</a>
    </div>
</section>

<section>
    <h2>{e(L["intro_h"])}</h2>
    <div class="prose">
{intro}
    </div>
</section>

<section id="how" style="padding-top:0;">
    <h2>{e(L["how_h"])}</h2>
    <p class="section-sub">{e(L["how_sub"])}</p>
    <div class="steps">
{steps}
    </div>
</section>

<section>
    <h2>{e(L["feat_h"])}</h2>
    <div class="features">
{feats}
    </div>
</section>

<section id="limits">
    <h2>{e(L["lim_h"])}</h2>
    <p class="section-sub">{e(L["lim_sub"])}</p>
    <div class="limits">
        <ul>
{lims}
        </ul>
    </div>
</section>

<section id="faq">
    <h2>{e(L["faq_h"])}</h2>
    <div class="faq">
{faqs}
    </div>
</section>

<section class="download" id="download">
    <h2>{e(L["dl_h"])}</h2>
    <p class="section-sub">{e(L["dl_sub"])}</p>
    <div class="stores">
        <a class="store-badge" href="{APPGALLERY}" target="_blank" rel="noopener">
            {BAG_SVG}
            <span><small>{e(L["badge"][0])}</small>{e(L["badge"][1])}</span>
        </a>
    </div>
    <p class="price-note">{other}</p>
    <div class="disclaimer"><p>{L["disclaimer"]}</p></div>
</section>

<footer>
    <p>&copy; 2026 Frank Nowicki. All rights reserved.</p>
    <p style="margin-top: 0.5rem;" dir="ltr">Frank Paul Nowicki, Sole Proprietor &middot; Roseville, MI 48066, USA &middot; <a href="mailto:checkinonme@checkinonme.app">checkinonme@checkinonme.app</a></p>
    <p style="margin-top: 0.5rem;">SafePulse&trade; &middot; <a href="/">{e(L["foot"][0])}</a> &middot; <a href="/privacy">{e(L["foot"][1])}</a> &middot; <a href="/terms">{e(L["foot"][2])}</a></p>
    <p style="margin-top: 0.75rem; font-size: 0.8rem; color: #888;">HUAWEI and AppGallery are trademarks of Huawei Technologies Co., Ltd. SafePulse is not affiliated with or endorsed by Huawei.</p>
</footer>

</body>
</html>
'''


def main():
    for code, L in LANGS.items():
        rel = L["path"].lstrip("/") + ".html"
        out = os.path.join(ROOT, rel)
        os.makedirs(os.path.dirname(out) or ROOT, exist_ok=True)
        with open(out, "w", encoding="utf-8", newline="\n") as f:
            f.write(render(code, L))
        print("wrote", rel)


if __name__ == "__main__":
    main()
