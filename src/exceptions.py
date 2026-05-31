
class InvalidDictPathError(Exception):

    def __init__(self, dict_path, msg: str|None=None):
        self.dict_path = dict_path
        self.msg = msg or f"Dict path '{self.dict_path}' isn't a valid dict path !"
        super().__init__(self.msg)

    def __str__(self) -> str:
        return self.msg