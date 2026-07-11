"""
Business Model Canvas.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field


@dataclass
class Canvas:

    customer_segments: list[str] = field(default_factory=list)

    value_proposition: list[str] = field(default_factory=list)

    channels: list[str] = field(default_factory=list)

    customer_relationships: list[str] = field(default_factory=list)

    revenue_streams: list[str] = field(default_factory=list)

    key_resources: list[str] = field(default_factory=list)

    key_activities: list[str] = field(default_factory=list)

    key_partnerships: list[str] = field(default_factory=list)

    cost_structure: list[str] = field(default_factory=list)

    # --------------------------------------------------

    def validate(self):

        return True

    # --------------------------------------------------

    def to_dict(self):

        return asdict(self)

    # --------------------------------------------------

    @classmethod
    def from_dict(cls, data):

        return cls(**data)

    # --------------------------------------------------

    def __str__(self):

        return "Business Model Canvas"
