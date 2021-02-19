#########################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Description: This program allows user to analyse CSV file to Dataframe
#Name: <Matthew Ng Wei Zhe>
#Group Name: <Python Underdog>
#Class: <PN2004J>
#Date: <17-02-21>
#Version: <5.0a>
#########################################################################

#########################################################################
#IMPORT Pandas Library for Data Analysis and Matplotlib for Graphic Mode
#########################################################################
#import pandas for data analysis
import pandas as pd

#import matplotlib for graphical conversion
import matplotlib.pyplot as pi
#########################################################################

#########################################################################
#CLASS Branch - Data Analysis
#load excel data (CSV format) to dataframe
#########################################################################
class DataAnalysis:
  def __init__(self):

    #load csv file to dataframe format
    dataframe = pd.read_csv('MonthyVisitors.csv')

    #show specific country dataframe
    sortCountry(dataframe)
#########################################################################

#########################################################################
#FUNCTION Branch - sortCountry
#parses data and displays sorted result(s)
#########################################################################
def sortCountry(df):
  #key to unlock functions
  graphical_token = 0

  #slice dataframe
  new_df = df.iloc[348:479, 0:9].reset_index(drop=True)

  #display new dataframe (rows and colums)
  print("\nRegion: South-East Asia" + "\nPeriod: 2007 - 2017\n" + "\nThe following Dataframe read as follow,\n")
  print(new_df)

  #select country columns, add them on a vertical axis in descending order based on top 3 and form new dataframe
  top3_country = new_df.iloc[:, 2:9].sum(axis=0).sort_values(ascending=False).nlargest(3).reset_index()

  #print top 3 
  print("\nHere are the top 3 countries coming to Singapore listed above,\n")

  #sort sum value output into columns based on country and visitors
  top3_country.columns = ['Country', 'Visitors']
  #change index to represent top 3
  top3_country.index = ['Most Visted →', 'Second Most Visted → ', 'Third Most Visted →']

  #display top 3 countries
  try:
   print(top3_country)
  except:
   print("An ERROR has occured!!!")
  else:
    graphical_token += 1 #give key

  if graphical_token >= 1: #check for key to unlock graphical conversion
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

  #load csv file to dataframe format seperated from function
  original = pd.read_csv('MonthyVisitors.csv')

  #error-checking region input
  while True:
   #create region list for desire input
   region = []

   #print region information
   print("\nHere are the available regions,")
   print("(1) South-East Asia"
        ,"\n(2) Asia-Pacific"
        , "\n(3) South-Asia Pacific"
        , "\n(4) Middle-East"
        , "\n(5) Europe"
        , "\n(6) North-America"
        , "\n(7) Australia & Africa")
   #ask for user region input
   country_input = input("\nPlease select a region, E.g. 4 for Europe: \n", )

   #lock user region input
   if country_input == '1':
     original = original.iloc[:, 0:9]#slice dataframe
     region.append("South-East Asia")#append to region list
     break
   elif country_input == '2':
     #.columns.tolist() returns/adds desire index to first silcing list ['Year', 'Month'] and slice the rest
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
   #report invalid input
   else:
     print("Invalid Input! Please try again!")

  #error-checking starting period input
  while True:
   #create list to check user period input
   year = str(list(range(1978, 2018))) #check valid year input
   month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] #check valid month input

   #ask for user starting period input YY MM or YY
   start_time = input("\nPlease choose a start period from 1978 Jan to 2017 Nov," + "\nE.g. 1990 Jan or 1990: \n",)

   #determine starting period input format YY MM or YY
   if len(start_time.split()) > 1:#if YY MM was used
     if start_time != "2017 Dec":#deny "2017 Dec" → not included
      #split YY MM to "YY" and "MM" into two variables start_year(YY) and start_month(MM)
      start_year, start_month = start_time.split()
      if start_year in year and start_month in month:#check valid year and month input
       break
      else:
       print("Invalid Input! Please try again!")
     else:
       print("Invalid Input! Please try again!")
   else:#if YY was used
     start_year = start_time#put "YY" into variable start_year(YY)
     start_month = 'Jan'#ensure YY always starting in the starting month of "Jan"
     if start_year in year:#check valid year input
       break
     else:
       print("Invalid Input! Please try again!")
  
  #error-checking starting period input
  while True:
   #ask for user ending period input YY MM or YY
   end_time = input("\nPlease choose a end period from your start period to 2017 Nov," + "\nE.g. 1990 Jan or 1990: \n",)
  
   #determine starting period input format YY MM or YY
   if len(end_time.split()) > 1:#if YY MM was used
     if end_time != "2017 Dec":#deny "2017 Dec" → not included
      #split YY MM to "YY" and "MM" into two variables end_year(YY) and end_month(MM)
      end_year, end_month = end_time.split()#check valid year and month input
      if end_year in year and end_month in month:
        if end_year < start_year:
          print("Invalid Input! Please try again!")#check end_year does not go behind start_year
        else:
          break
      else:
       print("Invalid Input! Please try again!")
     else:
       print("Invalid Input! Please try again!")
   else:#if YY was used
     end_year = end_time#put "YY" into variable start_year(YY)
     end_month = 'Dec'#ensure YY always starting in the starting month of "Jan"
     if end_year in year: #check valid year input
       if end_year < start_year:
         print("Invalid Input! Please try again!")#check end_year does not go behind start_year
       else:
         break
     else:
       print("Invalid Input! Please try again!")
       
  #sample used to analyse the total months in a year
  month_s = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
  
  #coat a new dataframe with a set format based on 'Year' and 'Month' column ONLY
  df = pd.DataFrame(columns=['Year', 'Month'])

  #create a empty dataframe based on user period input to replace new dataframe
  if (start_year < end_year):#check start_year(YY) is lower than end_year(YY) to intialise repeated adding of month from different years
    for i in range(int(start_year), int(end_year) + 1):#start adding first YY
      if i == int(start_year):
        #create month line based on first YY input and first MM input
        month_list = month_s[month_s.index(start_month):]
      elif i == int(end_year):#start adding from first YY to last YY
        #create month line(s) based on subsequent YY input until last YY input
        month_list = month_s[:month_s.index(end_month) + 1]#+1 to add on top of subsequent month line(s)
      else:#just fills up to "Dec" if no last MM was detected e.g. 1990
        month_list = month_s

      #create the new empty dataframe
      df_temp = pd.DataFrame()
      #add the month line(s) into new empty dataframe
      df_temp['Month'] = month_list
      #add the years into new empty dataframe
      df_temp['Year'] = i

      #add all information in empty dataframe to the new dataframe "df"
      df = df.append(df_temp, ignore_index=True)

  elif (start_year == end_year):#check start_year(YY) is same as end_year(YY)
    #create the new empty dataframe
    df_temp = pd.DataFrame()
    #add months within a year to desire last MM input
    df_temp['Month'] = month_s[month_s.index(start_month):month_s.index(end_month) + 1]
    #just add the 'year' into new empty dataframe
    df_temp['Year'] = start_year
    
    #add all information in empty dataframe to the new dataframe "df"
    df = df.append(df_temp, ignore_index=True)

  #error-checking to check print period functionality
  try:
   #make sure all columns are str to be able to merge successfully
   original['Year'] = original['Year'].astype(str)
   df['Year'] = df['Year'].astype(str)
  except:#if print period can function
   print("An ERROR has occured!!!")
  else:
   print('\n################################################')
   print('# Tertiary Data Analysis App - PYTHON Project #')
   print('################################################')
   #print region list 
   print("\nRegion: " + region[0]) 
   #print start_time to end_time
   print("Period: " + start_time + " - " + end_time)

   #merge the original region user input dataframe with period user input dataframe to find common variables
   requested_df = pd.merge(original, df, how = 'inner', on = ['Year', 'Month'])
   print("\nThe following Dataframe read as follow,\n")
   print(requested_df)

  #ask for user additional input
  end_input = input("\nDo you want to see the total visitors coming to Singapore \nwithin the period accordingly? Y/N? : ", ).lower()
  if end_input == 'y':
    print("Request has been passed!\n")
    #just select country columns, add them on a vertical axis in descending order 
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


