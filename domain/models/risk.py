"""
SIPE
Gestão de Riscos
"""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from uuid import uuid4


@dataclass
class Risk:

    id: str = field(default_factory=lambda: str(uuid4()))

    title: str = ""

    description: str = ""

    category: str = ""

    probability: int = 3

    impact: int = 3

    level: int = 9

    response: str = ""

    owner: str = ""

    status: str = "Aberto"

    contingency: str = ""

    def calculate_level(self):

        self.level = self.probability * self.impact

    def validate(self):

        return self.title != ""

    def to_dict(self):

        return asdict(self)

    @classmethod
    def from_dict(cls, data):

        return cls(**data)
