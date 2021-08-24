import logging
from pathlib import Path

class Utils:
    @classmethod
    def manageGlobalLogger(cls, name: str):

        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        cls.__logFolder();

        fh = logging.FileHandler('logs/greetingdto.log')
        fh.setLevel(logging.INFO)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(ch)

        return logger
    
    @classmethod
    def __logFolder(cls):
        Path("logs/").mkdir(parents=True, exist_ok=True)