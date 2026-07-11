"""
SIPE - Sistema Integrado de Planejamento Estratégico

Classe base para todas as páginas do sistema.

Todas as páginas devem herdar desta classe.

Autor:
Flávio Luiz de Moraes Barboza

Versão:
0.1.0
"""

from __future__ import annotations

from abc import ABC, abstractmethod

import streamlit as st

from core.session_manager import session
from config.logging import app_logger


class Page(ABC):
    """
    Classe base de todas as páginas do SIPE.

    Exemplo
    --------

    class HomePage(Page):

        def render(self):

            st.write("Home")
    """

    id: str = ""

    title: str = ""

    icon: str = ""

    show_sidebar: bool = True

    def __init__(self):

        self.session = session
        self.logger = app_logger

    # ------------------------------------------------------------------
    # Ciclo de vida
    # ------------------------------------------------------------------

    def load(self) -> None:
        """
        Executado antes da renderização.

        Sobrescreva quando necessário.
        """
        return

    @abstractmethod
    def render(self) -> None:
        """
        Método obrigatório.

        Toda página deve implementar este método.
        """
        ...

    def save(self) -> None:
        """
        Executado quando a página salva informações.

        Sobrescreva quando necessário.
        """
        return

    def validate(self) -> bool:
        """
        Valida os dados da página.

        Retorna
        -------
        bool
        """
        return True

    def before_leave(self) -> bool:
        """
        Executado antes da troca de página.

        Retorne False para impedir a navegação.
        """
        return True

    def after_enter(self) -> None:
        """
        Executado após entrar na página.
        """
        return

    # ------------------------------------------------------------------
    # Layout
    # ------------------------------------------------------------------

    def page_title(self) -> None:
        """
        Exibe o título da página.
        """

        if self.icon:
            st.title(f"{self.icon} {self.title}")
        else:
            st.title(self.title)

    def subtitle(self, text: str) -> None:
        st.subheader(text)

    def separator(self) -> None:
        st.divider()

    # ------------------------------------------------------------------
    # Mensagens
    # ------------------------------------------------------------------

    def info(self, text: str):

        st.info(text)

    def success(self, text: str):

        st.success(text)

    def warning(self, text: str):

        st.warning(text)

    def error(self, text: str):

        st.error(text)

    # ------------------------------------------------------------------
    # Logger
    # ------------------------------------------------------------------

    def log_info(self, message: str):

        self.logger.info(f"[{self.id}] {message}")

    def log_warning(self, message: str):

        self.logger.warning(f"[{self.id}] {message}")

    def log_error(self, message: str):

        self.logger.error(f"[{self.id}] {message}")

    # ------------------------------------------------------------------
    # Navegação
    # ------------------------------------------------------------------

    def go_to(self, page_id: str):
        """
        Solicita navegação para outra página.
        """

        self.session.current_page = page_id

        st.rerun()

    # ------------------------------------------------------------------
    # Utilidades
    # ------------------------------------------------------------------

    def refresh(self):
        """
        Recarrega a página.
        """

        st.rerun()

    @property
    def project(self):

        return self.session.project

    @property
    def company(self):

        return self.session.company

    @property
    def has_project(self):

        return self.session.project_loaded

    # ------------------------------------------------------------------
    # Execução
    # ------------------------------------------------------------------

    def run(self):
        """
        Executa o ciclo completo da página.
        """

        self.logger.info(f"Opening page: {self.id}")

        self.load()

        self.after_enter()

        self.render()
