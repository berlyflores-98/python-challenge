import os
import csv

file_path = os.path.join("Resources","election_data.csv")

with open(file_path,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    total_votes = 0
    candidates = []
    candidate_count = 0
    election_data_cand = []
    candidate_total_vote = []
    per_total_vote = []
    index =0
    for row in csvreader:
        election_data_cand.append(row[2])
        candidate_name = row[2]
        total_votes += 1
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_count +=1
    
    winning_cand = ""
    max=0

    for i in candidates:
        total_count = 0
        total_count = election_data_cand.count(i)
        candidate_total_vote.append(total_count)
        if max < election_data_cand.count(i):
            max= election_data_cand.count(i)
            winning_cand = i

    per_total_vote = [round((j/total_votes)*100,3) for j in candidate_total_vote]



    
        
    print("Election Results")
    print(30*"-")   
    print(f"Total Votes: {total_votes}")
    print(30*"-") 
    for k in candidates:
        print(f"{k}: {per_total_vote[index]}% ({candidate_total_vote[index]})")
        index += 1
    print(30*"-") 
    print(f"Winner: {winning_cand}")
    print(30*"-") 

index=0   
with open (os.path.join("Analysis","output_poll.txt"),"w") as output:
    output.write("Election Results\n")
    output.write(30*"-")   
    output.write(f"\nTotal Votes: {total_votes}\n")
    output.write(30*"-") 
    for k in candidates:
        output.write(f"\n{k}: {per_total_vote[index]}% ({candidate_total_vote[index]})\n")
        index += 1
    output.write(30*"-") 
    output.write(f"\nWinner: {winning_cand}\n")
    output.write(30*"-") 

