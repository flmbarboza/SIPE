"""
SIPE
Sistema Integrado de Planejamento Estratégico

Projeto Estratégico
"""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from datetime import datetime
from uuid import uuid4

from domain.models.company import Company
from domain.models.canvas import Canvas
from domain.models.pestel import Pestel
from domain.models.porter import Porter
from domain.models.swot import SWOT
from domain.models.identity import Identity
from domain.models.objective import Objective
from domain.models.financial import Financial


@dataclass
class Project:

    # =====================================================
    # Metadados
    # =====================================================

    id: str = field(default_factory=lambda: str(uuid4()))

    version: str = "0.1.0"

    title: str = ""

    description: str = ""

    status: str = "Planejamento"

    planning_horizon: int = 5

    responsible: str = ""

    created_at: str = field(
        default_factory=lambda: datetime.now().isoformat()
    )

    updated_at: str = field(
        default_factory=lambda: datetime.now().isoformat()
    )

    # =====================================================
    # Modelos de Domínio
    # =====================================================

    company: Company = field(default_factory=Company)

    canvas: Canvas = field(default_factory=Canvas)

    pestel: Pestel = field(default_factory=Pestel)

    porter: Porter = field(default_factory=Porter)

    swot: SWOT = field(default_factory=SWOT)

    identity: Identity = field(default_factory=Identity)

    objectives: list[Objective] = field(default_factory=list)

    financial: Financial = field(default_factory=Financial)

    # =====================================================
    # Controle
    # =====================================================

    attachments: list[str] = field(default_factory=list)

    tags: list[str] = field(default_factory=list)

    notes: str = ""

    # =====================================================
    # Métodos
    # =====================================================

    def touch(self):

        self.updated_at = datetime.now().isoformat()

    # -----------------------------------------------------

    def validate(self):

        return self.title.strip() != ""

    # -----------------------------------------------------

    def to_dict(self):

        return asdict(self)

    # -----------------------------------------------------

    @classmethod
    def from_dict(cls, data):

        obj = cls()

        obj.id = data.get("id", obj.id)
        obj.version = data.get("version", obj.version)

        obj.title = data.get("title", "")
        obj.description = data.get("description", "")
        obj.status = data.get("status", "Planejamento")
        obj.planning_horizon = data.get("planning_horizon", 5)
        obj.responsible = data.get("responsible", "")

        obj.created_at = data.get(
            "created_at",
            obj.created_at,
        )

        obj.updated_at = data.get(
            "updated_at",
            obj.updated_at,
        )

        obj.company = Company.from_dict(
            data.get("company", {})
        )

        obj.canvas = Canvas.from_dict(
            data.get("canvas", {})
        )

        obj.pestel = Pestel.from_dict(
            data.get("pestel", {})
        )

        obj.porter = Porter.from_dict(
            data.get("porter", {})
        )

        obj.swot = SWOT.from_dict(
            data.get("swot", {})
        )

        obj.identity = Identity.from_dict(
            data.get("identity", {})
        )

        obj.objectives = [
            Objective.from_dict(item)
            for item in data.get("objectives", [])
        ]

        obj.financial = Financial.from_dict(
            data.get("financial", {})
        )

        obj.attachments = data.get(
            "attachments",
            [],
        )

        obj.tags = data.get(
            "tags",
            [],
        )

        obj.notes = data.get(
            "notes",
            "",
        )

        return obj

    # -----------------------------------------------------

    def __str__(self):

        return self.title

    # -----------------------------------------------------

    @property
    def is_new(self):

        return self.title == ""

    # -----------------------------------------------------

    @property
    def total_objectives(self):

        return len(self.objectives)

    # -----------------------------------------------------

    @property
    def total_kpis(self):

        return sum(
            len(obj.kpis)
            for obj in self.objectives
        )

    # -----------------------------------------------------

    @property
    def total_initiatives(self):

        return sum(
            len(obj.initiatives)
            for obj in self.objectives
        )

    # -----------------------------------------------------

    @property
    def total_actions(self):

        return sum(
            len(init.actions)
            for obj in self.objectives
            for init in obj.initiatives
        )
