# Aurelia Arnett
# IST 652
# Homework assignment #1: Structured Data
# Purpose: Write a program that will read in the donor data & structure the data with lines representing one type of unity (one donor)
# Purpose cont: Your program will represent the data as Python data structures (a list of dictionaries, combination of lists, NumPy arrays, a pandas dataframe)
# Objective: Data exploration & cleaning the data (see line 119 below for assignment questions)

# Import function(s)
import csv

# Read in the data
donorData = 'donors_data.csv'

donorList = []
countDonors = 0 # a variable to count the total number of donors in the dataset
countFemaleDonors = 0
countMaleDonors = 0

with open(donorData, mode='r') as csvfile:
   donorReader = csv.reader(csvfile, dialect='excel')

# Represent & clean the data (dictionaries)

   for line in donorReader:
      if line[0].startswith('Row'):
         continue
      else:
         donor = {}
         donor['Index'] = line[0] 
         donor['Region1'] = line[2]
         donor['Region2'] = line[3]   
         donor['Region3'] = line[4]
         donor['Region4'] = line[5] 
         donor['Home'] = line[6]
         donor['NumChild'] = line[7]
         donor['Income'] = line[8]
         donor['Gender'] = line[9]
         donor['Wealth'] = line[10]
         donor['AvHomeValue'] = line[11]
         donor['MedFamIncome'] = line[12]
         donor['AvFamIncome'] = line[13]
         donor['PercentLowIncome'] = line[14]
         donor['LifetimePromotions'] = line[15]
         donor['GiftsValue'] = line[16]
         donor['LargestGiftValue'] = line[17]
         donor['RecentGiftValue'] = line[18]
         donor['MonthsSinceLastDonation'] = line[19]
         donor['MonthsBetweenGifts'] = line[20]
         donor['AvGiftsValue'] = line[21]
         donor['Donor?'] = line[22]
         donor['PredictedDonationValue'] = line[23]
         donorList.append(donor)

         # Determine total number of donors in dataset
         if donor['Donor?'] == '1':
            countDonors +=  1

         # Determine total number of female donors in dataset
         if donor['Donor?'] == '1' and donor['Gender'] == '1':
            countFemaleDonors +=  1

         # Determine total number of male donors in dataset
         if donor['Donor?'] == '1' and donor['Gender'] == '0':
            countMaleDonors +=  1

csvfile.close()

# Data Exploration
print("Read in", len(donorList), "rows of donor data")
print('Number of Donors:', countDonors)
percDonors = (countDonors / len(donorList)) * 100
print('Percent donors in dataset: ' + str(percDonors) + "%")
print('Percent donors that are female: ' + str(round((countFemaleDonors/countDonors)*100)) + '%')
print('Percent donors that are male: ' + str(round((countMaleDonors/countDonors)*100)) + '%')
print()

# Determine donor by region
Reg1 = 0
Reg2 = 0
Reg3 = 0
Reg4 = 0
for donor in donorList:
   if donor['Donor?'] == '1' and donor['Region1'] == '1':
      Reg1 +=  1
   if donor['Donor?'] == '1' and donor['Region2'] == '1':
      Reg2 +=  1
   if donor['Donor?'] == '1' and donor['Region3'] == '1':
      Reg3 +=  1
   if donor['Donor?'] == '1' and donor['Region4'] == '1':
      Reg4 +=  1

# Break out donors by regions:
print('Number of Donors in Region 1:', Reg1)
print('Number of Donors in Region 2:', Reg2)
print('Number of Donors in Region 3:', Reg3)
print('Number of Donors in Region 4:', Reg4)
print()
print()

# Confirm total donors in each region (combined) is equal to total donors
#sumReg = Reg1 + Reg2 + Reg3 + Reg4
#print(sumReg)
# 1560 matches 1560

# Determine donors vs non-donors
#for donor in donorList:
#   print('Donor Number:', donor['Index'], 'Donor?:', donor['Donor?'])

# Write a test file that shows information on donors
outfileTest = 'DonorsInfo-Test.csv'

