import os
import csv

path = "PyPoll/Resources/election_data.csv"

with open(path) as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    data=[row for row in csvreader]

    
    candidates = {}
    #Total
    total_votes = len(data)
    print(total_votes)


    candidate_votes = []
    for row in data:
        candidate_votes.append(row[2])

    unique_candidates = set(candidate_votes)

    for candidate in unique_candidates:
        candidates[candidate] = 0


    for vote in candidate_votes:
        candidates[vote] += 1
    print(candidates)

    candidates_perc = {}
    for candidate in unique_candidates:
        vote_count = candidates[candidate]
        candidates_perc[candidate] = int(round(vote_count/total_votes * 100, 0))
    print(candidates_perc)

    
    winner_name = ""
    winner_votes = 0
    winner_pct = 0
    for key, value in candidates.items():
        if value > winner_votes:
            winner_votes = value
            winner_name = key
            winner_perc = candidates_perc[key]


print("Election Results")
print("------------------------")
print(f"Total Votes:  {total_votes}")
print("------------------------")
for w in sorted(candidates, key=candidates.get, reverse=True):
    print(f"{w}: {candidates_perc[w]}% ({candidates[w]})")
print("------------------------")
print(f"{winner_name} IS THE WINNER")




output_file = os.path.join("analysis.txt")


with open(output_file, "w") as text_file:



    text_file.write("Election Results\n")
    text_file.write("------------------------\n")
    text_file.write(f"Total Votes:  {total_votes}\n")
    text_file.write("------------------------\n")
    for w in sorted(candidates, key=candidates.get, reverse=True):
        text_file.write(f"{w}: {candidates_perc[w]}% ({candidates[w]})\n")
    text_file.write("------------------------\n")
    text_file.write(f"Winner: {winner_name}\n")
    text_file.write("------------------------\n")