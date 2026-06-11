import random
from agents.simple_agent import Agent

class Evolver:
    def evolve(self, agents, results, memory, world):
        # selection pressure
        agents = sorted(agents, key=lambda a: a.energy, reverse=True)

        survivors = agents[: max(2, len(agents)//2)]

        new_agents = []

        for a in survivors:
            new_agents.append(a)

            # reproduction with mutation across genome
            child = Agent(a.id, a.memory)
            child.genome = {
                k: max(0.0, min(1.0, v + random.uniform(-0.1, 0.1)))
                for k, v in a.genome.items()
            }

            new_agents.append(child)

        # enforce diversity pressure
        return new_agents[:12]
