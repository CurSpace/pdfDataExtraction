import pytest 
import sys
sys.path.append('..') 
from project0 import project0

def test_fetchincidents():
    url = "https://www.normanok.gov/sites/default/files/documents/2022-02/2022-02-01_daily_incident_summary.pdf"
    data = project0.fetchincidents(url)
    assert type(data) == bytes