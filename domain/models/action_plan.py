"""
SIPE
Plano de Ação 5W2H
"""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from uuid import uuid4


@dataclass
class Action:

    id: str = field(default_factory=lambda: str(uuid4()))

    initiative_id: str = ""

    what: str = ""

    why: str = ""

    where: str = ""

    when: str = ""

    who: str = ""

    how: str = ""

    how_much: float = 0.0

    status: str = "Planejada"

    progress: float = 0.0

    def validate(self):

        return self.what != ""

    def to_dict(self):

        return asdict(self)

    @classmethod
    def from_dict(cls, data):

        return cls(**data)
