import csv

packing_list = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Tooth brushes', 2],
  ['Make up', 15],
  ['Shoes', 2]
]

try: 
    with open('packing_list.csv', 'r') as file:
       pass

except FileNotFoundError:
  print('Packing list file not found. Creating a new one.')

with open('packing_list.csv', 'w', newline='') as file:
   writer = csv.writer(file)
   writer.writerows(packing_list)
