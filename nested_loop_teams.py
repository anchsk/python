teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    print(home_team)
    for guest_team in teams:
        if home_team != guest_team:
            print(home_team + ' vs ' + guest_team)

# Output:
"""
Dragons
Dragons vs Wolves
Dragons vs Pandas
Dragons vs Unicorns
Wolves
Wolves vs Dragons
Wolves vs Pandas
Wolves vs Unicorns
Pandas
Pandas vs Dragons
Pandas vs Wolves
Pandas vs Unicorns
Unicorns
Unicorns vs Dragons
Unicorns vs Wolves
Unicorns vs Pandas
"""