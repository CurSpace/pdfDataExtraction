import urllib.request
import tempfile
import PyPDF2
import sqlite3
import re
import numpy as np
import pandas as pd
def fetchincidents(url):
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    data = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()
    return data

def extractincidents(incident_data):
    # Write the pdf data to a temp file
    fp = tempfile.TemporaryFile()
    fp.write(incident_data)

# Set the curser of the file back to the begining
    fp.seek(0)

# Read the PDF
    pdfReader = PyPDF2.pdf.PdfFileReader(fp)
    pagecount = pdfReader.getNumPages()

# get all pages
    allpages = []
    rows = []
    ls = []
    for pagenum in range(0, pagecount):
        pagen = pdfReader.getPage(pagenum).extractText()
        # getting rid of column names and headings in the 1st page
        if pagenum == 0:
            pagen = re.sub('Date / Time\nIncident Number\nLocation\nNature\nIncident ORI\n','',pagen)
            pagen = re.sub('NORMAN POLICE DEPARTMENT\n','',pagen)
            pagen = re.sub('Daily Incident Summary \(Public\)\n','',pagen)
        pagen = re.sub(' \n',' ',pagen)
        pagen = re.split(r'\s+(?=\d?\d?\/\d?\d?\/\d{4} \d?\d?:\d?\d?)', pagen)
        #print(pagen)
        '''
        pagen = pagen.split('\n')
        '''
        for lst in pagen:
            if (len(lst.split('\n')) == 5): # no of values to insert
                ls.append(lst.split('\n'))
       
        #allpages.append(pagen)
        #allpages[pagenum].remove(allpages[pagenum][-1])
        #row = [allpages[pagenum][n:n+5] for n in range(0,len(pagen),5) ]
        #rows.extend(row)
       
    # remove date from last page
    #rows[pagenum].remove(rows[pagenum][-1])
       
    #print(ls)
    #table = np.array(allpages, dtype='object')

        #table = table.reshape([5,5])
    #print(rows)
    return ls


def createdb():
    db = 'normanpd.db'
    con = sqlite3.connect(db)
    cur = con.cursor()

# Create table
    cur.execute(''' DROP TABLE if EXISTS incidents''')
    cur.execute('''CREATE TABLE incidents (
    incident_time TEXT,
    incident_number TEXT,
    incident_location TEXT,
    nature TEXT,
    incident_ori TEXT)''')

# Save (commit) the changes
    con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
    con.close()
    return db

def populatedb(db,incidents):
    print(incidents)
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.executemany('''INSERT INTO incidents values (?,?,?,?,?)''', incidents)
    con.commit()
    con.close()
    return True


def status(db):
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute('''SELECT nature, count(nature) FROM incidents GROUP BY nature ORDER BY nature''' )
    allpages = cur.fetchall()
    for page in allpages:

        print(page[0], page[1])
    con.commit()
    con.close()
    return True