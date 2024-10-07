"""Example usage of the WebWorld environment."""

import gymnasium as gym
from webworld.env import WebWorldEnv
from webworld.agent import WebAgent


def main():
    env = WebWorldEnv()
    agent = WebAgent("llama3.1")

    observation, info = env.reset()

    for _ in range(1):
        action = agent.act(observation)
        observation, reward, terminated, truncated, info = env.step(action)
        if terminated or truncated:
            observation, info = env.reset()

    env.close()


if __name__ == "__main__":
    main()
