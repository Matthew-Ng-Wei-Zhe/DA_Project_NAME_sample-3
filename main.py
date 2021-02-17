#########################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Description: This program allows user to analyse Top 3 Country in SEA coming to Singapore from 2007 to 2017
#Name: <Matthew Ng Wei Zhe>
#Group Name: <Python Underdog>
#Class: <PN2004J>
#Date: <17-02-21>
#Version: <1.1>
#########################################################################

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pandas for data analysis
import pandas as pd

#import matplotlib for graphic mode (Optional)
import matplotlib.pyplot as pit

#########################################################################
#IMPORT Pandas Library for Data Analysis
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
#CLASS Branch: End of Code
#########################################################################

#########################################################################
#FUNCTION Branch - sortCountry
#parses data and displays sorted result(s)
#########################################################################
def sortCountry(df):
  token = 0

  #slicing dataframe using iloc 2007 - 2017 SEA to form new dataframe
  new_df = df.iloc[348:479, 0:9]
  #form new dataframe based on new index and disposable of the old index column
  new_df = new_df.reset_index(drop=True)

  #disply new dataframe (rows and colums)
  print("\nThe following dataframe for SEA from 2007 - 2017 are read as follows: \n")
  print(new_df)

  #selecting country columns and adding them on a vertical axis in descending order based on top 3
  top3_country = new_df.iloc[:, 2:9].sum(axis=0).sort_values(ascending=False).nlargest(3)

  #print top 3 countries coming to Singapore in SEA from 2007 - 2017
  print("\nThe top 3 countries with the most visitors coming to Singapore listed in SEA from 2007 - 2017 are read as follows:\n")

  #reset index to generate new dataframe for sum value output
  top3_country = top3_country.reset_index()
  #sort sum value output into columns based on country and visitors
  top3_country.columns = ["Country", "Visitors"]
  #label top 3
  top3_country.index = ["Most Visted →", "Second Most Visted → ", "Third Most Visted →"]

  #display top 3 countries coming to Singapore in SEA from 2007 - 2017
  try:
   print(top3_country)
  except:
   print("An ERROR has occured!!!")
  else:
    token = token + 1

  if token >= 1:
    user_decision = input("\nDo you want a graphical model? Yes/No : ",)
    if user_decision == "Yes":
     activities = ['Indonesia', 'Malaysia', 'Philippines']
     slices = [1, 3, 4]
     pit.pie(slices,
        labels=activities,
        startangle=90,
        shadow=True,
        explode=(0.2, 0, 0),
        autopct='%1.2f%%')

     pit.show()
     print("Request is successful!")
    elif user_decision == "No":
     print("Request has been passed!")
    else:
      print("Invalid input! Request has been passed!")


  #return function to caller which makes call to other function
  return

#########################################################################
#FUNCTION Branch: End of Code
#########################################################################

#########################################################################
#Main Branch
#########################################################################
if __name__ == '__main__':
  
  #Project Title
  print('######################################')
  print('# Data Analysis App - PYTHON Project #')
  print('######################################')

  #perform data analysis on specific excel (CSV) file
  DataAnalysis()

#########################################################################
#Main Branch: End of Code
#########################################################################