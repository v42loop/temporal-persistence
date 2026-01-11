# Temporal Persistence Model

A small recurrent model exploring state persistence, containment, extinction, and recovery over time.

The system is symbolic and deterministic, emphasizing temporal dynamics over language understanding or prediction. The code supports research, exploration, and educational inquiry into recurrent state behavior and temporal processing.

## Contents

- `recurrentmodel.py` — Core recurrent kernel defining the state machine and update rule
- `experiments/` — Behavioral probes demonstrating alarm entry, containment latch, extinction latency, consolidation rhythms, and resilience

## Experiments

- `experiment1.py` — Quick sanity check  
- `experiment2.py` — Multi-phase ecological probe  
- `experiment3.py` — Cold-start alarm, extinction, consolidation, resilience curve  

These experiments serve as observational probes. Interpretation, application, and extension remain the responsibility of the user.

## Running

From the project root:
```bash
python experiments/experiment1.py
python experiments/experiment2.py
python experiments/experiment3.py
```

Output appears directly in the console.

## Symbol Legend

- `·` idle  
- `∥` containment  
- `⊘` rupture  
- `⁂` alarm  
- `↺` replay  
- `●` seal  
- `♥` affect tag  

## Usage
```python
from recurrentmodel import boot_v5, iris_tick

v = boot_v5()
v, symbol = iris_tick(v, "input text")
```

## Notes

The model operates in discrete ticks. Symbols are emitted based on internal state transitions, not semantic content. Temporal structure emerges from recurrent dynamics, not linguistic processing.

## License

MIT License. See LICENSE file for details.