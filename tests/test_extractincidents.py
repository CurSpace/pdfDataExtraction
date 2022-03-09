
import pytest 
import sys
sys.path.append('..') 
from project0 import project0

def test_size_extractincidents():
    url = "https://www.normanok.gov/sites/default/files/documents/2022-02/2022-02-01_daily_incident_summary.pdf"
    reports = project0.fetchincidents(url)
    # checking for the length of the data and the type of dat
    assert len(reports) > 0
    assert type(reports) is not None
