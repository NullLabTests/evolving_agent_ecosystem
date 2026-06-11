from core.ecosystem import Ecosystem

if __name__ == "__main__":
    print("=" * 58)
    print("  EVOLVING AGENT ECOSYSTEM")
    print("  Open-ended evolutionary simulation")
    print("=" * 58)
    eco = Ecosystem(num_agents=12)
    eco.run(steps=100)
    print("=" * 58)
    print("  Simulation complete.")
    print("=" * 58)
