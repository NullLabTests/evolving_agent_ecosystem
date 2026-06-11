import random
from agents.simple_agent import Agent

class Evolver:
    def evolve(self, agents, results, memory, world):
        if len(agents) < 1:
            return []

        agents = sorted(agents, key=lambda a: a.energy, reverse=True)

        # selection: keep top fraction proportional to resource availability
        resource = world.get("resource", 0.5)
        keep_ratio = min(0.8, max(0.3, resource * 0.6))
        n_keep = max(2, int(len(agents) * keep_ratio))
        survivors = agents[:n_keep]

        new_agents = []
        for a in survivors:
            new_agents.append(a)
            # probabilistic reproduction: energy surplus determines chance
            surplus = a.energy - 0.3
            if surplus > 0 and random.random() < surplus:
                a.energy -= 0.5
                child = Agent(a.id, a.memory)
                child.genome = {
                    k: max(0.0, min(1.0, v + random.uniform(-0.15, 0.15)))
                    for k, v in a.genome.items()
                }
                new_agents.append(child)

        return new_agents[:15]
