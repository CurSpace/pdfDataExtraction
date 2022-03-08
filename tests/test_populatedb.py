import pytest 
import sys
sys.path.append('..') 
from project0 import project0

def test_populatedb():
    database = 'normanpd.db'
    url = "https://www.normanok.gov/sites/default/files/documents/2022-02/2022-02-01_daily_incident_summary.pdf"
    incident_data = project0.fetchincidents(url)
    incidents = project0.extractincidents(incident_data)
    filledata = project0.populatedb(database,incidents)
    # check if the database has data 
    assert filledata is True
    


