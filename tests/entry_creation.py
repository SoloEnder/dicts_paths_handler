
from dicts_paths_handler import DictsPathsHandler, NotADictError

a = {
    "general":{
        "theme": {
            "current":"light",
            "choices":("dark", "light", "system")
        },
        "language": {
            "current":"fr",
            "choices":("fr", "en")
        }
    },
    "advanced":{
        "connection": {
            "use_mobile_data":{
                "current":True,
                "choices":(True, False)
            }
        }
    }
}
dph = DictsPathsHandler(a)
path = dph.create_entry("advanced", "dest_folder", "/download")
assert path == "advanced.dest_folder"
assert dph.get_value(path) == "/download"
assert a["advanced"].get("dest_folder")

try:
    dph.create_entry("general.theme.current", "transparency", "false")
    
except NotADictError:
    raise

else:
    raise AssertionError()