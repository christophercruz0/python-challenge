import pandas as pd, numpy as np, csv 
#Read file into Pandas for analysis
poll = pd.read_csv(r'/Users/christophercruz/Documents/python-challenge/PyPoll/election_data.csv')
#counting total votes 
total_votes = poll['Ballot ID'].count()
#Calculating %'s for each candidate
Percentage_votes =  np.round(100 * poll.groupby('Candidate')['Ballot ID'].count() /poll["Ballot ID"].count(),decimals=3) 
#Counting votes for each candidate
Candidate_votes = poll.groupby('Candidate')['Ballot ID'].count()
#combining %'s and counts into one data frame
results_combined = pd.merge(Percentage_votes,Candidate_votes, how='left', on='Candidate')
#Resetting index's for use later on
Candidate_votes = Candidate_votes.reset_index()
results_combined = results_combined.reset_index()
#Calculating Max amount of votes from dataframe candidate votes
mx = Candidate_votes[Candidate_votes['Ballot ID']==Candidate_votes['Ballot ID'].max()]
#resetting index for grabbing cadidate name 
winner = mx.reset_index()
#grabbing candidate name
winner = winner["Candidate"]

#renaming columns
results_combined = results_combined.rename(columns={'Ballot ID_x':'Vote Percentage','Ballot ID_y':'Vote Count'})

#printing out results
print('\nElection Results\n')
print('-------------------------\n')
print('Total Votes: ' + total_votes.astype(str)+'\n')
print('-------------------------\n')

#looping through data frame adding a space between results and converting percentage and vote count to strings to concat.
for index,row in results_combined.iterrows():
    print(row["Candidate"]+":  "+str(row['Vote Percentage'])+'% '+'('+str(row['Vote Count'])+")\n")
    
print('-------------------------\n')
print('Winner: '+winner.to_string(header=False,index=False)+'\n')
print('-------------------------')



file = open('PollSolution.csv','w')
writer = csv.writer(file)
writer.writerow([])
writer.writerow(["Election Results"])
writer.writerow([])
writer.writerow(["-------------------------"])
writer.writerow([])
writer.writerow(['Total Votes: ' + total_votes.astype(str)])
writer.writerow([])
writer.writerow(['-------------------------'])
writer.writerow([])

for index,row in results_combined.iterrows():
    writer.writerow([row["Candidate"]+":  "+str(row['Vote Percentage'])+'% '+'('+str(row['Vote Count'])+")"])
    writer.writerow([])    
    
writer.writerow(['-------------------------'])
writer.writerow([])
writer.writerow(['Winner: '+winner.to_string(header=False,index=False)])
writer.writerow([])
writer.writerow(['-------------------------'])
writer.writerow([])
file.close()



