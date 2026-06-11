import random
import math
import statistics
from agents.simple_agent import Agent
from memory.shared_memory import SharedMemory
from evolution.evolver import Evolver

class Ecosystem:
    def __init__(self, num_agents=6):
        self.memory = SharedMemory()
        self.agents = [Agent(i, self.memory) for i in range(num_agents)]
        self.evolver = Evolver()
        self.tick = 0
        self.base_resource = 1.0
        self.history = {"explore_variance": [], "mean_energy": [], "population": [], "message_entropy": []}
        self.total_deaths = 0

    def environment(self, pop_size):
        base = 1.0 + 0.8 * math.sin(self.tick / 6)
        noise = random.random() * 0.3
        total = base + noise
        effective = max(0.05, total - 0.06 * pop_size)
        return effective

    def step(self):
        self.tick += 1
        total_resource = self.environment(len(self.agents))

        # peer communication: parse last tick's risk signals
        peer_risks = []
        for a in self.agents:
            try:
                risk_part = a.message.split(":")[0]
                peer_risks.append(int(risk_part) / 10.0)
            except (ValueError, IndexError):
                peer_risks.append(0.5)
        mean_peer_risk = sum(peer_risks) / len(peer_risks) if peer_risks else 0.5

        weights = []
        for a in self.agents:
            trend = self.memory.resource_trend(k=8)
            mood = max(-0.3, min(0.3, trend * -2.0))
            # social influence: cooperate gene = conformity to peer risk
            peer_bias = (mean_peer_risk - 0.5) * (a.genome["cooperate"] * 2 - 1) * 0.3
            peer_bias = max(-0.3, min(0.3, peer_bias))
            expr_explore = max(0.0, min(1.0, a.genome["explore"] + mood + peer_bias))
            w = expr_explore * (1 + a.genome["risk"] * 0.5)
            weights.append(w)

        total_w = sum(weights) or 1.0

        results = []
        for i, a in enumerate(self.agents):
            share = total_resource * weights[i] / total_w
            r = a.act(share, self.agents)
            results.append(r)

        pre = len(self.agents)
        self.agents = [a for a in self.agents if a.energy > 0]
        self.total_deaths += pre - len(self.agents)

        self.memory.store({
            "tick": self.tick,
            "world": {"resource": total_resource},
            "results": results
        })

        self.agents = self.evolver.evolve(self.agents, results, self.memory, {"resource": total_resource})

    def diversity_metrics(self):
        if len(self.agents) < 2:
            return 0.0, 0.0, 0
        expresses = [a.genome["explore"] for a in self.agents]
        energies = [a.energy for a in self.agents]
        return statistics.variance(expresses), statistics.mean(energies), len(self.agents)

    def message_entropy(self):
        if len(self.agents) < 2:
            return 0.0
        signals = []
        for a in self.agents:
            try:
                signals.append(int(a.message.split(":")[0]))
            except (ValueError, IndexError):
                signals.append(5)
        counts = {}
        for s in signals:
            counts[s] = counts.get(s, 0) + 1
        total = len(signals)
        ent = 0.0
        for c in counts.values():
            p = c / total
            ent -= p * math.log2(p) if p > 0 else 0
        return ent / math.log2(min(total, 11))

    def run(self, steps=50):
        for _ in range(steps):
            self.step()
            var_exp, mean_en, pop = self.diversity_metrics()
            msg_ent = self.message_entropy()
            self.history["explore_variance"].append(var_exp)
            self.history["mean_energy"].append(mean_en)
            self.history["population"].append(pop)
            self.history["message_entropy"].append(msg_ent)
            if self.tick % 10 == 0 or self.tick == steps:
                print(
                    f"[tick {self.tick:3d}] pop={pop:2d} "
                    f"explore_var={var_exp:.4f} msg_ent={msg_ent:.3f} "
                    f"mean_en={mean_en:.3f} deaths={self.total_deaths}"
                )
        print(f"\n[POPULATION] trajectory: {self.history['population']}")
        print(f"[MSG ENTROPY] trajectory: {[round(e,3) for e in self.history['message_entropy']]}")
        print(f"[FINAL] agents={len(self.agents)} total_deaths={self.total_deaths}")
        if self.agents:
            print(f"[GENOMES] explore={[round(a.genome['explore'],2) for a in self.agents]} "
                  f"cooperate={[round(a.genome['cooperate'],2) for a in self.agents]} "
                  f"risk={[round(a.genome['risk'],2) for a in self.agents]} "
                  f"energies={[round(a.energy,2) for a in self.agents]}")
