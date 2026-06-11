from core.ecosystem import Ecosystem

if __name__ == "__main__":
    eco = Ecosystem(num_agents=8)
    eco.run(steps=80)
