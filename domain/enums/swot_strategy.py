from enum import Enum


class SWOTStrategy(str, Enum):

    FO = "Forças × Oportunidades"

    FA = "Forças × Ameaças"

    WO = "Fraquezas × Oportunidades"

    WT = "Fraquezas × Ameaças"
