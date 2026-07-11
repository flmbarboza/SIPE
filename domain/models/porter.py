"""
SIPE
Modelo das Cinco Forças de Porter.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field


@dataclass
class PorterFactor:
    """
    Representa um fator de uma das forças competitivas.
    """

    description: str = ""
    score: int = 3
    priority: int = 3
    evidence: str = ""

    def validate(self) -> bool:
        return True

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        return cls(**data)


@dataclass
class Porter:

    rivalry: list[PorterFactor] = field(default_factory=list)

    suppliers: list[PorterFactor] = field(default_factory=list)

    customers: list[PorterFactor] = field(default_factory=list)

    new_entrants: list[PorterFactor] = field(default_factory=list)

    substitutes: list[PorterFactor] = field(default_factory=list)

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
                    PorterFactor(**item)
                    for item in data[field_name]
                ],
            )

        return obj

    def __str__(self):

        return "Cinco Forças de Porter"
