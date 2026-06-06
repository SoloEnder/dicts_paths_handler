
from .exceptions import InvalidDictPathError, NotADictError

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
        
    def create_entry(self, parent_dict_path: str, name: str, value) -> str:
        """
        Creates a new entry and add it as a 'key':'value' to the base dict
        
        Parameters
        ----------
        parent_dict_path (str): the dict_path of the parent of the new entry
        name (str): the name of the new entry (used as a dict key)
        value: the value of the new entry (used as a dict value)
        
        Returns
        -------
        str: the dict_path of the new entry
        
        Raises
        ------
        NotADictError: exception triggered when the value of 'parent_dict_path' is not a dictionnary, unabling the addition
        """
        
        
        parent_dict = self.get_value(parent_dict_path)
        full_path = f"{parent_dict_path}.{name}"
        
        if isinstance(parent_dict, dict):
            parent_dict[name] = value
            self.edit_value(parent_dict_path, parent_dict)
            return full_path
        
        else:
            raise NotADictError(parent_dict_path)
        
    def delete_entry(self, dict_path: str):
        sections = dict_path.split(".")
        parent_dict_path = ".".join(sections[:-1])
        to_delete = dict_path.split(".")[-1]
        
        parent_value = self.get_value(parent_dict_path)
        del parent_value[to_delete]
        self.edit_value(parent_dict_path, parent_value)
        
        
        
        