
import json
from typing import List
from datetime import datetime
import config
from model import Issue

# Store issues as singleton to avoid reloads
_ISSUES:List[Issue] = None

class DataLoader:
    """
    Loads the issue data into a runtime object.
    """
    
    def __init__(self):
        """
        Constructor
        """
        self.data_path:str = config.get_parameter('ENPM611_PROJECT_DATA_PATH')
        
    def get_issues(self):
        """
        This should be invoked by other parts of the application to get access
        to the issues in the data file.
        """
        global _ISSUES # to access it within the function
        if _ISSUES is None:
            _ISSUES = self._load()
            print(f'Loaded {len(_ISSUES)} issues from {self.data_path}.')
        return _ISSUES
    
    def _load(self):
        """
        Loads the issues into memory.
        """
        with open(self.data_path,'r') as fin:
            return [Issue(i) for i in json.load(fin)]
    

if __name__ == '__main__':
    # Run the loader for testing
    issues = DataLoader().get_issues()
    for issue in issues:
        issue_dict = issue.__dict__.copy()  # Convert object to dictionary
        issue_dict.pop("text", None)  # Remove 'text' field if it exists

        print(json.dumps(issue_dict, indent=4, default=str))  # Convert everything to string
