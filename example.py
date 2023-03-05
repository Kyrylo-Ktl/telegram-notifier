from logging import config, getLogger

from src import LOG_CONFIG

config.dictConfig(LOG_CONFIG)
logger = getLogger(__name__)

logger.info('Some information')
logger.warning('Important information')
