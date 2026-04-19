
from abc import ABC, abstractmethod
# It is used to utilize the capability of abstract classes in Python.


class Shape(ABC):

    @abstractmethod
    def area(self):
        """ Classes that inherit from this must implement the `area` method"""
        pass


