import base64, html, pathlib, re, urllib.parse
import program as P
from build_tracker import font_css  # noqa

root = pathlib.Path(__file__).resolve().parent.parent
esc = html.escape


def en(s):
    return f'<bdi class="en" dir="ltr">{esc(s)}</bdi>'


def T(head, rows, cls="", first_en=False):
    h = "<div class='tw'><table class='%s'><thead><tr>%s</tr></thead><tbody>" % (cls, "".join(f"<th>{c}</th>" for c in head))
    for r in rows:
        h += "<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>"
    return h + "</tbody></table></div>"


def ul(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def sec(id, title, body, n=None):
    title = re.sub(r"^(\d+)\.", lambda m: m.group(1).translate(str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")) + ".", title)
    return f'<section id="{id}"><h2>{title}</h2>{body}</section>'


def yt(q):
    return "https://www.youtube.com/results?search_query=" + urllib.parse.quote_plus(q)


NUT = P.NUTRITION
chk = lambda n: n["p"] * 4 + n["c"] * 4 + n["f"] * 9

# ---------------------------------------------------------------- sections
S = []

# 1 profile
S.append(sec("profile", "1. پروفایل و هدف‌ها", T(
    ["مورد", "مقدار"],
    [["نام", "امیر، مرد، متولد ۲۱ ژانویه ۲۰۰۵ (۲۱ سال)"],
     ["قد / وزن", "183 cm / 89 kg (عکس‌های اخیر در 89 kg)"],
     ["چربی بدن", "حدود 18-20٪ (تخمین بصری). کالیپر قبلی: حدود 16.9٪ در 90 kg، June 2026"],
     ["توده بدون چربی (FFM)", "حدود 72 kg (73 kg اگر دقیقاً 18٪ چربی باشد)"],
     ["زمینه", "دانشجوی پزشکی (MBBS، Zhejiang University)، ساکن Yiwu. تمرین در خانه و گاهی باشگاه. ددلیفت قبلی 160 kg"],
     ["برنامه قبلی (جایگزین می‌شود)", "Lyfta شش‌روزه هایپرتروفی (Push / Pull / Arms / Legs / Core / Cardio)، ست‌های 4×8 تا 4×20"],
     ["پنجره غذا", "16/8، ساعت 12:00 تا 20:00"],
     ["غذاها", "سینه مرغ، تن، سالمون، استیک گوساله، تخم‌مرغ، ماست یونانی 0٪، شیک آماده (325 ml، 30 g پروتئین)، ON Gold Standard Whey/Isolate، برنج، پاستا، سیب‌زمینی ایرفرایر، قارچ، سویای سبز (Edamame)، گوشت سویا، گوشت چرخ‌کرده بره، آووکادو، بادام، روغن زیتون بکر، اسپری روغن آووکادو"]]) +
    "<h3>هدف‌ها به ترتیب اولویت</h3>" + ul([
        "<b>حفظ کل عضله و افزایش قدرت همه گروه‌های عضلانی</b> (کل بدن، نه فقط کشیدن).",
        "<b>چربی‌سوزی و خشکی</b> (رگ و تعریف) با حفظ فرم مدل: شانه پهن، سینه بالا، پشت عریض، بازو، کمر باریک.",
        f"<b>اولین {en('Muscle-Up')} سخت‌گیرانه روی میله.</b> این هدف یکی از اجزای برنامه است، نه کل برنامه.",
        "کسری کالری سنگین و 1.5 تا 2 ساعت پیاده‌روی در روز. هدف وزن: حدود 83 kg در 56 روز (برآورد، نه تضمین)."]), "profile"))

# 2 energy
S.append(sec("energy", "2. محاسبه مصرف انرژی", """
<p>BMR با دو فرمول:</p>""" + ul([
    f"{en('Mifflin-St Jeor')}: 10×89 + 6.25×183 - 5×21 + 5 = 890 + 1143.75 - 105 + 5 = <b>1934 kcal</b>",
    f"{en('Katch-McArdle')} با 18٪ چربی: FFM = 89×0.82 = 73 kg، سپس 370 + 21.6×73 = <b>1946 kcal</b>",
    "میانگین: <b>BMR ≈ 1940 kcal</b>"]) + T(
    ["نوع روز", "مصرف کل (TDEE)", "توضیح"],
    [["کم‌تحرک (حدود 2000 قدم + کارهای خانه، ×1.2)", "≈ 2300 kcal", "BMR × 1.2"],
     ["فقط پیاده‌روی (90 دقیقه، 5-6 km/h)", "≈ 2700 kcal", "خالص پیاده‌روی ≈ 350-450 kcal"],
     ["قدرتی (60 دقیقه) + پیاده‌روی 90 دقیقه", "≈ 3000-3100 kcal", "خالص قدرتی ≈ 300-350 kcal"],
     ["قدرتی + پیاده‌روی 120 دقیقه", "≈ 3150-3250 kcal", "خالص پیاده‌روی ≈ 450-600 kcal"]]) + """
<div class="note"><b>نکته‌ها.</b> اعداد پیاده‌روی برای زمین صاف‌اند؛ شیب یا سرعت بیشتر 15-25٪ اضافه می‌کند. اعداد <b>خالص</b> هستند (BMR همان ساعت کم شده). ساعت هوشمند معمولاً مقدار <b>ناخالص</b> نشان می‌دهد و 20-30٪ بیشتر برآورد می‌کند. هر 3-4 kg کاهش وزن دوباره محاسبه کن.</div>
<h3>کسری هفتگی</h3>""" + T(
    ["هفته‌های", "میانگین مصرف", "میانگین TDEE (تخمین)", "کسری", "کاهش وزن"],
    [["1-2 (شنبه 1900)", f"{(4*2100+3*1900)/7:.0f} kcal", "≈ 2950", "≈ 940", "≈ 0.85 kg/هفته"],
     ["3-8 (شنبه ریفید 2500)", f"{(4*2100+2*1900+2500)/7:.0f} kcal", "≈ 2950", "≈ 850", "≈ 0.75 kg/هفته"]]) +
    "<p>میانگین کسری 800-900 kcal/روز، یعنی حدود 0.7-0.9 kg در هفته و حدود 6-6.5 kg در 8 هفته: 89 → <b>حدود 83 kg</b>. (قاعده تقریبی 7700 kcal برای هر kg؛ در عمل بدن تطبیق می‌دهد، پس با قانون تعدیل (بخش 3) کنترل کن.)</p>", "energy"))

# 3 nutrition
rows = []
names = {"train": ("روزهای تمرین (دوشنبه، سه‌شنبه، پنجشنبه، جمعه)", "train"),
         "walk": ("روزهای پیاده‌روی (چهارشنبه، یکشنبه؛ و شنبه در هفته‌های 1-2)", "walk"),
         "refeed": ("ریفید (هر شنبه از هفته 3)", "refeed")}
for k in ("train", "walk", "refeed"):
    n = NUT[k]
    rows.append([names[k][0], f"<b>{n['kcal']}</b>", f"{n['p']} g", f"{n['f']} g", f"{n['c']} g", f"{chk(n)} kcal"])
S.append(sec("nutrition", "3. تغذیه", T(["نوع روز", "kcal", "پروتئین", "چربی", "کربوهیدرات", "بررسی (4P+4C+9F)"], rows) +
    "<p class='small'>همه ماکروها با کالری هدف در ±20 kcal می‌خوانند (2100 = 2100، 1900 = 1900، 2495 ≈ 2500).</p>" +
    "<h3>نمونه روز تمرین (پنجره 12:00 تا 20:00)</h3>" + T(
    ["ساعت", "وعده", "تقریب"],
    [["12:00", "5 سفیده + 3 زرده، 200 g ماست یونانی 0٪، 325 ml شیک پروتئین، 1 میوه", "~75 g P، ~600 kcal"],
     ["15:00 (پیش از تمرین)", "200 g سینه مرغ پخته، 200-250 g برنج پخته، سبزی، نمک", "~65 g P، ~650 kcal"],
     ["17:30 (بعد از تمرین)", "1 اسکوپ whey + 1 موز", "~25 g P، ~230 kcal"],
     ["19:30", "150-200 g سالمون/استیک/تن + 300 g سیب‌زمینی ایرفرایر یا سویای سبز (Edamame) + سالاد با 1 قاشق غذاخوری روغن زیتون", "~45 g P، ~650 kcal"]]) +
    "<p>جمع نمونه: حدود 210 g پروتئین و 2130 kcal (در محدوده هدف 2100).</p>" + ul([
        "روزهای فقط پیاده‌روی: همین الگو، کربوهیدرات حدود 50 g کمتر (برنج/سیب‌زمینی کمتر).",
        "ریفید: کربوهیدرات اضافه از برنج، پاستا، سیب‌زمینی و میوه، <b>نه چربی</b>.",
        "پروتئین در 4 وعده، هر وعده حداقل 35-40 g. فیبر حداقل 30 g در روز.",
        "صفر کالری مایع (قهوه سیاه و نوشیدنی بدون قند آزاد است). روغن را با قاشق اندازه بگیر. همه چیز را وزن کن و بلافاصله ثبت کن.",
        "تمرین قدرتی <b>داخل</b> پنجره غذا و 1.5-2 ساعت بعد از یک وعده. هرگز تمرین سنگین ناشتا."]) +
    "<h3>قانون تعدیل</h3>" + T(
    ["شرط", "اقدام"],
    [["میانگین 7 روزه وزن در 2 هفته پیاپی کمتر از 0.4 kg/هفته کاهش یابد", "150 kcal کربوهیدرات از روزهای استراحت (پیاده‌روی) کم کن"],
     ["کاهش بیشتر از 1.2 kg/هفته", "150 kcal اضافه کن"],
     ["افت قدرت در 2 جلسه پیاپی", "150 kcal اضافه کن"]]), "nutrition"))

# 4 water etc
S.append(sec("hydration", "4. آب، الکترولیت، مکمل و خواب", T(
    ["شرایط", "حداقل آب"],
    [["کم‌تحرک", "3.0-3.5 L"], ["روز پیاده‌روی", "3.5-4.0 L"], ["تمرین + پیاده‌روی یا هوای گرم", "4.0-4.5 L"]]) +
    "<p>مبنا: حدود 35 ml/kg (89 kg ≈ 3.1 L) + 500-750 ml برای هر ساعت فعالیت. هدف: ادرار رنگ کاه روشن. بعد از بیدار شدن 500 ml بنوش.</p>" + ul([
        "<b>سدیم:</b> به غذا نمک بزن. در روز تمرین قبل از تمرین یک لیوان آب با حدود ¼ قاشق چایخوری نمک یا یک ساشه الکترولیت. در کسری کالری و با تعریق زیاد، به سدیم بیشتری نیاز داری.",
        "<b>پتاسیم:</b> سیب‌زمینی، موز، ماست، سویای سبز (Edamame)، سبزی برگ‌دار.",
        f"<b>منیزیم:</b> {en('Magnesium glycinate')} 200-400 mg شب (اختیاری)."]) +
    "<h3>مکمل‌ها</h3>" + T(
    ["مکمل", "دوز", "زمان", "چرا"],
    [[en("Creatine Monohydrate"), "5 g روزانه", "هر زمان از روز (ثابت و روزانه)", "قدرت؛ 1-2 kg آب داخل عضله (نه چربی)"],
     [en("Whey Protein"), "1-2 اسکوپ در صورت نیاز", "هر وقت برای رسیدن به پروتئین لازم است", "رسیدن به هدف پروتئین"],
     [en("Caffeine"), "200-270 mg (~3 mg/kg)", "45 دقیقه قبل تمرین؛ آخرین دوز تا 16:00 (اگر تمرین بعد از 16:45 شروع می‌شود، کافئین را حذف کن یا نصف کن)", "عملکرد (و خواب بهتر با قطع زودتر)"],
     [en("Vitamin D3"), "1000-2000 IU", "با وعده چرب", "اگر آفتاب کم است یا سطح پایین است"],
     [en("Omega-3 (EPA/DHA)"), "1-2 g", "روزهای بدون ماهی", "اختیاری"]]) +
    "<p><b>خواب:</b> 7.5-9 ساعت با ساعت بیدار شدن ثابت.</p>", "hydration"))

# 5 program
prog = []
prog.append("<h3>منطق برنامه</h3>" + ul([
    "در کسری کالری، <b>بار سنگین</b> مهم‌ترین سیگنال حفظ عضله است. اگر شدت بالا بماند، حجم کمتر هم عضله را حفظ می‌کند (Bickel 2011: یک‌سوم حجم قبلی اندازه فیبر عضله را در جوانان حفظ کرد).",
    "هدف: حدود 6-10 ست سخت در هفته برای هر عضله، با خستگی کمتر از شش‌روزه قبلی. جدول واقعی حجم در پایین است: پشت و شانه بالاتر، ساق پایین‌تر است.",
    "هر جلسه با کار سنگین قدرتی (2-6 تکرار، RPE 7-9، استراحت 2-3 دقیقه) شروع و با کار «شکل» (8-15 تکرار، 1-2 تکرار ذخیره، استراحت 60-90 ثانیه) برای شانه جانبی، سینه بالا، پشت، بازو و ساق تمام می‌شود.",
    f"کار {en('Muscle-Up')} حدود یک‌سوم حجم کشیدن است.",
    f"هر حرکت نسخه {en('Gym')} و {en('Home')} دارد. جلسه‌ها 60-75 دقیقه."]))
prog.append("<h3>چیدمان هفته (شروع از دوشنبه)</h3>" + T(
    ["روز", "برنامه"],
    [["دوشنبه", f"{en('Workout A')}: قدرت بالاتنه"], ["سه‌شنبه", f"{en('Workout B')}: قدرت پایین‌تنه"],
     ["چهارشنبه", f"پیاده‌روی + {en('GTG')}"], ["پنجشنبه", f"{en('Workout C')}: شکل بالاتنه + مهارت Muscle-Up"],
     ["جمعه", f"{en('Workout D')}: قدرت کل بدن"], ["شنبه", f"پیاده‌روی طولانی (+ ریفید از هفته 3) + {en('GTG')}"],
     ["یکشنبه", f"پیاده‌روی + چک‌این هفتگی + {en('GTG')}"]]))
prog.append("<h3>قوانین کلی</h3>" + ul([
    "ست اصلی: استراحت 2-3 دقیقه. ست فرعی: 60-90 ثانیه.",
    "<b>هرگز تا ناتوانی کامل نرو</b>؛ 1-2 تکرار ذخیره (RPE 7-9). خراب شدن فرم یعنی پایان ست.",
    "تجهیزات خانه: میله بارفیکس، میله دیپ یا دو صندلی محکم، کش مقاومتی، کوله‌پشتی وزنه‌دار (دمبل اختیاری).",
    "پیشرفت: وقتی همه ست‌ها با RPE هدف انجام شد، دفعه بعد وزنه را کمی بالا ببر."]))
prog.append("<h3>گرم کردن (8-10 دقیقه، هر جلسه)</h3>" + T(
    ["حرکت", "دوز"], [[en(a), b or "-"] for a, b in P.WARMUP]))
prog.append("<h3>دوره‌بندی</h3>" + T(
    ["هفته", "فاز", "ویژگی"],
    [["1-3", "انباشت (Accumulation)", "حجم کامل، RPE 7-8"],
     ["4", "دیلود (Deload)", "نصف ست‌ها، سبک‌تر؛ جمعه تست میانی"],
     ["5-7", "تشدید (Intensification)", "تکرار کمتر، سنگین‌تر، کار Transition بیشتر"],
     ["8", "اوج و تست (Peak & Test)", f"حجم کم؛ جمعه = {en('Muscle-Up Day')}"]]))
prog.append("<h3>جدول دوز هفتگی (طرح‌ها)</h3>" + T(
    ["طرح"] + [f"W{i}" for i in range(1, 9)],
    [[en(k)] + [en(v) for v in vals] for k, vals in P.SCHEMES.items()]) +
    "<p class='small'>«ثابت X / دیلود Y» یعنی X در هفته‌های 1-3 و 5-7، و Y در هفته‌های 4 و 8.</p>")
for L in "ABCD":
    W = P.WORKOUTS[L]
    rows = []
    for k, ex in enumerate(W["ex"], 1):
        g, h = P.LIBD[ex["gym"]]["en"], P.LIBD[ex["home"]]["en"]
        name = f"<a href='#ex-{ex['gym']}'>{en(g)}</a>" + ("" if g == h else f"<br><span class='muted small'>خانه: <a href='#ex-{ex['home']}'>{en(h)}</a></span>")
        cells = []
        for w in range(1, 9):
            d = P.dose_for(ex, w)
            dh = P.dose_for(ex, w, True)
            cells.append(en(d if d != "test" else "test") + ("" if dh == d else f"<br><span class='small muted'>{en(dh)}</span>"))
        rows.append([str(k), name, en(ex["rest"])] + cells)
    prog.append(f"<h3 id='w{L}'>{esc(W['fa'])}</h3>" + T(["#", "حرکت (Gym | Home)", "استراحت"] + [f"W{i}" for i in range(1, 9)], rows, "wk") +
                ul([f"<b>{en(P.LIBD[ex['gym']]['en'])}:</b> {esc(ex['fa'])}" for ex in W["ex"] if ex["fa"]]))
vt = P.volume_table()
prog.append("<h3>ست‌های سخت هفتگی برای هر عضله</h3><p>شمارش: ست‌های سخت (بدون ست‌های مهارتی/انفجاری سبک: Explosive Chest-to-Bar، High Pull-up، Negative، False Grip، Hollow، Farmer's Carry). عضله اصلی هر ست = 1 ست، عضله فرعی = 0.5 ست. نسخه Gym.</p>" + T(
    ["عضله"] + [f"W{i}" for i in range(1, 9)],
    [[P.MUSCLE_FA[k]] + [f"{x:g}" for x in vt[k]] for k in P.MUSCLE_FA if k != "grip"]) +
    f"<div class='note'><b>صادقانه:</b> پشت/لت با 18-20 ست و شانه با 14-15 ست بالاتر از محدوده 6-10 هستند؛ سینه و جلو بازو (10-12) در لبه بالای محدوده‌اند. دلیل: کشیدن اولویت اول برنامه است و ست‌های 3-5 تکراری سنگین خستگی موضعی کمی دارند (شمارش شامل سهم عضله فرعی است). ساق با 3 ست پایین‌تر از 6 است (فقط یک حرکت در برنامه). اگر ریکاوری پشت افت کرد، اول {en('Weighted Chin-up')} را به 2 ست کاهش بده؛ اگر ساق عقب ماند، یک ست ساق اضافه در چهارشنبه اختیاری است.</div>")
S.append(sec("program", "5. برنامه تمرین", "".join(prog), "program"))

# 6 walking
S.append(sec("walking", "6. پیاده‌روی", ul([
    "روزهای هفته 60-90 دقیقه، آخر هفته 90-120 دقیقه، سرعت مکالمه (Zone 2 / LISS). مجموع 12-15 هزار قدم در روز.",
    "تا جای ممکن از Incline Walking استفاده کن (کسری بیشتر بدون خستگی زیاد).",
    "پیاده‌روی ناشتای صبح (سبک تا متوسط، Zone 2) اشکال ندارد، <b>به شرط</b> آب + نمک/الکترولیت. Incline شدید و کار پرشدت ناشتا نه.",
    "روز تمرین، پیاده‌روی را صبح انجام بده تا پاها برای تمرین عصر تازه باشند."])))

# 7 library
cards = ""
for e in P.LIB:
    cards += f"""<article class="ex" id="ex-{e['id']}"><h3>{en(e['en'])}</h3><p>{esc(e['fa'])}</p>
<div class="g2"><div><b>نکات فرم</b>{ul([esc(x) for x in e['cues']])}</div><div><b>اشتباه‌های رایج</b>{ul([esc(x) for x in e['mistakes']])}</div></div>
<p><b>ساده‌تر:</b> {esc(e['reg'])}<br><b>سخت‌تر:</b> {esc(e['prog'])}</p>
<p class="small"><a href="{yt(e['yt'])}" target="_blank" rel="noopener">جستجوی YouTube: <bdi class="en" dir="ltr">{esc(e['yt'])}</bdi></a></p></article>"""
S.append(sec("library", "7. کتابخانه حرکت‌ها", "<p>همه نام‌ها انگلیسی‌اند تا بتوانی جستجو کنی. هر حرکت لینک جستجوی YouTube دارد.</p>" + cards))

# 8 challenges
S.append(sec("challenges", "8. چالش‌ها", T(
    ["چالش", "قانون"],
    [[en("Grease the Groove (GTG)"), "روزهای بدون وزنه (چهارشنبه، شنبه، یکشنبه): 5 ست Pull-up سخت‌گیرانه با 40-50٪ حداکثر، فاصله حداقل 60 دقیقه، هرگز نزدیک ناتوانی. (روش عملی Pavel Tsatsouline، نه تحقیق)"],
     [en("Dead Hang Accumulation"), "3 دقیقه مجموع در روز. هفته‌های 1-2 گریپ معمولی؛ از هفته 3 نصف آن False Grip."],
     [en("Step Streak"), "56 روز پیاپی حداقل 12,000 قدم."],
     [en("Hollow Body 60"), "یک Hollow Hold تمیز 60 ثانیه‌ای تا هفته 8."],
     [en("Muscle-Up Day"), "جمعه هفته 8: گرم کردن کامل، 3 Explosive Chest-to-Bar Pull-up، سپس تا 5 تلاش Muscle-Up با 3 دقیقه استراحت. اگر نشد، 3 تکرار Band-Assisted و ثبت. اهداف دوم: 12 Pull-up سخت‌گیرانه، 15 Dip، 3 Pull-up تا سطح جناغ."]])))

# 9 tests
S.append(sec("tests", "9. تست‌ها", "<p>زمان: روز 1، جمعه هفته 4، جمعه هفته 8. بین تست‌ها 3-5 دقیقه استراحت.</p>" + T(
    ["تست", "واحد"],
    [[en(a), b] for a, b in [("Max Strict Pull-ups", "reps"), ("Max Chest-to-Bar Pull-ups", "reps"), ("Max Parallel Bar Dips", "reps"),
                             ("Max Straight Bar Dips", "reps"), ("Dead Hang", "s"), ("False Grip Hang", "s"), ("Hollow Body Hold", "s"),
                             ("Weighted Pull-up 3RM", "kg added"), ("Bodyweight (7-day average)", "kg"), ("Waist at navel", "cm"), ("Muscle-Up", "reps")]]) +
    "<p><b>ترتیب پیشنهادی در روز تست:</b> گرم کردن کامل، سپس Weighted Pull-up 3RM و Muscle-Up (در هفته 8 همان Muscle-Up Day)، بعد Max Strict Pull-ups، Chest-to-Bar، Dip ها، و در آخر Dead Hang / False Grip / Hollow. بین هر تست 3-5 دقیقه استراحت. در هفته 4 اگر خسته‌ای 3RM را سبک‌تر (RPE 8) ثبت کن.</p><p><b>چک‌این هفتگی (هر یکشنبه):</b> عکس جلو/پشت/پهلو (همان ساعت و نور)، دور شکم در ناف، کالیپر 3 نقطه Jackson-Pollock.</p>"))

# 10 safety
S.append(sec("safety", "10. ایمنی", ul([
    "تمرین سنگین ناشتا نه. 1.5-2 ساعت بعد از وعده با کربوهیدرات و نمک تمرین کن.",
    "اگر سرگیجه گرفتی: فوراً بنشین یا دراز بکش و پاها را بالا بگیر. بین ست‌های پا آهسته راه برو، ثابت نایست.",
    "اگر غش <b>حین</b> تلاش (نه بعد از آن) رخ داد، یا با تپش قلب، درد قفسه سینه یا تنگی نفس غیرعادی همراه بود: قبل از ادامه ECG بگیر."])))

# 11 science
refs = [
    ("Helms ER, Zinn C, Rowlands DS, Brown SR. A systematic review of dietary protein during caloric restriction in resistance trained lean athletes: a case for higher intakes. Int J Sport Nutr Exerc Metab. 2014;24(2):127-138.", "24092765", "10.1123/ijsnem.2013-0054"),
    ("Helms ER, Aragon AA, Fitschen PJ. Evidence-based recommendations for natural bodybuilding contest preparation: nutrition and supplementation. J Int Soc Sports Nutr. 2014;11:20.", "24864135", "10.1186/1550-2783-11-20"),
    ("Guest NS, VanDusseldorp TA, Nelson MT, et al. International society of sports nutrition position stand: caffeine and exercise performance. J Int Soc Sports Nutr. 2021;18(1):1.", "33388079", "10.1186/s12970-020-00383-4"),
    ("Kreider RB, Kalman DS, Antonio J, et al. International Society of Sports Nutrition position stand: safety and efficacy of creatine supplementation in exercise, sport, and medicine. J Int Soc Sports Nutr. 2017;14:18.", "28615996", "10.1186/s12970-017-0173-z"),
    ("Bickel CS, Cross JM, Bamman MM. Exercise dosing to retain resistance training adaptations in young and older adults. Med Sci Sports Exerc. 2011;43(7):1177-1187.", "21131862", "10.1249/MSS.0b013e318207c15d"),
    ("Schoenfeld BJ, Grgic J, Ogborn D, Krieger JW. Strength and hypertrophy adaptations between low- vs. high-load resistance training: a systematic review and meta-analysis. J Strength Cond Res. 2017;31(12):3508-3523.", "28834797", "10.1519/JSC.0000000000002200"),
    ("Nedeltcheva AV, Kilkus JM, Imperial J, Schoeller DA, Penev PD. Insufficient sleep undermines dietary efforts to reduce adiposity. Ann Intern Med. 2010;153(7):435-441.", "20921542", "10.7326/0003-4819-153-7-201010050-00006"),
    ("Morton RW, Murphy KT, McKellar SR, et al. A systematic review, meta-analysis and meta-regression of the effect of protein supplementation on resistance training-induced gains in muscle mass and strength in healthy adults. Br J Sports Med. 2018;52(6):376-384.", "28698222", "10.1136/bjsports-2017-097608"),
]
rr = ""
for i, (c, pm, doi) in enumerate(refs, 1):
    rr += f"<li id='ref{i}'>{esc(c)} <a href='https://pubmed.ncbi.nlm.nih.gov/{pm}/' target='_blank' rel='noopener'>PMID {pm}</a>, <a href='https://doi.org/{doi}' target='_blank' rel='noopener'>DOI</a></li>"
S.append(sec("science", "11. علم پشت برنامه و منابع", T(
    ["ادعا", "منبع", "نوع"],
    [["پروتئین 2.3-3.1 g/kg FFM، با شدت کسری و لاغری بالاتر می‌رود. برای 72 kg FFM: حدود 166-223 g (≈ 170-220)؛ 200 g انتخاب شد (≈ 2.8 g/kg FFM، 2.25 g/kg وزن).", "<a href='#ref1'>[1]</a>", "پژوهش (مرور سیستماتیک)"],
     ["فراتحلیل رگرسیونی جدیدتر: فایده تا حدود 1.9 g/kg وزن یا 2.5 g/kg FFM. (200 g بالاتر از این سقف است؛ در کسری سنگین و لاغری، حاشیه امن عمدی است.)", "منبع در PubMed پیدا و تأیید نشد", "ادعای تأییدنشده، فقط راهنما"],
     ["در تمرین بدون کسری، با مکمل پروتئین، سود اضافه بالای حدود 1.6 g/kg/روز دیده نشد. در کسری سنگین و لاغری، مقادیر بالاتر (Helms) منطقی است.", "<a href='#ref8'>[8]</a>", "فراتحلیل (شرایط بدون کسری)"],
     ["کاهش 0.5-1٪ وزن بدن در هفته برای بیشترین حفظ عضله (برای تو ≈ 0.45-0.9 kg/هفته)", "<a href='#ref2'>[2]</a>", "مرور (متخصصان)"],
     ["کافئین 3-6 mg/kg عملکرد را بهتر می‌کند؛ 9 mg/kg عوارض زیاد و فایده اضافه ندارد. (3 mg/kg × 89 kg ≈ 267 mg)", "<a href='#ref3'>[3]</a>", "ISSN position stand"],
     ["کراتین: مکمل‌سازی ذخیره کراتین/فسفوکراتین عضله را 20-40٪ بالا می‌برد؛ بهبود عملکرد تمرین پرشدت حدود 10-20٪ است. ایمن در مصرف بلندمدت.", "<a href='#ref4'>[4]</a>", "ISSN position stand"],
     ["با حفظ شدت، کاهش حجم (یک‌سوم یا یک‌نهم) اندازه فیبر عضله را در جوانان حفظ کرد", "<a href='#ref5'>[5]</a>", "پژوهش (RCT، حفظ در دوره بدون افزایش)"],
     ["بار سنگین قدرت 1RM را بیشتر بالا می‌برد؛ هایپرتروفی در بازه بار وسیع مشابه است", "<a href='#ref6'>[6]</a>", "فراتحلیل"],
     ["محدودیت خواب در کسری کالری سهم کاهش چربی را 55٪ کم و از دست رفتن توده بدون چربی را 60٪ بیشتر کرد (10 نفر، 14 روز)", "<a href='#ref7'>[7]</a>", "پژوهش (RCT متقاطع کوچک)"],
     [f"{en('Grease the Groove')}: ست‌های پراکنده و دور از ناتوانی در طول روز", "Pavel Tsatsouline (کتاب Power to the People!)", "<b>روش عملی (practitioner)</b>، نه پژوهش"]]) +
    "<h3>فهرست منابع</h3><ol>" + rr + "</ol><p class='small'>شناسه‌ها با PubMed بررسی شدند (عنوان، سال، مجله).</p>"))

# 12 cheat sheet
cs = f"""<div class="cheat"><h3>برگه تقلب یک‌صفحه‌ای</h3>
<div class="g3"><div><b>هفته</b><br>Mon A · Tue B · Wed walk+GTG · Thu C · Fri D · Sat long walk (+refeed از W3) · Sun walk+check-in</div>
<div><b>تغذیه</b><br>Train 2100 kcal: P200 F60 C190<br>Walk 1900: P200 F60 C140<br>Refeed 2500: P180 F55 C320<br>پنجره 12:00-20:00، پروتئین 4 وعده، فیبر ≥ 30 g</div>
<div><b>آب</b><br>روز تمرین ≥ 4 L · پیاده‌روی ≥ 3.5 L · کم‌تحرک ≥ 3 L<br>صبح 500 ml · پیش از تمرین ¼ tsp نمک<br>خواب 7.5-9 h</div>
<div><b>مکمل</b><br>Creatine 5 g · Whey طبق نیاز · Caffeine 200-270 mg (45 min قبل، تا 16:00) · D3 1000-2000 IU · Omega-3 1-2 g</div>
<div><b>قوانین تمرین</b><br>RPE 7-9، 1-2 تکرار ذخیره، هرگز تا ناتوانی<br>اصلی 2-3 min · فرعی 60-90 s<br>فرم خراب = پایان ست<br>گرم کردن 8-10 min</div>
<div><b>دوره‌بندی</b><br>W1-3 انباشت · W4 دیلود + تست · W5-7 تشدید · W8 اوج + Muscle-Up Day</div>
<div><b>تعدیل</b><br>&lt; 0.4 kg/هفته در 2 هفته: -150 kcal کربو از روزهای استراحت<br>&gt; 1.2 kg/هفته یا افت قدرت در 2 جلسه: +150 kcal</div>
<div><b>چالش‌ها</b><br>GTG (Wed/Sat/Sun) · Dead Hang 3 min/day (از W3 نصف False Grip) · 12k steps × 56 · Hollow 60 s · Muscle-Up Day W8 Fri</div>
<div><b>ایمنی</b><br>ناشتا سنگین نه · سرگیجه: بنشین، پاها بالا · غش حین تلاش یا با تپش/درد سینه: ECG</div>
<div><b>تست‌ها</b><br>Day 1 · Fri W4 · Fri W8<br>چک‌این Sunday: عکس، دور ناف، کالیپر 3 نقطه</div></div></div>"""
S.append(sec("cheat", "12. برگه تقلب", cs))

toc = "".join(f"<li><a href='#{i}'>{t}</a></li>" for i, t in [
    ("profile", "پروفایل و هدف‌ها"), ("energy", "مصرف انرژی"), ("nutrition", "تغذیه"), ("hydration", "آب، مکمل، خواب"),
    ("program", "برنامه تمرین"), ("walking", "پیاده‌روی"), ("library", "کتابخانه حرکت‌ها"), ("challenges", "چالش‌ها"),
    ("tests", "تست‌ها"), ("safety", "ایمنی"), ("science", "علم و منابع"), ("cheat", "برگه تقلب")])

CSS = font_css() + """
:root{--bg:#E9ECEF;--surface:#F6F7F8;--surface2:#DDE2E7;--ink:#1B2430;--ink2:#465362;--line:#C6CDD5;--steel:#3A6A94;--steel-ink:#2D5578;--grip:#C99A36;--grip-ink:#6E4F0E;color-scheme:light}
@media (prefers-color-scheme:dark){:root{--bg:#11161C;--surface:#19212A;--surface2:#222C37;--ink:#E6EAEE;--ink2:#A2AEBB;--line:#2E3946;--steel:#7EB0DC;--steel-ink:#9CC4E8;--grip:#D9A94A;--grip-ink:#E3BE6E;color-scheme:dark}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:'Vazirmatn','Tahoma',system-ui,sans-serif;line-height:1.85;font-size:16px}
.en{font-family:'Barlow Condensed','Arial Narrow',Arial,sans-serif;font-weight:600;direction:ltr;unicode-bidi:isolate}
main{max-width:980px;margin:0 auto;padding:24px 16px 80px}
header.hero{padding:24px 0 8px;border-bottom:4px solid var(--steel)}
header h1{font-size:2rem;margin:0;line-height:1.3}
header p{color:var(--ink2);margin:6px 0 0}
h2{font-size:1.5rem;margin:0 0 12px;padding-top:6px;border-top:1px solid var(--line);padding-top:20px}
section{margin:36px 0;scroll-margin-top:12px}
h3{font-size:1.1rem;margin:20px 0 6px}
a{color:var(--steel-ink)}
a:focus-visible{outline:3px solid var(--steel);outline-offset:2px}
.tw{overflow-x:auto;margin:8px 0}
table{border-collapse:collapse;width:100%;font-size:.93rem}
th,td{padding:6px 8px;text-align:start;vertical-align:top}
thead th{border-bottom:2px solid var(--ink2);white-space:nowrap}
tbody tr+tr td{border-top:1px solid var(--line)}
table.wk td:nth-child(n+4){white-space:nowrap;text-align:center}
.note{border-inline-start:4px solid var(--grip);background:var(--surface);padding:10px 14px;margin:10px 0;border-radius:10px}
.small{font-size:.85rem}.muted{color:var(--ink2)}
nav.toc{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:8px 16px;margin:16px 0}
nav.toc ol{columns:2;margin:4px 0;padding-inline-start:22px}
article.ex{border-top:1px solid var(--line);padding:10px 0;break-inside:avoid}
article.ex h3{margin:0;font-size:1.25rem}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.g3{display:grid;grid-template-columns:repeat(3,1fr);gap:10px 14px}
.cheat .g3>div{border-top:2px solid var(--steel);padding-top:4px;font-size:.88rem;line-height:1.6}
ul,ol{margin:6px 0;padding-inline-start:22px}
@media (max-width:640px){.g2,.g3{grid-template-columns:1fr}nav.toc ol{columns:1}}
@media print{
 @page{size:A4;margin:14mm 12mm}
 :root{--bg:#fff;--surface:#fff;--ink:#111;--ink2:#444;--line:#bbb}
 body{font-size:10.5pt;line-height:1.6;background:#fff;color:#111}
 main{max-width:none;padding:0}
 section{break-inside:auto}h2,h3{break-after:avoid}
 tr,article.ex,.note{break-inside:avoid}
 table{font-size:8.8pt}.tw{overflow:visible}
 #cheat{break-before:page}
 a{color:inherit;text-decoration:none}
 .g3{grid-template-columns:repeat(3,1fr)}
}
"""

import re
_TOK = r"[A-Za-z0-9](?:[A-Za-z0-9.,:/×%@+\-'&]*[A-Za-z0-9%])?"
_RUN = re.compile(r"((?:[~≥≤<>]\s?)?" + _TOK + r"(?:\s+" + _TOK + r")*)")
def wrap_ltr(h):
    out, depth, skip = [], 0, 0
    for part in re.split(r"(<[^>]+>)", h):
        if part.startswith("<"):
            m = re.match(r"<(/?)(\w+)", part)
            if m:
                tag, close = m.group(2).lower(), bool(m.group(1))
                if tag in ("bdi", "style", "script", "title"):
                    skip += -1 if close else 1
            out.append(part)
        elif skip > 0 or not part.strip():
            out.append(part)
        else:
            out.append(_RUN.sub(lambda mo: '<bdi dir="ltr">' + mo.group(1) + "</bdi>", part))
    return "".join(out)

doc = f"""<!doctype html><html lang="fa" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>راهنمای کامل برش ۸ هفته‌ای</title><style>{CSS}</style></head><body><main>
<header class="hero"><h1>راهنمای کامل برش ۸ هفته‌ای</h1><p>حفظ عضله، قدرت کل بدن، خشکی، اولین Muscle-Up. امیر، شروع پیش‌فرض <bdi dir='ltr'>2026-10-05</bdi>.</p></header>
<nav class="toc" aria-label="فهرست"><b>فهرست</b><ol>{toc}</ol><p class="small muted">ترکر تعاملی: <a href="../tracker/index.html">tracker/index.html</a></p></nav>
{''.join(S)}
</main></body></html>"""
body_start=doc.index("<main>")
doc=doc[:body_start]+wrap_ltr(doc[body_start:])
(root / "guide/index.html").write_text(doc)
print("guide ok", len(doc))
