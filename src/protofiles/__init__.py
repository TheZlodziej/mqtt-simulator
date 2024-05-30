from os.path import dirname, basename, isfile, join, abspath, dirname
from sys import path
from glob import glob
modules = glob(join(dirname(__file__), "*.py"))
__all__ = [basename(f)[:-3] for f in modules if isfile(f)
           and not f.endswith('__init__.py')]
path.insert(0, abspath(dirname(__file__)))
