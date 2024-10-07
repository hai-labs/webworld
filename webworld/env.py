"""Environment for navigating the web."""

import re
from typing import Any

import gymnasium as gym
from webworld.spaces import Tokens, WebGraph


DEFAULT_TARGET = "https://en.wikipedia.org/wiki/Dog"


class WebWorldEnv(gym.Env):
    """WebWorld environment."""

    metadata = {"render_modes": ["human", "ansi"]}

    def __init__(
        self,
        start_url: str | None = None,
        tokenizer: Any | None = None,
        render_mode: str | None = None,
    ):
        """Initialize the environment."""
        self.render_mode = render_mode

        self.observation_space = WebGraph(start_url=start_url)
        self.action_space = Tokens(tokenizer=tokenizer)

        assert render_mode is None or render_mode in self.metadata["render_modes"]
        self.render_mode = render_mode

        # initialize the window that will display the enviornment and the clock
        # to ensure the environment is rendered at the correct framerate in
        # human mode
        self.window = None
        self.clock = None

    def reset(self, seed: int | None = None, options: dict | None = None):
        """Reset the environment."""
        observation = {
            "content": self.observation_space.sample(),
            "target": DEFAULT_TARGET,
        }
        # TODO: implement info as the distance (definition TBD) to the target text
        info = {}
        # replace more than 2 newlines with a single newline
        return observation, info

    def step(self, action: dict):
        """Take a step in the environment."""
        import ipdb; ipdb.set_trace()

    def render(self):
        """Render the environment."""

    def close(self):
        """Close the environment."""
