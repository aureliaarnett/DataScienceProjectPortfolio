# Aurelia Arnett
# Objective: Demonstrate ability to combine datasets and produce meaningful analysis. The goal is to provide more than just data but with insights, understanding, and wisdom
# Case: To recommend the best salary for the next football coach


##### PHASE 1: OBTAIN & SCRUB DATA, DATA DISCOVERY, & DATA PRE-PROCESSING #####
# Import function to call in the Coaches dataset
import csv
# Function to process dataset into a pandas dictionary for data cleansing
import pandas as pd

# Read in data & preprocess for calculations
coaches = 'Coaches9.csv'
# convert data in csv to pandas dataframe that you can float variables to convert later
coachesList = [] # Create a list to store column variables

with open(coaches, mode='r') as csvfile: # open the csv file into the program
   coachesReader = csv.reader(csvfile, dialect='excel')

# Represent the data as a list dictionaries
   for line in coachesReader:
      if line[0].startswith('ï»¿School'): #skip first row containing column titles
         continue
      else:
         coach = {}
         coach['School'] = line[0] 
         coach['Conference'] = line[1]
         coach['Coach'] = line[2]   

# Cleanse variables that are blank (represented as '--') and have extra characters (such as '$' and ',')
# Convert dollars to type int in order to use in calculations and graphics
         line[3] = line[3].replace(",","")
         line[3] = line[3].replace("--","0")
         if line[3].startswith('$'):
            line[3] = line[3].replace("$", "")
            coach['SchoolPay'] = int(line[3])
         else:
            coach['SchoolPay'] = int(line[3])

# repeat for remaining columns:
         line[4] = line[4].replace(",","")
         line[4] = line[4].replace("--","0")
         if line[4].startswith('$'):
            line[4] = line[4].replace("$", "")
            coach['TotalPay'] = int(line[4])
         else:
            coach['TotalPay'] = int(line[4])

         line[5] = line[5].replace(",","")
         line[5] = line[5].replace("--","0")
         if line[5].startswith('$'):
            line[5] = line[5].replace("$", "")
            coach['Bonus'] = int(line[5])
         else:
            coach['Bonus'] = int(line[5])

         line[6] = line[6].replace(",","")
         line[6] = line[6].replace("--","0")
         if line[6].startswith('$'):
            line[6] = line[6].replace("$", "")
            coach['BonusPaid'] = int(line[6])
         else:
            coach['BonusPaid'] = int(line[6])

         line[7] = line[7].replace(",","")
         line[7] = line[7].replace("--","0")
         if line[7].startswith('$'):
            line[7] = line[7].replace("$", "")
            coach['AssistantPay'] = int(line[7])
         else:
            coach['AssistantPay'] = int(line[7])

         line[8] = line[8].replace(",","")
         line[8] = line[8].replace("--","0")
         if line[8].startswith('$'):
            line[8] = line[8].replace("$", "")
            coach['Buyout'] = int(line[8])
         else:
            coach['Buyout'] = int(line[8])

         coachesList.append(coach)
csvfile.close()


# Convert list into pandas dataframe
coachesData = pd.DataFrame(coachesList)

# Review data to ensure it's properly called in:
#print('Table containing coaches data')
del coachesData['TotalPay'] # remove TotalPay as it's nearly the same as SchoolPay and will skew data modeling
del coachesData['AssistantPay'] # will not use this column
#print(coachesData[0:5]) #Preview the dataframe
#print(coachesData['SchoolPay'][0:5]) #Confirm data cleansing returned properly
#print('Number of schools in coaches dataframe: ', len(coachesList)) #129 coaches in dataset
#print()
# Dataframe is ready for analysis



# ADDITIONAL DATA: Read in Graduation Rate data
gradRateData = pd.read_csv("DS4-D1GradSuccess.tsv", sep='\t') # read in the tsv data file
#print(gradRateData.columns[0:5]) # examine the first few columns to understand what data exists
#print(gradRateData) #Data for 345 schools exist
gradRateData = gradRateData.loc[:,["SCL_NAME","DIV1_FB_CONFERENCE","FED_N_SA", "FED_RATE_SA", "GSR_N_SA", "GSR_SA"]]

#print(gradRateData["SCL_NAME"].to_list()) #School names audit in order to match this dataset to Coaches

# UPDATE COLUMN DATA: Update school names in the conference dataframe to match the coaches dataset
gradRateData["SCL_NAME"] = gradRateData["SCL_NAME"].replace("United States Air Force Academy", "Air Force")
gradRateData["SCL_NAME"] = gradRateData["SCL_NAME"].replace("University of Akron Main Campus", "Akron")
coachesData['School'] = coachesData['School'].replace("Alabama","The University of Alabama") #Multiple instances of 'Alabama' exist in the grad rating dataset so need to update the school name in the coaches dataset so that the program is clear when matching schools to add the scores
gradRateData["SCL_NAME"] = gradRateData["SCL_NAME"].replace("Arizona State University-Tempe', 'University of Arizona'", "Arizona State")
gradRateData["SCL_NAME"] = gradRateData["SCL_NAME"].replace("University of Arizona", "Arizona")
coachesData['School'] = coachesData['School'].replace("Arkansas","University of Arkansas")
gradRateData["SCL_NAME"] = gradRateData["SCL_NAME"].replace("Arkansas State University-Main Campus", "Arkansas State")
gradRateData["SCL_NAME"] = gradRateData["SCL_NAME"].replace("United States Military Academy", "Army")
coachesData['School'] = coachesData['School'].replace("California","University of California-Berkeley")
coachesData['School'] = coachesData['School'].replace("Colorado","University of Colorado Boulder")
gradRateData["SCL_NAME"] = gradRateData["SCL_NAME"].replace("Colorado State University-Fort Collins", "Colorado State")
coachesData['School'] = coachesData['School'].replace("Connecticut","University of Connecticut")
coachesData['School'] = coachesData['School'].replace("Florida","University of Florida")
coachesData['School'] = coachesData['School'].replace("Georgia","University of Georgia")
gradRateData["SCL_NAME"] = gradRateData["SCL_NAME"].replace("Georgia Institute of Technology-Main Campus", "Georgia Tech")
coachesData['School'] = coachesData['School'].replace("Houston","University of Houston")
coachesData['School'] = coachesData['School'].replace("Illinois","University of Illinois at Urbana-Champaign")
coachesData['School'] = coachesData['School'].replace("Indiana","Indiana University-Bloomington")
coachesData['School'] = coachesData['School'].replace("Iowa","University of Iowa")
coachesData['School'] = coachesData['School'].replace("Kansas","University of Kansas")
coachesData['School'] = coachesData['School'].replace("Kentucky","University of Kansas")
coachesData['School'] = coachesData['School'].replace("Louisiana-Lafayette","University of Louisiana at Layfayette")
coachesData['School'] = coachesData['School'].replace("Louisiana-Monroe","University of Louisiana at Monroe")
gradRateData["SCL_NAME"] = gradRateData["SCL_NAME"].replace("Louisiana State University and Agricultural & Mechanical College", "LSU")
coachesData['School'] = coachesData['School'].replace("Maryland","University of Maryland-College Park")
gradRateData["SCL_NAME"] = gradRateData["SCL_NAME"].replace("University of Miami", "Miami (Fla.)")
gradRateData["SCL_NAME"] = gradRateData["SCL_NAME"].replace("Miami University-Oxford", "Miami (Ohio)")
coachesData['School'] = coachesData['School'].replace("Michigan","University of Michigan-Ann Arbor")
coachesData['School'] = coachesData['School'].replace("Mississippi","University of Mississippi")
coachesData['School'] = coachesData['School'].replace("Missouri","University of Missouri-Columbia")
gradRateData["SCL_NAME"] = gradRateData["SCL_NAME"].replace("United States Naval Academy", "Navy")
coachesData['School'] = coachesData['School'].replace("Nevada","University of Nevada-Reno")
coachesData['School'] = coachesData['School'].replace("Nevada-Las Vegas","University of Nevada-Las Vegas")
coachesData['School'] = coachesData['School'].replace("North Carolina","University of North Carolina at Chapel Hill")
coachesData['School'] = coachesData['School'].replace("Northwestern","Northwestern University")
coachesData['School'] = coachesData['School'].replace("Ohio","Ohio University")
coachesData['School'] = coachesData['School'].replace("Penn State","Pennsylvania State University-Main Campus")
coachesData['School'] = coachesData['School'].replace("Purdue","Purdue University-Main Campus")
coachesData['School'] = coachesData['School'].replace("South Carolina","University of South Carolina-Columbia")
coachesData['School'] = coachesData['School'].replace("Tennessee","The University of Tennessee-Knoxville")
coachesData['School'] = coachesData['School'].replace("Texas","The University of Texas at Austin")
coachesData['School'] = coachesData['School'].replace("Texas A&M","Texas A & M University-College Station")
coachesData['School'] = coachesData['School'].replace("Texas-El Paso","The University of Texas at El Paso")
coachesData['School'] = coachesData['School'].replace("Texas-San Antonio","The University of Texas at San Antonio")
coachesData['School'] = coachesData['School'].replace("UCLA","University of California-Los Angeles")
coachesData['School'] = coachesData['School'].replace("Utah","University of Utah")
coachesData['School'] = coachesData['School'].replace("Virginia","University of Virginia-Main Campus")
gradRateData["SCL_NAME"] = gradRateData["SCL_NAME"].replace("Virginia Polytechnic Institute and State University", "Virginia Tech")
coachesData['School'] = coachesData['School'].replace("Washington", "University of Washington-Seattle Campus")
coachesData['School'] = coachesData['School'].replace("Wisconsin", "University of Wisconsin-Madison")

