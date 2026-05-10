import logging
logger = logging.getLogger(__name__)

def show() -> None:
    logger.info("Mostrando imagen")
    logger.debug("Función show ejecutada desde %s", __name__)