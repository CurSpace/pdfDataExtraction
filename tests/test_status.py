import pytest 
import sys
sys.path.append('..') 
from project0 import project0

def test_status():
    database = 'normanpd.db'
    status = project0.status(database)
    assert len(status) == 73    
