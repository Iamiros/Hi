# Single source of truth for the program. Used by build.py for tracker + guide.
# No em/en dashes in visible strings (ranges use a hyphen).

SCHEMES = {
    "heavy":    ["4×5 @RPE7", "4×5 @RPE7.5", "5×5 @RPE8", "3×3 @RPE6", "5×3 @RPE8", "5×3 @RPE8.5", "6×2-3 @RPE8.5", "3×2 light"],
    "pu":       ["5×3", "6×3", "5×4", "3×3", "5×4", "5×5", "4×5-6", "3×3"],
    "assist":   ["4×6", "4×6", "5×6", "3×5", "4×8", "4×8", "5×8", "3×5 light"],
    "highpull": ["5×3", "5×3", "6×3", "3×2", "6×2", "6×2", "6×2", "3×2"],
    "negative": ["3×2", "3×2", "4×2", "2×1", "4×2", "4×2", "5×2", "2×1"],
    "hangs":    ["3×15s", "3×20s", "3×25s", "2×20s", "3×30s", "3×35s", "3×40s", "2×30s"],
    "hollow":   ["3×30s", "3×35s", "3×40s", "2×30s", "3×45s", "3×50s", "3×60s", "2×45s"],
}

PHASES = [  # (weeks, key, fa, en)
    ([1, 2, 3], "acc", "انباشت", "Accumulation"),
    ([4], "deload", "دیلود", "Deload"),
    ([5, 6, 7], "int", "تشدید", "Intensification"),
    ([8], "peak", "اوج و تست", "Peak & Test"),
]

WARMUP = [
    ("Wrist & Shoulder CARs", "1 min"),
    ("Band Pull-Apart", "2×15"),
    ("Scapular Pull-up", "1×8"),
    ("Arch Hang / Active Hang", "2×10 s"),
    ("Push-up", "1×10"),
    ("Two light sets of the session's first exercise", ""),
]

# ---------------------------------------------------------------------------
# Exercise library. id -> dict. fa = description, cues, mistakes, reg, prog, yt
# ---------------------------------------------------------------------------
def E(id, en, fa, cues, mistakes, reg, prog, yt=None):
    return dict(id=id, en=en, fa=fa, cues=cues, mistakes=mistakes, reg=reg, prog=prog,
                yt=yt or (en + " proper form"))

