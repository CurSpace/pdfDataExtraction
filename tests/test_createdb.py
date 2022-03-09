
import pytest 
import sys
sys.path.append('..') 
from project0 import project0
import os.path
path=os.getcwd()

def test_createdb():
    project0.createdb()
    path1=path+'/normanpd.db'
    # testing if the databse has been created
    assert os.path.exists(path1)
