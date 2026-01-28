from functools import reduce

playlist = [
  ('Streets', 5.47), 
  ('Eyes Without A Face', 4.59), 
  ('Genie', 5.49), 
  ('Mr Magic (Through the Smoke)', 3.57), 
  ('Open My Door', 2.33),
  ('Chronic Sunshine', 4.31),
  ('Discrecion', 5.00),
  ('Green Eyes', 3.18),
  ('Steeeam', 2.51),
  ('flame', 4.03),
  ('Back to the old house', 3.06)
  ]

def longer_than_five_minutes(song):
  return song[1] > 5

filtered_songs = list(filter(longer_than_five_minutes, playlist))
  
def minutes_to_seconds(song):
  duration = song[1]
  minutes = int(duration)
  seconds = (duration - minutes) * 60
  total_seconds = minutes * 60 + round(seconds)
  return minutes * 60 + round(seconds)

converted_playlist = list(map(minutes_to_seconds, playlist))

def add_durations(total, duration):
  return total + duration

total_time = reduce(add_durations, converted_playlist)
  
print('The songs that last more than 5 minutes are:', list(filtered_songs))
print('Your music in seconds:', converted_playlist)
print('The total of seconds of your songs:', total_time)
