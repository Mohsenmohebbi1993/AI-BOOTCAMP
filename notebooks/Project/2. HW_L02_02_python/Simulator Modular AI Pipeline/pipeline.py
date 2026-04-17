

# packages
# The abc package in Python stands for Abstract Base Classes
from abc import ABC, abstractmethod
from typing import Any, List


class PipelineStep(ABC):
    """ An abstract base class representing a single step in a processing pipeline. """

    @abstractmethod # is used to create one abstract class
    def process(self, data: Any) -> Any:
        """ Processes the input data and returns the result.  
        This method must be implemented by all concrete subclasses. """
        pass


class DataLoader(PipelineStep):
    """ Loads data from a text file, returning a list of lines. """
    def process(self, filepath: str) -> List[str]:
        """ Reads a file from the given filepath and returns its lines as a list of strings.
        Handles FileNotFoundError and other potential exceptions. """ 
        # TODO: Implement file reading logic here.
        # Use a try-except block to handle potential errors.
        # Remember to strip newline characters from each line.
        self.filepath = filepath
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                lines_of_text = f.readlines()
            self.lines_of_text = lines_of_text
            
            # count line
            counter_line = 0
            for _ in lines_of_text:
                counter_line += 1
            return lines_of_text, counter_line
        except FileNotFoundError:
            print("Not Found file, Please enter the correct path")

    def Preprocessor(self):
        return lines_of_text



PATH = r".\notebooks\Project\2. HW_L02_02_python\Simulator Modular AI Pipeline\TEXT.txt"
lines_of_text, counter_line= DataLoader().process(PATH)
a = DataLoader().Preprocessor()

for i in a:
    print(i)