#print('Table containing graduation data')
#print(gradRateData[0:5])
#print('Number of schools in graduation dataframe:', len(gradRateData))
#print()


def lookup_FGR(ip):
   for column in gradRateData.itertuples():
      if (ip in column[1]):
         return column[4]

coachesData['FGR'] = coachesData['School'].apply(lookup_FGR)
#print(coachesData)
#print(gradRateData)
#print(gradRateData["FED_RATE_SA"].to_list())

def lookup_GSR(ip):
   for column in gradRateData.itertuples():
      if (ip in column[1]):
         return column[6]
coachesData['GSR'] = coachesData['School'].apply(lookup_GSR)



# ADDITIONAL DATA: Read in Stadium Size
import requests #library to process web urls
website_url = requests.get('https://en.wikipedia.org/wiki/List_of_NCAA_Division_I_FBS_football_stadiums').text
from bs4 import BeautifulSoup
soup = BeautifulSoup(website_url,'lxml')

#print(soup.title)
#print(soup.prettify()) #View the underlying HTML for the page to understand how the data fits in
#print(soup.p) #View first paragraph on the page
#print(soup.a) #View first link type on the page
#for anchor in soup.find_all('a'): #View links on the page
#   print(anchor.get('href', '/'))

#all_tables=soup.find_all("table") #View all tables on the page
#print(all_tables)


My_table = soup.find('table',{'class':'wikitable sortable'}) #Find the table that has the stadium, school, and capacity information
#print(My_table)
### NOTES ABOUT THE CAPACITY TABLE ###
#1. We can't just pull links (<a href>) in this case because the capacity isn't linked
#2. The table is set up in rows (starting with <tr> tags) with the data sitting within <td> tags in ea row
#3. We aren't too worried about the header row with the <th> elements since we know what ea of the columns represent by looking at the table
#4. Let's look through the rows to get the data for every club in the table: In the Wikipedia stadium size table, there are only 4 columns I care about: Team, Conference, Capacity, and Record. However I need to set up empty lists to store ea column in (there are 11 columns).

A=[] #store data for column 2 (skip column 1 containing image because no text exists here)
B=[] #store data for column 3, and so on
C=[]
D=[]
E=[]
F=[]
G=[]
H=[]
I=[]
J=[]

# Now set up the loop to search each row for the appropriate <td> tags with the 'td' string (the data)
for row in My_table.findAll('tr'): # start with tr as the head of ea row
   cells = row.findAll('td')         #the var 'cells' will store the data; now use td to search for the tags
   if len(cells) == 11:
      A.append(cells[1].find(text=True))
      B.append(cells[2].find(text=True))
      C.append(cells[3].find(text=True))
      D.append(cells[4].find(text=True))
      E.append(cells[5].find(text=True))
      F.append(cells[6].find(text=True))
      G.append(cells[7].find(text=True))
      H.append(cells[8].find(text=True))
      I.append(cells[9].find(text=True))
      J.append(cells[10].find(text=True))


# Convert capacity data to int for future calculation:
F = [n.replace(",","") for n in F]
F = [int(n) for n in F]
#print(F)
G = [n.replace(",","") for n in G]
G = [n.replace("\n","0") for n in G]
G = [n.replace("*","") for n in G]
G = [int(n) for n in G]
#print(G)

# Now create a dataframe to call store data:
capacityFrame = pd.DataFrame(D, columns=['School'])
#Texas-San Antonio = UTSA

capacityFrame['Conference'] = E
capacityFrame['Capacity'] = F
#capacityFrame['RecordAttendance'] = G # Note that column G is record attendance which we do not necessarily need to account for so let's remove this column. Some records account for COVID while others don't causing discrepancies
# Note: I only wanted a table of the 4 columns however I can pull more column data if I determine it to be useful later#
#print('Table containing capacity data')
#print(capacityFrame[0:5])
#print('Number of schools in capacity dataframe:', len(capacityFrame))
#print()

