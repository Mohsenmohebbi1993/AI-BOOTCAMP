
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
            text = text.replace("    "," ") # remove 4 space to 1 space
            text = text.replace("   "," ") # remove 3 space to 1 space
            text = text.replace("  "," ") # remove 2 space to 1 space
            cleaned_lines.append(text)

        return cleaned_lines


class Analyzer(PipelineStep):
    """ Analyzes the text data to compute basic statistics. """ 

    def process(self, data: List[str]) -> dict:
        """ Calculates total lines, average words per line, and number of unique words. """
        # TODO: Implement the analysis logic here
        # Calculate the required statistics and return them in a dictionary
        # Handle the case where the input data is empty
        # # For unique words, using a set is a good approach. pass

        print("----Calculate line, world in each line, avrage world and total world----")
        # 1. count number of line
        total_line_in_text = len(data)
        print(f"Total line in all text is : {total_line_in_text}")

        # 2. count total word in each line
        # 3. count word in all text
        # 4. fund avrage word in line
        total_word_in_each_line = {} # dict of line and wold
        counter_word_in_all_text = 0 # count world

        for number_line in range(len(data)):
            list_of_line = data[number_line].split() # create list for count word
            number_word = len(list_of_line) # count word in each line

            counter_word_in_all_text += number_word # add count word in each line to all
            total_word_in_each_line[f"line {number_line+1}"] = number_word # creat dict fram line and count word

        avrage_word_in_each_line = counter_word_in_all_text / len(data) # avrage world
        # 5. print result by f-string
        print(f"world in each line : {total_word_in_each_line}")
        print(f"avrage world in each line : {avrage_word_in_each_line}")
        print(f"total world in text : {counter_word_in_all_text}")



PATH = r"C:\Mohsen Folder\Ai Bootcamp\Ai Bootcamp\notebooks\Project\2. HW_L02_02_python\Simulator Modular AI Pipeline\TEXT.txt"

# 1 -----------------------
lines_of_text, counter_line = DataLoader().process(PATH)
print("TEXT      :", lines_of_text)
# 2 -----------------------
cleaned_lines = Preprocessor().process(lines_of_text)
print("TEXT clear:", cleaned_lines)
# 3 -----------------------
Analyzer().process(cleaned_lines)

