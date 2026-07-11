"""
SIPE
Modelo SWOT.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from uuid import uuid4


@dataclass
class SWOTItem:

    id: str = field(default_factory=lambda: str(uuid4()))

    description: str = ""

    weight: float = 1.0

    priority: int = 3

    observations: str = ""

    def validate(self):

        return True

    def to_dict(self):

        return asdict(self)

    @classmethod
    def from_dict(cls, data):

        return cls(**data)


@dataclass
class SWOTStrategy:

    id: str = field(default_factory=lambda: str(uuid4()))

    title: str = ""

    description: str = ""

    priority: int = 3

    responsible: str = ""

    due_date: str = ""

    status: str = "Planejada"

    def to_dict(self):

        return asdict(self)

    @classmethod
    def from_dict(cls, data):

        return cls(**data)


@dataclass
class SWOT:

    strengths: list[SWOTItem] = field(default_factory=list)

    weaknesses: list[SWOTItem] = field(default_factory=list)

    opportunities: list[SWOTItem] = field(default_factory=list)

    threats: list[SWOTItem] = field(default_factory=list)

    fo: list[SWOTStrategy] = field(default_factory=list)

    fa: list[SWOTStrategy] = field(default_factory=list)

    wo: list[SWOTStrategy] = field(default_factory=list)

    wt: list[SWOTStrategy] = field(default_factory=list)

    def validate(self):

        return True

    def to_dict(self):

        return asdict(self)

    @classmethod
    def from_dict(cls, data):

        obj = cls()

        for group in [
            "strengths",
            "weaknesses",
            "opportunities",
            "threats",
        ]:

            setattr(
                obj,
                group,
                [
                    SWOTItem(**item)
                    for item in data.get(group, [])
                ],
            )

        for group in [
            "fo",
            "fa",
            "wo",
            "wt",
        ]:

            setattr(
                obj,
                group,
                [
                    SWOTStrategy(**item)
                    for item in data.get(group, [])
                ],
            )

        return obj

    def __str__(self):

        return "SWOT"