#print(D) #School names audit in order to match this dataset to Coaches
# UPDATE COLUMN DATA: Update school names in the capacity dataframe to match the coaches dataset
#print(A2) #School names audit in order to match this dataset to Coaches
# UPDATE COLUMN DATA: Update school names in the records dataframe to match the coaches dataset
capacityFrame["School"] = capacityFrame["School"].replace("Alabama", "The University of Alabama")
capacityFrame['School'] = capacityFrame['School'].replace("Arkansas","University of Arkansas")
capacityFrame['School'] = capacityFrame['School'].replace("California","University of California-Berkeley")
capacityFrame['School'] = capacityFrame['School'].replace("Colorado","University of Colorado Boulder")
capacityFrame['School'] = capacityFrame['School'].replace("Connecticut","University of Connecticut")
capacityFrame['School'] = capacityFrame['School'].replace("Florida","University of Florida")
capacityFrame['School'] = capacityFrame['School'].replace("Georgia","University of Georgia")
capacityFrame['School'] = capacityFrame['School'].replace("Houston","University of Houston")
capacityFrame['School'] = capacityFrame['School'].replace("Illinois","University of Illinois at Urbana-Champaign")
capacityFrame['School'] = capacityFrame['School'].replace("Indiana","Indiana University-Bloomington")
capacityFrame['School'] = capacityFrame['School'].replace("Iowa","University of Iowa")
capacityFrame['School'] = capacityFrame['School'].replace("Kentucky","University of Kansas")
capacityFrame['School'] = capacityFrame['School'].replace("Kansas","University of Kentucky")
capacityFrame["School"] = capacityFrame["School"].replace("Louisiana", "Louisiana-Lafayette")
capacityFrame["School"] = capacityFrame["School"].replace("Louisiana–Monroe", "Louisiana-Monroe")
capacityFrame['School'] = capacityFrame['School'].replace("Maryland","University of Maryland-College Park")
capacityFrame['School'] = capacityFrame['School'].replace("Michigan","University of Michigan-Ann Arbor")
capacityFrame['School'] = capacityFrame['School'].replace("Mississippi","University of Mississippi")
capacityFrame['School'] = capacityFrame['School'].replace("Missouri","University of Missouri-Columbia")
capacityFrame['School'] = capacityFrame['School'].replace("Nevada","University of Nevada-Reno")
capacityFrame['School'] = capacityFrame['School'].replace("Nevada-Las Vegas","University of Nevada-Las Vegas")
capacityFrame['School'] = capacityFrame['School'].replace("North Carolina","University of North Carolina at Chapel Hill")
capacityFrame['School'] = capacityFrame['School'].replace("Penn State","Pennsylvania State University-Main Campus")
capacityFrame['School'] = capacityFrame['School'].replace("Texas A&M","Texas A & M University-College Station")
capacityFrame['School'] = capacityFrame['School'].replace("Texas-El Paso","The University of Texas at El Paso")
capacityFrame['School'] = capacityFrame['School'].replace("Texas-San Antonio","The University of Texas at San Antonio")
capacityFrame['School'] = capacityFrame['School'].replace("UCLA","University of California-Los Angeles")
capacityFrame["School"] = capacityFrame['School'].replace("Washington","University of Washington-Seattle Campus")
capacityFrame["School"] = capacityFrame['School'].replace("Wisconsin", "University of Wisconsin-Madison")
capacityFrame["School"] = capacityFrame["School"].replace("BYU", "Brigham Young")
capacityFrame["School"] = capacityFrame["School"].replace("FIU", "Florida International")
capacityFrame["School"] = capacityFrame["School"].replace("Miami (FL)", "Miami (Fla.)")
capacityFrame["School"] = capacityFrame["School"].replace("Miami (OH)", "Miami (Ohio)")
capacityFrame["School"] = capacityFrame["School"].replace("NC State", "North Carolina State")
capacityFrame["School"] = capacityFrame["School"].replace("SMU", "Southern Methodist")
capacityFrame["School"] = capacityFrame["School"].replace("Southern Miss", "Southern Mississippi")
capacityFrame["School"] = capacityFrame["School"].replace("TCU", "Texas Christian")
capacityFrame["School"] = capacityFrame["School"].replace("UAB", "Alabama at Birmingham")
capacityFrame["School"] = capacityFrame["School"].replace("UCF", "Central Florida")
capacityFrame["School"] = capacityFrame["School"].replace("UConn", "Connecticut")
capacityFrame["School"] = capacityFrame["School"].replace("UMass", "Massachusetts")
capacityFrame["School"] = capacityFrame["School"].replace("UNLV", "Nevada-Las Vegas")
capacityFrame["School"] = capacityFrame["School"].replace("USC", "Southern California")
capacityFrame["School"] = capacityFrame["School"].replace("UTEP", "Texas-El Paso")
capacityFrame["School"] = capacityFrame["School"].replace("UTSA", "Texas-San Antonio")

def lookup_capacity(ip):
   for column in capacityFrame.itertuples():
      if (ip in column[1]):
         return column[3]
coachesData['StadiumSize'] = coachesData['School'].apply(lookup_capacity)
#print(coachesData)




# ADDITIONAL DATA: Read in win-loss records
records_url = requests.get('https://en.wikipedia.org/wiki/NCAA_Division_I_FBS_football_win-loss_records').text
soup2 = BeautifulSoup(records_url,'lxml')

My_table2 = soup2.find('table',{'class':'wikitable sortable'}) #Find the table that has the win-loss records
#print(My_table2)

A2=[] #store data for column 1
B2=[] #store data for column 2, and so on
C2=[]
D2=[]
E2=[]
F2=[]
G2=[]
H2=[]

for row in My_table2.findAll('tr'): # start with tr as the head of ea row
   cells = row.findAll('td')         #the var 'cells' will store the data; now use td to search for the tags
   if len(cells) == 8:
      A2.append(cells[0].find(text=True))
      B2.append(cells[1].find(text=True))
      C2.append(cells[2].find(text=True))
      D2.append(cells[3].find(text=True))
      E2.append(cells[4].find(text=True))
      F2.append(cells[5].find(text=True))
      G2.append(cells[6].find(text=True))
      H2.append(cells[7].find(text=True))

# Convert won, lost, tied, percent, and total games data to int for future calculation:
B2 = [int(n) for n in B2]
C2 = [int(n) for n in C2]
D2 = [int(n) for n in D2]
G2 = [int(n) for n in G2]
H2 = [char.replace("\n","") for char in H2]

# Now create a dataframe to call store data:
recordsFrame = pd.DataFrame(A2, columns=['School'])
recordsFrame['Conference'] = H2
recordsFrame['Won'] = B2
recordsFrame['Loss'] = C2
recordsFrame['Tied'] = D2
recordsFrame['TotalGames'] = G2
recordsFrame['PercentWin'] = round((recordsFrame['Won']/(recordsFrame['Won']+recordsFrame['Loss']+recordsFrame['Tied'])),3)


#print('Table containing record data')
#print(recordsFrame[0:5])
#print('Number of schools in records dataframe:', len(recordsFrame))
#print()

