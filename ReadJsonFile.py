import json
from abc import ABC, abstractmethod


class AbstractRid(ABC):
    @abstractmethod
    def read_json(self, filename):
        pass


class ReadJson(AbstractRid):
    """This class rid json files"""

    def read_json(self, filename):
        with open(filename, 'r') as file:
            data = json.loads(file.read())
            return data
