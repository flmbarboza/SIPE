"""
SIPE - Sistema Integrado de Planejamento Estratégico

Gerenciador de navegação.

Responsável pelo registro e navegação entre páginas.

Autor:
Flávio Luiz de Moraes Barboza

Versão:
0.1.0
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional, Type

from sipe.core.page import Page
from sipe.core.session_manager import session


# ============================================================
# Item de Navegação
# ============================================================

@dataclass(slots=True)
class NavigationItem:
    """
    Representa uma página registrada na aplicação.
    """

    id: str
    title: str
    icon: str
    page_class: Type[Page]
    order: int = 0
    visible: bool = True
    enabled: bool = True


# ============================================================
# Navigation
# ============================================================

class Navigation:
    """
    Gerenciador central de navegação.
    """

    def __init__(self):

        self._pages: Dict[str, NavigationItem] = {}

    # --------------------------------------------------------
    # Registro
    # --------------------------------------------------------

    def register(self, item: NavigationItem):

        if item.id in self._pages:
            raise ValueError(
                f"Página '{item.id}' já registrada."
            )

        self._pages[item.id] = item

    # --------------------------------------------------------
    # Consulta
    # --------------------------------------------------------

    def exists(self, page_id: str) -> bool:

        return page_id in self._pages

    def get(self, page_id: str) -> Optional[NavigationItem]:

        return self._pages.get(page_id)

    def pages(self) -> List[NavigationItem]:

        return sorted(
            self._pages.values(),
            key=lambda p: p.order
        )

    # --------------------------------------------------------
    # Página atual
    # --------------------------------------------------------

    @property
    def current(self) -> NavigationItem:

        page_id = session.current_page

        if page_id not in self._pages:

            raise ValueError(
                f"Página '{page_id}' não registrada."
            )

        return self._pages[page_id]

    # --------------------------------------------------------
    # Navegação
    # --------------------------------------------------------

    def navigate(self, page_id: str):

        if page_id not in self._pages:

            raise ValueError(
                f"Página '{page_id}' não registrada."
            )

        current_page = self.create_current_page()

        if not current_page.before_leave():
            return

        session.current_page = page_id

    # --------------------------------------------------------
    # Instanciação
    # --------------------------------------------------------

    def create_current_page(self) -> Page:

        item = self.current

        return item.page_class()

    def create_page(self, page_id: str) -> Page:

        if page_id not in self._pages:
            raise ValueError(
                f"Página '{page_id}' não registrada."
            )

        return self._pages[page_id].page_class()

    # --------------------------------------------------------
    # Sidebar
    # --------------------------------------------------------

    def sidebar_items(self) -> List[NavigationItem]:

        return [
            page
            for page in self.pages()
            if page.visible and page.enabled
        ]

    # --------------------------------------------------------
    # Informações
    # --------------------------------------------------------

    def count(self) -> int:

        return len(self._pages)

    def clear(self):

        self._pages.clear()

    # --------------------------------------------------------
    # Debug
    # --------------------------------------------------------

    def dump(self):

        return {
            page.id: page.title
            for page in self.pages()
        }


# Singleton
navigation = Navigation()
