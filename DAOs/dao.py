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
        if key in self.__cache:
            self.__cache[key] = obj
            self.__dump()

    def get(self, key):
        if key in self.__cache:
            return self.__cache.get(key)

    def remove(self, key):
        if key in self.__cache:
            self.__cache.pop(key)
            self.__dump()

    def get_all(self):
        return self.__cache.values()

    def clear(self):
        self.__cache.clear()
        self.__dump()
