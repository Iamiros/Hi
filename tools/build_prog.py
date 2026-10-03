import json, pathlib, program as P
root = pathlib.Path(__file__).resolve().parent.parent
lib = {e["id"]: {k: e[k] for k in ("en", "fa", "cues", "mistakes", "reg", "prog", "yt")} for e in P.LIB}
for k, v in lib.items(): v["fan"] = P.FAN.get(k, "")
foods = [dict(id=f[0], n=f[1], en=f[2], k=f[3], p=f[4], c=f[5], f=f[6], u=f[7], ug=f[8]) for f in P.FOODS]
prog = dict(schemes=P.SCHEMES, phases=P.PHASES, warmup=P.WARMUP, nutrition=P.NUTRITION, lib=lib,
            workouts={k: dict(fa=v["fa"], ex=v["ex"], info=P.WORKOUT_INFO[k]) for k, v in P.WORKOUTS.items()}, muscles=P.MUSCLE_FA, foods=foods)
