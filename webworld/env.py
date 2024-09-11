"""Environment for navigating the web."""

import gymnasium as gym
from webworld.spaces import Tokens, WebGraph


class WebWorldEnv(gym.Env):
    """WebWorld environment."""

    metadata = {"render_modes": ["human", "ansi"]}

    def __init__(self, render_mode: str | None = None):
        """Initialize the environment."""
        self.render_mode = render_mode

        self.observation_space = WebGraph(start_url=None)
        self.action_space = Tokens(tokenizer=None)

        assert render_mode is None or render_mode in self.metadata["render_modes"]
        self.render_mode = render_mode

        # initialize the window that will display the enviornment and the clock
        # to ensure the environment is rendered at the correct framerate in
        # human mode
        self.window = None
        self.clock = None

    def reset(self, seed: int | None = None, options: dict | None = None):
        """Reset the environment."""

    def step(self, action: str):
        """Take a step in the environment."""

    def render(self):
        """Render the environment."""

    def close(self):
        """Close the environment."""
