valid_count = 0
valid_count_2 = 0

with open("input.txt", 'r') as file:
    for line in file:
        policy, letter, password = line.split(" ")
        min_pol, max_pol = policy.split("-")
        letter = letter[0]
        appearances = password.count(letter)
        if int(min_pol) <= appearances <= int(max_pol):
            valid_count += 1
        if sum((password[int(min_pol)-1] == letter, password[int(max_pol)-1] == letter)) == 1:
            valid_count_2 += 1

print(valid_count)
print(valid_count_2)

