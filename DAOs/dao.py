import pickle
from abc import ABC, abstractmethod


class DAO(ABC):
    @abstractmethod
    def __init__(self, datasource=""):
        self.__datasource = datasource
        self.__cache = {}

        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, "wb"))

    def __load(self):
        self.__cache = pickle.load(open(self.__datasource, "rb"))

    def add(self, key, obj):
        self.__cache[key] = obj
        self.__dump()

    def update(self, key, obj):
        if self.has(key):
            self.__cache[key] = obj
            self.__dump()

    def get(self, key):
        try:
            return self.__cache.get(key)
        except KeyError:
            return None

    def remove(self, key):
        try:
            self.__cache.pop(key)
            self.__dump()
        except KeyError:
            return False

    def get_all(self):
        return self.__cache.values()

    def clear(self):
        self.__cache.clear()
        self.__dump()

    def has(self, key):
        """Checa se a chave está presente no dicionário."""
        return key in self.__cache
