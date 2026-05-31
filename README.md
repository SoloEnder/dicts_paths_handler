# dicts_paths_handler
A library that allows access to Python dictionary values in a more readable way by separating keys using dot notation.

## Installation
```bash
pip install dicts_paths_handler 
#or
py -m pip install dicts_paths_handler
```

## Usage :
First, create a new instance of DictsPathsHandler :

```py
import dicts_paths_handler

your_dict = {
    "language":{
        "availables":("Python", "C", "Java", "C#"),
        "selected":"Python",
    }
}
dph = dicts_paths_handler.DictsPathsHandler(your_dict)
```

You can access any value in  `your_dict` simply by calling its 'dict_path'. In the following example, we want to access to the value of  `your_dict['language']['selected']`

```py
selected_language = dph.get_value("language.selected")
print(selected_language)

# Should print 'Python'
```
An `InvalidDictPathError` exception will be raised if the dict_path is not found or invalid

You can also edit a value. In this example, we want to change the value of  `your_dict[language]['selected']` :

```py
dph.edit_value("language.selected", "C#")
print(dph.get_value("language.selected")) # Should print 'C#'
```
An `InvalidDictPathError` exception will be raised if the dict path is not found or invalid 

## How does it work ?
Each key of the dict is a part of the dict path, in the normal order of python dict keys : keyA.keyAA.keyAAA.


