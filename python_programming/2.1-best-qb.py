""" open csv file python_programming/nfl_offensive_stats.csv and read the data from the file, do not print the rows """
import csv

qb_yards = {}

# Open the CSV file
with open('python_programming/nfl_offensive_stats.csv', mode='r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    
    # Read the header
    header = next(csv_reader)
    # print(f'Header: {header}')

    """ 3rd column is a player's position, 4th column is a player and 8th column is yards. for each plaer whose position in the 3rd column is QB, calculate the sum of yards from column 8 """
    for row in csv_reader:
        position = row[2]
        player = row[3]
        yards = int(row[7])
        
        if position == 'QB':
            # Create a player if it doesn't exist in the dict
            if player not in qb_yards:
                qb_yards[player] = 0
            qb_yards[player] += yards

""" Print the sum of yards sorted in decreasing order """
sorted_qb_yards = sorted(qb_yards.items(), key=lambda item: item[1], reverse=True)
for player, yards in sorted_qb_yards:
    if yards > 4000:
        if player != "Tom Brady":
            print(f'{player}: {yards}')

print(f'The best quarterback is: {sorted_qb_yards[0][0]}')

