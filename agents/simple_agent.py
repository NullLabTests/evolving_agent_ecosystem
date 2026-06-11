import random

class Agent:
    def __init__(self, agent_id, memory):
        self.id = agent_id
        self.memory = memory

        # multi-dimensional genome (IMPORTANT)
        self.genome = {
            "explore": random.random(),
            "cooperate": random.random(),
            "risk": random.random()
        }

        self.energy = 1.0
        self.message = ""

    def act(self, world, population):
        resource = world["resource"]

        # interaction pressure
        others = len(population)
        crowd_penalty = 0.01 * others

        # behavioral decision
        gain = resource * self.genome["explore"]
        cooperation_bonus = self.genome["cooperate"] * 0.05

        self.energy += gain + cooperation_bonus - crowd_penalty

        # emergent signal (proto-language channel)
        self.message = f"{int(self.genome['risk']*10)}:{int(gain*10)}"

        return {
            "id": self.id,
            "energy": self.energy,
            "message": self.message
        }
