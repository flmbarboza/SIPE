"""
SIPE
Identidade Organizacional.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass
class Identity:

    business: str = ""

    mission: str = ""

    vision: str = ""

    values: list[str] = None

    purpose: str = ""

    positioning: str = ""

    slogan: str = ""

    def __post_init__(self):

        if self.values is None:
            self.values = []

    def validate(self):

        return self.mission.strip() != ""

    def to_dict(self):

        return asdict(self)

    @classmethod
    def from_dict(cls, data):

        return cls(**data)

    def __str__(self):

        return self.mission
