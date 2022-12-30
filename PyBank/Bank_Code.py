import pandas as pd, numpy as np, csv 
#grabbing data and creating a dataframe 
bank = pd.read_csv(r'/Users/christophercruz/Documents/python-challenge/PyBank/budget_data.csv')
#creating a new column that completes the difference between each month
bank['Profit/Losses Diff'] = bank['Profit/Losses'].diff()
#calculating mean of the differences 
avg = bank['Profit/Losses Diff'].mean()
#rounding the mean
avg = np.round(avg,decimals=2)
#Running a comparison to look for the max and min
mx, mn = bank[['Profit/Losses Diff']][bank['Profit/Losses Diff']==bank['Profit/Losses Diff'].max()],bank[['Profit/Losses Diff']][bank['Profit/Losses Diff']==bank['Profit/Losses Diff'].min()]
mn, mx = mn.astype(int), mx.astype(int)
#running a comparison to look for the date of the max and min
dtmx ,dtmn = bank[['Date']][bank['Profit/Losses Diff']==bank['Profit/Losses Diff'].max()],bank[['Date']][bank['Profit/Losses Diff']==bank['Profit/Losses Diff'].min()]

#Printing out results
print("\n\nFinanacial Analysis\n")
print("----------------------------\n")
#change type to string and added a new line 
print("Total Months: "+bank["Date"].count().astype(str)+'\n')
print("Total: $"+bank["Profit/Losses"].sum().astype(str)+'\n')
print("Average Change: $" + avg.astype(str)+'\n')
#removed header and index from displaying in the terminal and output file
print("Greatest Increase in Profits: "+dtmx.to_string(header=False,index=False)+' ($'+ mx.to_string(header=False,index=False)+')\n')
print("Greatest Decrease in Profits: "+dtmn.to_string(header=False,index=False)+' ($'+ mn.to_string(header=False,index=False)+')\n\n')


file = open('BankSolution.csv','w')
writer = csv.writer(file)
writer.writerow([])
writer.writerow(["Finanacial Analysis"])
writer.writerow([])
writer.writerow(["----------------------------"])
writer.writerow([])
writer.writerow(["Total Months: "+bank["Date"].count().astype(str)])
writer.writerow([])
writer.writerow(["Total: $"+bank["Profit/Losses"].sum().astype(str)])
writer.writerow([])
writer.writerow(["Average Change: $" + avg.astype(str)])
writer.writerow([])
writer.writerow(["Greatest Increase in Profits: "+dtmx.to_string(header=False,index=False)+' ($'+ mx.to_string(header=False,index=False)+')'])
writer.writerow([])
writer.writerow(["Greatest Decrease in Profits: "+dtmn.to_string(header=False,index=False)+' ($'+ mn.to_string(header=False,index=False)+')'])
file.close()

