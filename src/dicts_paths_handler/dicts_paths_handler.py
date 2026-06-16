from .exceptions import InvalidDictPathError, NotADictError


class DictsPathsHandler:
    def __init__(self, base_dict: dict | None = None):
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

        if dict_path == "":
            return self.base_dict

        path_sections = dict_path.split(".")
        current_value = self.base_dict.copy()

        try:
            for key in path_sections:
                current_value = current_value[key]

        except KeyError:
            raise InvalidDictPathError(dict_path)

        else:
            return current_value

    def edit_value(self, dict_path, new_value) -> None:
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

    def get_all_dicts_paths(self, base_path: str) -> list[str] | list:
        """
        Walk trough the values of a dict_path and return their dict_path

        Parameters
        ----------
        `base_path(str)`: the base dict path where the walk start

        Returns
        -------
        list: a list containing all the dicts_paths found

        Note
        ----
        If `initial_path` is equal to "", then "" will be in the returned list
        """

        current_path = base_path
        cheched_paths = []
        all_dicts_paths = self._walk(current_path, cheched_paths, current_path)

        if all_dicts_paths is None:
            all_dicts_paths = []

        return all_dicts_paths

    def _walk(
        self, current_path: str, checked_paths: list, initial_path: str
    ) -> list[str]:
        """
        Walk trough the values of a dict_path and return their dict_path

        Parameters
        ----------
        `current_path(str)`: The currently traversed path.
        `checked_path(list)`: The paths already traversed by the method; must initially be an empty list.
        `initial_path(str)`: The first path traversed by the function (normally equal to `current_path` when this function is called).

        Returns
        -------
        list: a list containing all the dicts_paths found

        Note
        ----
        If `initial_path` is equal to "", then "" will be in the returned list
        """
        content = self.get_value(current_path)

        if isinstance(content, dict):
            for key in content:
                potential_path = current_path + "." + key

                if potential_path.startswith("."):
                    potential_path = potential_path.replace(".", "", 1)

                if potential_path not in checked_paths:
                    print(f"- Found one untested path ({potential_path}) rewalking")
                    current_path = potential_path
                    return self._walk(current_path, checked_paths, initial_path)

            else:
                old_current_path = current_path
                checked_paths.append(current_path)
                current_path = ".".join(current_path.split(".")[:-1])

                if current_path:
                    if not current_path == initial_path:
                        return self._walk(current_path, checked_paths, initial_path)

                    else:
                        return checked_paths

                else:
                    if old_current_path in self.base_dict.keys():
                        print(f"{old_current_path=}")
                        return self._walk("", checked_paths, initial_path)

                    else:
                        return checked_paths

        else:
            checked_paths.append(current_path)
            current_path_splited = current_path.split(".")
            current_path = ".".join(current_path_splited[:-1])
            return self._walk(current_path, checked_paths, initial_path)
