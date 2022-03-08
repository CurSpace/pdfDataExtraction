from importlib_metadata import NullFinder
import pytest 
import sys
sys.path.append('..') 
from project0 import project0

def test_createdb():
    database = project0.createdb()
    # testing if the databse has been created
    assert database is not None