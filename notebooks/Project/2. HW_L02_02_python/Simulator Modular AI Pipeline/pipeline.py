

# packages
# The abc package in Python stands for Abstract Base Classes
from abc import ABC, abstractmethod
from typing import Any, List
import re

class PipelineStep(ABC):
    """An abstract base class representing a single step in a processing pipeline """

    @abstractmethod
    def process(self, data: Any) -> Any:
        """
        Processes the input data and returns the result.
        This method must be implemented by all concrete subclasses.
        """
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


class Preprocessor(PipelineStep):
    """ Cleans a list of text strings by converting to lowercase,
    removing punctuation, and stripping extra whitespace. """
    def __init__(self, punctuation_to_remove: str = r'[^\w\s]'):
        self.punctuation_pattern = re.compile(punctuation_to_remove)
        
    def process(self, data: List[str]) -> List[str]:
        """ Applies cleaning steps to each string in the input list."""
        # TODO: Implement the cleaning logic.
        # For each text in the 'data' list, apply:
        # 1. Lowercasing 
        # 2. Punctuation removal using self.punctuation_pattern 
        # 3. Extra whitespace removal
        cleaned_lines = [] # creat empty list
        for text in data:
            text = text.lower()
            text = self.punctuation_pattern.sub("", text)
            text = text.replace("   "," ") # remove 3 space to 1 space
            text = text.replace("  "," ") # remove 2 space to 1 space
            cleaned_lines.append(text)

        return cleaned_lines




PATH = r".\notebooks\Project\2. HW_L02_02_python\Simulator Modular AI Pipeline\TEXT.txt"


read_text = DataLoader()
lines_of_text, counter_line = read_text.process(PATH)
print("TEXT      :", lines_of_text)

preprocessor_text = Preprocessor()

cleaned_lines = preprocessor_text.process(lines_of_text)
print("TEXT clear:", cleaned_lines)
 
