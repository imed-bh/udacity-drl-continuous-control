import numpy as np

from src.agent import Agent
from src.reacher_env import ReacherEnv


class RandomAgent(Agent):
    def __init__(self, env: ReacherEnv):
        super().__init__(env)

    def compute_action(self, state, epsilon):
        return np.clip(np.random.randn(self.env.action_size)*0.2, -1, 1)
