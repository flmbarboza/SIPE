from enum import Enum


class Periodicity(str, Enum):

    DAILY = "Diária"

    WEEKLY = "Semanal"

    MONTHLY = "Mensal"

    BIMONTHLY = "Bimestral"

    QUARTERLY = "Trimestral"

    SEMIANNUAL = "Semestral"

    ANNUAL = "Anual"
