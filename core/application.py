"""
SIPE
Sistema Integrado de Planejamento Estratégico

Classe principal da aplicação.

Autor:
Flávio Luiz de Moraes Barboza
"""

from __future__ import annotations

import streamlit as st

from config import settings
from config.logging import app_logger
from config.paths import create_directories
from sipe.core.navigation import NavigationItem, navigation
from sipe.core.session_manager import session


class Application:
    """
    Classe principal do SIPE.
    """

    def __init__(self):

        self.logger = app_logger

        self.settings = settings

        self.session = session

        self.navigation = navigation

    # =====================================================
    # Inicialização
    # =====================================================

    def initialize(self):
        """
        Inicializa a aplicação.
        """

        create_directories()

        self.session.initialize()

        self.configure_streamlit()

        self.register_pages()

        self.logger.info("SIPE inicializado.")

    # =====================================================
    # Configuração Streamlit
    # =====================================================

    def configure_streamlit(self):

        st.set_page_config(
            page_title=self.settings.APP_NAME,
            page_icon="📈",
            layout="wide",
            initial_sidebar_state="expanded",
        )

    # =====================================================
    # Registro das páginas
    # =====================================================

    def register_pages(self):
        """
        Registra as páginas da aplicação.

        Será expandido conforme os módulos forem criados.
        """

        if self.navigation.count() > 0:
            return

        from sipe.ui.pages.home import HomePage

        self.navigation.register(
            NavigationItem(
                id="home",
                title="Início",
                icon="🏠",
                page_class=HomePage,
                order=1,
            )
        )

    # =====================================================
    # Sidebar
    # =====================================================

    def render_sidebar(self):

        with st.sidebar:

            st.title(self.settings.APP_NAME)

            st.caption(
                f"Versão {self.settings.VERSION}"
            )

            st.divider()

            current = self.session.current_page

            for item in self.navigation.sidebar_items():

                label = f"{item.icon}  {item.title}"

                if st.button(
                    label,
                    use_container_width=True,
                    type="primary"
                    if current == item.id
                    else "secondary",
                ):

                    self.navigation.navigate(item.id)

                    st.rerun()

            st.divider()

            st.caption("© SIPE")

    # =====================================================
    # Página Atual
    # =====================================================

    def render_page(self):

        page = self.navigation.create_current_page()

        page.run()

    # =====================================================
    # Execução
    # =====================================================

    def run(self):

        self.initialize()

        self.render_sidebar()

        self.render_page()
