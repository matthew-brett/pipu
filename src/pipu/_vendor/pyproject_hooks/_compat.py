__all__ = ("tomllib",)

import sys

if sys.version_info >= (3, 11):
    import tomllib
else:
    from pipu._vendor import tomli as tomllib