#print(A2) #School names audit in order to match this dataset to Coaches
# UPDATE COLUMN DATA: Update school names in the records dataframe to match the coaches dataset
recordsFrame["School"] = recordsFrame["School"].replace("Alabama", "The University of Alabama")
recordsFrame['School'] = recordsFrame['School'].replace("Arkansas","University of Arkansas")
recordsFrame['School'] = recordsFrame['School'].replace("California","University of California-Berkeley")
recordsFrame['School'] = recordsFrame['School'].replace("Colorado","University of Colorado Boulder")
recordsFrame['School'] = recordsFrame['School'].replace("Connecticut","University of Connecticut")
recordsFrame['School'] = recordsFrame['School'].replace("Florida","University of Florida")
recordsFrame['School'] = recordsFrame['School'].replace("Georgia","University of Georgia")
recordsFrame['School'] = recordsFrame['School'].replace("Houston","University of Houston")
recordsFrame['School'] = recordsFrame['School'].replace("Illinois","University of Illinois at Urbana-Champaign")
recordsFrame['School'] = recordsFrame['School'].replace("Indiana","Indiana University-Bloomington")
recordsFrame['School'] = recordsFrame['School'].replace("Iowa","University of Iowa")
recordsFrame['School'] = recordsFrame['School'].replace("Kentucky","University of Kansas")
recordsFrame['School'] = recordsFrame['School'].replace("Kansas","University of Kentucky")
recordsFrame["School"] = recordsFrame["School"].replace("Louisiana", "Louisiana-Lafayette")
recordsFrame["School"] = recordsFrame["School"].replace("Louisiana–Monroe", "Louisiana-Monroe")
recordsFrame['School'] = recordsFrame['School'].replace("Maryland","University of Maryland-College Park")
recordsFrame['School'] = recordsFrame['School'].replace("Michigan","University of Michigan-Ann Arbor")
recordsFrame['School'] = recordsFrame['School'].replace("Mississippi","University of Mississippi")
recordsFrame['School'] = recordsFrame['School'].replace("Missouri","University of Missouri-Columbia")
recordsFrame['School'] = recordsFrame['School'].replace("Nevada","University of Nevada-Reno")
recordsFrame['School'] = recordsFrame['School'].replace("Nevada-Las Vegas","University of Nevada-Las Vegas")
recordsFrame['School'] = recordsFrame['School'].replace("North Carolina","University of North Carolina at Chapel Hill")
recordsFrame['School'] = recordsFrame['School'].replace("Penn State","Pennsylvania State University-Main Campus")
recordsFrame['School'] = recordsFrame['School'].replace("Texas A&M","Texas A & M University-College Station")
recordsFrame['School'] = recordsFrame['School'].replace("Texas-El Paso","The University of Texas at El Paso")
recordsFrame['School'] = recordsFrame['School'].replace("Texas-San Antonio","The University of Texas at San Antonio")
recordsFrame['School'] = recordsFrame['School'].replace("UCLA","University of California-Los Angeles")
recordsFrame["School"] = recordsFrame['School'].replace("Washington","University of Washington-Seattle Campus")
recordsFrame["School"] = recordsFrame['School'].replace("Wisconsin", "University of Wisconsin-Madison")
recordsFrame["School"] = recordsFrame["School"].replace("BYU", "Brigham Young")
recordsFrame["School"] = recordsFrame["School"].replace("FIU", "Florida International")
recordsFrame["School"] = recordsFrame["School"].replace("Miami (FL)", "Miami (Fla.)")
recordsFrame["School"] = recordsFrame["School"].replace("Miami (OH)", "Miami (Ohio)")
recordsFrame["School"] = recordsFrame["School"].replace("NC State", "North Carolina State")
recordsFrame["School"] = recordsFrame["School"].replace("SMU", "Southern Methodist")
recordsFrame["School"] = recordsFrame["School"].replace("Southern Miss", "Southern Mississippi")
recordsFrame["School"] = recordsFrame["School"].replace("TCU", "Texas Christian")
recordsFrame["School"] = recordsFrame["School"].replace("UAB", "Alabama at Birmingham")
recordsFrame["School"] = recordsFrame["School"].replace("UCF", "Central Florida")
recordsFrame["School"] = recordsFrame["School"].replace("UConn", "Connecticut")
recordsFrame["School"] = recordsFrame["School"].replace("UMass", "Massachusetts")
recordsFrame["School"] = recordsFrame["School"].replace("UNLV", "Nevada-Las Vegas")
recordsFrame["School"] = recordsFrame["School"].replace("USC", "Southern California")
recordsFrame["School"] = recordsFrame["School"].replace("UTEP", "Texas-El Paso")
recordsFrame["School"] = recordsFrame["School"].replace("UTSA", "Texas-San Antonio")

def lookup_won(ip):
   for column in recordsFrame.itertuples():
      if (ip in column[1]):
         return column[3]
def lookup_loss(ip):
   for column in recordsFrame.itertuples():
      if (ip in column[1]):
         return column[4]
def lookup_tie(ip):
   for column in recordsFrame.itertuples():
      if (ip in column[1]):
         return column[5]
def lookup_PercWin(ip):
   for column in recordsFrame.itertuples():
      if (ip in column[1]):
         return column[7]

coachesData['Won'] = coachesData['School'].apply(lookup_won)
coachesData['Loss'] = coachesData['School'].apply(lookup_loss)
coachesData['Tied'] = coachesData['School'].apply(lookup_tie)
coachesData['PercentWin'] = coachesData['School'].apply(lookup_PercWin)

#print(coachesData)



# ADDITIONAL DATA: enrollment
#pre-processing: convernt enrollment to a number for ranking (bin)
#find min & max
#can make a histogram to help rank

enrollment_url = requests.get('https://en.wikipedia.org/wiki/List_of_NCAA_Division_I_FBS_football_programs').text
soup3 = BeautifulSoup(enrollment_url,'lxml')

My_table3 = soup3.find('table',{'class':'wikitable sortable'}) #Find the table that has the win-loss records
#print(My_table3)

A3=[] #store data for column 1
B3=[] #store data for column 2, and so on
C3=[]
D3=[]
E3=[]
F3=[]
G3=[]
H3=[]
I3=[]

for row in My_table3.findAll('tr'): # start with tr as the head of ea row
   cells = row.findAll('td')         #the var 'cells' will store the data; now use td to search for the tags
   if len(cells) == 9:
      A3.append(cells[0].find(text=True))
      B3.append(cells[1].find(text=True))
      C3.append(cells[2].find(text=True))
      D3.append(cells[3].find(text=True))
      E3.append(cells[4].find(text=True))
      F3.append(cells[5].find(text=True))
      G3.append(cells[6].find(text=True))
      H3.append(cells[7].find(text=True))
      I3.append(cells[7].find(text=True))

# Convert won, lost, tied, percent, and total games data to int for future calculation:
E3 = [char.replace("\n","") for char in E3]
E3 = [char.replace(",","") for char in E3]
E3 = [char.replace("NaN","0") for char in E3]
E3 = [int(n) for n in E3]

# Now create a dataframe to call store data:
enrollmentFrame = pd.DataFrame(A3, columns=['School'])
enrollmentFrame['Enrollment'] = E3

#print('Table containing enrollment data')
#print(enrollmentFrame[0:5])
#print('Number of schools in enrollments dataframe:', len(enrollmentFrame))
#print()

