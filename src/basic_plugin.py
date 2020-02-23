import logging

from ruxit.api.base_plugin import RemoteBasePlugin

logger = logging.getLogger(__name__)


class BasicPlugin(RemoteBasePlugin):

    def query(self, **kwargs) -> None:
        pass




