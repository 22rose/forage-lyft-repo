from abc import ABC, abstractmethod
"""Base class for engine"""
"""Adding a new engine is as simple as creating a new
class which implements this given interface."""


class Engine(ABC):
    @abstractmethod
    def needs_service(self):
        pass
