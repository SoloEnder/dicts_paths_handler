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
dph.delete_entry("general.theme.current")
assert a["general"]["theme"].get("current")