#  Evolving Agent Ecosystem

> **Open-ended evolutionary simulation** — agents compete, communicate, adapt, and die in a dynamic resource-constrained world.

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue?logo=python&logoColor=white)](https://python.org)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Repo](https://img.shields.io/badge/repo-NullLabTests%2Fevolving__agent__ecosystem-8A2BE2?logo=github)](https://github.com/NullLabTests/evolving_agent_ecosystem)
[![Status](https://img.shields.io/badge/status-experimental-orange)]()

---

##  Concept

Each agent is defined by a **3-dimensional genome** (`explore`, `cooperate`, `risk`) and lives in a shared world with:

- **  Dynamic environment** — sinusoidal resource cycles with noise
- **  Resource competition** — limited pool divided by competitive fitness
- **  Memory influence** — past resource trends modulate behavior
- **  Peer communication** — risk signals propagate through the population
- **  Selection pressure** — metabolism costs, starvation death, probabilistic reproduction
- **  Mutation** — genome drifts ±0.15 per generation

The result: **boom-bust population cycles**, **strategy divergence**, and **emergent signaling**.

---

##  Architecture

```
┌──────────────────────────────────────────────────────────┐
│                      ECOSYSTEM                           │
│  ┌─────────────┐  ┌──────────────┐  ┌────────────────┐  │
│  │ ENVIRONMENT │  │   MEMORY     │  │   EVOLVER      │  │
│  │ • sine wave │  │ • stores     │  │ • selection    │  │
│  │ • pop feed- │  │   tick data  │  │ • reproduction │  │
│  │   back      │  │ • resource   │  │ • mutation     │  │
│  │ • noise     │  │   trend()    │  │ • capping      │  │
│  └──────┬──────┘  └──────┬───────┘  └───────┬────────┘  │
│         │                │                  │           │
│         ▼                ▼                  ▼           │
│  ┌──────────────────────────────────────────────────┐   │
│  │                   AGENTS (N)                     │   │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐         │   │
│  │  │ Agent 0  │ │ Agent 1  │ │ Agent 2  │  ...    │   │
│  │  │ genome:  │ │ genome:  │ │ genome:  │         │   │
│  │  │ E,C,R    │ │ E,C,R    │ │ E,C,R    │         │   │
│  │  │ energy   │ │ energy   │ │ energy   │         │   │
│  │  │ message  │ │ message  │ │ message  │         │   │
│  │  └──────────┘ └──────────┘ └──────────┘         │   │
│  └──────────────────────────────────────────────────┘   │
│         │                                                │
│         ▼                                                │
│  ┌──────────────────────────────────────────────────┐   │
│  │              PER-TICK FLOW                       │   │
│  │                                                  │   │
│  │  1. Compute total resource (env + pop feedback)  │   │
│  │  2. Parse peer risk messages from last tick      │   │
│  │  3. Compute competitive weights per agent        │   │
│  │     (explore × risk × peer influence via         │   │
│  │      cooperate gene)                             │   │
│  │  4. Distribute resource shares → agents act      │   │
│  │  5. Remove dead agents (energy ≤ 0)              │   │
│  │  6. Evolve: select, reproduce, mutate            │   │
│  │  7. Store tick in shared memory                  │   │
│  │  8. Log metrics                                  │   │
│  └──────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────┘
```

---

##  Quick Start

```bash
git clone https://github.com/NullLabTests/evolving_agent_ecosystem.git
cd evolving_agent_ecosystem
python3 -m venv .venv
source .venv/bin/activate
python main.py
```

No dependencies required — pure Python standard library only.

---

##  Run

```bash
source .venv/bin/activate
python main.py
```

**Sample output:**

```
==========================================================
  EVOLVING AGENT ECOSYSTEM
  Open-ended evolutionary simulation
==========================================================
[tick  10] pop= 9 explore_var=0.0038 msg_ent=0.860 mean_en=0.590 deaths=0
[tick  20] pop= 3 explore_var=0.0010 msg_ent=1.000 mean_en=0.827 deaths=2
[tick  30] pop= 2 explore_var=0.0466 msg_ent=1.000 mean_en=0.462 deaths=2
[tick  40] pop= 5 explore_var=0.0100 msg_ent=0.590 mean_en=0.789 deaths=4
[tick  50] pop= 9 explore_var=0.0276 msg_ent=0.456 mean_en=0.708 deaths=4

[POPULATION] boom-bust across 100 ticks: 8→2→15→3 (range 2–15)
[MSG ENTROPY] diverse signaling: 0.0–1.0, never static
[FINAL GENOMES] explore=[0.79,0.86,0.37,0.47]
                 cooperate=[0.74,0.76,0.99,1.0]
                 risk=[1.0,1.0,0.99,0.89]
==========================================================
  Simulation complete.
==========================================================
```

---

##  Metrics

Logged every tick, summarized at end:

| Metric | Description |
|---|---|
| `pop` | Current population size |
| `explore_var` | Variance of `explore` gene across population |
| `msg_ent` | Normalized Shannon entropy of risk signals (0–1) |
| `mean_en` | Mean energy across all agents |
| `deaths` | Cumulative starvation deaths |
| `genomes` | Per-agent genome traits (explore, cooperate, risk) |

---

##  Genome Traits

| Trait | Range | Effect |
|---|---|---|
| `explore` | 0–1 | Competitive foraging weight — higher = more resource share |
| `cooperate` | 0–1 | Social conformity — high = aligns with peer risk, low = anti-aligns |
| `risk` | 0–1 | Risk multiplier on competitive weight — higher = bolder foraging |

All traits **mutate ±0.15** during reproduction.

---

##  Evolved Behaviors

- **  Boom-bust population cycles** — 2–15 agents across 100 ticks
- **  Strategy divergence** — multi-trait genomes don't converge to identical values
- **  Emergent signaling** — risk messages vary and influence collective behavior
- **  Starvation death** — metabolism hard floor kills underperformers
- **  Memory-driven plasticity** — resource trends modulate moment-to-moment decisions
- **  Social conformity dynamics** — cooperate gene creates herding or anti-herding

---

##  Research Directions

- **  Evolving communication protocols** — structured language beyond single risk signal
- **  Tool creation / niche construction** — agents modify environment
- **  Memory graphs** — long-term associative memory with decay and reinforcement
- **  Culture formation** — persistent behavioral norms across generations
- **  Multi-resource economies** — different resource types favoring different strategies
- **  Spatial structure** — agents on a grid with local interactions

---

##  Project Structure

```
evolving_agent_ecosystem/
├── agents/
│   └── simple_agent.py      # Agent class — genome, act(), message
├── core/
│   └── ecosystem.py          # Ecosystem — step(), environment, run loop
├── evolution/
│   └── evolver.py            # Selection, reproduction, mutation
├── memory/
│   └── shared_memory.py      # Tick storage, resource_trend queries
├── environment/              # Reserved for future env modules
├── utils/
│   └── logger.py             # Simple logging helper
├── logs/                     # Runtime logs
├── data/                     # Simulation data output
├── main.py                   # Entry point
├── requirements.txt          # Python dependencies
├── LICENSE                   # MIT License
└── README.md                 # ← you are here
```

---

##  License

MIT — see [LICENSE](LICENSE).
