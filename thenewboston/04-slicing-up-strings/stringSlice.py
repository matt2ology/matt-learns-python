user = "Tuna McFish"

print(user[0]) # Prints the letter 'T'
print(user[-1]) # Prints the letter 'h' counts from the right to left
print(user[-3]) # Prints the letter 'i' counts three characters right to left
print(user[2:7]) # Prints "na Mc" start from the 2nd index and stop at the 7th
print(user[:7])  # Prints "Tuna Mc" assumes you want from 0th index and stop at the 7th
print(user[2:])  # Prints "na McFish" starts at 2nd index and finishes to the end
print(user[:])  # Prints "Tuna McFish" starts at the beginning and stops at the end

print("===")

print(len('asdfghjklqweuioemvatt'))  # len() returns the length of the string. Returns 21
print(len(user))  # len() returns length of string stored in user var. Returns 11