LIB = [
 E("cars", "Wrist & Shoulder CARs",
   "چرخش‌های کنترل‌شده و کامل مچ و شانه برای گرم کردن مفصل‌ها. آهسته و در بیشترین دامنه حرکتی انجام می‌شود.",
   ["مچ: دایره‌های بزرگ با مشت بسته", "شانه: دست صاف، دایره کامل بدون خم شدن تنه", "تنفس آرام و حرکت آهسته"],
   ["سریع انجام دادن", "کمک گرفتن از کمر و تنه"], "دامنه کوچک‌تر", "کمی فشار ملایم در انتهای دامنه",
   "wrist and shoulder CARs controlled articular rotations"),
 E("bpa", "Band Pull-Apart",
   "کشیدن کش به طرفین با دست‌های صاف؛ پشت شانه و کتف را فعال می‌کند و سلامت شانه را حفظ می‌کند.",
   ["کتف‌ها را به هم نزدیک کن", "آرنج‌ها تقریباً صاف، بدون قفل شدن کامل", "کش را تا لمس سینه بکش (کتف‌ها کاملاً جمع شوند)"],
   ["بالا آوردن شانه‌ها به سمت گوش", "کمر را قوس دادن"], "کش سبک‌تر", "کش سفت‌تر یا مکث ۲ ثانیه در انتها",
   "band pull apart shoulder health"),
 E("scap", "Scapular Pull-up",
   "آویزان شدن از بار و بالا و پایین بردن کتف (Elevation/Depression) بدون خم شدن آرنج. پایه‌ی کنترل کتف برای Pull-up و Muscle-Up.",
   ["آرنج‌ها صاف", "کتف‌ها را پایین و عقب بکش تا بدن چند سانت بالا بیاید", "در بالا ۱ ثانیه مکث"],
   ["خم کردن آرنج", "تاب خوردن بدن"], "اجرا با کش کمکی", "مکث ۳ ثانیه در بالا یا شروع Pull-up با دامنه کوچک (Mini Pull-up)",
   "scapular pull up form"),
 E("archhang", "Arch Hang / Active Hang",
   "آویزان شدن با کتف‌های فعال و کمی قوس در بالاتنه. به آماده شدن مچ، شانه و گریپ کمک می‌کند.",
   ["کتف‌ها را از گوش دور کن", "سینه کمی بیرون، لگن زیر بدن", "گریپ محکم ولی بدون لرزش شدید"],
   ["آویزان شدن شل و رها (Passive)", "نگه داشتن نفس"], "پا روی زمین یا صندلی", "افزایش زمان یا استفاده از False Grip",
   "active hang vs passive hang pull up bar"),
 E("pushup", "Push-up",
   "شنا؛ حرکت پایه‌ی فشاری برای گرم کردن سینه، شانه و پشت بازو.",
   ["بدن یک خط صاف", "آرنج‌ها حدود ۴۵ درجه از بدن", "سینه تا نزدیک زمین"],
   ["افتادن کمر", "باز شدن بیش از حد آرنج‌ها"], "شنا روی زانو یا روی سطح بالاتر", "پا روی ارتفاع یا افزودن وزنه",
   "perfect push up form"),
 # --- Workout A ---
 E("bench", "Barbell Bench Press",
   "پرس سینه با هالتر در باشگاه. جایگزین Dip در روزهای باشگاه.",
   ["کتف‌ها جمع و پایین", "میله به پایین سینه", "پاها محکم روی زمین"],
   ["جدا شدن باسن از نیمکت", "پرش میله از روی سینه"], "Dumbbell Bench Press", "افزایش وزنه در پله‌های کوچک",
   "barbell bench press technique"),
 E("dbrow", "One-Arm Dumbbell Row",
   "پارویی یک‌دست با دمبل؛ ضخامت پشت. در خانه می‌توان از کوله‌پشتی یا کش استفاده کرد.",
   ["تنه موازی زمین", "آرنج به سمت لگن", "مکث کوتاه در بالا"],
   ["چرخیدن تنه", "کشیدن با بازو به‌جای پشت"], "کش یا وزنه‌ی سبک‌تر", "وزنه سنگین‌تر یا مکث ۲ ثانیه",
   "one arm dumbbell row form"),
 E("bbrow", "Barbell Row",
   "پارویی با هالتر در باشگاه؛ جایگزین Dumbbell Row.",
   ["کمر خنثی", "هالتر به شکم", "زانوها کمی خم"],
   ["کمر گرد شدن", "کمک گرفتن شدید از تنه"], "Chest-Supported Row", "افزایش وزنه",
   "barbell row proper form"),
 E("lat", "Dumbbell Lateral Raise",
   "نشر جانب با دمبل؛ عرض شانه (سر میانی دلتوئید) برای فرم V شکل. در خانه با کش یا کوله‌پشتی سبک.",
   ["آرنج کمی خم", "تا سطح شانه بالا بیا", "پایین آمدن آهسته"],
   ["تاب دادن بدن", "بالا کشیدن شانه‌ها (شراگ)"], "وزنه‌ی سبک‌تر", "مکث ۱ ثانیه در بالا یا کش",
   "dumbbell lateral raise form"),
 E("squat", "Back Squat",
   "اسکوات هالتر پشت؛ حرکت اصلی پای باشگاه.",
   ["هالتر روی عضلات ذوزنقه‌ی بالایی", "زانوها در راستای پنجه", "عمق حداقل موازی"],
   ["جمع شدن زانوها به داخل", "جلو آمدن بیش از حد تنه"], "Goblet Squat", "افزایش وزنه یا مکث پایین",
   "barbell back squat form"),
 E("bss", "Weighted Bulgarian Split Squat",
   "اسکوات تک‌پا با پای عقب روی نیمکت یا صندلی و وزنه (کوله‌پشتی)؛ جایگزین خانگی Back Squat.",
   ["پای جلو محکم", "تنه کمی مایل", "زانوی عقب نزدیک زمین"],
   ["قدم خیلی کوتاه", "فشار روی پنجه"], "Split Squat بدون وزنه", "کوله‌پشتی سنگین‌تر و مکث",
   "bulgarian split squat form"),
 E("rdl", "Romanian Deadlift",
   "ددلیفت رومانیایی؛ همسترینگ و باسن با خم شدن از مفصل ران.",
   ["لگن به عقب", "کمر خنثی", "میله نزدیک پا"],
   ["گرد شدن کمر", "خم کردن بیش از حد زانو"], "RDL با دمبل سبک", "وزنه‌ی سنگین‌تر",
   "romanian deadlift technique"),
 E("slrdl", "Single-Leg RDL",
   "RDL تک‌پا با دمبل یا کوله‌پشتی؛ جایگزین خانگی RDL و تمرین تعادل.",
   ["لگن‌ها موازی زمین", "پای عقب هم‌راستا با تنه", "کمر خنثی"],
   ["چرخش لگن", "گرد شدن کمر"], "با تکیه به دیوار یا انگشتی روی زمین", "وزنه‌ی بیشتر",
   "single leg romanian deadlift form"),
 E("lunge", "Walking Lunge",
   "لانچ راه‌رونده؛ چهارسر و باسن با دامنه‌ی بلند.",
   ["قدم متوسط", "تنه راست", "زانوی عقب نزدیک زمین"],
   ["قدم خیلی کوتاه", "افتادن زانو به داخل"], "Reverse Lunge ثابت", "افزودن دمبل",
   "walking lunge form"),
 E("stepup", "Step-up",
   "بالا رفتن از جعبه یا صندلی محکم با وزنه؛ جایگزین خانگی Walking Lunge.",
   ["کل کف پا روی سطح", "با پای روی جعبه بلند شو و از پای پایین کمک نگیر", "پایین آمدن کنترل‌شده"],
   ["هل دادن با پای عقب", "ارتفاع خیلی زیاد"], "ارتفاع کمتر", "کوله‌پشتی سنگین‌تر یا ارتفاع بیشتر",
   "weighted step up form"),
 E("nordic", "Nordic Hamstring Curl (Eccentric)",
   "پایین آمدن آهسته (۳ تا ۵ ثانیه) از حالت زانو؛ پیشگیری از آسیب همسترینگ و قدرت پشت ران.",
   ["مچ پا را محکم قفل کن (خانه: زیر مبل سنگین یا با کمک شریک)", "بدن از زانو تا سر یک خط", "فرود را آهسته نگه دار؛ وقتی کنترل از دست رفت، با دست‌ها زمین را بگیر"],
   ["خم شدن از کمر", "افتادن سریع"], "Nordic با کش کمکی یا دامنه کوتاه‌تر", "فرود ۵ ثانیه‌ای تا انتها و برگشت با حداقل کمک دست؛ در نهایت بدون دست",
   "nordic hamstring curl eccentric"),
 E("calf", "Standing Calf Raise",
   "بلند شدن روی پنجه در حالت ایستاده؛ ساق پا. در خانه تک‌پا روی پله با کوله‌پشتی.",
   ["دامنه‌ی کامل", "مکث ۱ ثانیه بالا", "پایین آمدن کامل و کش‌آمدن"],
   ["حرکت‌های پرشی و کوتاه", "خم کردن زانو"], "با هر دو پا", "تک‌پا و وزنه‌ی بیشتر",
   "standing calf raise form"),
 E("rollout", "Ab Wheel Rollout",
   "غلتاندن چرخ شکم؛ ثبات مرکزی بدن و شکم.",
   ["لگن زیر بدن (Posterior Tilt)", "دست‌ها صاف", "تا جایی که ناحیه کمر گود نشود"],
   ["افتادن کمر", "رفتن بیش از حد دور"], "Rollout از زانو با دامنه کم", "دامنه‌ی بیشتر، سپس مکث ۲ ثانیه در انتها",
   "ab wheel rollout form"),
 # --- Workout C ---
 E("highpull", "Band-Assisted High Pull-up",
   "بارفیکس با کش کمکی که در آن میله را تا زیر سینه یا شکم بالا می‌کشی و آرنج‌ها را به سمت لگن می‌رانی؛ قدرت کشیدن بالای Pull-up.",
   ["کشیدن به سمت لگن", "سینه به‌سمت میله", "کتف عقب"],
   ["نگه داشتن سر جلو", "استفاده از کش خیلی قوی"], "کش قوی‌تر", "کش ضعیف‌تر",
   "high pull up muscle up progression"),
 E("incdb", "Incline Dumbbell Press",
   "پرس بالاسینه با دمبل؛ سینه‌ی بالایی برای فرم مدل.",
   ["شیب ۲۵ تا ۳۰ درجه", "آرنج‌ها حدود ۴۵ درجه", "دمبل‌ها به سمت بالا"],
   ["شیب زیاد (شبیه پرس شانه)", "باز شدن آرنج‌ها"], "وزنه‌ی سبک‌تر", "وزنه‌ی سنگین‌تر",
   "incline dumbbell press form"),
 E("fepu", "Weighted Feet-Elevated Push-up",
   "شنا با پاها روی ارتفاع و کوله‌پشتی؛ جایگزین خانگی پرس شیب‌دار.",
   ["بدن خط صاف", "پاها روی ارتفاع ۳۰ تا ۵۰ سانتی‌متر", "کوله‌پشتی روی کمر بالا"],
   ["افتادن کمر", "سر جلو"], "شنا بدون وزنه", "ارتفاع بیشتر یا وزنه‌ی بیشتر",
   "feet elevated weighted push up"),
 E("ohp", "Standing Overhead Press",
   "پرس بالای سر ایستاده؛ شانه و پشت بازو.",
   ["شکم و باسن سفت", "میله از جلوی صورت", "در بالا سر زیر میله"],
   ["قوس کمر", "پرس با پا"], "Dumbbell Press", "افزایش وزنه",
   "standing overhead press form"),
 E("pike", "Deficit Pike Push-up",
   "شنا پایک با دست‌ها روی ارتفاع (Deficit)؛ جایگزین خانگی پرس شانه.",
   ["باسن بالا", "سر بین دست‌ها پایین بیاید", "آرنج‌ها حدود ۴۵ درجه"],
   ["دامنه‌ی کوتاه", "افتادن کمر"], "Pike Push-up ساده", "پاها روی ارتفاع",
   "deficit pike push up"),
 E("facepull", "Lateral Raise + Face Pull / Band Pull-Apart (superset)",
   "ابرست: نشر جانب سپس Face Pull (باشگاه) یا Band Pull-Apart (خانه)؛ شانه‌ی جانبی و پشت شانه.",
   ["نشر جانب: آرنج کمی خم", "Face Pull: کش یا طناب به سمت صورت", "ابتدا شانه، سپس پشت شانه"],
   ["وزنه‌ی سنگین و تاب دادن", "استراحت طولانی بین دو حرکت"], "وزنه‌ی سبک‌تر", "وزنه یا مقاومت کش بیشتر، تکرار تا ۱۵ در هر دو حرکت",
   "face pull and lateral raise superset"),
 E("hlr", "Hanging Leg Raise",
   "بالا آوردن پاها در حالت آویزان؛ شکم پایینی و گریپ.",
   ["لگن را به عقب بچرخان", "پاها بدون تاب", "پایین آمدن کنترل‌شده"],
   ["استفاده از تاب", "فقط بالا آوردن زانو"], "Knee Raise", "پای صاف تا میله (Toes-to-Bar)",
   "hanging leg raise strict"),
 # --- Workout D ---
 E("dl", "Deadlift",
   "ددلیفت از زمین؛ قدرت کل بدن. 1RM قبلی 160 kg؛ بار هدف ۸۰ تا ۸۵٪ از 1RM فعلی (نه رکورد قبلی) با ۳ تکرار.",
   ["هالتر روی وسط پا", "کتف‌ها روی میله", "هل دادن زمین"],
   ["گرد شدن کمر", "بلند کردن باسن زودتر از سینه"], "Trap Bar یا Romanian Deadlift", "افزایش وزنه از ۸۰ به ۸۵٪",
   "conventional deadlift form"),
 E("pistol", "Box Pistol Squat",
   "اسکوات تک‌پا تا نشستن روی جعبه؛ جایگزین خانگی Deadlift. توجه: چهارسر-محور است و الگوی Hip Hinge ندارد، پس جایگزین تقریبی است (برای هینج می‌توانی Single-Leg RDL را اضافه کنی).",
   ["پای دیگر جلو", "کنترل فرود روی جعبه", "زانو هم‌راستای پنجه"],
   ["افتادن روی جعبه", "جمع شدن زانو به داخل"], "جعبه‌ی بلندتر", "جعبه‌ی کوتاه‌تر یا وزنه",
   "box pistol squat progression"),
 E("hollow", "Hollow Body Hold",
   "نگه داشتن حالت هلو (کمر چسبیده به زمین، دست و پا دراز)؛ ثبات تنه برای Pull-up تمیز بدون تاب.",
   ["کمر پایین چسبیده به زمین", "دنده‌ها پایین", "پاها و دست‌ها صاف"],
   ["قوس کمر", "نگه داشتن نفس"], "Tuck Hollow Hold", "Hollow Rock یا ۶۰ ثانیه",
   "hollow body hold form"),
 E("farmer", "Farmer's Carry",
   "راه رفتن با وزنه‌ی سنگین در دو دست؛ گریپ، ذوزنقه و ثبات. در خانه با کوله‌پشتی یا کیسه‌ی سنگین.",
   ["قامت بلند", "گام‌های کوتاه و ثابت", "شانه‌ها پایین"],
   ["خم شدن به جلو", "گام خیلی بلند"], "وزنه‌ی سبک‌تر", "وزنه‌ی سنگین‌تر یا مسافت بیشتر",
   "farmers carry form"),
 E("pullup", "Pull-up",
   "بارفیکس سخت‌گیرانه با وزن بدن. هدف این ۸ هفته: از ۴-۵ تکرار به ۸-۱۰ تکرار. وزن بدن خودش بار است و وزنه اضافه فعلاً لازم نیست. ست‌ها را با ۲ تکرار کمتر از حداکثر تمام کن و هر هفته تکرار یا ست اضافه کن.",
   ["شروع از آویز کامل با کتف فعال", "چانه بالای میله، آرنج‌ها به سمت لگن", "پایین آمدن کنترل‌شده ۲ ثانیه تا آویز کامل"],
   ["نیم‌حرکت یا کیپینگ", "رفتن تا ناتوانی کامل (فرم می‌شکند)"],
   "Assisted Pull-up (ماشین) یا Band-Assisted Pull-up", "وقتی همه ست‌ها تمیز انجام شد، ۱ تکرار به هر ست اضافه کن؛ از ۸ تکرار به بعد وزنه ۱.۲۵ تا ۲.۵ kg",
   "strict pull up progression 5 to 10 reps"),
 E("dip", "Dip",
   "دیپ موازی با وزن بدن (نسخه‌ی خانگی جایگزین Bench Press). برای شروع کمتر از ۸ تکرار؛ ست‌ها را با ۱-۲ تکرار ذخیره انجام بده.",
   ["شانه‌ها پایین و عقب", "کمی خم به جلو برای درگیری سینه", "تا زاویه‌ی حدود ۹۰ درجه‌ی آرنج"],
   ["عمق بیش از حد و فشار روی شانه", "لق خوردن و ناپایداری روی صندلی"],
   "Assisted Dip یا Negative Dip (فرود ۳-۴ ثانیه)", "تکرار بیشتر؛ بعد از ۱۲ تکرار وزنه",
   "parallel bar dip progression beginner"),
 E("deadhang", "Dead Hang",
   "آویز با دست‌های صاف؛ گریپ و سلامت شانه. در زمان‌های کوتاه چند ست.",
   ["گریپ محکم", "شانه‌ها فعال نه شل", "بدون تاب"],
   ["رها کردن زودهنگام", "رها شدن شانه‌ها به گوش"], "پا روی صندلی", "افزایش زمان یا Active Hang",
   "dead hang pull up bar benefits"),
 E("pun", "Pull-up Negative",
   "بپر یا با پله به بالای میله برو و ۳ تا ۵ ثانیه آهسته پایین بیا. سریع‌ترین راه برای قوی شدن در دامنه‌ی پایین Pull-up.",
   ["چانه بالای میله شروع کن", "فرود ۴-۵ ثانیه‌ای", "پایین کامل و ریست"],
   ["افتادن سریع", "بالا رفتن با کیپینگ"], "فرود ۳ ثانیه", "فرود ۵ ثانیه، مکث در وسط",
   "negative pull up technique"),
 E("apu", "Assisted Pull-up",
   "Pull-up با ماشین کمکی (باشگاه). وزنه‌ی کمکی را هر هفته کم کن. روز تقویت حجم (۶-۸ تکرار).",
   ["همان فرم Pull-up", "هر ست تا ۱-۲ تکرار ذخیره", "ثبت میزان کمک"],
   ["کمک خیلی زیاد", "نیم‌حرکت"], "کمک بیشتر", "کمک کمتر ۲.۵-۵ kg در هفته",
   "assisted pull up machine form"),
 E("bapu", "Band-Assisted Pull-up",
   "Pull-up با کش کمکی (خانه). نسخه‌ی خانگی Assisted Pull-up. با کش ضعیف‌تر پیشرفت کن.",
   ["کش زیر زانو یا پا", "همان فرم Pull-up", "ست را با ۱-۲ تکرار ذخیره تمام کن"],
   ["کش خیلی قوی", "نیم‌حرکت"], "کش قوی‌تر", "کش ضعیف‌تر",
   "band assisted pull up"),
 E("adip", "Assisted Dip (3 s eccentric)",
   "Dip با ماشین کمکی و فرود ۳ ثانیه‌ای (باشگاه). جایگزین Dip وزن بدن تا وقتی ۸+ تکرار زدی.",
   ["شانه‌ها پایین", "فرود ۳ ثانیه", "تا ۹۰ درجه آرنج"],
   ["فرود سریع", "کمک خیلی زیاد"], "کمک بیشتر", "کمک کمتر",
   "assisted dip machine"),
 E("tdip", "Tempo Dip (3 s eccentric)",
   "Dip با فرود ۳ ثانیه‌ای روی میله‌ی موازی یا دو صندلی محکم (خانه).",
   ["شانه‌ها پایین و عقب", "فرود ۳ ثانیه", "کمی خم به جلو"],
   ["فرود سریع", "ساپورت ناپایدار"], "Negative Dip با پا روی زمین", "Dip با تکرار بیشتر",
   "tempo dip form"),
 E("chin", "Chin-up",
   "چین‌آپ وزن بدن (کف دست رو به خود)؛ دوسر بازو و پشت. معمولاً از Pull-up راحت‌تر است.",
   ["گریپ به عرض شانه", "چانه بالای میله", "پایین آمدن کامل"],
   ["نیم‌حرکت", "تاب خوردن"], "Assisted Chin-up یا Negative", "تکرار بیشتر؛ بعد از ۱۰ تکرار وزنه",
   "chin up form"),
 E("cablelat", "Cable Lateral Raise",
   "نشر جانب با کابل (باشگاه)؛ کشش ثابت روی سر میانی شانه. نسخه خانگی: Band Lateral Raise.",
   ["آرنج کمی خم", "تا سطح شانه", "پایین آمدن آهسته"], ["تاب دادن بدن", "شراگ کردن شانه‌ها"],
   "وزنه‌ی سبک‌تر", "مکث ۱ ثانیه بالا", "cable lateral raise form"),
 E("bandlat", "Band Lateral Raise",
   "نشر جانب با کش (خانه).",
   ["کش زیر پا", "آرنج کمی خم", "تا سطح شانه"], ["تاب دادن", "شراگ"], "کش ضعیف‌تر", "کش سفت‌تر",
   "band lateral raise"),
 E("reardelt", "Rear Delt Fly",
   "باز کردن دست به طرفین برای پشت شانه (Reverse Pec Deck یا دمبل خم). برای تعادل شانه و فرم عقب.",
   ["تنه ثابت", "آرنج کمی خم", "کتف‌ها را فشار نده، پشت شانه را حس کن"], ["استفاده از کمر", "وزنه‌ی زیاد"],
   "وزنه‌ی سبک‌تر", "مکث ۱ ثانیه", "rear delt fly reverse pec deck"),
 E("bandrear", "Band Reverse Fly",
   "نسخه خانگی Rear Delt Fly با کش.",
   ["کش در سطح سینه", "آرنج کمی خم", "پشت شانه"], ["شراگ", "کمر قوس"], "کش ضعیف‌تر", "کش سفت‌تر",
   "band reverse fly rear delt"),
 E("inccurl", "Incline Dumbbell Curl",
   "جلو بازو روی نیمکت شیب‌دار؛ کشش کامل جلو بازو.",
   ["آرنج‌ها زیر شانه", "پایین کامل با کنترل", "بدون تاب"], ["تاب خوردن", "حرکت آرنج به جلو"],
   "وزنه‌ی سبک‌تر", "مکث ۱ ثانیه بالا", "incline dumbbell curl form"),
 E("bandcurl", "Band Curl",
   "جلو بازو با کش یا دمبل (خانه).",
   ["آرنج‌ها کنار بدن", "پایین آهسته"], ["تاب خوردن"], "کش ضعیف‌تر", "کش سفت‌تر یا مکث",
   "band curl"),
 E("pushdown", "Triceps Rope Pushdown",
   "پشت بازو با طناب روی کابل؛ در پایین طناب را باز کن.",
   ["آرنج‌ها کنار بدن", "تا باز شدن کامل", "بالا آمدن کنترل‌شده"], ["حرکت آرنج", "تنه تکان دادن"],
   "وزنه‌ی سبک‌تر", "مکث ۱ ثانیه پایین", "triceps rope pushdown form"),
 E("bandtri", "Band Triceps Pushdown",
   "نسخه خانگی Pushdown با کش بسته‌شده بالای در یا میله.",
   ["آرنج‌ها کنار بدن", "تا باز شدن کامل"], ["حرکت آرنج"], "کش ضعیف‌تر", "کش سفت‌تر",
   "band triceps pushdown"),
 E("cablecrunch", "Cable Crunch",
   "کرانچ با کابل برای شکم؛ ستون فقرات گرد می‌شود، نه خم شدن از ران.",
   ["لگن ثابت", "دنده‌ها به سمت لگن", "پایین آمدن کنترل‌شده"], ["کشیدن با دست", "وزنه‌ی زیاد"],
   "وزنه‌ی سبک‌تر", "مکث ۱ ثانیه پایین", "cable crunch form"),
 E("bpcrunch", "Backpack Crunch",
   "کرانچ با کوله‌پشتی روی سینه (خانه).",
   ["پاها صاف روی زمین", "گردن راحت", "بالا آمدن کنترل‌شده"], ["کشیدن گردن"], "بدون وزنه", "کوله‌پشتی سنگین‌تر",
   "weighted crunch"),
 E("pallof", "Pallof Press",
   "پرس ضدچرخش با کابل یا کش؛ مرکز بدن و ثبات.",
   ["کتف‌ها ثابت", "دست‌ها را از سینه صاف کن", "بدن نچرخد"], ["چرخش تنه", "کش خیلی سنگین"],
   "مقاومت کمتر", "مکث ۲ ثانیه با دست صاف", "pallof press form"),
]
LIBD = {e["id"]: e for e in LIB}

