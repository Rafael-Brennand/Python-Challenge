# Python Challenge
# Rafael Brennand

import pandas as pd

#Path to PyPoll data
csv_path = "../Resources/election_data.csv"

poll = pd.read_csv(csv_path)

#Count total number of votes
index = poll.index
number_of_votes = len(index)


#Get list of candidates who received votes
percent = round(100 * poll["Candidate"].value_counts(normalize=True), 2)
counts = poll["Candidate"].value_counts()
candidates = pd.DataFrame({"Percent": percent, "Count": counts })


#Get the Poll Winner
Winnerc = poll['Candidate'].value_counts()[:1].index.tolist()
Winner = Winnerc[0]


#Print results
print(f"Election Results\n")
print(f"----------------\n")
print(f"Total votes: {number_of_votes}\n")
print(f"----------------\n")
print(f"{candidates}\n")
print(f"----------------\n")
print(f"The winner is : {Winner}\n")

#Export Results
Results = open("Results.txt","w+")
Results.write(
    f"Election Results\n"
    f"----------------\n"
    f"Total votes: {number_of_votes}\n"
    f"----------------\n"
    f"{candidates}\n"
    f"----------------\n"
    f"The winner is : {Winner}\n")