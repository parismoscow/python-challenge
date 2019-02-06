import csv
import os
cvs_path = os.path.join('..', 'Resources', 'budget_data.csv')

with open(cvs_path, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    print(csv_reader)

    csv_header = next(csv_reader)
    print(csv_header, '\n')
    # print(f'CSV Header: {csv_header}' '\n')

    net_total = 0
    count = 0
    changes = []

    for row in csv_reader:
        row_data = (row[0]).split(',')
        profit_loss = int(row_data[1])
        changes.append(profit_loss)
        print(profit_loss)
        net_total = net_total + profit_loss
        count += 1

    print()
    print('Financial Analysis', '\n' '-------------------')
    print('Total Months: ', count)
    print('Total:', '$', net_total)

    i = 0
    j = 1
    total_net_changes = []
    while j < len(changes):
        net_change = changes[j] - changes[i]
        total_net_changes.append(net_change)
        i += 1
        j += 1

    sum_of_total_net_changes = sum(total_net_changes)
    average_change = round(sum_of_total_net_changes / (len(total_net_changes)), 2)
    greatest_increase = max(total_net_changes)
    greatest_decrease = min(total_net_changes)

    print('Average Change', '$', average_change)
    print('Greatest Increase in Profits:', greatest_increase)
    print('Greatest Decrease in Profits:', greatest_decrease)