#print(A3) #School names audit in order to match this dataset to Coaches
# UPDATE COLUMN DATA: Update school names in the enrollment dataframe to match the coaches dataset
enrollmentFrame["School"] = enrollmentFrame["School"].replace("Alabama", "The University of Alabama")
enrollmentFrame['School'] = enrollmentFrame['School'].replace("Arkansas","University of Arkansas")
enrollmentFrame['School'] = enrollmentFrame['School'].replace("California","University of California-Berkeley")
enrollmentFrame['School'] = enrollmentFrame['School'].replace("Colorado","University of Colorado Boulder")
enrollmentFrame['School'] = enrollmentFrame['School'].replace("Connecticut","University of Connecticut")
enrollmentFrame['School'] = enrollmentFrame['School'].replace("Florida","University of Florida")
enrollmentFrame['School'] = enrollmentFrame['School'].replace("Georgia","University of Georgia")
enrollmentFrame['School'] = enrollmentFrame['School'].replace("Houston","University of Houston")
enrollmentFrame['School'] = enrollmentFrame['School'].replace("Illinois","University of Illinois at Urbana-Champaign")
enrollmentFrame['School'] = enrollmentFrame['School'].replace("Indiana","Indiana University-Bloomington")
enrollmentFrame['School'] = enrollmentFrame['School'].replace("Iowa","University of Iowa")
enrollmentFrame['School'] = enrollmentFrame['School'].replace("Kentucky","University of Kansas")
enrollmentFrame['School'] = enrollmentFrame['School'].replace("Kansas","University of Kentucky")
enrollmentFrame["School"] = enrollmentFrame["School"].replace("Louisiana", "Louisiana-Lafayette")
enrollmentFrame["School"] = enrollmentFrame["School"].replace("Louisiana–Monroe", "Louisiana-Monroe")
enrollmentFrame['School'] = enrollmentFrame['School'].replace("Maryland","University of Maryland-College Park")
enrollmentFrame['School'] = enrollmentFrame['School'].replace("Michigan","University of Michigan-Ann Arbor")
enrollmentFrame['School'] = enrollmentFrame['School'].replace("Mississippi","University of Mississippi")
enrollmentFrame['School'] = enrollmentFrame['School'].replace("Missouri","University of Missouri-Columbia")
enrollmentFrame['School'] = enrollmentFrame['School'].replace("Nevada","University of Nevada-Reno")
enrollmentFrame['School'] = enrollmentFrame['School'].replace("Nevada-Las Vegas","University of Nevada-Las Vegas")
enrollmentFrame['School'] = enrollmentFrame['School'].replace("North Carolina","University of North Carolina at Chapel Hill")
enrollmentFrame['School'] = enrollmentFrame['School'].replace("Penn State","Pennsylvania State University-Main Campus")
enrollmentFrame['School'] = enrollmentFrame['School'].replace("Texas A&M","Texas A & M University-College Station")
enrollmentFrame['School'] = enrollmentFrame['School'].replace("Texas-El Paso","The University of Texas at El Paso")
enrollmentFrame['School'] = enrollmentFrame['School'].replace("Texas-San Antonio","The University of Texas at San Antonio")
enrollmentFrame['School'] = enrollmentFrame['School'].replace("UCLA","University of California-Los Angeles")
enrollmentFrame["School"] = enrollmentFrame['School'].replace("Washington","University of Washington-Seattle Campus")
enrollmentFrame["School"] = enrollmentFrame['School'].replace("Wisconsin", "University of Wisconsin-Madison")
enrollmentFrame["School"] = enrollmentFrame["School"].replace("BYU", "Brigham Young")
enrollmentFrame["School"] = enrollmentFrame["School"].replace("FIU", "Florida International")
enrollmentFrame["School"] = enrollmentFrame["School"].replace("Miami (FL)", "Miami (Fla.)")
enrollmentFrame["School"] = enrollmentFrame["School"].replace("Miami (OH)", "Miami (Ohio)")
enrollmentFrame["School"] = enrollmentFrame["School"].replace("NC State", "North Carolina State")
enrollmentFrame["School"] = enrollmentFrame["School"].replace("SMU", "Southern Methodist")
enrollmentFrame["School"] = enrollmentFrame["School"].replace("Southern Miss", "Southern Mississippi")
enrollmentFrame["School"] = enrollmentFrame["School"].replace("TCU", "Texas Christian")
enrollmentFrame["School"] = enrollmentFrame["School"].replace("UAB", "Alabama at Birmingham")
enrollmentFrame["School"] = enrollmentFrame["School"].replace("UCF", "Central Florida")
enrollmentFrame["School"] = enrollmentFrame["School"].replace("UConn", "Connecticut")
enrollmentFrame["School"] = enrollmentFrame["School"].replace("UMass", "Massachusetts")
enrollmentFrame["School"] = enrollmentFrame["School"].replace("UNLV", "Nevada-Las Vegas")
enrollmentFrame["School"] = enrollmentFrame["School"].replace("USC", "Southern California")
enrollmentFrame["School"] = enrollmentFrame["School"].replace("UTEP", "Texas-El Paso")
enrollmentFrame["School"] = enrollmentFrame["School"].replace("UTSA", "Texas-San Antonio")

def lookup_enrollment(ip):
   for column in enrollmentFrame.itertuples():
      if (ip in column[1]):
         return column[2]

coachesData['Enrollment'] = coachesData['School'].apply(lookup_enrollment)



##### EXPLORE DATA #####
# View final dataset:
print('Coaches Dataset with Additional Data:')
print(coachesData[0:10])
print('Number of coaches in dataset:', len(coachesData))
print()
#print(coachesData.describe())
#print()
# Note we see some coaches don't have salary data:
#print(coachesData[coachesData.SchoolPay == 0])
coachesData = coachesData.drop(coachesData[coachesData.SchoolPay == 0].index)
print(coachesData.describe())
print()


##### PHASE 2: DATA EXPLORATION #####
# Read in libraries for modeling
import numpy as np # arrays and math functions
import matplotlib.pyplot as plt  # 2D plotting
import seaborn as sns  # provides trellis and small multiple plotting

# Bin enrollment to understand relative scale
#plt.hist(coachesData['Enrollment'], normed = False, stacked = False, rwidth = .9)
#plt.title("Enrollment Histogram")
#plt.xlabel('Enrollment')
#plt.ylabel('Frequency')
#plt.show()
#Model doesn't tell us very much about what the enrollment means


# Summary Statistics #
#print('Mean salary:', np.mean(coachesData['SchoolPay']))
#print('Min salary:', np.min(coachesData['SchoolPay']))
#print('Max salary:',np.max(coachesData['SchoolPay']))

#print(coachesData["School"].to_list())
print('Syracuse Coach Information (current data/baseline):')
print(coachesData.loc[102,:])
print()

# Let's look at the school pay for all schools
#sns.boxplot(y = "SchoolPay", data = coachesData, showmeans=True, meanprops={"marker":"o", "markerfacecolor":"white", "markeredgecolor":"black","markersize":"10"}).set(title='School pay distribution for 129 coaches', ylabel='Salary in 2018', xlabel='All Coaches in D1')
#plt.show() # Note this graphic is not helpful as it doesn't give us differentiation

#Create a histogram of salary to understand the distribution
plt.hist(coachesData['SchoolPay'], normed = False, stacked = False, rwidth = .9)
plt.title("Salary Histogram")
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()

#print('SEC conference', coachesData.loc[coachesData.Conference == 'SEC'])
#np.mean(coachesData.loc[coachesData.Conference == 'SEC']) # Show means for ea column
#coachesSEC = coachesData.loc[coachesData.Conference == 'SEC']
#print('Mean salary:', np.mean(coachesSEC['SchoolPay']))
#print()
# Consider dropping SEC coaches with SchoolPay >= 6500000
#print('SchoolPay over 7000000:', coachesData[coachesData.SchoolPay >= 6500000])
#The University of Alabama, Auburn, University of Georgia, Texas A&M University
#coachesData = coachesData.drop(coachesData[coachesData.SchoolPay >= 6500000].index)
# Index #s: 2, 10, 36, 105


