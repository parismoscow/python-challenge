import csv
import os
cvs_path = os.path.join('..', 'Resources', 'election_data.csv')

with open(cvs_path, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # print(csv_reader)

    csv_header = next(csv_reader)
    # print(csv_header, '\n')
    # print(f'CSV Header: {csv_header}' '\n')

    candidates = []  # ['Khan', 'Correy', 'Li', "O'Tooley"]
    k_vote_counter = 0
    c_vote_counter = 0
    l_vote_counter = 0
    o_vote_counter = 0

    number_of_votes = 0

    for row in csv_reader:
        number_of_votes += 1
        # Getting all candidates
        if row[2] not in candidates:
            candidates.append(row[2])
        if row[2] == 'Khan':
            k_vote_counter += 1  # Counting Khan's vote
        elif row[2] == 'Correy':
            c_vote_counter += 1  # Counting Correy's vote
        elif row[2] == 'Li':
            l_vote_counter += 1  # Counting Li's vote
        else:
            o_vote_counter += 1  # Counting O'Tooley's vote

    k_vote_percent = round((k_vote_counter / number_of_votes) * 100, 2)
    c_vote_percent = round((c_vote_counter / number_of_votes) * 100, 2)
    l_vote_percent = round((l_vote_counter / number_of_votes) * 100, 2)
    o_vote_percent = round((o_vote_counter / number_of_votes) * 100, 2)

    print('Election Results\n-------------------------')
    print('Total Votes: {}'.format(number_of_votes), '\n-------------------------')
    print('{}:  {}%  ({})'.format(candidates[0], k_vote_percent, k_vote_counter))
    print('{}:  {}%  ({})'.format(candidates[1], c_vote_percent, c_vote_counter))
    print('{}:  {}%  ({})'.format(candidates[1], l_vote_percent, l_vote_counter))
    print('{}:  {}%  ({})'.format(candidates[3], o_vote_percent, o_vote_counter))
    print('-------------------------')

    max_vote = (max(k_vote_counter, c_vote_counter, l_vote_counter, o_vote_counter))

    results = {}
    list_counter = [k_vote_counter, c_vote_counter, l_vote_counter, o_vote_counter]

    for i in range(len(candidates)):
        results[candidates[i]] = list_counter[i]

    for name, vote in results.items():
        if vote == max_vote:
            winner = name
    print('Winner:', winner)
    
    PyPoll_final_file = os.path.join("..",'Resources', "PyPoll_Summary.txt")
    with open (PyPoll_final_file, "w") as file:
    # Write methods to print PyPoll_summary
        file.write('Election Results')
        file.write("\n")
        file.write('------------------')
        file.write("\n")
        file.write(f"Total Votes: {number_of_votes}")
        file.write("\n")
        file.write('------------------')
        file.write("\n")
        file.write(f"{candidates[0], k_vote_percent, '%', k_vote_counter}")
        file.write("\n")
        file.write(f"{candidates[1], c_vote_percent , '%', c_vote_counter}")
        file.write("\n")
        file.write(f"{candidates[2], l_vote_percent , '%', l_vote_counter}")
        file.write("\n")
        file.write(f"{candidates[3], o_vote_percent , '%', o_vote_counter}")
        file.write("\n")
        file.write('------------------')
        file.write("\n")
        file.write(f"Winner: {winner}")