# Python Challenge
# Rafael Brennand

import pandas as pd

#Path to PyBank data
csv_path = "../Resources/budget_data.csv"

bank_df = pd.read_csv(csv_path)

#Count number of months 
index = bank_df.index
number_of_months = len(index)

#Net amount of profit/losses
PLsum = bank_df["Profit/Losses"].sum()

#Average of Profit/Losses (INCOMPLETE)
bank_df["Changes"] = bank_df["Profit/Losses"].diff()
PLavg = round(bank_df["Changes"].mean(), 2)


#Greatest Profit
Profit = bank_df[bank_df["Changes"] == bank_df["Changes"].max()]
GProfit = Profit[["Date","Changes"]]

#Greatest Loss
Loss = bank_df[bank_df["Profit/Losses"] == bank_df["Profit/Losses"].min()]
GLoss = Loss[["Date","Changes"]]

#Print Results
print("Financial Analysis\n")
print("-------------------------\n")
print(f"Total Months: {number_of_months}\n")
print(f"The net amount of Profit/Losses is: ${PLsum}\n")
print(f"The average amount of Profit/Losses is: ${PLavg}\n")
print(f"The greatest profit is:\n {GProfit}\n")
print(f"The greatest loss is:\n {GLoss}")

#Export Results

Results = open("Results.txt","w+")
Results.write( 
    f"Financial Analysis\n" 
    f"-------------------------\n"
    f"Total Months: {number_of_months}\n"
    f"The net amount of Profit/Losses is: ${PLsum}\n"
    f"The average amount of Profit/Losses is: ${PLavg}\n"
    f"The greatest profit is:\n {GProfit}\n"
    f"The greatest loss is:\n {GLoss}")

