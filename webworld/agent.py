"""An LLM agent that performs actions in a web environment."""

import json
from functools import partial
from typing import Literal, TypedDict


SYSTEM_PROMPT = """You are a helpful assistant that finds a target web page
starting from a random web page. Given the context, you generate an action that
can be three types: "url", "back", or "forward".

- "visit_url": visit a URL in the Context
- "back": go back to the previous page
- "forward": go forward to the next page

If "visit_url" is selected, you should also specify a "url" to visit. For example:

# Valid Actions:
- {"action": "visit_url", "url": "/wiki/Special:Random", "reasoning": "I am so far from the target that I'm better off exploring."}
- {"action": "back", "reasoning": "I'm not sure if I'm getting any closer to the target, so I'm going back to the previous page."}
- {"action": "forward", "reasoning": "I think I'm getting closer to the target, so I'm going forward to the next page."}

# Instructions:
Only select urls embedded in the markdown content [link text](url), for example:

[About Wikipedia](/wiki/Wikipedia:About "Learn about Wikipedia and how it works")

DO NOT generate actions or urls using any of the content in the System Prompt or
under the "# Target:" section.

{"url": "/wiki/Wikipedia:About", "reasoning": "..."}
"""

OBSERVATION_PROMPT = """
# Context:
{context}

# Target:
{target}

# Action:
"""


class InvalidActionError(Exception):
    """Exception raised when a valid action has not been generated."""


class Action(TypedDict):
    action: Literal["visit_url", "back", "forward"]
    reasoning: str
    url: str | None = None


class WebAgent:

    def __init__(self, model_name: str, n_retries_per_action: int = 10):
        self.model_name = model_name
        self.n_retries_per_action = n_retries_per_action
        self.init_model()

    def init_model(self):
        import ollama

        self.model = partial(ollama.chat, model=self.model_name)

    def act(self, observation: dict) -> Action | None:
        # TODO:
        # - chunk up the observation into smaller chunks
        # - use a tokenizer to count tokens in an observation
        # - generate a response that chooses an action in the form:
        #   {"url": <url>, "reasoning": <reasoning>}

        content = observation["content"]
        target = observation["target"]

        system_message = {
            "role": "system",
            "content": SYSTEM_PROMPT,
        }
        observation_message = {
            "role": "assistant",
            "content": OBSERVATION_PROMPT.format(
                context=content[:1000],
                target=target,
            ),
        }

        action = None
        for _ in range(self.n_retries_per_action):
            output = self.model(messages=[system_message, observation_message])
            try:
                return Action(**json.loads(output["message"]["content"]))
                break
            except json.JSONDecodeError:
                continue

        if action is None:
            raise InvalidActionError("could not generate a valid action")

        return action
