"""
SIPE
Objetivos Estratégicos
"""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from uuid import uuid4


@dataclass
class Objective:

    id: str = field(default_factory=lambda: str(uuid4()))

    title: str = ""

    description: str = ""

    perspective: str = ""

    strategic_theme: str = ""

    priority: int = 3

    responsible: str = ""

    start_date: str = ""

    end_date: str = ""

    status: str = "Planejado"

    observations: str = ""

    def validate(self):

        return self.title != ""

    def to_dict(self):

        return asdict(self)

    @classmethod
    def from_dict(cls, data):

        return cls(**data)

    def __str__(self):

        return self.title
