import sys
from pathlib import Path

from src.reacher_env import ReacherEnv
from src.ddpg_agent import DDPGAgent, DDPGConfig
from src.random_agent import RandomAgent


# choose agent: ddpg | random
AGENT = "ddpg"


def get_env_path():
    if len(sys.argv) != 2:
        print("ERROR: invalid arguments list")
        print("Usage: rollout.py <path_to_unity_env>")
        sys.exit(1)
    return sys.argv[1]


if __name__ == "__main__":
    env = ReacherEnv(get_env_path())
    agent = RandomAgent(env) if AGENT == "random" else DDPGAgent(env, DDPGConfig(
        fc1_units=128,
        fc2_units=64,
    ))
    if Path("actor_model.pt").exists() and Path("critic_model.pt").exists():
        agent.restore("actor_model.pt", "critic_model.pt")
    agent.run_episode()
    env.close()
