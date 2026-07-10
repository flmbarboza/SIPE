from config import settings, theme, app_logger
from config.paths import create_directories

create_directories()

print(settings.APP_NAME)
print(settings.VERSION)
print(theme.PRIMARY)
app_logger.info("SIPE iniciado com sucesso.")
