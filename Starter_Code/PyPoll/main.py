import csv

voter_ids = []
counties = []
candidates = []

# Load the election data from the CSV file
with open('PyPoll\\Resources\\election_data.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvfile)

    for row in csvreader:
        voter_ids.append(row[0])
        counties.append(row[1])
        candidates.append(row[2])

# Calculate the total number of votes cast
total_votes = len(voter_ids)

# Create a dictionary to store candidate vote counts
candidate_votes = {}

# Calculate the number of votes each candidate won
for candidate in candidates:
    if candidate in candidate_votes:
        candidate_votes[candidate] += 1
    else:
        candidate_votes[candidate] = 1

# Determine the winner based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)

# Create the analysis summary
analysis_summary = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
"""

# Loop through the candidate vote counts and calculate percentages
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    analysis_summary += f"{candidate}: {percentage:.3f}% ({votes})\n"

analysis_summary += f"-------------------------\nWinner: {winner}\n-------------------------"

# Print the analysis to the terminal
print(analysis_summary)

# Export the results to a text file
output_file = "election_results.txt"
with open(output_file, "w") as text_file:
    text_file.write(analysis_summary)

print(f"Analysis results have been saved to {output_file}")