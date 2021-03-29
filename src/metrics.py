from collections import deque
import numpy as np
import matplotlib.pyplot as plt


class Metrics:
    def __init__(self):
        self.step_count = 0
        self.episode_count = 0
        self.score_window = deque([0], maxlen=100)
        self.score = 0
        self.current_episode_length = 0
        self.xdata, self.ydata = [], []
        self.line, self.ax = None, None

    def on_step(self, reward, done):
        self.step_count += 1
        self.current_episode_length += 1
        self.score += reward
        if done:
            self.episode_count += 1
            self.score_window.append(self.score)
            self.score = 0
            self.current_episode_length = 0
            if self.ax is not None:
                self.ax.set_xlim(0, self.episode_count)
                self.xdata.append(self.episode_count)
                self.ydata.append(self.running_score())
                self.line.set_data(self.xdata, self.ydata)
                plt.pause(0.001)

    def running_score(self):
        return np.mean(self.score_window)

    def plot(self):
        fig, self.ax = plt.subplots()
        self.line, = plt.plot([], [], 'b-')

        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 50)
        self.ax.set_title('DDPG Training')
        self.ax.set_xlabel('Episodes')
        self.ax.set_ylabel('Score')
        plt.pause(0.001)


