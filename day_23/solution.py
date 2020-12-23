def perform_moves_ll(cups, n_moves = 100):
    linked_list = [0]*(len(cups)+1)
    for current_cup, next_cup in zip(cups, cups[1:]):
        linked_list[current_cup] = next_cup
    linked_list[cups[-1]] = cups[0]

    current_cup = cups[0]
    for i in range(n_moves):
        # step 1
        three_cups = []
        remove_cup = linked_list[current_cup]
        for i in range(3):
            three_cups.append(remove_cup)
            remove_cup = linked_list[remove_cup]
        linked_list[current_cup] = remove_cup

        # step 2
        destination_cup = (current_cup - 1) % len(linked_list)
        while destination_cup in three_cups or destination_cup <= 0:
            destination_cup = (destination_cup - 1) % len(linked_list)

        # step 3
        next_cup = linked_list[destination_cup]
        linked_list[destination_cup] = three_cups[0]
        linked_list[three_cups[0]] = three_cups[1]
        linked_list[three_cups[1]] = three_cups[2]
        linked_list[three_cups[2]] = next_cup

        # step 4
        current_cup = linked_list[current_cup]

    return linked_list

def ll_to_list(input):
    result = []
    current_cup = input[1]
    while current_cup != 1:
        result.append(current_cup)
        current_cup = input[current_cup]
    return result

# part 1
original_cups = [int(x) for x in '538914762']
cups = perform_moves_ll(original_cups, n_moves=100)
print(''.join([str(x) for x in ll_to_list(cups)]))

# part 2
cups = [int(x) for x in '538914762']
for i in range(max(cups)+1, int(1e6)+1):
    cups.append(i)
cups = perform_moves_ll(cups, n_moves=int(10e6))
print(cups[1]*cups[cups[1]])

