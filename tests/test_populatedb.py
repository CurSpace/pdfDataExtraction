import pytest 
import sys
sys.path.append('..') 
from project0 import project0
import sqlite3

def test_populatedb():
    database = 'normanpd.db'
    url = "https://www.normanok.gov/sites/default/files/documents/2022-02/2022-02-01_daily_incident_summary.pdf"
    incident_data = project0.fetchincidents(url)
    incidents = project0.extractincidents(incident_data)
    filledata = project0.populatedb(database,incidents)
    con=sqlite3.Connection(database)
    cur = con.cursor()
    result = cur.execute('''SELECT count(*) FROM incidents''').fetchone()[0]
    con.close()
    # check if the database has data 
    assert result == 369
    