with open(outfileTest, 'w', newline='') as csvfileout:
   donorWriter1 = csv.writer(csvfileout, delimiter=',', quoting=csv.QUOTE_MINIMAL)

   # write the header row as a list of column labels (line 102)
   donorWriter1.writerow(['Donor Number', 'Gender', 'Predicted Donation Value'])

   for donor in donorList:
      if (donor['Donor?'] == '1'):
         donorWriter1.writerow([donor['Index'], donor['Gender'], donor['PredictedDonationValue']])
   
csvfileout.close()


# ASSIGNMENT QUESTIONS HERE

# Question 1: For each region 1-4, first find the average household income per region and then calculate the average dollar amount of lifetime gifts to date for females and for males. (AvGiftsValue)
print('Question 1: Does income and/or gender of a region have an impact on how much a donor has gifted?')

# Define the variables
reg1Hinc = 0
reg2Hinc = 0
reg3Hinc = 0
reg4Hinc = 0
femaleDonor1 = 0
femaleValue1 = 0
femaleDonor2 = 0
femaleValue2 = 0
femaleDonor3 = 0
femaleValue3 = 0
femaleDonor4 = 0
femaleValue4 = 0
maleDonor1 = 0
maleValue1 = 0
maleDonor2 = 0
maleValue2 = 0
maleDonor3 = 0
maleValue3 = 0
maleDonor4 = 0
maleValue4 = 0

# Calculate the average household income per region:
for donor in donorList:
   if donor['Donor?'] == '1':
      if donor['Region1'] == '1':
         reg1Hinc += float(donor['Income'])
      elif donor['Region2'] == '1':
         reg2Hinc += float(donor['Income'])
      elif donor['Region3'] == '1':
         reg3Hinc += float(donor['Income'])
      else:
         reg4Hinc += float(donor['Income'])

avreg1Hinc = "%.2f" % (reg1Hinc/(Reg1))
avreg2Hinc = "%.2f" % (reg2Hinc/(Reg2))
avreg3Hinc = "%.2f" % (reg3Hinc/(Reg3))
avreg4Hinc = "%.2f" % (reg4Hinc/(Reg4))
print('Average Household Incomes by Region')
print('The average household income for donors in region 1 is a category', avreg1Hinc)
print('The average household income for donors in region 2 is a category', avreg2Hinc)
print('The average household income for donors in region 3 is a category', avreg3Hinc)
print('The average household income for donors in region 4 is a category', avreg4Hinc)
print()

# Calculate the total number of female donors per region and their total dollar amount of lifetime gifts within that region (line 147)
for donor in donorList:
   if donor['Donor?'] == '1' and donor['Gender'] == '1':
      if donor['Region1'] == '1':
         femaleDonor1 += 1
         femaleValue1 += float(donor['GiftsValue'])
      elif donor['Region2'] == '1':
         femaleDonor2 += 1
         femaleValue2 += float(donor['GiftsValue'])
      elif donor['Region3'] == '1':
         femaleDonor3 += 1
         femaleValue3 += float(donor['GiftsValue'])
      else:
         femaleDonor4 += 1
         femaleValue4 += float(donor['GiftsValue'])

# Calculate the average dollar amount of lifetime gifts for females per region
avDonationFemale1 = "%.2f" % (femaleValue1/femaleDonor1) # round to two decimals
avDonationFemale2 = "%.2f" % (femaleValue2/femaleDonor2)
avDonationFemale3 = "%.2f" % (femaleValue3/femaleDonor3)
avDonationFemale4 = "%.2f" % (femaleValue4/femaleDonor4)

# Print female donor information
print('Female Donors by Region')
print(femaleDonor1, 'females are donors from region 1 and have donated an average amount of $' + str(avDonationFemale1), ' within their lifetime.')
print(femaleDonor2, 'females are donors from region 2 and have donated an average amount of $' + str(avDonationFemale2), ' within their lifetime.')
print(femaleDonor3, 'females are donors from region 3 and have donated an average amount of $' + str(avDonationFemale3), ' within their lifetime.')
print(femaleDonor4, 'females are donors from region 4 and have donated an average amount of $' + str(avDonationFemale4), ' within their lifetime.')
print()

