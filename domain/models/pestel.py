"""
Modelo PESTEL.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field


@dataclass
class PestelItem:

    description: str = ""

    impact: int = 3

    probability: int = 3

    priority: int = 3

    observations: str = ""

    def to_dict(self):

        return asdict(self)


@dataclass
class Pestel:

    political: list[PestelItem] = field(default_factory=list)

    economic: list[PestelItem] = field(default_factory=list)

    social: list[PestelItem] = field(default_factory=list)

    technological: list[PestelItem] = field(default_factory=list)

    environmental: list[PestelItem] = field(default_factory=list)

    legal: list[PestelItem] = field(default_factory=list)

    def validate(self):

        return True

    def to_dict(self):

        return asdict(self)

    @classmethod
    def from_dict(cls, data):

        obj = cls()

        for field_name in data:

            setattr(
                obj,
                field_name,
                [
                    PestelItem(**x)
                    for x in data[field_name]
                ],
            )

        return obj

    def __str__(self):

        return "PESTEL"
