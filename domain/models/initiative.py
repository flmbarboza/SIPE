"""
SIPE
Iniciativas Estratégicas
"""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from uuid import uuid4


@dataclass
class Initiative:

    id: str = field(default_factory=lambda: str(uuid4()))

    objective_id: str = ""

    title: str = ""

    description: str = ""

    sponsor: str = ""

    manager: str = ""

    budget: float = 0.0

    start_date: str = ""

    end_date: str = ""

    progress: float = 0.0

    status: str = "Planejada"

    risks: list[str] = field(default_factory=list)

    def validate(self):

        return self.title != ""

    def to_dict(self):

        return asdict(self)

    @classmethod
    def from_dict(cls, data):

        return cls(**data)
