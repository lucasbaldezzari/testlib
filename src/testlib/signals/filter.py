import logging
logger = logging.getLogger(__name__)

class Filter():
    def __init__(self):
            logger.debug("Inicializando Filter")

    def pasabanda(self,signal):
        logger.info("Aplicando pasabanda")

        if signal is None:
                    logger.warning("Entrada vacía")
                    return None
        
        return True
        
    def pasabajos(self,signal):
        logger.info("Aplicando pasabajos")

        if signal is None:
                    logger.warning("Entrada vacía")
                    return None
        
        return True
    
if __name__ == "__main__":
        
    logging.basicConfig(
        level=logging.INFO,
        format="%(name)s - %(levelname)s - %(message)s"
    )

    f = Filter()
    _ = f.pasabanda([10,11,12])