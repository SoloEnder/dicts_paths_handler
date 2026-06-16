

## v1.3.0 (16/06/2026)

### feature
- calling `get_value` method with "" as `dict_path` now return the value of `base_dict` attribute
- added `get_all_dicts_path` method which returned all the dict_path presents in a dict_path
- 
## v1.2.0 (06/06/2026)

### docs
- added link to the Home page and the issues of the project in the README
- updated the pull request template

### feature
- added the `create_entry` method to the `DictsPathsHandler` for adding a new pair of `key:value` to the `base_dict`.

- added the `delete_entry` method to the ``DictsPathsHandler` for deleting a value of the `base_dict`


### tests
- added tests for the new `create_entry` and `delete_entry` methods

## v1.1.0 (03/06/2026)

### docs 
- added contribution and pull request files
- improved the docstrings of `DictsPathsHandler.get_value()` and `DictsPathsHandler.edit_value()` methods
