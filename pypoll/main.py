import os
import csv

# Set the path to the CSV file
csv_path = os.path.join("/Users", "peijuwu", "Desktop", "python-challenge", "PyPoll", "Resources", "election_data.csv")

# Open the CSV file
with open(csv_path, "r") as f:
    csv_reader = csv.reader(f)
    header= next(csv_reader)  # Store the header row
    
    total_votes = 0
    candidates = []
    candidate_count = {}

    # Iterate over each line in the CSV file
    for line in csv_reader:
        total_votes += 1 # Increment the total number of votes
        candidate = line[2]# Extract the candidate from the line

        # Track unique candidate names
        if candidate not in candidates:
            candidates.append(candidate)

        # Count votes for each candidate
        candidate_count[candidate] = candidate_count.get(candidate, 0) + 1

    # Print the election results
    print("Election Results")
    print("-----------------------")
    print(f"Total Votes: {str(total_votes)}")
    print("-----------------------")
    
    # Calculate and print the vote percentage for each candidate
    for candidate, count in candidate_count.items():
        percentage = (count / total_votes) * 100
        print(f'{str(candidate)} : {percentage:.3f}% ({str(count)})')
        
        # Determine the winner
        winner = max(candidate_count, key=candidate_count.get)
    
    print("----------------------")
    print(f"Winner: {str(winner)}")
    print("----------------------")

# Set the path for the output file
file_path = os.path.join("/Users", "peijuwu", "Desktop", "python-challenge", "PyPoll", "analysis", "Election Results.txt")

# Write the results to a text file
with open(file_path, "w") as new_f:
    new_f.write("Election Results\n")
    new_f.write("-------------------------\n")
    new_f.write(f"Total Votes: {str(total_votes)}\n")
    new_f.write("-------------------------\n")
    
    # Write the vote percentage for each candidate to the file
    for candidate, count in candidate_count.items():
        percentage = (count / total_votes) * 100
        new_f.write(f'{str(candidate)}: {percentage:.3f}% ({str(count)})\n')
        
    # Write the winner information to the file
    new_f.write("-------------------------\n")
    new_f.write(f"Winner: {str(winner)}\n")
    new_f.write("-------------------------\n")
