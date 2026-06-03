
from .exceptions import InvalidDictPathError
class DictsPathsHandler():

    def __init__(self, base_dict: dict|None=None):
        self.base_dict = base_dict if base_dict else {}

    def get_value(self, dict_path: str):
        """
        Get the value of a dict value by it's dict path and return it.
        setting path must have the following format:
        keyA.keyAA.keyAAA, etc. For exemple : 
        {"general":{"ui":{"theme":"dark"}}
        in this case, the dict path of "theme" will be :
        "general.ui.theme", and this method will return "dark"
        
        Parameters
        ----------
        dict_path: str
            A valid dict_path (following the format defined above)
            
        Raises
        ------
        InvalidDcitPathError: if 'dict_path' isn't a valid dict_path
        """
        path_sections = dict_path.split(".")
        current_value = self.base_dict.copy()

        try:
            for key in path_sections:
                current_value = current_value[key]

        except KeyError:
            raise InvalidDictPathError(dict_path)
        
        else:
            return current_value
    
    def edit_value(self, dict_path, new_value)-> None:
        """
        Replace the value of a key in the dict by <new_value>
        dict_path must have the following format:
        keyA.keyAA.keyAAA, etc. For exemple : 
        {"general":{"ui":{"theme":"dark"}}
        in this case, the dict path of "theme" will be :
        "general.ui.theme"
        
        Parameters
        ----------
        dict_path: str
            A valid dict_path (following the format defined above)
            
        new_value
            The new value that will be assigned to 'dict_path'
            
        Raises
        ------
        InvalidDcitPathError: if 'dict_path' isn't a valid dict_path
        """
        path_sections = dict_path.split(".")
        current_value = self.base_dict.copy()

        try:
            for key in path_sections[:-1]:
                current_value = current_value[key]

            current_value[path_sections[-1]] = new_value

        except KeyError:
            raise InvalidDictPathError(dict_path)
        