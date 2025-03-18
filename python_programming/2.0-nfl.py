""" 
open csv file nfl_offensive_stats.csv and read the data from the file
"""

import csv

# Open the CSV file
with open('python_programming/nfl_offensive_stats.csv', mode='r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    # Skip the header (if not using list)
    # next(csv_reader)
    nfl_data = list(csv_reader)

    """ in this data, the 4th column is a player, and the 8th column is yards. Get a sum of yards from the column 8 where the 4th column value is Aaron Rogers  """
    
    passing_yards = 0
    for row in nfl_data:
        if row[3] == "Aaron Rodgers":
            passing_yards += int(row[7])

            
print(f'Passing yards for Aaron Rodgers: {passing_yards}')