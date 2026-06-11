import random

METABOLISM = 0.22

class Agent:
    def __init__(self, agent_id, memory):
        self.id = agent_id
        self.memory = memory

        self.genome = {
            "explore": random.random(),
            "cooperate": random.random(),
            "risk": random.random()
        }

        self.energy = 1.0
        self.message = ""
        self.age = 0

    def act(self, resource_share, population):
        self.age += 1
        gain = resource_share
        self.energy += gain - METABOLISM

        self.message = f"{int(self.genome['risk']*10)}:{int(gain*10)}"

        return {
            "id": self.id,
            "energy": self.energy,
            "message": self.message,
            "trait": self.genome["explore"]
        }
