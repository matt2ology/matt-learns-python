players = [29, 58, 66, 71, 87]  # numbers assigned to players

print(players[2])  # prints player number 66
players[2] = 68  # index 2 is assigned element number 68
print(players)  # outputs [29, 58, 68, 71, 87]

print("===")

# add on a new list of numbers to the ones assigned to players: [29, 58, 66, 71, 87, 90, 91, 98]
print(players + [90, 91, 98])
print(players)  # outputs the original list: [29, 58, 68, 71, 87]
# adds 120 to the list of numbers originally assigned to players
players.append(120)
print(players)  # outputs the original list plus 120: [29, 58, 68, 71, 87, 120]

print("===")

# outputs the start and stops right before index 2: [29, 58]
print(players[:2])
players[:2] = [0, 0]  # Replaces the first two elements with zeros
print(players)  # [0, 0, 68, 71, 87, 120]

players[:2] = []  # Removes the first two elements
print(players)  # [68, 71, 87, 120]

players[:] = []  # deletes the entire list
print(players)  # empty list
