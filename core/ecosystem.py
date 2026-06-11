import random
import math
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

    def environment(self):
        # dynamic, non-stationary world
        self.base_resource = 0.5 + 0.5 * math.sin(self.tick / 5)
        noise = random.random() * 0.3
        return {"resource": self.base_resource + noise}

    def step(self):
        self.tick += 1
        world_state = self.environment()

        results = []
        for a in self.agents:
            results.append(a.act(world_state, self.agents))

        self.memory.store({
            "tick": self.tick,
            "world": world_state,
            "results": results
        })

        self.agents = self.evolver.evolve(self.agents, results, self.memory, world_state)

    def run(self, steps=50):
        for _ in range(steps):
            self.step()
            print(
                f"[tick {self.tick}] pop={len(self.agents)} mem={len(self.memory.data)}"
            )
