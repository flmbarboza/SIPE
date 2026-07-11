from enum import Enum


class RiskResponse(str, Enum):

    AVOID = "Evitar"

    MITIGATE = "Mitigar"

    TRANSFER = "Transferir"

    ACCEPT = "Aceitar"

    EXPLOIT = "Explorar"

    SHARE = "Compartilhar"

    ENHANCE = "Potencializar"
