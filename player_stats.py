#  Kansas City Chiefs players

players = [
 {'name': 'kareem hunt',
  'position': 'RB',
  'jersey_number': 29,
  'yds': 611,
  'touchdowns': 8},

 {'name': 'patrick mahones',
  'position': 'QB',
  'jersey_number': 15,
  'yds': 3587,
  'touchdowns': 22},

 {'name': 'chris oladokum',
  'position': 'QB',
  'jersey_number': 19,
  'yds': 235,
  'touchdowns': 1},

 {'name': 'chamarri conner',
  'position': 'DB',
  'jersey_number': 27,
  'yds': 0,
  'touchdowns': 0},

 {'name': 'gardner mindshew',
  'position': 'QB',
  'jersey_number': 17,
  'yds': 37,
  'touchdowns': 0},

 {'name': 'isiah pacheco',
  'position': 'RB',
  'jersey_number': 10,
  'yds': 432,
  'touchdowns': 1},

 {'name': 'rashee rice',
  'position': 'WR',
  'jersey_number': 4,
  'yds': 571,
  'touchdowns': 5},

 {'name': 'marquise brown',
  'position': 'WR',
  'jersey_number': 5,
  'yds': 587,
  'touchdowns': 5},

 {'name': 'xavier worthy',
  'position': 'WR',
  'jersey_number': 5,
  'yds': 587,
  'touchdowns': 5},

 {'name': 'juju smith schuster',
  'position': 'WR',
  'jersey_number': 9,
  'yds': 345,
  'touchdowns': 1},
]

positions = [player['position'] for player in players]
print('Player positions:', positions)

total_yds = sum(player['yds'] for player in players)
total_touchdowns = sum(player['touchdowns'] for player in players)

average_yds = total_yds / len(players)
average_touchdowns = total_touchdowns / len(players)

print(f"Average yards gained: {average_yds:.2f}")
print(f"Average touchdowns: {average_touchdowns:.2f}")

for player in players:
  if player['name'] == 'Isiah Pacheco':
    player['yds'] += 85
    player['touchdowns'] += 1