#print('ACC conference', coachesData.loc[coachesData.Conference == 'ACC'])
#print('Mean salary:', np.mean(coachesData.loc[coachesData.Conference == 'ACC']['SchoolPay']))
#print()
# Consider dropping the ACC schools over 4000000:
#Clemson, Florida State, Miami (Fla.), Virginia Tech
# Index #s: 23, 34, 60


#print('Big Ten conference', coachesData.loc[coachesData.Conference == 'Big Ten'])
#print('Mean salary:', np.mean(coachesData.loc[coachesData.Conference == 'Big Ten']['SchoolPay']))
#print()
# Consider dropping Big Ten schools over 4500000:


#Let's evaluate pay based on conference binning: 
#salary in ten thousands for plotting 
#coachesData['SchoolPay_000'] = coachesData['SchoolPay']/10000 #Not necessary, keep scale
sns.boxplot(x="Conference", y="SchoolPay", data=coachesData, color="gray", showmeans=True, meanprops={"marker":"*", "markerfacecolor":"orange", "markeredgecolor":"black","markersize":"10"}).set(title='School pay distribution by conference', ylabel='Salary', xlabel='Conference')
plt.show()
#Outliers -- trellis plots to evaluate what to remove: SchoolPay vs StadSize for SEC, Big12, BigTen (median & mean are very off)

# Let's evaluate pay based on conference & school size (enrollment)
#print('Min enrollment', np.min(coachesData["Enrollment"])) #3297
#print('Max enrollment', np.max(coachesData["Enrollment"])) #70,900
binsEnroll=[0, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000]
labelsEnroll=[0,1,2,3,4,5,6,7]
# Where 0 is 10K students or less, 1 is 10K-20K, and so on
coachesData["EnrollmentBinned"] = pd.cut(coachesData["Enrollment"], binsEnroll, labels=labelsEnroll)
#print(coachesData)

#print('Min salary', np.min(coachesData["SchoolPay"])) #0
#print('Max salary', np.max(coachesData["SchoolPay"])) #8,307,000
binsSal=[0, 500000, 1000000, 1500000, 2000000, 2500000, 3000000, 3500000, 4000000, 4500000, 5000000, 5500000, 6000000, 6500000, 7000000, 7500000, 8000000, 8500000]
labelsSal=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# Where 0 is 500K students or less, 1 is 500K-1M, and so on
coachesData["SalaryBinned"] = pd.cut(coachesData["SchoolPay"], binsSal, labels=labelsSal)
#print(coachesData)
#sns.swarmplot(x="SalaryBinned", y="Conference", hue="EnrollmentBinned", data=coachesData)
#plt.show() # This plot doesn't tell us very much


#trellis/lattice plot salary by stadium size, graduation rate, percent wins, and enrollment
sns.set(style="darkgrid")

ss=sns.FacetGrid(coachesData, hue="Conference") # Filtered by conference
ss.map(plt.scatter, "StadiumSize", "SchoolPay", alpha=.7) # Plot by stadium size
ss.add_legend();

gsr=sns.FacetGrid(coachesData, hue="Conference") # Filtered by conference
gsr.map(plt.scatter, "GSR", "SchoolPay", alpha=.7) # Plot by graduation score (GSR)
gsr.add_legend();

fgr=sns.FacetGrid(coachesData, hue="Conference") # Filtered by conference
fgr.map(plt.scatter, "FGR", "SchoolPay", alpha=.7) # Plot by graduation score (FGR)
fgr.add_legend();

# Explore schools to drop based on lowest FGR scores:
#print('FGR under 0:', coachesData.loc[coachesData.FGR < 0])
#coachesData = coachesData.drop(coachesData[coachesData.FGR < 0].index)

#fgr2=sns.FacetGrid(coachesData, hue="Conference") # Filtered by conference
#fgr2.map(plt.scatter, "FGR", "SchoolPay", alpha=.7) # Plot by graduation score (FGR) with scores under 0 dropped
#fgr2.add_legend();

pw=sns.FacetGrid(coachesData, hue="Conference") # Filtered by conference
pw.map(plt.scatter, "PercentWin", "SchoolPay", alpha=.7) # Plot by percent win
pw.add_legend();

e=sns.FacetGrid(coachesData, hue="Conference") # Filtered by conference
e.map(plt.scatter, "Enrollment", "SchoolPay", alpha=.7) # Plot by enrollment
e.add_legend();
plt.show()

# After modeling: we see significant impact from Buyout and Won columns: (looking for outliers)
#b=sns.FacetGrid(coachesData, hue="Conference") # Filtered by conference
#b.map(plt.scatter, "Buyout", "SchoolPay", alpha=.7) # Plot by buyout
#b.add_legend();

#w=sns.FacetGrid(coachesData, hue="Conference") # Filtered by conference
#w.map(plt.scatter, "Won", "SchoolPay", alpha=.7) # Plot by won
#w.add_legend();
plt.show()


# treillis/lattice for ACC conference
#accPlot=sns.FacetGrid(coachesData[coachesData.Conference == "ACC"], hue="EnrollmentBinned") # Filtered by enrollment
#accPlot.map(plt.scatter, "StadiumSize", "SchoolPay", alpha=.7) # Plot by stadium size
#accPlot.add_legend();

# Explore schools to drop based on outliers:
#print('Outliers:', coachesData.loc[(coachesData.Conference == 'ACC')])

#pw2=sns.FacetGrid(coachesData[coachesData.Conference == "ACC"], hue="EnrollmentBinned") # Filtered by enrollment
#pw2.map(plt.scatter, "PercentWin", "SchoolPay", alpha=.7) # Plot by percent win
#pw2.add_legend();

#w2=sns.FacetGrid(coachesData[coachesData.Conference == "ACC"], hue="EnrollmentBinned") # Filtered by enrollment
#w2.map(plt.scatter, "Won", "SchoolPay", alpha=.7) # Plot by percent win
#w2.add_legend();
#plt.show()

# These plots follow the same patterns for all coaches/schools all up and not necessary to include in report out



##### PHASE 3: DATA MODELING #####
from scipy.stats import uniform  # for training-and-test split
import statsmodels.api as sm  # statistical models (including regression)
import statsmodels.formula.api as smf  # R-like model specification

#Model 1 - based all coaches
# build training-and-test set for model validation
np.random.seed(1234)
coachesData['runiform'] = uniform.rvs(loc = 0, scale = 1, size = len(coachesData)) # Uniform distribution for continuous random variables
coaches_train = coachesData[coachesData['runiform'] >= 0.33] #Original training dataset of 67% data
coaches_test = coachesData[coachesData['runiform'] < 0.33] #Original testing dataset of 33% data

# print training data frame
#print('\ncoaches_train data frame (rows, columns): ',coaches_train.shape)
#print(coaches_train.head())
# print test data frame
#print('\ncoaches_test data frame (rows, columns): ',coaches_test.shape)
#print(coaches_test.head())

#Build model 1:
allCoachesModel = str('SchoolPay ~ Conference + Bonus + Buyout + StadiumSize + FGR + GSR + PercentWin + Enrollment') #returns string version of the dataset

