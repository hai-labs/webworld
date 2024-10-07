"""Definition of spaces in WebWorld."""

import re

import gymnasium as gym
import httpx
from markdownify import markdownify as md


DEFAULT_START_URL = "https://en.wikipedia.org/wiki/Main_Page"


class WebGraph(gym.Space):
    """The space of web pages."""

    def __init__(self, start_url: str | None, text_format: str = "html"):
        """Initialize the web page."""
        self.start_url = start_url or DEFAULT_START_URL

    def sample(self) -> str:
        """Sample a web page."""
        # TODO: implement pagination based on LM context length
        # add metadata e.g. url
        response = httpx.get(self.start_url)
        return re.sub(r"\n+", "\n\n", md(response.text))


class Tokens(gym.Space):
    """The space of language model tokens."""

    def __init__(self, tokenizer):
        """Initialize the text."""
        self.tokenizer = tokenizer

    def sample(self):
        """Sample a text."""
        return None
