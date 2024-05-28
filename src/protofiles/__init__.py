from os.path import dirname, basename, isfile, join
import os
import sys
import glob
modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [basename(f)[:-3] for f in modules if isfile(f)
           and not f.endswith('__init__.py')]
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
