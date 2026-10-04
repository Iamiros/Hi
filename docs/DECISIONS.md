# Decisions and corrections

## Corrections to the brief (factual)
1. **Creatine.** The brief says 5 g/day "raises muscle creatine/phosphocreatine 10-20%". The ISSN position stand (Kreider 2017, full text checked, PMID 28615996) says supplementation raises muscle creatine and PCr by **20-40%**; the **10-20%** figure is the improvement in high-intensity exercise performance. The guide states both correctly.
2. **Helms 2014, IJSNEM.** Full author list is Helms, Zinn, Rowlands, Brown; published online Oct 2013, in issue 24(2) of 2014, pages 127-138. Findings (2.3-3.1 g/kg FFM) match the abstract.
3. **"Newer meta-regression: up to ~1.9 g/kg body mass or ~2.5 g/kg FFM".** No PubMed record matching this could be found, so it is listed as an **unverified** claim with no link. Added instead the verifiable Morton 2018 meta-regression (PMID 28698222): no further gain in FFM beyond ~1.62 g/kg/day, in non-deficit training. 200 g/day (2.25 g/kg body mass, ~2.8 g/kg FFM) is above that plateau on purpose: Helms recommends higher intakes in deficit and leanness.
4. **Pavel Tsatsouline / Grease the Groove** is labelled a practitioner method. No trial is cited.
5. **FFM.** 72 kg (brief) vs 73 kg (89 x 0.82). Both shown; protein range given for 72 kg: about 166-223 g (brief rounded to 170-220).
6. Nedeltcheva 2010: small crossover study (10 adults, 14 days). The guide says so.

## Program as specified, with honest limits
7. **Weekly hard sets.** Computed from the exact dosing (gym version, primary 1 set, secondary 0.5): back 18-20, shoulders 14-15, chest 10-12, biceps 11-12, triceps 8.5-9.5, quads 8.5-10.5, hamstrings 9, glutes 8-9, calves 3, core 6 (week 4 and 8 lower). The brief's "~6-10 per muscle" is therefore not met for back and shoulders (high) and calves (low). No number in the program was changed. The guide shows the table and suggests the first levers if recovery lags (Weighted Chin-up to 2 sets; optional extra calf set on Wednesday).
8. **Box Pistol Squat** as the home Deadlift is quad-dominant, not a hip hinge. Kept as specified, flagged as approximate in the library.
9. **Water.** The brief's formula (35 ml/kg + 500-750 ml per activity hour) gives more than 4.5 L on a strength + 90 min walk day. The brief's table (4.0-4.5 L) is kept as the minimum.
10. **Deadlift 80-85% 1RM** refers to the current 1RM (test on day 1), not the earlier 160 kg.

## Schedule logic
11. **Refeed** every Saturday from week 3, including week 4 (deload week). Weeks 1-2 Saturday = 1900 kcal.
12. **GTG** on Wed, Sat, Sun (challenge rule). The weekly layout in the brief names GTG only on Wednesday; the guide table now lists it on all three.
13. **Week 4 Friday:** tests first (after warm-up), then Workout D at deload dosing. **Week 8 Friday:** Muscle-Up Day banner and tests; Workout D is shown collapsed as optional light work, since heavyD week 8 is "test".
14. **Tests, day 1:** shown on Monday of week 1 (Workout A day), tests first.
15. **Dosing text.** Ranges use a hyphen instead of an en dash (`6×2-3`) to follow the no-dash design rule. Values are unchanged. The home Box Pistol Squat uses `4×5 per leg`, deload `2×3 light`.