# ---------------------------------------------------------------------------
# Workouts. dose: scheme key or [fixed, deload]. gym/home -> LIB ids.
# m = muscle credit per set (primary 1, secondary 0.5). h = counts as hard set.
# rest in seconds label. main = per-exercise logging.
# ---------------------------------------------------------------------------
def X(id, gym, home, dose, rest, m, h=1, main=0, fa="", dose_home=None):
    return dict(id=id, gym=gym, home=home, dose=dose, rest=rest, m=m, h=h, main=main, fa=fa,
                dose_home=dose_home)

WORKOUTS = {
 "A": dict(name="Workout A", fa="تمرین A: قدرت بالاتنه", day="Sat", ex=[
   X("a1", "pullup", "pullup", "pu", "3 min", dict(back=1, bi=.5), 1, 1,
     "وزن بدن. هر ست ۲ تکرار کمتر از حداکثر؛ وقتی همه ست‌ها تمیز بود، هفته بعد تکرار اضافه کن."),
   X("a2", "bench", "dip", "heavy", "3 min", dict(chest=1, tri=.5, delt=.5), 1, 1,
     "باشگاه: Barbell Bench Press. خانه: Dip وزن بدن (۴×۴، دیلود ۲×۳).",
     dose_home=["4×4", "2×3"]),
   X("a3", "bbrow", "dbrow", ["3×6-8", "2×6"], "60-90 s", dict(back=1, bi=.5), 1, 0,
     "باشگاه: Barbell Row. خانه: One-Arm Dumbbell Row."),
   X("a4", "lat", "lat", ["3×12-15", "2×12"], "60-90 s", dict(delt=1), 1, 0,
     "۱ تا ۲ تکرار ذخیره."),
   X("a5", "deadhang", "deadhang", "hangs", "60-90 s", dict(grip=1), 0, 0,
     "آویز با شانه‌های فعال."),
 ]),
 "B": dict(name="Workout B", fa="تمرین B: قدرت پایین‌تنه", day="Sun", ex=[
   X("b1", "squat", "bss", "heavy", "3 min", dict(quad=1, glute=.5), 1, 1,
     "باشگاه: Back Squat (شروع حدود ۱۲۰-۱۳۰ kg برای ۵ تکرار با RPE7، بر اساس ۱۵۰×۴). خانه: Weighted Bulgarian Split Squat."),
   X("b2", "rdl", "slrdl", ["3×6", "2×6"], "60-90 s", dict(ham=1, glute=.5), 1, 1,
     "باشگاه: Romanian Deadlift. خانه: Single-Leg RDL."),
   X("b3", "lunge", "stepup", ["3×8 per leg", "2×8 per leg"], "60-90 s", dict(quad=1, glute=.5), 1, 0,
     "باشگاه: Walking Lunge (یا Leg Press اگر زانو خسته بود). خانه: Step-up."),
   X("b4", "nordic", "nordic", ["3×4-6", "2×4"], "60-90 s", dict(ham=1), 1, 0,
     "فرود ۳ تا ۵ ثانیه."),
   X("b5", "calf", "calf", ["3×10-12", "2×10"], "60-90 s", dict(calf=1), 1, 0,
     "دامنه‌ی کامل، مکث ۱ ثانیه بالا و کش‌آمدن کامل پایین."),
   X("b6", "rollout", "rollout", ["3×8", "2×6"], "60-90 s", dict(core=1), 1, 0,
     "کمر نیفتد؛ دامنه را کم کن اگر لازم است."),
 ]),
 "C": dict(name="Workout C", fa="تمرین C: شکل بالاتنه و حجم Pull-up", day="Tue", ex=[
   X("c1", "highpull", "highpull", "highpull", "2-3 min", dict(back=1, bi=.5), 0, 0,
     "Band-Assisted High Pull-up تا زیر سینه، آرنج به سمت لگن."),
   X("c2", "pun", "pun", "negative", "2-3 min", dict(back=.5, bi=.5), 0, 0,
     "فرود ۴-۵ ثانیه. بپر یا از پله شروع کن."),
   X("c3", "incdb", "fepu", ["3×6-8", "2×6"], "60-90 s", dict(chest=1, delt=.5, tri=.5), 1, 1,
     "باشگاه: Incline Dumbbell Press. خانه: Weighted Feet-Elevated Push-up."),
   X("c4", "ohp", "pike", ["3×5-6", "2×5"], "60-90 s", dict(delt=1, tri=.5), 1, 1,
     "باشگاه: Standing Overhead Press. خانه: Deficit Pike Push-up."),
   X("c5", "chin", "chin", ["3×3-4", "2×3"], "60-90 s", dict(back=1, bi=1), 1, 1,
     "وزن بدن؛ ۱-۲ تکرار ذخیره. بعد از ۱۰ تکرار تمیز وزنه."),
   X("c6", "facepull", "facepull", ["3×12-15", "2×12"], "60-90 s", dict(delt=1, back=.5), 1, 0,
     "ابرست: Lateral Raise سپس Face Pull (کابل) یا Band Pull-Apart (خانه)."),
   X("c7", "hlr", "hlr", ["3×10", "2×8"], "60-90 s", dict(core=1), 1, 0,
     "بدون تاب."),
 ]),
 "D": dict(name="Workout D", fa="تمرین D: قدرت کل بدن", day="Thu", ex=[
   X("d1", "dl", "pistol", ["3×3 @80-85% 1RM", "2×3 light"], "3 min", dict(ham=1, glute=1, back=.5, quad=.5), 1, 1,
     "باشگاه: Deadlift (بر اساس ۱۵۰×۴ حدود ۱۳۵-۱۴۵ kg برای ۳ تکرار؛ روز ۱ بسنج). خانه: Box Pistol Squat (۴×۵ برای هر پا).",
     dose_home=["4×5 per leg", "2×3 light"]),
   X("d2", "apu", "bapu", "assist", "3 min", dict(back=1, bi=.5), 1, 0,
     "باشگاه: Assisted Pull-up. خانه: Band-Assisted Pull-up. کمک را هر هفته کم کن. تست Pull-up جمعه است."),
   X("d3", "adip", "tdip", ["3×6-8", "2×6"], "60-90 s", dict(chest=1, tri=.5, delt=.5), 1, 0,
     "فرود ۳ ثانیه‌ای. باشگاه: Assisted Dip. خانه: Tempo Dip (۳×۴-۶، دیلود ۲×۴).",
     dose_home=["3×4-6", "2×4"]),
   X("d4", "hollow", "hollow", "hollow", "60-90 s", dict(core=1), 0, 0,
     "کمر چسبیده به زمین."),
   X("d5", "farmer", "farmer", ["3×40 m", "-"], "60-90 s", dict(grip=1, core=.5), 0, 0,
     "در هفته‌ی دیلود حذف می‌شود. خانه: کوله‌پشتی یا کیسه‌ی سنگین."),
 ]),
 "E": dict(name="Workout E", fa="تمرین E: سبک، شانه و بازو و مرکز بدن", day="Fri", ex=[
   X("e1", "cablelat", "bandlat", ["3×15-20", "2×15"], "60 s", dict(delt=1), 1, 0, "پمپ سبک؛ ۲ تکرار ذخیره."),
   X("e2", "reardelt", "bandrear", ["3×12-15", "2×12"], "60 s", dict(delt=.5, back=.5), 1, 0, "باشگاه: Reverse Pec Deck. خانه: Band Reverse Fly."),
   X("e3", "inccurl", "bandcurl", ["3×10-12", "2×10"], "60 s", dict(bi=1), 1, 0, "باشگاه: Incline Dumbbell Curl. خانه: Band Curl."),
   X("e4", "pushdown", "bandtri", ["3×10-12", "2×10"], "60 s", dict(tri=1), 1, 0, "باشگاه: Triceps Rope Pushdown. خانه: Band Triceps Pushdown."),
   X("e5", "cablecrunch", "bpcrunch", ["3×12-15", "2×12"], "60 s", dict(core=1), 1, 0, "باشگاه: Cable Crunch. خانه: Backpack Crunch."),
   X("e6", "pallof", "pallof", ["3×10 per side", "2×8 per side"], "60 s", dict(core=.5), 1, 0, "کابل یا کش."),
 ]),
}

