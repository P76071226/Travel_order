from abc import ABC, abstractmethod

class ValidatorInterface(ABC):
    @abstractmethod
    def validate(self, data):
        pass