# fit the model to the training set
train_model_fit = smf.ols(allCoachesModel, data = coaches_train).fit() # Plug in data & use OLS(=Ordinary least squares (linear regression for continuous response variables))
# NOTES: Want to use OLS here to model a single response variable based on multiple explanatory categorical variables
# Want to predict the salary (& later salary range) based on other variables
# Also note we re-added the removed coaches from FGR outliers to start

# summary of model fit to the training set
#print(train_model_fit.summary())
# NOTES: We get an R2 of 0.705 and a p-value of 0.007 (significant though low R2)
# Consider dropping enrollment as the data in the trellis chart was all over
# Also received warning of collinearity: could be enrollment to FGR data, or enrollment to StadiumSize -> will drop and see results

# Create summary table to store regression results in clear, callable manner:
SummaryModelsList = ['R-squared value:', 'Adj R-squared:', 'p-value:']
SummaryModelsTable = pd.DataFrame(SummaryModelsList, columns=['Model:'])

# Add model 1 results
#allCoachesModelResults = ['0.705', '0.688', '0.007']
#SummaryModelsTable['1-AllCoaches (numerical var)'] = pd.DataFrame(allCoachesModelResults)
#print(SummaryModelsTable)
#print()

#Now let's tune the model so that it returns a higher R2 value:
#Here we are tweaking existing variables
allCoachesModel2 = str('SchoolPay ~ StadiumSize + FGR + PercentWin') #remove Enrollment variable
train_model_fit2 = smf.ols(allCoachesModel2, data = coaches_train).fit() 
#print(train_model_fit2.summary())
# RESULTS: We get an R2 of 0.698 and a p-value of 0.013 (R2 decreased & p-value increased slightly)
# Removing ea variable individually results in reduced R2 value - try adding

#Tuning the model again
#Here we are evaluating all variables
allCoachesModel3 = str('SchoolPay ~ Buyout + StadiumSize + GSR + FGR + Won + Enrollment') #add buyout & GSR
train_model_fit3 = smf.ols(allCoachesModel3, data = coaches_train).fit() 
print('Regression results for model 1:')
print(train_model_fit3.summary())
# NOTES ON TUNING: 
#adding the Conference var results in insignificant p-value
#the Bonus and BonusPaid vars seems to have little to no impact
#replacing PercentWin with Won increased R2 and still significant p-value
#adding Loss var has no impact
#both increasing and decreasing the training dataset decreases the R2 value

# RESULTS: 
allCoachesModelResults3 = ['0.835', '0.821', '0.014']
SummaryModelsTable['SalaryModel1'] = pd.DataFrame(allCoachesModelResults3)
#print(SummaryModelsTable)
#print()

# Let's see what our model suggests for a salary
#coaches_train['predict_salary'] = train_model_fit3.fittedvalues #Training set predictions from the model fit to the training set
#coaches_test['predict_salary'] = train_model_fit3.predict(coaches_test) #Test set predictions from the model fit to the training set
# First let's see how how train/test dataframes compare
#print(coaches_train['predict_salary'][0:5])
#print(coaches_test['predict_salary'][0:5])

# Now apply model to coachesData:
coachesData['predict_salary'] = train_model_fit3.predict(coachesData)
#print(coachesData[0:5]) #Check to see new column exists
#print()

print('New Syracuse Coach Information:')
#print(coachesData.loc[102,:])
#print('Model 1 considers all of the coaches (including outlier schools) and the categorical variables Buyout, StadiumSize, GSR, FGR, Won, Enrollment')
#print('Model 1 suggested salary for Syracuse coach: $' + str(round((coachesData.loc[102,'predict_salary']),2)))
#print()

#Create dataframe to track suggested salaries based on model updates:
SalaryModelsList = ['Suggested Salary:']
SalaryModelsTable = pd.DataFrame(SalaryModelsList, columns=['Model:'])

salaryCurrent = ['$2,401,206.00'] #Pull in current data
SalaryModelsTable['CurrentSalary'] = pd.DataFrame(salaryCurrent)

salaryModel1 = ['$2,509,127.52'] #Suggested salary based on all coaches & conferences + independent vars: Buyout + StadiumSize + GSR + FGR + Won + Enrollment
SalaryModelsTable['SalaryModel1'] = pd.DataFrame(salaryModel1)



#Model 2 - ACC conference
#Build model to include conference
conferencesModel = str('SchoolPay ~ Conference + Buyout + StadiumSize + GSR + FGR + Won + Enrollment') # Add conference value
train_model_fit4 = smf.ols(conferencesModel, data = coaches_train).fit() 
#print(train_model_fit4.summary())
confModel = ['0.894', '0.864', '0.506']
SummaryModelsTable['ConfModel'] = pd.DataFrame(confModel)

coachesACC = coachesData.loc[coachesData.Conference == 'ACC']
coachesACC['predict_salary'] = train_model_fit4.predict(coachesACC)
#print(coachesACC) #Check to see new column exists
#print()

#print('Model 2 considers all of coaches in the ACC conference only and adds the "Conference" var into the model')
#print('Model 2 suggested salary for Syracuse coach: $' + str(round((coachesACC.loc[102,'predict_salary']),2)))
#print()

salaryModel2ACC = ['$2,785,676.95'] #Suggested salary based on the same model, applied to the ACC conference
SalaryModelsTable['SalaryModel2-ACC'] = pd.DataFrame(salaryModel2ACC)


#Model 2.2 - Big Ten
#print('Syracuse runiform', coachesData.loc[coachesData.School == 'Syracuse']['runiform'])
#print()
coachesBigTen = coachesData.loc[coachesData.Conference == 'Big Ten']
syracuse = {'School':'Syracuse', 'Conference':'Big Ten', 'Coach':'Dino Babers', 'SchoolPay':int(2401206), 'Bonus':int(0), 'BonusPaid':int(0), 'Buyout':int(0), 'FGR':int(73), 'GSR':int(90), 'StadiumSize':int(49250), 'Won':int(724), 'Loss':int(547), 'Tied':int(49), 'PercentWin':int(0.548), 'Enrollment':int(22900), 'runiform':int(0.796867)}
coachesBigTen = coachesBigTen.append(syracuse,ignore_index=True)
#print(coachesBigTen)
coachesBigTen['predict_salary'] = train_model_fit4.predict(coachesBigTen)
#print('Model 3 considers all of coaches in the Big Ten conference only, adds Syracuse to the Big Ten, and uses the same trained model as model 2')
#print('Model 3 suggested salary for Syracuse coach: $' + str(round((coachesBigTen.loc[14,'predict_salary']),2)))
print()

salaryModel3B10 = ['$2,828,073.80'] #Suggested salary based on the same model, applied to the ACC conference
SalaryModelsTable['SalaryModel2-B10'] = pd.DataFrame(salaryModel3B10)




