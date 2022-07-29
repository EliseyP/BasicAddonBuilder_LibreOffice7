# BasicAddonBuilder_LibreOffice7 

## 0.6.7

`LibreOffice` extension for extension compiling.  

Known instrument from **Paolo Mantovani,** fixed for `LO ver >= 7.1`.

Fixed: toolbar buttons adding.

Finished a feature started by author - **save and load settings of project** (in LO-registry).

### Added features

- Optional creating Update XML file in extension creation dir.
- Optional removing version from extension filename (version is present in the extension itself).  
- Python Libraries support.  

### Python Libraries support

You can select directory with python modules. This directory's structure must be prepared (remember about `pythonpath` directory for other modules). Then it will be copied to extension root and renamed to `python`.  

Extension's name must be set manually if only Python library selected (if both selected - Basic and Python - extension named from Basic library automatically).

Functions from python modules are available for mapping on toolbar or menus creation steps. This functions must be into `g_exportedScripts = ...`.


### TODO: 
- Add other directories and files to extension.