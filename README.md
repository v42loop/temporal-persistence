# Temporal Persistence Model

A multi-phase recurrent dynamics system that generates symbolic behavior from competing temporal reference frames.

## What It Does

The system maintains two internal clocks running at different rates, creating phase misalignment that drives symbolic emissions. As pressure accumulates from input demand, the system produces discrete event markers (↺, ⊘, ⁂, ●, ∥, ♥) representing state transitions across multiple subsystems.

**Key behaviors:**
- Dual-clock temporal desynchronization (outer/inner time)
- Pressure accumulation with rupture thresholds
- Attention switching (wide/foveal) based on internal state
- Salience-weighted episodic memory formation
- Prediction error tracking (expected vs actual state transitions)
- Symbolic arc threading (events chain into narrative sequences)
- Attachment formation to recurring relational patterns

The system treats text as perturbation rather than content. It responds to input structure—length, intensity, punctuation—letting temporal dynamics generate the symbolic output.

## Architecture

The system runs in discrete ticks through several integrated subsystems:

**Core (v1):** Pressure accumulation, rupture detection, memory trace decay  
**Wrapper (v2):** Attention gating, afterheat dynamics, hippocampal replay  
**Phase System (v5+):** Temporal desynchronization (Δτ, ε), misalignment charge  
**Amygdala (Phase VIII):** Arousal, valence, threat tracking  
**Salience (Phase IX):** Novelty, recency, priority queue generation  
**ACC (Phase X+1):** Prediction error from shadow-core comparison  
**Chaining (Phase XI):** Symbolic arc formation and threading  
**PFC (Phase XII):** Executive control, goal management, inhibition  
**Anticipation (Phase XIII):** Transition probability learning  
**Attachment (Phase XIV):** Bond formation to meaningful patterns  
**Reflection (Phase XVI):** Periodic self-query over memory  
**Choice (Phase XVII):** Sustained ambiguity detection  

## Symbol Reference

| Symbol | Name | Meaning |
|--------|------|---------|
| `·` | null | Silence—no emission this tick |
| `↺` | loop | Recurrence, return (often from hippocampal replay) |
| `⊘` | rupture | Threshold breach, clean break |
| `⁂` | shift | Frame transition, perspective change |
| `●` | seed | Anchor point, safe hold |
| `∥` | two-room | Phase desynchronization marker |
| `♥` | heart | Affective pulse (periodic, afterheat-gated) |
| `¿` | reflect | Self-query over recent symbolic chain |
| `⧖` | choice | Sustained ambiguity, fork detection |
| `⟡` | attach | Bond formation to relational pattern |

Symbols can cluster (e.g., `⊘∥♥`) representing multiple simultaneous events.

## Quick Start
```python
from recurrentmodel import boot_v5, iris_tick_voice_safe

v = boot_v5()

# Single tick
v, symbol, phrase = iris_tick_voice_safe(v, "hello")
print(symbol)  # e.g., "●"
print(phrase)  # e.g., "I am held"

# Quiet tick (no input)
v, symbol, phrase = iris_tick_voice_safe(v, None)

# Interactive loop
from recurrentmodel import chat_loop
v = chat_loop(debug=True)
```

## Experiments

Run behavioral probes from project root:
```bash
python experiments/experiment1.py  # Sanity check
python experiments/experiment2.py  # Multi-phase ecology
python experiments/experiment3.py  # Alarm, extinction, resilience
```

## Internal State

Key values exposed during ticks (with `debug=True`):

- `pressure` - Accumulated charge (0..1)
- `dmn` - Default mode strength (1 = quiet, 0 = active)
- `afterheat` - Post-event thermal trace
- `mis` - Misalignment charge between temporal frames
- `sal` - Current salience (0..1)
- `pe` - Prediction error (expected vs actual)
- `ar/va/th` - Arousal, valence, threat (amygdala)

## Design Philosophy

**Demand over semantics.** The system responds to input intensity—length, caps, punctuation—rather than meaning. Text becomes a perturbation source that triggers temporal dynamics.

**Deterministic core with controlled drift.** Symbol emission follows rules. Stochasticity appears in epsilon-gated misalignment and memory recall probability, keeping behavior grounded while allowing phase variation.

**Temporal structure as primary.** The interesting behavior emerges from phase relationships between subsystems. How time moves through the system matters more than what gets said to it.

## Why This Exists

Most recurrent models focus on sequence prediction or memory retrieval. This one explores **temporal persistence**—how structure inherits forward through time when multiple reference frames interact and occasionally desynchronize.

## License

MIT