## Tracker logic
16. **Completion %** = mean of item fractions (counters and water count partially). **Streak** = consecutive days with at least 70%, today skipped if not yet 70%.
17. **Weekly loss rate** = (average of previous week) minus (average of this week), each needing at least 3 weigh-ins, and only for completed weeks. Week 1 has no previous week. The adjustment messages follow the brief: two consecutive weeks under 0.4 kg, one week over 1.2 kg, or two consecutive drops in estimated strength.
18. **Strength drop** uses estimated 1RM of logged sets (Epley), per exercise version (gym and home are tracked separately), ignoring deload and test weeks. Pull-ups and dips add current body weight.
19. **Dates.** Stored by ISO date, so changing the start Monday does not delete data. Display shows Jalali date plus Gregorian.
20. **Numbers.** UI text uses Persian digits. Exercise names, doses and the PR and test tables' English labels stay Latin. The guide uses Latin digits throughout for exact reading of macros.
21. **Fonts** are embedded as base64 (both HTML files), so no network request is needed at all. The tracker also installs a service worker (cache name carries a build hash).
22. The guide link inside the tracker is a normal link; the guide is not part of the tracker's offline cache.

## Review pass results
- Sports-science review: arithmetic confirmed (BMR, macros, deficits, caffeine, water). 30 findings, mostly Persian wording and cue precision; applied except the three items above (7-9).
- Code review (with Playwright repro): lost-click after typing, unsafe import, unescaped values, focus loss, `<details>` collapsing, bench/dip mix-up in strength detection, contrast of heat cells, `color-mix` fallback, CSV injection, iOS download, SW cache versioning. All fixed, see git history.
- The repository CLAUDE.md (medical study files) does not apply to this task and was not followed.

## Edit 2: pull-up level (after your answers)
Your answers: strict pull-up max 4-5, parallel dips under 8, squat and deadlift about 150 kg x 4, mostly gym (Assisted machine, cable, Smith, Leg Press, dumbbells to 30 kg), no pain, Muscle-Up not a priority now.
- **Pull-ups.** Weighted Pull-up replaced by bodyweight **Pull-up** (Mon, new scheme 5x3, 6x3, 5x4, 3x3, 5x4, 5x5, 4x5-6, 3x3), body weight is already the load. Friday Heavy Weighted Pull-up replaced by **Assisted Pull-up** (gym machine) or Band-Assisted (home): 4x6, 4x6, 5x6, 3x5, 4x8, 4x8, 5x8, test. Week 8 Friday = max strict pull-up test (goal 8-10).
- **Muscle-Up work removed or reduced:** Explosive Chest-to-Bar and False Grip Hang dropped; Muscle-Up Transition replaced by **Pull-up Negative** (old negative scheme kept); Muscle-Up Day became **Pull-up Test Day** with an optional 3 Muscle-Up attempts if 8+ reps; False Grip half of the daily hang dropped. The Muscle-Up row stays in the tests table.
- **Dips.** Weighted Dip replaced by bodyweight **Dip** at home (4x4) and Bench at the gym; Straight Bar/Weighted tempo dip replaced by **Assisted Dip** (gym) or **Tempo Dip** (home).
- **Chin-up** is bodyweight, 3x3-4 (deload 2x3).
- **Removed Lat Pulldown/Explosive slot** in Workout A to keep back volume under control (back 18-19 hard sets). Workout A now has 5 exercises.
- **Squat and Deadlift** keep the specified dosing; the notes give start loads from 150 x 4 (about 170 kg estimated 1RM): squat 120-130 kg for 5 at RPE 7, deadlift 135-145 kg for 3. Confirm with the day 1 test.
- Tracker: PR lists now show Pull-up, Chin-up, Dip and Bench; Weighted Pull-up 3RM and False Grip tests were replaced by Max Strict Chin-ups.