DAYS = ["Sat", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri"]
DAY_PLAN = {0: "A", 1: "B", 2: None, 3: "C", 4: None, 5: "D", 6: "E"}  # Sat..Fri

MUSCLE_FA = dict(back="پشت و لت", chest="سینه", delt="شانه", bi="جلو بازو", tri="پشت بازو",
                 quad="چهارسر", ham="همسترینگ", glute="باسن", calf="ساق", core="مرکز بدن", grip="گریپ")

NUTRITION = {
 "train":  dict(kcal=1900, p=200, f=60, c=140),
 "walk":   dict(kcal=1900, p=200, f=60, c=140),
 "refeed": dict(kcal=2500, p=180, f=55, c=320),
}


def dose_for(ex, week, home=False):
    d = ex["dose"]
    if home and ex.get("dose_home"):
        d = ex["dose_home"]
    if isinstance(d, str):
        return SCHEMES[d][week - 1]
    return d[1] if week in (4, 8) else d[0]


def sets_of(dose):
    import re
    m = re.match(r"(\d+)×", dose)
    return int(m.group(1)) if m else 0


def volume_table():
    """weekly hard sets per muscle for weeks 1..8 (gym version). Returns (rows, skill_back)."""
    rows = {k: [0.0] * 8 for k in MUSCLE_FA}
    for w in range(1, 9):
        for L, W in WORKOUTS.items():
            for ex in W["ex"]:
                if not ex["h"]:
                    continue
                s = sets_of(dose_for(ex, w))
                if L == "D" and ex["id"] == "d2" and w == 8:
                    s = 0
                for mu, f in ex["m"].items():
                    rows[mu][w - 1] += s * f
    return rows

# Persian professional names (shown with the English name on exercise pages)
FAN = dict(
    cars="چرخش کنترل‌شده‌ی مچ و شانه", bpa="باز کردن کش از جلو", scap="بارفیکس کتف", archhang="آویز فعال",
    pushup="شنا سوئدی", bench="پرس سینه هالتر", dbrow="زیربغل دمبل تک‌خم", bbrow="زیربغل هالتر خم",
    lat="نشر جانب دمبل", squat="اسکوات پشت با هالتر", bss="اسکوات بلغاری با وزنه", rdl="ددلیفت رومانیایی",
    slrdl="ددلیفت رومانیایی تک‌پا", lunge="لانج راه‌رونده", stepup="استپ‌آپ با وزنه", nordic="نوردیک همسترینگ (فاز منفی)",
    calf="ساق پا ایستاده", rollout="چرخ شکم", highpull="بارفیکس بلند با کش کمکی", incdb="پرس سینه بالا دمبل",
    fepu="شنا پا بالا با وزنه", ohp="پرس سرشانه ایستاده", pike="شنا پایک دفیسیت", facepull="نشر جانب + فیس‌پول (سوپرست)",
    hlr="بالا آوردن پا در حالت آویزان", dl="ددلیفت", pistol="پیستول اسکوات روی جعبه", hollow="نگه‌داشت هالو بادی",
    farmer="راه رفتن کشاورز", pullup="بارفیکس دست باز", dip="دیپ پارالل", deadhang="آویز مرده",
    pun="بارفیکس منفی", apu="بارفیکس با دستگاه کمکی", bapu="بارفیکس با کش کمکی", adip="دیپ با دستگاه کمکی (فاز منفی ۳ ثانیه)",
    tdip="دیپ تمپو (فاز منفی ۳ ثانیه)", chin="بارفیکس دست جمع", cablelat="نشر جانب سیم‌کش", bandlat="نشر جانب با کش",
    reardelt="فلای معکوس (دلتوئید خلفی)", bandrear="فلای معکوس با کش", inccurl="جلو بازو دمبل روی نیمکت شیب‌دار",
    bandcurl="جلو بازو با کش", pushdown="پشت بازو سیم‌کش با طناب", bandtri="پشت بازو با کش", cablecrunch="کرانچ سیم‌کش",
    bpcrunch="کرانچ با کوله‌پشتی", pallof="پرس پالوف (ضدچرخش)",
)

# Workout group pages: goal + principles
WORKOUT_INFO = {
 "A": dict(goal="قدرت بالاتنه با بار سنگین؛ سیگنال اصلی حفظ عضله‌ی پشت، سینه و بازو در کسری کالری، و ستون پیشرفت Pull-up.",
           rules=["اول سنگین‌ترین حرکت (Pull-up و Bench/Dip) با بدن تازه، بعد حرکت‌های فرعی.",
                  "ست‌های اصلی ۳ دقیقه استراحت، فرعی ۶۰ تا ۹۰ ثانیه.",
                  "Pull-up با وزن بدن: هر ست ۲ تکرار کمتر از حداکثر؛ وقتی همه تمیز بود هفته بعد تکرار اضافه کن.",
                  "Dead Hang آخر جلسه برای گریپ و سلامت شانه."], time="۶۰ تا ۷۰ دقیقه"),
 "B": dict(goal="قدرت پایین‌تنه: یک حرکت سنگین اسکوات، یک هینج، کار تک‌پا، همسترینگ فاز منفی، ساق و مرکز بدن.",
           rules=["اسکوات سنگین اول، با گرم کردن پله‌ای (۴ تا ۵ ست سبک تا وزنه‌ی کار).",
                  "بین ست‌های پا آهسته راه برو، ثابت نایست (به‌خاطر سابقه‌ی سرگیجه).",
                  "Nordic را آهسته (۳ تا ۵ ثانیه) پایین بیا؛ وقتی کنترل رفت، با دست زمین را بگیر.",
                  "هرگز ناشتا؛ ۱٫۵ تا ۲ ساعت بعد از وعده با کربوهیدرات و نمک."], time="۶۰ تا ۷۵ دقیقه"),
 "C": dict(goal="شکل بالاتنه و حجم Pull-up: کشش‌های کمکی و منفی، پرس بالاسینه، پرس سرشانه، Chin-up و کار شانه‌ی جانبی.",
           rules=["High Pull-up و Negative را با کیفیت و بدون خستگی انجام بده؛ اینها تمرین مهارت‌اند.",
                  "Negative: ۴ تا ۵ ثانیه پایین بیا، از پله یا پرش بالا برو.",
                  "پرس‌ها ۱ تا ۲ تکرار ذخیره؛ سینه‌ی بالا و شانه برای فرم V.",
                  "ابرست شانه‌ی جانبی و پشت شانه با استراحت کوتاه."], time="۶۰ تا ۷۰ دقیقه"),
 "D": dict(goal="قدرت کل بدن: ددلیفت سنگین، حجم Pull-up با کمک، Dip با فاز منفی، ثبات تنه و گریپ.",
           rules=["ددلیفت ۸۰ تا ۸۵٪ 1RM فعلی با ۳ تکرار؛ کمر خنثی، هر تکرار ریست روی زمین.",
                  "Assisted Pull-up: کمک را هر هفته کم کن تا به Pull-up کامل برسی.",
                  "Dip با فرود ۳ ثانیه‌ای برای قدرت در پایین حرکت.",
                  "Hollow و Farmer's Carry آخر جلسه."], time="۶۰ تا ۷۰ دقیقه"),
 "E": dict(goal="جلسه‌ی سبک: شانه‌ی جانبی و پشت شانه، بازو و مرکز بدن برای فرم، با خستگی کم تا شنبه تازه باشی.",
           rules=["همه‌ی ست‌ها RPE ۷ تا ۸؛ پمپ، نه ناتوانی.",
                  "استراحت ۶۰ ثانیه.",
                  "اگر هفته سنگین بوده، یک ست از هر حرکت کم کن.",
                  "بعد از جلسه پیاده‌روی ۶۰ تا ۹۰ دقیقه."], time="۴۰ تا ۵۰ دقیقه"),
}

# Food database: per 100 g unless unit given (unit = grams per piece/serving). USDA-style approximations.
FOODS = [
 # id, Persian name, English, kcal, P, C, F, unit_name, unit_g
 ("chk", "سینه مرغ پخته", "Chicken breast, cooked", 165, 31, 0, 3.6, None, 0),
 ("tuna", "تن ماهی در آب (آبکش‌شده)", "Tuna in water, drained", 116, 25.5, 0, 0.8, None, 0),
 ("salmon", "سالمون پخته", "Salmon, cooked", 206, 22, 0, 12, None, 0),
 ("steak", "استیک گوساله لخم پخته", "Beef steak, lean, cooked", 200, 29, 0, 9, None, 0),
 ("lamb", "گوشت چرخ‌کرده بره پخته", "Ground lamb, cooked", 283, 25, 0, 20, None, 0),
 ("eggw", "سفیده تخم‌مرغ", "Egg white", 52, 10.9, 0.7, 0.2, "عدد", 33),
 ("eggy", "زرده تخم‌مرغ", "Egg yolk", 322, 15.9, 3.6, 26.5, "عدد", 17),
 ("egg", "تخم‌مرغ کامل", "Whole egg", 143, 12.6, 0.7, 9.5, "عدد", 50),
 ("yog", "ماست یونانی ۰٪", "Greek yogurt 0%", 59, 10.2, 3.6, 0.4, None, 0),
 ("shake", "شیک پروتئین آماده (۳۲۵ ml)", "Protein shake RTD 325 ml", 160, 30, 6, 2, "بطری", 0),
 ("whey", "ON Whey Gold Standard (۱ اسکوپ)", "ON Gold Standard Whey, 1 scoop", 120, 24, 3, 1, "اسکوپ", 0),
 ("iso", "ON Isolate (۱ اسکوپ)", "ON Gold Standard Isolate, 1 scoop", 110, 25, 1, 0.5, "اسکوپ", 0),
 ("rice", "برنج سفید پخته", "White rice, cooked", 130, 2.7, 28, 0.3, None, 0),
 ("pasta", "ماکارونی پخته", "Pasta, cooked", 158, 5.8, 31, 0.9, None, 0),
 ("potato", "سیب‌زمینی ایرفرایر (بدون روغن)", "Potato, air-fried", 93, 2.5, 21, 0.1, None, 0),
 ("mush", "قارچ", "Mushroom", 22, 3.1, 3.3, 0.3, None, 0),
 ("edam", "سویای سبز (Edamame)", "Edamame", 121, 11.9, 8.9, 5.2, None, 0),
 ("soy", "گوشت سویا (خشک)", "Textured soy protein, dry", 330, 51, 33, 1, None, 0),
 ("avo", "آووکادو", "Avocado", 160, 2, 8.5, 14.7, None, 0),
 ("alm", "بادام", "Almonds", 579, 21, 22, 50, None, 0),
 ("olive", "روغن زیتون (۱ قاشق غذاخوری)", "Olive oil, 1 tbsp", 119, 0, 0, 13.5, "قاشق", 0),
 ("spray", "اسپری روغن آووکادو (۱ ثانیه)", "Avocado oil spray, 1 s", 2, 0, 0, 0.25, "ثانیه", 0),
 ("banana", "موز", "Banana", 89, 1.1, 23, 0.3, "عدد متوسط", 118),
 ("apple", "سیب", "Apple", 52, 0.3, 14, 0.2, "عدد متوسط", 182),
 ("veg", "سالاد / سبزی", "Salad vegetables", 20, 1.5, 3.5, 0.2, None, 0),
]

# Starting load model: lib id -> (kind, estimated 1RM). Kinds: bar (barbell total), db (per dumbbell),
# cable / machine (stack), bw (bodyweight + added; 1RM is effective incl. bodyweight), assist (assisted machine,
# 1RM of the bodyweight version), carry (fixed load per hand). Squat/deadlift from the reported 150 kg × 4;
# pull-ups from 4-5 strict reps, dips from ~7; the rest are conservative estimates to confirm in week 1.
LOAD = {
    "squat": ("bar", 170), "dl": ("bar", 170), "bench": ("bar", 95), "bbrow": ("bar", 85), "ohp": ("bar", 60),
    "rdl": ("bar", 120), "lunge": ("db", 24), "dbrow": ("db", 40), "incdb": ("db", 34), "lat": ("db", 12),
    "inccurl": ("db", 16), "facepull": ("cable", 30), "cablelat": ("cable", 10), "pushdown": ("cable", 45),
    "cablecrunch": ("cable", 70), "pallof": ("cable", 25), "reardelt": ("machine", 50), "calf": ("machine", 140),
    "farmer": ("carry", 30), "pullup": ("bw", 104), "chin": ("bw", 107), "dip": ("bw", 110),
    "apu": ("assist", 104), "adip": ("assist", 110),
}
