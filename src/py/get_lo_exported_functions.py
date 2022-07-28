#!/usr/bin/env python

from pathlib import Path
import sys
import ast

"""Get exported py-functions for OpenOffice from given script
Return as |-separated string.      
"""


def main(_url: str):
    # from pathlib import Path
    if _url is None:
        return

    text = Path(_url).read_text()

    try:
        code = ast.parse(text)
    except:
        print("pythonscript: getFuncsByUrl: exception while parsing: ")
        raise

    allFuncs = []

    if code is None:
        return allFuncs

    _g_exportedScripts = []
    for node in ast.iter_child_nodes(code):
        if isinstance(node, ast.FunctionDef):
            allFuncs.append(node.name)
        elif isinstance(node, ast.Assign):
            for target in node.targets:
                try:
                    identifier = target.id
                except AttributeError:
                    identifier = ""
                    pass
                if identifier == "g_exportedScripts":
                    for value in node.value.elts:
                        _g_exportedScripts.append(value.id)
                    return '|'.join(_g_exportedScripts)

    return '|'.join(allFuncs)


if __name__ == "__main__":
    script_url: str = sys.argv[1]
    script_path = Path(script_url)
    if not script_path.exists():
        print(f'Script {script_url} not exists!')
        exit(1)

    print(main(script_url))
