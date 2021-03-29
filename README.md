# Udacity Deep Reinforcement Learning NanoDegree
## Project Continuous Control

### Introduction
This project aims to train an agent to control a double-joint arm to reach a moving target and keep following it as much as possible.

### Getting Started

1. Download the environment from one of the links below.  You need only select the environment that matches your operating system:
    - Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher_Linux.zip)
    - Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher.app.zip)
    - Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher_Windows_x86.zip)
    - Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher_Windows_x86_64.zip)

2. Place the file under this repository, and unzip (or decompress) the file. 
3. The code is written in Python 3 and uses the PyTorch library. You can install the requirements with:

```
conda create -n drlnd python=3.6
conda activate drlnd
pip install torch
pip install unityagents
```


### Environment Details

The observation given to the agent is a 33 dimension vector and contains position, rotation, velocity and angular velocities of the arm.

The agent action is a 4 dimension vector corresponding to torque applicable to two joints.
Each value in the vector should be a number between -1 and 1.

A reward of +0.1 is provided for each step that the agent's hand is touching the target location.
So the goal is to maintain the position at the target location for as many steps as possible.

The task is episodic, and the environment is considered solved, when the agent gets an average score of +30 over 100 consecutive episodes.

### Solving with TODO

In this section, we try to solve the problem using TODO.
Details of the model are provided in `Report.md`. 

Note: you can skip the training part and use the provided pretrained `model.pt` to rollout a trained agent.

#### Training

To launch training, you need to run the train script with the file path to Unity environment as argument:

`python train.py <path_to_unity_env_here>`

For example on Linux: `python train.py Reacher_Linux/Reacher.x86_64`

You can customize the different options for training by modifying the variables at the top of file `train.py`.

### Rollout

To launch rollout, you need to run the rollout script with the file path to Unity environment as argument:

`python rollout.py <path_to_unity_env_here>`

For example on Linux: `python rollout.py Reacher_Linux/Reacher.x86_64`

You can customize the different options for rollout by modifying the variables at the top of file `rollout.py`.