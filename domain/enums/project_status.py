from enum import Enum


class ProjectStatus(str, Enum):

    PLANNING = "Planejamento"

    ACTIVE = "Em Execução"

    PAUSED = "Pausado"

    COMPLETED = "Concluído"

    CANCELLED = "Cancelado"

    ARCHIVED = "Arquivado"
