#!/usr/bin/env python

from pathlib import Path
import sys
import importlib
"""Get exported py-functions for OpenOffice from given script
Return as |-separated string.      
"""


def main(_scr_url: str = None):
    if _scr_url is None:
        return
    _scr_path = Path(_scr_url)
    _parent = _scr_path.parent.as_posix()
    sys.path.append(_parent)

    _mod_name = _scr_path.stem
    try:
        _mod = importlib.import_module(_mod_name)
    except ModuleNotFoundError as e:
        print(f"Can't find module: {e}")
        return None
    except Exception as er:
        return None
    else:
        if _mod and 'g_exportedScripts' in _mod.__dir__():
            _f_list = [_f.__name__ for _f in _mod.g_exportedScripts]
            return '|'.join(_f_list)
        else:
            return None


g_exportedScripts = (
    main,
)

if __name__ == "__main__":
    script_url: str = sys.argv[1]
    script_path = Path(script_url)
    if not script_path.exists():
        print(f'Script {script_url} not exists!')
        exit(1)

    print(main(script_url))