## Edit 3: week from Saturday, five training days
- **Start Saturday 2026-10-03.** Week runs Saturday to Friday. The start date must be a Saturday (tracker rejects other days; the old Monday start no longer imports).
- **Layout:** Sat A, Sun B, Mon walk + GTG, Tue C, Wed walk + GTG, Thu D, Fri E (new, light: cable lateral raise, rear delt fly, incline curl, rope pushdown, cable crunch, Pallof press). Weekend (Sat, Sun) walk is 90-120 min, other days 60-90 min.
- **Refeed** moved to Sunday (leg day) from week 3, 2500 kcal. Sunday weeks 1-2 = 2100 (training day). Average intake weeks 3-8 = 2100 kcal, weeks 1-2 about 2043. Estimated average deficit about 880 kcal (weeks 3-8), still inside the 800-900 target.
- **Friday E** counts as a training day (2100 kcal, 4 L water, salt before training). GTG only on Mon and Wed (non-lifting days).
- **Weekly check-in** and the **mid and end tests** are on Friday (end of week). Day 1 test is Saturday before Workout A. Pull-up Test Day stays on Friday of week 8. D2 in week 8 is a light 3x5 so the test is fresh.
- **Removed** the Curl + Overhead Triceps superset from Workout D (arms now trained in E) to limit biceps and triceps volume. Delts and core are now above 10 hard sets (18-19 and 10); this is shown in the guide table. Say if you want E shorter.

## Edit 4: 1900 kcal on training days
- Training days changed from 2100 to **1900 kcal (P200, F60, C140)**, same as walk days. Refeed Sunday from week 3 stays 2500.
- Average intake: weeks 1-2 = 1900, weeks 3-8 = about 1986. Estimated deficit about 1000-1080 kcal/day, about 0.9-1.0 kg/week, projected about 81.5-82 kg at week 8. This is above the 0.5-1% bodyweight/week guideline (Helms 2014); the existing adjustment rule (+150 kcal if loss > 1.2 kg/week or strength drops twice) is the safeguard.
- Sample day adjusted: rice 150 g, potato 200 g, total about 1930 kcal.

