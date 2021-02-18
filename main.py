#########################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Description: This program allows user to analyse CSV file to Dataframe
#Name: <Matthew Ng Wei Zhe>
#Group Name: <Python Underdog>
#Class: <PN2004J>
#Date: <17-02-21>
#Version: <2.0>
#########################################################################

#########################################################################
#IMPORT Pandas Library for Data Analysis and Matplotlib for Graphic Mode
#########################################################################
#import pandas for data analysis
import pandas as pd

#import matplotlib for graphic mode
import matplotlib.pyplot as uo
#########################################################################

#########################################################################
#CLASS Branch - Data Analysis
#load excel data (CSV format) to dataframe
#########################################################################
class DataAnalysis:
  def __init__(self):

    #load excel data (CSV format) to dataframe - 'df'
    dataframe = pd.read_csv('MonthyVisitors.csv')

    #show specific country dataframe
    sortCountry(dataframe)
#########################################################################

#########################################################################
#FUNCTION Branch - sortCountry
#parses data and displays sorted result(s)
#########################################################################
def sortCountry(df):
  #key to unlock graphical mode if function goes well
  graphical_token = 0

  #slicing dataframe using iloc based on primary objective and form new dataframe properly
  new_df = df.iloc[348:479, 0:9].reset_index(drop=True)

  #disply new dataframe (rows and colums)
  print("\nRegion: South East Asia" + "\nPeriod: 2007 - 2017\n" + "\nThe following Dataframe read as follow,\n")
  print(new_df)

  #selecting country columns and adding them on a vertical axis in descending order based on top 3 and form new dataframe
  top3_country = new_df.iloc[:, 2:9].sum(axis=0).sort_values(ascending=False).nlargest(3).reset_index()

  #print top 3 countries coming to Singapore in SEA from 2007 - 2017
  print("\nHere are the top 3 countries coming to Singapore listed above,\n")

  #sort sum value output into columns based on country and visitors
  top3_country.columns = ['Country', 'Visitors']
  #change index to represnet top 3
  top3_country.index = ['Most Visted →', 'Second Most Visted → ', 'Third Most Visted →']

  #display top 3 countries coming to Singapore in SEA from 2007 - 2017 and validate token in case of error
  try:
   print(top3_country)
  except:
   print("An ERROR has occured!!!")
  else:
    graphical_token += 1 #give token/key +1

  if graphical_token >= 1: #identify token/key to unlock user input for graphical mode decision
    user_decision = input("\nDo you want a graphical model? Y/N : ",).lower() #convert all input to lowercase to minimize user input error
    if user_decision == 'y': #accept graphical mode
     print("Request has been passed!")
     #fill in graphical mode information
     countries = ['Brunei Darussalam ', 'Indonesia', 'Malaysia', 'Philippines', 'Thailand', 'Viet Nam', 'Myanmar']
     slices = [715883, 27572424, 11337420, 6548622, 4945136, 3914607, 1042608]
     uo.pie(slices, labels=countries, startangle=90, shadow=False, autopct='%1.2f%%')
     uo.legend()
    elif user_decision == 'n': #deny graphical mode
     print("Request has been aborted!")
    else: #report and deny graphical mode
      print("Invalid input! Request has been aborted!")


  #return function to caller which makes call to other function
  return
#########################################################################

#########################################################################
#Primary Branch
#########################################################################
if __name__ == '__main__':
  
  #Project Title
  print('##############################################')
  print('# Primary Data Analysis App - PYTHON Project #')
  print('##############################################')

  #perform data analysis on specific excel (CSV) file
  DataAnalysis()

  print('\n\n################################################')
  print('# Secondary Data Analysis App - PYTHON Project #')
  print('################################################')

  uo.show()
#########################################################################


#########################################################################
#End of Code 
#########################################################################
