"""
SIPE
Sistema Integrado de Planejamento Estratégico

Página Inicial
"""

from __future__ import annotations

import streamlit as st

from core.page import Page
from config import settings


class HomePage(Page):

    id = "home"

    title = "Sistema Integrado de Planejamento Estratégico"

    icon = "🏠"

    def render(self):

        self.page_title()

        st.markdown(
            """
            Bem-vindo ao **SIPE**.

            Esta plataforma auxiliará a elaboração completa do planejamento
            estratégico organizacional.
            """
        )

        st.divider()

        c1, c2, c3 = st.columns(3)

        with c1:

            st.metric(
                "Projeto",
                "Nenhum"
            )

        with c2:

            st.metric(
                "Etapa",
                "-"
            )

        with c3:

            st.metric(
                "Versão",
                settings.VERSION
            )

        st.divider()

        st.subheader("Fluxo do SIPE")

        st.write("""
        1. Cadastro da Empresa

        2. Business Model Canvas

        3. Análise PESTEL

        4. Cinco Forças de Porter

        5. Benchmarking

        6. SWOT

        7. SWOT Cruzada

        8. Identidade Organizacional

        9. Objetivos Estratégicos

        10. Indicadores (KPIs)

        11. Plano de Ação (5W2H)

        12. Gestão de Riscos

        13. Planejamento Financeiro

        14. Dashboard

        15. Relatórios
        """)

        st.divider()

        st.info(
            "Selecione um módulo no menu lateral para iniciar."
        )
