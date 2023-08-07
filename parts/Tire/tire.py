from abc import ABC, abstractmethod
"""Base class for tire"""
"""Adding a new tire is as simple as creating a new
class which implements this given interface."""


class Tire(ABC):
    @abstractmethod
    def needs_service(self):
        pass