#Model 3 - Removing outlier schools
#Build the dataframe:
# Outliers: military schools - remove & discuss in report
#Index #s: 0, 9, 69       - Air Force, Army, Navy 
removeOutliersData = coachesData.drop(coachesData[coachesData.FGR < 0].index)
# Outliers: High salary this year
#Index #s: 2, 10, 36, 105 - The University of Alabama, Auburn, University of Georgia, Texas A&M University
#Index #s: 23, 34, 60     - Clemson, Florida State, Miami (Fla.), Virginia Tech
#Index #s: 42, 44, 88     - University of Illinois, University of Iowa, Pennsylvania State University
removeOutliersData = removeOutliersData.drop(removeOutliersData[removeOutliersData.School == 'The University of Alabama'].index)
removeOutliersData = removeOutliersData.drop(removeOutliersData[removeOutliersData.School == 'Auburn'].index)
removeOutliersData = removeOutliersData.drop(removeOutliersData[removeOutliersData.School == 'University of Georgia'].index)
removeOutliersData = removeOutliersData.drop(removeOutliersData[removeOutliersData.School == 'Texas A & M University-College Station'].index)
#removeOutliersData = removeOutliersData.drop(removeOutliersData[removeOutliersData.School == 'Clemson'].index)
#removeOutliersData = removeOutliersData.drop(removeOutliersData[removeOutliersData.School == 'Florida State'].index)
#removeOutliersData = removeOutliersData.drop(removeOutliersData[removeOutliersData.School == 'Miami (Fla.)'].index)
#removeOutliersData = removeOutliersData.drop(removeOutliersData[removeOutliersData.School == 'Virginia Tech'].index)
#removeOutliersData = removeOutliersData.drop(removeOutliersData[removeOutliersData.School == 'University of Illinois at Urbana-Champaign'].index)
#removeOutliersData = removeOutliersData.drop(removeOutliersData[removeOutliersData.School == 'University of Iowa'].index)
#removeOutliersData = removeOutliersData.drop(removeOutliersData[removeOutliersData.School == 'Pennsylvania State University-Main Campus'].index)
#print(removeOutliersData['School'].to_list())
removeOutliersData = removeOutliersData.drop(['predict_salary'], axis=1)
removeOutliersData = removeOutliersData.drop(['runiform'], axis=1)
#print(removeOutliersData[0:5])
#print(len(removeOutliersData))

#Build the model:
removeOutliersData['runiform'] = uniform.rvs(loc = 0, scale = 1, size = len(removeOutliersData)) # Uniform distribution for continuous random variables
outliers_train = removeOutliersData[removeOutliersData['runiform'] >= 0.33] #Original training dataset of 67% data
outliers_test = removeOutliersData[removeOutliersData['runiform'] < 0.33] #Original testing dataset of 33% data

outliersRemovedModel = str('SchoolPay ~ Buyout + StadiumSize + GSR + FGR + Won + Enrollment')
train_model_fit5 = smf.ols(outliersRemovedModel, data = outliers_train ).fit() 
print('Regression results for the outlier model:')
print(train_model_fit5.summary())

outlierModel = ['0.805', '0.784', '0.163']
SummaryModelsTable['OutliersRemovedModel'] = pd.DataFrame(outlierModel)

removeOutliersData['predict_salary'] = train_model_fit5.predict(removeOutliersData)
#print('Model 3 considers coaches dataset with outliers removed')
#print('Model 3 suggested salary for Syracuse coach: $' + str(round((removeOutliersData.loc[102,'predict_salary']),2)))
#print()

outlierModelData = ['$2,376,727.46'] #Suggested salary based on the same model with outliers removed
SalaryModelsTable['outlierModelData'] = pd.DataFrame(outlierModelData)



### Conclusion: summary table (formatted with pandas df)
print()
print('Addressing recommendation questions:')
print()
print('Summary of models predictions')
print(SalaryModelsTable)
print()
print()
# Which var has the biggest impact on salary size? - Using the full data set to obtain an estimate
print('Which variables account for the biggest impact on salary size?')
print('Based on model output (no validation of regression results)')
# Evaluation of conference:
#Var 'Conference'
confModel2 = smf.ols(str('SchoolPay ~ Conference'), data = coachesData).fit()
#print(confModel2.summary())
confResults2 = ['0.689', '0.662', '0.000']
SummaryModelsTable['ConfModel2'] = pd.DataFrame(confResults2)
print('Estimated effect of "Conference" var impact:  $' + str(round(confModel2.params[1],2)))

# Model 1.3: Buyout + StadiumSize + GSR + FGR + Won + Enrollment
#Var 'Buyout'
BuyoutModel = smf.ols(str('SchoolPay ~ Buyout'), data = coachesData).fit()
#print(BuyoutModel.summary())
buyoutResults = ['0.606', '0.603', '0.000']
SummaryModelsTable['BuyoutModel'] = pd.DataFrame(buyoutResults)
print('Estimated effect of "Buyout" var impact:      $' + str(round(BuyoutModel.params[1],2)))

#Var 'StadiumSize'
StadiumSizeModel = smf.ols(str('SchoolPay ~ StadiumSize'), data = coachesData).fit()
#print(StadiumSizeModel.summary())
ssResults = ['0.725', '0.722', '0.000']
SummaryModelsTable['StadiumSizeModel'] = pd.DataFrame(ssResults)
print('Estimated effect of "StadiumSize" var impact: $' + str(round(StadiumSizeModel.params[1],2)))

#Var 'GSR'
GSRModel = smf.ols(str('SchoolPay ~ GSR'), data = coachesData).fit()
#print(GSRModel.summary())
gsrResults = ['0.105', '0.098', '0.011']
SummaryModelsTable['GSRModel'] = pd.DataFrame(gsrResults)
print('Estimated effect of "GSR" var impact:         $' + str(round(GSRModel.params[1],2)))

#Var 'FGR'
FGRModel = smf.ols(str('SchoolPay ~ FGR'), data = coachesData).fit()
#print(FGRModel.summary())
fgrResults = ['0.031', '0.023', '0.000']
SummaryModelsTable['FGRModel'] = pd.DataFrame(fgrResults)
print('Estimated effect of "FGR" var impact:         $' + str(round(FGRModel.params[1],2)))

#Var 'Won'
WonModel = smf.ols(str('SchoolPay ~ Won'), data = coachesData).fit()
#print(WonModel.summary())
wonResults = ['0.389', '0.383', '0.018']
SummaryModelsTable['wonModel'] = pd.DataFrame(wonResults)
print('Estimated effect of "Won" var impact:         $' + str(round(WonModel.params[1],2)))

#Var 'Enrollment'
EnrollmentModel = smf.ols(str('SchoolPay ~ Enrollment'), data = coachesData).fit()
#print(EnrollmentModel.summary())
enrollResults = ['0.147', '0.139', '0.026']
SummaryModelsTable['EnrollmentModel'] = pd.DataFrame(enrollResults)

print('Estimated effect of "Enrollment" var impact:  $' + str(round(EnrollmentModel.params[1],2)))
print()
print('Which variables account for the biggest impact on salary size?')
print('Based on regression results')
#del SummaryModelsTable['SalaryModel1']
#del SummaryModelsTable['ConfModel']
#del SummaryModelsTable['OutliersRemovedModel']
print(SummaryModelsTable)
print()


# Adding regression results:
#allCoachesModelResults3 = ['0.835', '0.821', '0.018']
#SummaryModelsTable['SalaryModel1'] = pd.DataFrame(allCoachesModelResults3)
