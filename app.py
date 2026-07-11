"""
SIPE
Sistema Integrado de Planejamento Estratégico

Arquivo principal da aplicação.
"""

from __future__ import annotations

import streamlit as st

from config.settings import settings
from core.application import Application


# ==========================================================
# Configuração da página
# ==========================================================

st.set_page_config(
    page_title=Settings.APP_NAME,
    page_icon=Settings.APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded",
)


# ==========================================================
# Inicialização
# ==========================================================

def main():

    app = Application()

    app.run()


# ==========================================================
# Execução
# ==========================================================

if __name__ == "__main__":

    main()
