from enum import Enum


class InitiativeStatus(str, Enum):

    PLANNED = "Planejada"

    IN_PROGRESS = "Em Andamento"

    ON_HOLD = "Suspensa"

    COMPLETED = "Concluída"

    CANCELLED = "Cancelada"
