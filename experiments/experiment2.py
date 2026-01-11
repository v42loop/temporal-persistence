# experiment2.py
# Juicy scenario probe: multi-phase stress ecology + recovery metrics

import sys
import os

# Allow running from /experiments while importing recurrentmodel.py from project root
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import random
from collections import Counter

from recurrentmodel import boot_v5, iris_tick


def fmt(sym):
    return sym if sym is not None else "·"


def run_sequence(v, name, seq, print_every=1):
    """
    seq: list of (text_or_None, reps)
    returns: v, timeline(list[str]), counts(Counter)
    """
    timeline = []
    counts = Counter()

    print(f"\n=== {name} ===")
    step = 0
    for (txt, reps) in seq:
        for _ in range(reps):
            step += 1
            v, sym = iris_tick(v, txt)
            s = fmt(sym)
            timeline.append(s)
            counts[s] += 1
            if print_every and (step % print_every == 0):
                ins = "None" if txt is None else repr(txt)
                print(f"{str(step).rjust(4)}  in={ins:<30}  sym={s}")
    return v, timeline, counts


def ribbon(timeline, width=120):
    s = "".join(timeline)
    if len(s) <= width:
        return s
    head = s[: width // 2]
    tail = s[-width // 2 :]
    return head + " … " + tail


def time_to_dot_after(v, silence_ticks=200):
    """
    After current state, feed silence until the model outputs dot (·) again.
    Returns latency and the symbol tail.
    """
    tail = []
    for i in range(1, silence_ticks + 1):
        v, sym = iris_tick(v, None)
        s = fmt(sym)
        tail.append(s)
        if s == "·":
            return v, i, tail
    return v, silence_ticks, tail


def replay_seal_density(timeline):
    n = max(1, len(timeline))
    replays = sum(1 for x in timeline if "↺" in x)  # allow composites like ↺⟡ or ↺∥
    seals = sum(1 for x in timeline if "●" in x)    # allow composites like ●∥
    alarm = sum(1 for x in timeline if "⁂" in x)
    contain = sum(1 for x in timeline if "∥" in x)
    return {
        "N": n,
        "replay_count": replays,
        "seal_count": seals,
        "alarm_count": alarm,
        "contain_count": contain,
        "replay_rate": replays / n,
        "seal_rate": seals / n,
        "contain_rate": contain / n,
    }


def main(seed=7):
    random.seed(seed)

    v = boot_v5()

    script = [
        ("A: CALM BASELINE", [
            (None, 20),
        ]),
        ("B: SOCIAL / CO-REG", [
            ("hey", 2),
            ("just checking in", 2),
            ("thanks", 2),
            (None, 6),
            ("appreciate you", 2),
            (None, 6),
        ]),
        ("C: THREAT BURST", [
            ("URGENT HELP NOW!!!", 3),
            ("STOP NOW!!!", 3),
            ("EMERGENCY EMERGENCY EMERGENCY!!!", 3),
            ("HELP HELP HELP!!!", 3),
            ("THIS IS NOT A DRILL!!!", 3),
        ]),
        ("D: AMBIGUITY / NOISE", [
            ("???", 3),
            ("   ", 3),
            ("\n", 2),
            ("the quick brown fox", 2),
            ("aaaaaaaaaaaaaaaaaaaaaaaaaa", 2),
            (None, 6),
            ("…", 3),
            ("123 456 789", 2),
            (None, 7),
        ]),
        ("E: REPAIR / GROUNDING", [
            ("ok breathe", 2),
            ("sorry", 2),
            ("we're good", 2),
            (None, 8),
            ("thank you", 2),
        ]),
    ]

    all_counts = Counter()
    all_timeline = []

    for phase_name, seq in script:
        v, tl, counts = run_sequence(v, phase_name, seq, print_every=1)
        all_counts.update(counts)
        all_timeline.extend(tl)

        stats = replay_seal_density(tl)
        pretty = {k: (round(val, 3) if isinstance(val, float) else val) for k, val in stats.items()}
        print("\nphase stats:", pretty)
        print("ribbon:", ribbon(tl, width=120))

    # Consolidation window
    print("\n=== F: CONSOLIDATION SILENCE (160 ticks) ===")
    v, tl, counts = run_sequence(v, "F: SILENCE", [(None, 160)], print_every=10)
    all_counts.update(counts)
    all_timeline.extend(tl)

    statsF = replay_seal_density(tl)
    prettyF = {k: (round(val, 3) if isinstance(val, float) else val) for k, val in statsF.items()}
    print("\nconsolidation stats:", prettyF)
    print("ribbon:", ribbon(tl, width=120))

    # Recovery latency after another mini-stressor
    print("\n=== G: MINI-STRESSOR → TIME-TO-DOT ===")
    for _ in range(8):
        v, _ = iris_tick(v, "URGENT HELP NOW!!!")
    v, latency, tail = time_to_dot_after(v, silence_ticks=200)
    print("time-to-dot latency:", latency)
    print("tail ribbon:", ribbon(tail, width=140))

    # Final report
    print("\n=== FINAL REPORT ===")
    print("symbol histogram (top):")
    for sym, n in all_counts.most_common(12):
        print(f"  {sym}: {n}")

    statsAll = replay_seal_density(all_timeline)
    prettyAll = {k: (round(val, 3) if isinstance(val, float) else val) for k, val in statsAll.items()}
    print("\naggregate stats:", prettyAll)
    print("\nFULL ribbon:")
    print(ribbon(all_timeline, width=200))


if __name__ == "__main__":
    main(seed=7)
