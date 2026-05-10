import logging
from typing import TextIO


DEFAULT_FORMAT = (
    "%(asctime)s | %(levelname)-8s | %(name)s | "
    "%(funcName)s:%(lineno)d | %(message)s"
)


def configure_logging(
    level: int | str = logging.INFO,
    logger_name: str = "testlib",
    stream: TextIO | None = None,
    force: bool = True,
) -> logging.Logger:
    """
    Configura el sistema de logging para testlib.

    Parámetros
    ----------
    level:
        Nivel mínimo de logging. Puede ser logging.DEBUG, logging.INFO,
        logging.WARNING, logging.ERROR o un string como "DEBUG".
    logger_name:
        Nombre del logger a configurar. Por defecto configura todo testlib.
    stream:
        Stream de salida. Por defecto usa sys.stderr.
    force:
        Si es True, fuerza la reconfiguración del logging raíz.

    Retorna
    -------
    logging.Logger
        Logger configurado.
    """
    logging.basicConfig(
        level=level,
        format=DEFAULT_FORMAT,
        stream=stream,
        force=force,
    )

    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    return logger