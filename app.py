"""
SIPE

Ponto de entrada da aplicação.
"""

from sipe.core.application import Application


def main():

    app = Application()

    app.run()


if __name__ == "__main__":

    main()
