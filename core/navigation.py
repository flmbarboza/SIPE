"""
SIPE
Sistema Integrado de Planejamento Estratégico

Gerenciador de navegação.
"""

from __future__ import annotations

import streamlit as st

from pages.home import HomePage
from pages.project import ProjectPage
from pages.canvas import CanvasPage


class Navigation:

    def __init__(self):

        self.pages = {
            "🏠 Home": HomePage(),
            "📁 Projetos": ProjectPage(),
            "🧩 Business Model Canvas": CanvasPage(),
        }

    # =====================================================
    # Sidebar
    # =====================================================

    def sidebar(self):

        st.sidebar.title("SIPE")

        st.sidebar.caption(
            "Sistema Integrado de Planejamento Estratégico"
        )

        page = st.sidebar.radio(
            "Menu",
            options=list(self.pages.keys()),
            key="navigation_page",
        )

        st.sidebar.divider()

        st.sidebar.caption("Release")

        st.sidebar.info("v0.1")

        return page

    # =====================================================
    # Renderização
    # =====================================================

    def render(self):

        page = self.sidebar()

        self.pages[page].render()
