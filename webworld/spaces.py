"""Definition of spaces in WebWorld."""

import gymnasium as gym


class WebGraph(gym.Space):
    """The space of web pages."""

    def __init__(self, start_url: str):
        """Initialize the web page."""
        self.start_url = start_url

    def sample(self):
        """Sample a web page."""


class Tokens(gym.Space):
    """The space of language model tokens."""

    def __init__(self, tokenizer):
        """Initialize the text."""
        self.tokenizer = tokenizer

    def sample(self):
        """Sample a text."""