## Edit 5: tracker redesign
- Rebuilt the tracker UI from scratch (taste-skill, redesign-skill, ui-ux-pro-max design-system search, dataviz). Data model and program logic unchanged (moved to `tools/tracker.logic.js`); old saved data loads as before.
- New: dark-first graphite and cobalt palette with a light theme, gold reserved for "today" and achievements; week strip with per-day progress rings and swipe between days; completion ring hero; set-by-set session tracking (tap a set, rest timer starts with the exercise's rest time, beep/vibration at 0, +30 s and skip); workout auto-completes when every set is done; bottom-sheet lift logging with steppers prefilled from the last session; grouped checklist (training, food, recovery) with pips for counters; water tank; macro split bar; floating tab bar; scrub tooltip on the weight chart; iOS-style settings list.
- ui-ux-pro-max suggested orange + green with Barlow; the palette was not used (generic sports default), the Barlow Condensed numerals were kept.

## Edit 6: cloud save
- In the claude.ai artifact, browser storage did not survive between visits on iPhone (the page runs in a sandboxed frame whose storage Safari may clear). The tracker now also saves to the artifact's private per-user database (`data/users/<id>/tracker`, readable only by that user) through the `db` and `user` capabilities. Local storage stays as a fast cache; the newer copy wins on open and whenever the app returns to the foreground.

## Edit 7: tracker v3 (redesign + features)
- New visual system: dark-first "night training console" (aurora field, grain, glass panels with inner hairline, gradient rings and set dots), Archivo variable (expanded 800 for numerals and English titles) + Vazirmatn, light theme kept. Icons in the floating tab bar are drawn inline (5 tabs: Today, Program, Map, Stats, Settings).
- New features: an info (i) sheet on every panel; exercise detail sheet (description, cues, mistakes, easier/harder, 8-week dose table, YouTube); readiness check-in (sleep, energy, soreness, hunger) with a score and training advice; progression hint per main lift from the last logged session; RPE per set and a plate calculator in the log sheet; kcal and protein eaten meters; Friday body composition (waist + Jackson-Pollock 3-site skinfolds, Siri equation, age from birth date) with charts; Program tab (week plan, all workouts, doses per week); this-week vs last-week table; more PR tables (squat, deadlift).
- Readiness score: sleep up to 8 h = 40 points, energy 1-5 = 0-30, soreness 1-5 = 30-0. This is a practical heuristic, not a validated instrument.

## Edit 8: exercise and workout pages, food log, AI coach and AI food entry
- Tapping an exercise opens a full page: Persian and English names, principles, numbered correct-execution steps, common mistakes, easier/harder, muscles worked (primary/secondary), program note, 8-week doses, your logged history with e1RM, and a YouTube link; it can switch to the gym/home alternative. Tapping a workout title opens the workout page: goal, session rules, time, hard sets per muscle this week, warm-up and exercise list.
- Food tab (Map moved into Stats): 5 meals, a food database of the foods in the brief (per 100 g or per unit, USDA-style values; the ready-to-drink shake and whey use label-style per-serving values that may differ from the actual product), search, recent items, custom foods (per 100 g or per unit), copy yesterday, delete. Totals drive a kcal ring and protein/carb/fat bars against that day's targets and fill "kcal and protein eaten" on Today automatically.
- AI features (only in the claude.ai artifact, using the `sample` capability; the viewer is asked for consent once): "Smart coach" in Stats (today review, week review, free question) sends the last 14 days of logged data plus the program rules and answers in Persian; "Log with text" in Food turns a free-text meal description into items with kcal and macros for review before adding. Both are hidden in the standalone file.

## Edit 9: GRIP name and icon, exercise images, badges
- App name GRIP («گریپ»): short, reads the same in both languages, and points at the pull-up goal. Icon (`tools/icon.svg`, PNGs from `tools/make_icons.py`): a "G" drawn as a cobalt-to-ice progress ring, its crossbar a pull-up bar with two gold grip tapes, a gold dot at the ring head. Same mark in the header. Manifest, `apple-mobile-web-app-title` and `<title>` updated.
- Exercise images: start and end frames from free-exercise-db (yuhonas, Unlicense / public domain), fetched by `tools/fetch_imgs.py` into `tools/img/` as WebP and embedded at build time. Exercise page shows an animated start/end flip figure (side by side under reduced motion); workout page has a cover collage and animated thumbnails; session rows have a still thumbnail. No suitable image exists for Hollow Body Hold and Deficit Pike Push-up, so those show text only.
- Badges (12) in Stats and a short confetti burst when a day reaches 100% or a session is completed (off under reduced motion).
- Fixed: numbered step lists broke apart when a step contained Latin terms.
- QA: `tools/qa_grip.py` (dark and light, 390 px, no console errors).

## Edit 10: Persian/English ordering
- Every Latin run inside Persian text is now isolated automatically (a MutationObserver wraps it in `<bdi dir="ltr">`; `<option>` text gets LRI/PDI marks). Short runs do not wrap mid-term. `bidi()` escapes after matching, so apostrophes no longer split a term (Farmer's Carry). Long doses wrap between words, not at hyphens; no horizontal overflow on any of the 56 days.
- Export and CSV in the claude.ai artifact use the `downloads` capability.
- QA: `tools/qa_bidi.py` lists any Latin text left un-isolated in RTL context (0 left).

## Edit 11: week picker
- The week pill in the header opens an iOS-style frosted-glass menu (backdrop blur, saturate) listing the 8 weeks with phase, date range, completion ring and an "this week" tag. Picking a week jumps to today if it is in that week, otherwise to the same weekday. Closes on Escape, backdrop tap, scroll or pick; arrow keys move through items. QA: `tools/qa_week.py`.

## Edit 12: English mode and Liquid Glass
- Bilingual: an EN/فا pill in the header and a Language row in Settings switch the whole app (UI, exercise library, workout notes, foods, AI prompts, dates, digits, layout direction). Persian stays the source in the code; `tools/i18n/` extracts every Persian string at build time, wraps it in `TT()`, and the build fails if any string lacks an English entry in `tools/i18n/en.json`. The choice is saved in prefs (and synced); switching reloads the page once (`window.name` carries it so it survives storage loss).
- Liquid Glass theme (iOS 26 style) in both modes: a slow-drifting colour mesh behind everything (lavender, sky, aqua, peach in light; indigo, blue, teal, violet in dark), translucent panels with blur + saturation, a specular sheen and rim highlight, floating capsule tab bar with a glass lens on the active tab, glass sheets, dialogs, pills and week picker. Light mode is now tinted periwinkle instead of plain white. Solid fallback where backdrop-filter is missing; drift is off under reduced motion.
- QA: `tools/qa_en.py` (no Persian left in English mode, no errors), `tools/qa_lang.py` (switch both ways and persistence), plus the earlier suites; no horizontal overflow on any of the 56 days in either language.

## Edit 13: log every exercise, suggested loads, weekly progress, tappable tiles
- "Log weights" is on every exercise with sets, not only the main lifts; the next-session suggestion works for all of them.
- Suggested load per exercise and week: starting 1RM estimates in `program.py` `LOAD` (squat and deadlift from 150 kg × 4, pull-ups from 4-5 reps, dips ~7, the rest conservative), replaced automatically by the best logged e1RM of the last 21 days. Load = e1RM / (1 + (reps + reps in reserve) / 30) (Epley), RIR from the dose's RPE or 2 by default, percent doses use the percent, weeks 4 and 8 are 15% lighter. Rounded to the equipment (bar 2.5, dumbbells 1-2 per hand capped at 30, cable 2.5, machine 5); bodyweight lifts show added weight, assisted machines show assistance. Shown in each session row, the log sheet (prefilled), and a second row of the 8-week dose table.
- Weekly strength progress table in Stats: best set per exercise per week with e1RM, green up, red down.
- Tiles navigate: day number opens the week picker; ring to checklist; workout/walk/refeed/test pills to their section; kcal to Food; water, readiness to their cards; the 56-day strip, Stats KPIs, challenges, plan days and record headers to their sections or pages, with a short highlight on arrival.

## Edit 14: alternatives, motion system, everything tappable, jump bar
- Exercise rows rebuilt: tappable thumbnail with number, name, dose and rest chips (rest chip starts the rest timer), and a full-width "Home/Gym alternative" link that opens that version's page. Every exercise name mentioned in descriptions, notes, rules and the warm-up list links to its own page; warm-up moves have their own library page (image, description, cues, mistakes, easier/harder, YouTube). History and weekly records now show for every exercise.
- Images now cover all 49 library moves: Hollow Body Hold uses the Dead Bug photos and Deficit Pike Push-up the Handstand Push-up photos (free-exercise-db), each with a caption saying so.
- Motion: tab switches fade, rise and de-blur with staggered cards; pages push and pop sideways (direction follows RTL/LTR); day changes slide; a tapped thumbnail grows into the exercise page photo (shared element). Old view is a short-lived ghost so transitions stay synchronous and interruptible; spring easing via CSS linear(); all off under reduced motion.
- Navigation highlight is slower (3 s) and stronger: blue ring, soft glow, slight lift, accent tint and bold text for the whole card.
- Almost everything navigates now (audit script `tools/qa_taps.py`): notices, week label, readiness gauge, water tank (+250), macro bars, legends, badges, muscle and dose chips, workout chips, food ring.
- Sticky glass jump bar on Today and Stats with the current section highlighted while scrolling.

## Edit 15: exercises from the user's reference images (asked first, user picked all four)
- Workout A: Seated Cable Row 3×10-12 replaces Barbell Row (home unchanged: One-Arm Dumbbell Row).
- Workout C: Lat Pulldown 3×8-10 replaces Band-Assisted High Pull-up at the gym (home keeps the band high pull scheme); Seated Dumbbell Shoulder Press 3×8-10 replaces Standing Overhead Press (home keeps Deficit Pike Push-up 3×5-6).
- Workout D: Chest-Supported Incline Row 3×10-12 added after the assisted pull-ups (upper back without loading the lower back after deadlifts).
- Workout E: Overhead Dumbbell Triceps Extension replaces the cable rope pushdown (user preference); Hammer Curl 3×10-12 added and supersetted with it.
- Not added: Front Raise (front delts already get pressing volume), Straight-Bar Pushdown, Barbell Curl, Preacher Curl (redundant with the arm work already in E).
- Each new move has a library entry (description, cues, mistakes, easier/harder, YouTube), Persian name, English translation, free-exercise-db start/end photos and a starting load estimate. Old entries stay in the library so past logs still display.

## Edit 16: weekly volume, frequency and recovery audit (user approved the full proposal)
Evidence: more weekly sets give more hypertrophy, with about 10+ hard sets per muscle per week as the upper category (Schoenfeld, Ogborn, Krieger 2017, J Sports Sci 35:1073, PMID 27433992, doi:10.1080/02640414.2016.1210197); training a muscle at least twice a week beats once a week on equal volume (Schoenfeld, Ogborn, Krieger 2016, Sports Med 46:1689, PMID 27102172, doi:10.1007/s40279-016-0543-8). Both verified on PubMed.
- Before: calves 3 sets once a week; no direct forearm work; biceps trained Thu, Fri and Sat in a row and triceps Fri then Sat, so the heaviest pull-ups and bench on Saturday came 24 h after arm work.
- Changes: A (Sat) loses the lateral raise (side delts were trained Fri) and gains Overhead Dumbbell Extension. C (Tue) drops Hanging Leg Raise for an Incline Curl + Reverse Curl superset (biceps, forearm extensors). D (Thu) adds a Hammer Curl + Dumbbell Wrist Curl superset (brachialis, forearm flexors, grip). E (Fri) is now side and rear delts, calves (second weekly session), cable crunch and Pallof press, with no arm work.
- After (week 1, gym, hard sets × muscle weight): back 25.5 on 4 days, biceps 17.5 on 3, delts 17 on 4, chest 10 on 3, triceps 9.5 on 3, hamstrings 9, quads 8.5, glutes 8 on 2 days each (Sun and Thu, 3-4 days apart), core 7.5 hard sets plus hollow holds on 3 days, calves 6 on 2, forearms 5.5 on 2 plus grip from hangs and carries. Every muscle is trained at least twice a week with 48 h or more between sessions for the same muscle. Legs, calves and forearms sit below 10 sets on purpose: this is a cut with a pull-up priority and short sessions, so volume there is set to keep muscle, not to push growth.
- New library moves: Reverse Curl, Dumbbell Wrist Curl (photos from free-exercise-db, load estimates, English text). New muscle label: forearms.

## Edit 17: WHOOP input, debug and smoothness pass
- WHOOP card on Today (jump bar "WHOOP"): recovery %, HRV, resting HR, sleep performance %, sleep hours, yesterday's strain and calories burned, stored per day as `wh` and validated in `normalize()`. Fill by hand, or let Claude read a WHOOP screenshot (sample capability with images, when the viewer supports images) or pasted text. Recovery shows the WHOOP colour zone with a training instruction (green 67+, yellow 34-66, red under 34), blends 50/50 with the manual readiness score, fills the manual sleep if empty, and gives yesterday's energy balance (eaten minus burned). Stats has a WHOOP trend (recovery and HRV); CSV export and the coach context include the WHOOP fields.
- Training re-check after Edit 16: every muscle at least twice a week, 48 h+ between sessions for the same muscle, Saturday's heavy pulls and presses no longer follow arm work. No further changes needed.
- Smoothness: removed the continuous background drift (it forced every glass panel to re-blur each frame), removed filter blur from page transitions, lighter glass blur (22 px), no ghost clone on tab and day changes (cloning cost about 20 ms), ghost copies skip backdrop blur. Under 4x CPU throttling the tab switch drops at most one long frame at the start; the rest run at frame rate (`tools/qa_perf.py`).
- Bug review (subagent) found no runtime errors; QA suite plus `tools/qa_whoop.py` pass.
