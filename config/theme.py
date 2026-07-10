"""
Tema oficial do SIPE.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Theme:

    PRIMARY = "#0F62FE"

    SECONDARY = "#393939"

    SUCCESS = "#24A148"

    WARNING = "#F1C21B"

    ERROR = "#DA1E28"

    BACKGROUND = "#FFFFFF"

    CARD = "#F4F4F4"

    TEXT = "#161616"

    BORDER_RADIUS = 10

    CARD_PADDING = 15

    TITLE_SIZE = 28

    SUBTITLE_SIZE = 20

    TEXT_SIZE = 15

    FONT = "sans-serif"


theme = Theme()
