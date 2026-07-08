import logging
import sys

logger = logging.getLogger("fastapi-app")
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)

logger.addHandler(handler)