# Calculate the total number of male donors per region and their total dollar amount of lifetime gifts within that region (line 179)
for donor in donorList:
   if donor['Donor?'] == '1' and donor['Gender'] == '0':
      if donor['Region1'] == '1':
         maleDonor1 += 1
         maleValue1 += float(donor['GiftsValue'])
      elif donor['Region2'] == '1':
         maleDonor2 += 1
         maleValue2 += float(donor['GiftsValue'])
      elif donor['Region3'] == '1':
         maleDonor3 += 1
         maleValue3 += float(donor['GiftsValue'])
      else:
         maleDonor4 += 1
         maleValue4 += float(donor['GiftsValue'])

# Calculate the average dollar amount of lifetime gifts for males per region (line 195)
avDonationMale1 = "%.2f" % (maleValue1/maleDonor1)
avDonationMale2 = "%.2f" % (maleValue2/maleDonor2)
avDonationMale3 = "%.2f" % (maleValue3/maleDonor3)
avDonationMale4 = "%.2f" % (maleValue4/maleDonor4)

# Print male donor information
print('Male Donors by Region')
print(maleDonor1, 'males are donors from region 1 and have donated an average amount of $' + str(avDonationMale1), ' within their lifetime.')
print(maleDonor2, 'males are donors from region 2 and have donated an average amount of $' + str(avDonationMale2), ' within their lifetime.')
print(maleDonor3, 'males are donors from region 3 and have donated an average amount of $' + str(avDonationMale3), ' within their lifetime.')
print(maleDonor4, 'males are donors from region 4 and have donated an average amount of $' + str(avDonationMale4), ' within their lifetime.')
print()
print()

# Write a file that executes the average donation $ amount per gender and per region
outfile1 = 'AvDonateValue-GenderAndRegion.csv'

with open(outfile1, 'w', newline='') as csvfileout:
   donorWriter2 = csv.writer(csvfileout, delimiter=',', quoting=csv.QUOTE_MINIMAL)
   donorWriter2.writerow(['Average donation value per gender per region for donors'])
   donorWriter2.writerow(['Variable', 'Region 1', 'Region 2', 'Region 3', 'Region 4'])
   donorWriter2.writerow(['Av household income', avreg1Hinc, avreg2Hinc, avreg3Hinc, avreg4Hinc])
   donorWriter2.writerow(['Females average donation value', avDonationFemale1, avDonationFemale2, avDonationFemale3, avDonationFemale4])
   donorWriter2.writerow(['Males average donation value', avDonationMale1, avDonationMale2, avDonationMale3, avDonationMale4])
csvfileout.close()


# Question 2: For each wealth type 0-9, calculate the average predicted donation amount based on the last time they donated
print('Question 2: Does the number of months since someone last donated impact how much they are predicted to donate next?')

wealth0 = 0
donor0 = 0
months0 = 0
wealth1 = 0
donor1 = 0
months1 = 0
wealth2 = 0
donor2 = 0
months2 = 0
wealth3 = 0
donor3 = 0
months3 = 0
wealth4 = 0
donor4 = 0
months4 = 0
wealth5 = 0
donor5 = 0
months5 = 0
wealth6 = 0
donor6 = 0
months6 = 0
wealth7 = 0
donor7 = 0
months7 = 0
wealth8 = 0
donor8 = 0
months8 = 0
wealth9 = 0
donor9 = 0
months9 = 0

for donor in donorList:
   if donor['Donor?'] == '1':
      if donor['Wealth'] == '0': 
         donor0 += 1
         wealth0 += float(donor['PredictedDonationValue'])
         months0 += int(donor['MonthsSinceLastDonation'])
      elif donor['Wealth'] == '1':
         donor1 += 1
         wealth1 += float(donor['PredictedDonationValue'])
         months1 += int(donor['MonthsSinceLastDonation'])
      elif donor['Wealth'] == '2':
         donor2 += 1
         wealth2 += float(donor['PredictedDonationValue'])
         months2 += int(donor['MonthsSinceLastDonation'])
      elif donor['Wealth'] == '3':
         donor3 += 1
         wealth3 += float(donor['PredictedDonationValue'])
         months3 += float(donor['MonthsSinceLastDonation'])
      elif donor['Wealth'] == '4':
         donor4 += 1
         wealth4 += float(donor['PredictedDonationValue'])
         months4 += int(donor['MonthsSinceLastDonation'])
      elif donor['Wealth'] == '5':
         donor5 += 1
         wealth5 += float(donor['PredictedDonationValue'])
         months5 += int(donor['MonthsSinceLastDonation'])
      elif donor['Wealth'] == '6':
         donor6 += 1
         wealth6 += float(donor['PredictedDonationValue'])
         months6 += int(donor['MonthsSinceLastDonation'])
      elif donor['Wealth'] == '7':
         donor7 += 1
         wealth7 += float(donor['PredictedDonationValue'])
         months7 += int(donor['MonthsSinceLastDonation'])
      elif donor['Wealth'] == '8':
         donor8 += 1
         wealth8 += float(donor['PredictedDonationValue'])
         months8 += int(donor['MonthsSinceLastDonation'])
      else:
         donor9 += 1
         wealth9 += float(donor['PredictedDonationValue'])
         months9 += float(donor['MonthsSinceLastDonation'])

