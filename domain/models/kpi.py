"""
SIPE
Indicadores Estratégicos
"""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from uuid import uuid4


@dataclass
class KPI:

    id: str = field(default_factory=lambda: str(uuid4()))

    name: str = ""

    objective_id: str = ""

    formula: str = ""

    unit: str = ""

    baseline: float = 0.0

    target: float = 0.0

    current: float = 0.0

    frequency: str = "Mensal"

    responsible: str = ""

    source: str = ""

    observations: str = ""

    def progress(self):

        if self.target == 0:
            return 0

        return round(
            (self.current / self.target) * 100,
            2,
        )

    def validate(self):

        return self.name != ""

    def to_dict(self):

        return asdict(self)

    @classmethod
    def from_dict(cls, data):

        return cls(**data)
