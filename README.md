# cs5293sp22-project0

### Author : Pradipkumar Rajasekaran

__Summary:__

The goal of this project is to extract data from a pdf given a url. The pdf contains data in the form of a table. The contents of this table 
is parsed and extraced. The extracted contents is inserted into a data base. Finally the data is grouped and ordered by the 'nature' field and the 
result is printed.

## Developement Process

- Created main.py with the funcions call in the right sequence.
- Created project0.py with function definitions.
- Fetch the data.
- Extract data using Py2PDF and regex to remove the headers and footers. 
- Created database 'normapd.db' with table incidents.

__Installation__


1. Clone the repository- git clone git@github.com:CurSpace/cs5293sp22-project0.git
2. Navigate to the project0 folder - cd "cs5293sp22-project0/project0"
3. Install pipenv - pip install pipenv
4. Install the required packages - pipenv install -r requirements.txt
5. Navigate to test folder and run pytest - pipenv run pytest


__Python packages used:__

- argparser
- urllib
- tempfile
- PyPDF2
- sqlite3
- pytest
- sys
- PyPDF2

### Description

- The main.py controls the flow of operations.
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

 
 __Description of User Defined Functions:__
 
 1. main() - calls all the functions in the following order:
 
           ```
                  fetch_incidents(url)
                  
                  extract_incidents(incident_data)
                  
                  createdb()
                  
                  populatedb(db,incidents)
                  
                  statusdb(db)
           ```
 2. fetch_incidents() 
    ->  reads the data from the given url.

 3. extract_incidents()

    -> Loops through all the pages.

    -> The headers, footers and column names are removed using the
       re.sub() function.
 
    ->  Each list contains the rows in the give pdf. The headers, footers and column names are removed using the
       re.sub() function.

    -> Sustitutes space before \n to solve the issue when the address span over 2 lines.

    -> Spilits by date to get a list of list.

    -> Checks the inner list to see if it has 5 elements. I this is true then it means 
       that all the fields exist. If not then fields 3 and 4 are empty in this case we 
       fill the fields with N/A.
             
 4. createdb() 

    -> create a database called 'normanpd.db'
    -> create table called 'incidents'.

 5. populatedb() 

    -> insterts values returned by extract_incidents()into the table incidents.
 
 6. status() 

    -> Executes a select statement that returns unique nature and the number of ocurrences of each.


    __Sample Output:__
   
 ```
9Alarm | 12
Alarm Holdup/Panic | 1
Animal Complaint | 1
Animal Dead | 2
Animal Injured | 2
Animal Livestock | 1
Animal Trapped | 2
Animal Vicious | 3
Animal at Large | 4
Assault | 3
Assault EMS Needed | 4
Assist Fire | 1
Back Pain | 2
Breathing Problems | 7
Burglary | 1
COP Activity | 2
COP DDACTS | 2
COP Relationships | 5
Cardiac Respritory Arrest | 2
Check Area | 9
Chest Pain | 4
Contact a Subject | 20
Convulsion/Seizure | 7
Debris in Roadway | 1
Diabetic Problems | 2
Disturbance/Domestic | 24
Drug Violation | 1
Extra Patrol | 4
Eye Problems/Injuries | 1
Falls | 4
Fight | 1
Fire Alarm | 6
Fire Carbon Monoxide Alarm | 2
Fire Controlled Burn | 2
Fire Down Power Line | 1
Fire Mutual Aid | 2
Fire Smoke Investigation | 1
Fire Transformer Blown | 1
Follow Up | 6
Foot Patrol | 1
Found Item | 6
Fraud | 2
Harassment / Threats Report | 6
Heart Problems/AICD | 3
Heat/Cold Exposure | 1
Hemorrhage/Lacerations | 1
Hit and Run | 2
Indecent Exposure | 1
Larceny | 12
MVA Non Injury | 11
MVA With Injuries | 8
Medical Call Pd Requested | 7
Motorist Assist | 2
Mutual Aid | 1
N/A | 6
Parking Problem | 8
Pick Up Items | 3
Pick Up Partner | 1
Public Assist | 5
Public Intoxication | 1
Reckless Driving | 1
Road Rage | 1
Runaway or Lost Child | 2
Sick Person | 14
Stroke | 3
Supplement Report | 4
Suspicious | 12
Traffic Stop | 30
Transfer/Interfacility | 20
Trespassing | 5
Unconscious/Fainting | 8
Welfare Check | 22
 ```
__Assumptions__

1. Assuming that if address is empty then nature is empty.

2. Headers and footers exist only on the first and last pages respectively.

3. Assumming only nature and address fields are empty.

4. If the address is 2 lines then the 2nd line has an empty in front.
 
 
__Anomalies in the Data__

1. The address might span over two lines.
  Fix - The 2nd line of the address was preceeded by a space and \n. Used regex ' \n' and substituted with a space.
  
2. The nature and incidend_ori fields might be missing.
   Fix - Use date as seperator and when the list size is 3 shift the element in the 3rd field to the 5th field and insert N/A into the 3rd and 4th fields.


__Testing__

1. test_download.py

   -> tests if data exists and the  type of data is bytes

2. test_extractincidents.py

   -> tests if the lenght of data is greater than zero and makes sure the type of data is not None

3. test_createdb.py 

   -> tests if the normanpd.pd file exists in the current working directory
   
4. test_populatedb.py 

   -> tests if the number of rows inserted for a particular pdf which is 369 in this case.

5. test_status.py
 
   -> test if the distinct count of nature is 73.

 
 