# calculate months average and predicted next gift / wealth rating and round to 2 decimals
avWealth0 = '$' + str("%.2f" % (wealth0/donor0))
avMonths0 = "%.2f" % (months0/donor0)
avWealth1 = '$' + str("%.2f" % (wealth1/donor1))
avMonths1 = "%.2f" % (months1/donor1)
avWealth2 = '$' + str("%.2f" % (wealth2/donor2))
avMonths2 = "%.2f" % (months2/donor2)
avWealth3 = '$' + str("%.2f" % (wealth3/donor3))
avMonths3 = "%.2f" % (months3/donor3)
avWealth4 = '$' + str("%.2f" % (wealth4/donor4))
avMonths4 = "%.2f" % (months4/donor4)
avWealth5 = '$' + str("%.2f" % (wealth5/donor5))
avMonths5 = "%.2f" % (months5/donor5)
avWealth6 = '$' + str("%.2f" % (wealth6/donor6))
avMonths6 = "%.2f" % (months6/donor6)
avWealth7 = '$' + str("%.2f" % (wealth7/donor7))
avMonths7 = "%.2f" % (months7/donor7)
avWealth8 = '$' + str("%.2f" % (wealth8/donor8))
avMonths8 = "%.2f" % (months8/donor8)
avWealth9 = '$' + str("%.2f" % (wealth9/donor9))
avMonths9 = "%.2f" % (months9/donor9)

import pandas as pd
donorDict = {'Wealth':['0','1','2','3','4','5','6','7','8','9'], 'NumDonors':[donor0, donor1, donor2, donor3, donor4, donor5, donor6, donor7, donor8, donor9], 'AvMonths': [avMonths0, avMonths1, avMonths2, avMonths3, avMonths4, avMonths5, avMonths6, avMonths7, avMonths8, avMonths9], 'PredictedDonation': [avWealth0, avWealth1, avWealth2, avWealth3, avWealth4, avWealth5, avWealth6, avWealth7, avWealth8, avWealth9]}
donorTable = pd.DataFrame(donorDict, columns=['Wealth', 'NumDonors', 'AvMonths', 'PredictedDonation'])
donorTable = donorTable.set_index('Wealth')
print(donorTable)


# Write a file that executes the pandas table
outfile2 = 'PredictedDontation.csv'

with open(outfile2, 'w', newline='') as csvfileout:
   donorWriter3 = csv.writer(csvfileout, delimiter=',', quoting=csv.QUOTE_MINIMAL)
   donorWriter3.writerow(['Predicted Donation Value and Average Number of Kids per Wealth Rating'])
   donorWriter3.writerow(['Wealth', 'Donors', 'AvMonthsSinceDonated', 'PredictedDonation'])
   donorWriter3.writerow(['0', donor0, avMonths0, avWealth0])
   donorWriter3.writerow(['1', donor1, avMonths1, avWealth1])
   donorWriter3.writerow(['2', donor2, avMonths2, avWealth2])
   donorWriter3.writerow(['3', donor3, avMonths3, avWealth3])
   donorWriter3.writerow(['4', donor4, avMonths4, avWealth4])
   donorWriter3.writerow(['5', donor5, avMonths5, avWealth5])
   donorWriter3.writerow(['6', donor6, avMonths6, avWealth6])
   donorWriter3.writerow(['7', donor7, avMonths7, avWealth7])
   donorWriter3.writerow(['8', donor8, avMonths8, avWealth8])
   donorWriter3.writerow(['9', donor9, avMonths9, avWealth9])

csvfileout.close()



