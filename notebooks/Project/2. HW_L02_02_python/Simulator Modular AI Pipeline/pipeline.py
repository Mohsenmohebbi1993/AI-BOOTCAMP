

from abc import ABC, abstractmethod
from typing import Any, List


class PipelineStep(ABC):
    """ An abstract base class representing a single step in a processing pipeline. """
    @abstractmethod
    def process(self, data: Any) -> Any:
        """ Processes the input data and returns the result.  
        This method must be implemented by all concrete subclasses. """
        pass



