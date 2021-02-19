#########################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Description: This program allows user to analyse CSV file to Dataframe
#Name: <Matthew Ng Wei Zhe>
#Group Name: <Python Underdog>
#Class: <PN2004J>
#Date: <17-02-21>
#Version: <4.0alpha>
#########################################################################

#########################################################################
#IMPORT Pandas Library for Data Analysis and Matplotlib for Graphic Mode
#########################################################################
#import pandas for data analysis
import pandas as pd

#import matplotlib for graphic mode
import matplotlib.pyplot as pi
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
  print("\nRegion: South-East Asia" + "\nPeriod: 2007 - 2017\n" + "\nThe following Dataframe read as follow,\n")
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
    user_decision = input("\nDo you want a graphical model? Y/N : ", ).lower() #convert all input to lowercase to minimize user input error
    if user_decision == 'y': #accept graphical mode
     print("Request has been passed!")
     #fill in graphical mode information
     countries = ['Brunei Darussalam ', 'Indonesia', 'Malaysia', 'Philippines', 'Thailand', 'Viet Nam', 'Myanmar']
     slices = [715883, 27572424, 11337420, 6548622, 4945136, 3914607, 1042608]
     pi.pie(slices, labels=countries, startangle=90, shadow=False, autopct='%1.2f%%')
     pi.legend()

     pi.show(block=False)#show pie chart without stopping program

    elif user_decision == 'n': #deny graphical mode
     print("Request has been aborted!")

    else: #report and deny graphical mode
      print("Invalid input! Request has been aborted!")


  #return function to caller which makes call to other function
  return
#########################################################################

#########################################################################
#Main Branch
#########################################################################
if __name__ == '__main__':
  
  #project title
  print('##############################################')
  print('# Primary Data Analysis App - PYTHON Project #')
  print('##############################################')

  #perform data analysis on specific excel (CSV) file
  DataAnalysis()

  #optional branch to find user input based on region and time 
  print('\n################################################')
  print('# Secondary Data Analysis App - PYTHON Project #')
  print('################################################')

  original = pd.read_csv('MonthyVisitors.csv')

  while True:

   region = []

   print("\nHere are the available regions,")
   print("(1) South-East Asia"
        ,"\n(2) Asia-Pacific"
        , "\n(3) South-Asia Pacific"
        , "\n(4) Middle-East"
        , "\n(5) Europe"
        , "\n(6) North-America"
        , "\n(7) Australia & Africa")
   country_input = input("\nPlease select a region, E.g. 4 for Europe: \n", )

   if country_input == '1':
     original = original.iloc[:, 0:9]
     region.append("South-East Asia")
     break
   elif country_input == '2':
     original = original[['Year','Month'] + original.iloc[:, 9: 14].columns.tolist()]
     region.append("South-Asia Pacific")
     break
   elif country_input == '3':
     original = original[['Year','Month'] + original.iloc[:, 14: 17].columns.tolist()]
     region.append("South-Asia Pacific")
     break
   elif country_input == '4':
     original = original[['Year','Month'] + original.iloc[:, 17: 20].columns.tolist()]
     region.append("Middle-East")
     break
   elif country_input == '5':
     original = original[['Year','Month'] + original.iloc[:, 20: 31].columns.tolist()]
     region.append("Europe")
     break
   elif country_input == '6':
     original = original[['Year','Month'] + original.iloc[:, 31: 33].columns.tolist()]
     region.append("North-America")
     break
   elif country_input == '7':
     original = original[['Year','Month'] + original.iloc[:, 33: 36].columns.tolist()]
     region.append("Australia & Africa")
     break
   else:
     print("Invalid Input! Please try again!")

  while True:
   year = str(list(range(1978, 2018)))
   month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

   start_time = input("\nPlease choose a start period from 1978 Jan to 2017 Nov," + "\nE.g. 1990 Jan or 1990: \n",)

   if len(start_time.split()) > 1:
     if start_time != "2017 Dec":
      start_year, start_month = start_time.split()
      if start_year in year and start_month in month:
       start_year
       break
      else:
       print("Invalid Input! Please try again!")
     else:
       print("Invalid Input! Please try again!")
   else:
     start_year = start_time
     start_month = 'Jan'
     if start_year in year:
       break
     else:
       print("Invalid Input! Please try again!")
  
  while True:
   end_time = input("\nPlease choose a end period from your start period to 2017 Nov," + "\nE.g. 1990 Jan or 1990: \n",)
  
   if len(end_time.split()) > 1:
     if end_time != "2017 Dec":
      end_year, end_month = end_time.split()
      if end_year in year and end_month in month:
       break
      else:
       print("Invalid Input! Please try again!")
     else:
       print("Invalid Input! Please try again!")
   else:
     end_year = end_time
     end_month = 'Dec'
     if end_year in year:
       break
     else:
       print("Invalid Input! Please try again!")
       
  month_s = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
  
  df = pd.DataFrame(columns=['Year', 'Month'])

  if (start_year < end_year):
    for i in range(int(start_year), int(end_year) + 1):
      if i == int(start_year):
        month_list = month_s[month_s.index(start_month):]
      elif i == int(end_year):
        month_list = month_s[:month_s.index(end_month) + 1]
      else:
        month_list = month_s

      df_temp = pd.DataFrame()
      df_temp['Month'] = month_list
      df_temp['Year'] = i

      df = df.append(df_temp, ignore_index=True)

  elif (start_year == end_year):
    df_temp = pd.DataFrame()
    df_temp['Month'] = month_s[month_s.index(start_month):month_s.index(end_month) + 1]
    df_temp['Year'] = start_year

    df = df.append(df_temp, ignore_index=True)

  try:
   original['Year'] = original['Year'].astype(str)
   df['Year'] = df['Year'].astype(str)
  except:
   print("An ERROR has occured!!!")
  else:
   print('\n################################################')
   print('# Tertiary Data Analysis App - PYTHON Project #')
   print('################################################')
   print("\nRegion: " + region[0]) 
   print("Period: " + start_time + " - " + end_time)
   requested_df = pd.merge(original, df, how = 'inner', on = ['Year', 'Month'])
   print("\nThe following Dataframe read as follow,\n")
   print(requested_df)

  end_input = input("\nDo you want to see the total visitors coming to Singapore \nwithin the period accordingly? Y/N? : ", ).lower()
  if end_input == 'y':
    print("Request has been passed!\n")
    last_df = requested_df.iloc[:, 2:].sum(axis=0).sort_values(ascending=False).reset_index()
    last_df.columns = ['Country', 'Visitors']
    print(last_df)
  elif end_input == 'n':
    print("Request has been aborted!")
  else:
    print("Invalid Input! Request has been aborted!")     
#########################################################################


#########################################################################
#End of Code 
#########################################################################


