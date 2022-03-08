# cs5293sp22-project0

### Author : Pradipkumar Rajasekaran

__Summary:__

The goal of this project is to extract data from a pdf given a url. The pdf contains data in the form of a table. The contents of this table 
is parsed and extraced. The extracted contents is inserted into a data base. Finally the data is grouped and ordered by the 'nature' field and the 
result is printed.

__Installation__


1. clone the repository- git clone git@github.com:CurSpace/cs5293sp22-project0.git
2. Navigate to the project0 folder - cd "cs5293sp22-project0/project0"
3. Install pipenv - pip install pipenv
4. Install the required packages - pipenv install -r requirements.txt
5. pipenv run pytest

__Python packages used:__

-argparser
-urllib
-tempfile
-PyPDF2
-sqlite3
-pytest
-sys
-PyPDF2

### Description

- The main.py shows the flow of operations.
- The functions are implemted in the project0.py
- Run the program by:
```
   pipenv run python main.py --incidents url
```
- the url is link to a pdf that is a table. For this project i have used the norman police incidents report.
   Ex: 
   
   ```
       pipenv run python main.py --incidents https://www.normanok.gov/sites/default/files/documents/2022-02/2022-02-01_daily_incident_summary.pdf
   ```
   __Sample Output:__
   
 ```
911 Call Nature Unknown 3
Alarm 12
Alarm Holdup/Panic 1
Animal Complaint 1
Animal Dead 2
Animal Injured 2
Animal Livestock 1
Animal Trapped 2
Animal Vicious 3
Animal at Large 4
Assault 3
Assault EMS Needed 4
Assist Fire 1
Back Pain 2
Breathing Problems 7
Burglary 1
COP Activity 2
COP DDACTS 2
COP Relationships 5
Cardiac Respritory Arrest 2
Check Area 9
Chest Pain 4
Contact a Subject 20
Convulsion/Seizure 7
Debris in Roadway 1
Diabetic Problems 2
Disturbance/Domestic 24
Drug Violation 1
Extra Patrol 4
Eye Problems/Injuries 1
Falls 4
Fight 1
Fire Alarm 6
Fire Carbon Monoxide Alarm 2
Fire Controlled Burn 2
Fire Down Power Line 1
Fire Mutual Aid 2
Fire Smoke Investigation 1
Fire Transformer Blown 1
Follow Up 6
Foot Patrol 1
Found Item 6
Fraud 2
Harassment / Threats Report 6
Heart Problems/AICD 3
Heat/Cold Exposure 1
Hemorrhage/Lacerations 1
Hit and Run 2
Indecent Exposure 1
Larceny 12
MVA Non Injury 11
MVA With Injuries 8
Medical Call Pd Requested 7
Motorist Assist 2
Mutual Aid 1
Parking Problem 8
Pick Up Items 3
Pick Up Partner 1
Public Assist 5
Public Intoxication 1
Reckless Driving 1
Road Rage 1
Runaway or Lost Child 2
Sick Person 14
Stroke 3
Supplement Report 4
Suspicious 12
Traffic Stop 30
Transfer/Interfacility 20
Trespassing 5
Unconscious/Fainting 8
Welfare Check 22
 ```
 
 __Description of User Defined Functions:__
 
 1. main() - calls all the functions in the following order:
 
            ```
                  fetch_incidents()
                  
                  extract_incidents(incident_data)
                  
                  createdb()
                  
                  populatedb(db,incidents)
                  
                  statusdb()
            ```
 2. fetch_incidents() - reads the data from the given url as bytes.
 3. extract_incidents() - converts the data into a list of list. Each list contains the rows in the give pdf. 
 4. createdb() - creates a database called 'normanpd.db' with a table called 'incidents'.
 5. populatedb() - inserts the values of the from the pdf to the database
 6. status() - groups by nature and orders by nature
 
 
__Anomalies in the Data__

1. The address might span over two lines.
  Fix - The 2nd line of the address was preceeded by a space and \n. Used regex ' \n' substituted with a space.
  
2. The nature and incidend_ori fields might be missing.
   Fix - Use data as seperator.

__Testing__

1. test_download.py - tests if type of data is bytes
2. test_extractincidents.py - tests for the lenght of data and makes sure the type of data is not NULL
3. test_createdb.py - tests if the database has been created
4. test_populatedb.py - tests if the database has been populated
5. test_status.py - tests if the database has been updated

 
 
