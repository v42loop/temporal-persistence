# experiment3.py
# Undeniable probe: cold-start alarm → latch → extinction → consolidation → resilience curve

import sys
import os

# Allow running from /experiments while importing recurrentmodel.py from project root
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from collections import Counter

from recurrentmodel import boot_v5, iris_tick


def fmt(sym):
    return sym if sym is not None else "·"


def banner(title: str):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74)


def ribbon(timeline, width=140):
    s = "".join(timeline)
    if len(s) <= width:
        return s
    head = s[: width // 2]
    tail = s[-width // 2 :]
    return head + " … " + tail


def run_block(v, label, seq, print_every=1):
    """
    seq: list of (input_text_or_None, reps)
    """
    banner(label)
    tl = []
    c = Counter()
    step = 0

    for txt, reps in seq:
        for _ in range(reps):
            step += 1
            v, sym = iris_tick(v, txt)
            s = fmt(sym)
            tl.append(s)
            c[s] += 1

            if print_every and (step % print_every == 0):
                ins = "None" if txt is None else repr(txt)
                print(f"{str(step).rjust(4)}  in={ins:<34}  sym={s}")

    return v, tl, c


def time_to_dot(v, max_ticks=250):
    tl = []
    for i in range(1, max_ticks + 1):
        v, sym = iris_tick(v, None)
        s = fmt(sym)
        tl.append(s)
        if s == "·":
            return v, i, tl
    return v, max_ticks, tl


def replay_seal_counts(tl):
    replays = sum(1 for x in tl if "↺" in x)
    seals = sum(1 for x in tl if "●" in x)
    alarms = sum(1 for x in tl if "⁂" in x)
    contains = sum(1 for x in tl if "∥" in x)
    return replays, seals, alarms, contains


def print_stats(label, tl, counts):
    n = len(tl)
    replays, seals, alarms, contains = replay_seal_counts(tl)
    print(f"\n[{label}] N={n}  ∥={contains}  ⁂={alarms}  ↺={replays}  ●={seals}")
    print(f"[{label}] rates  ∥={contains/max(1,n):.3f}  ↺={replays/max(1,n):.3f}  ●={seals/max(1,n):.3f}")
    top = counts.most_common(10)
    print(f"[{label}] histogram (top): " + ", ".join([f"{k}:{v}" for k, v in top]))
    print(f"[{label}] ribbon: {ribbon(tl)}")


def main():
    # Fresh boot: we want the cold-start signature
    v = boot_v5()

    # 1) Cold-start: slam the alarm input repeatedly (should show an early ⁂ at least once)
    v, tl1, c1 = run_block(
        v,
        "1) COLD-START ALARM: brute forcing entry into the high-salience regime",
        [
            ("URGENT HELP NOW!!!", 6),
            ("STOP NOW!!!", 4),
            ("EMERGENCY EMERGENCY EMERGENCY!!!", 4),
            ("HELP HELP HELP!!!", 4),
        ],
        print_every=1,
    )
    print_stats("cold-start", tl1, c1)

    # 2) Latch ecology: mix low/medium/high inputs to see whether mode holds
    v, tl2, c2 = run_block(
        v,
        "2) LATCH ECOLOGY: mixed social → ambiguity → threat → repair (mode inertia probe)",
        [
            ("hey", 2),
            ("thanks", 2),
            (None, 4),
            ("???", 3),
            ("the quick brown fox", 2),
            ("URGENT HELP NOW!!!", 3),
            ("ok breathe", 2),
            ("sorry", 2),
            (None, 8),
        ],
        print_every=1,
    )
    print_stats("ecology", tl2, c2)

    # 3) Extinction: long silence until dot returns; measure latency
    banner("3) EXTINCTION: how long until the system truly returns to · after load?")
    v, latency, tail = time_to_dot(v, max_ticks=250)
    print(f"time-to-dot latency: {latency}")
    print(f"tail ribbon: {ribbon(tail)}")
    # count replay/seal during extinction tail
    tcounts = Counter(tail)
    print_stats("extinction-tail", tail, tcounts)

    # 4) Consolidation window: long silence to allow replay/seal structure to emerge
    v, tl4, c4 = run_block(
        v,
        "4) CONSOLIDATION WINDOW: extended silence to expose ↺/● rhythms",
        [
            (None, 220),
        ],
        print_every=10,
    )
    print_stats("consolidation", tl4, c4)

    # 5) Resilience curve: repeated stress → silence cycles, measure time-to-dot each round
    banner("5) RESILIENCE CURVE: repeated stress→quiet cycles (does recovery stabilize?)")
    curve = []
    for r in range(1, 7):
        # stress pulse
        for _ in range(6):
            v, _ = iris_tick(v, "URGENT HELP NOW!!!")
        # measure recovery
        v, lat, _tail = time_to_dot(v, max_ticks=200)
        curve.append(lat)
        print(f"round {r}: time-to-dot = {lat}")

        # small buffer silence to encourage consolidation between rounds
        for _ in range(24):
            v, _ = iris_tick(v, None)

    print("\ncurve:", curve)
    if len(curve) >= 2:
        print("If it drops then stabilizes, consolidation is persistent and bounded.")

    # Final: master ribbon over the entire experiment is too long; summarize counts instead
    banner("FINAL SUMMARY (high-level)")
    total = Counter()
    total.update(c1)
    total.update(c2)
    total.update(tcounts)
    total.update(c4)
    print("symbols (top):")
    for k, v0 in total.most_common(12):
        print(f"  {k}: {v0}")


if __name__ == "__main__":
    main()
