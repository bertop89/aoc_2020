player_1 = []
player_2 = []
is_player_1 = True
with open("input.txt", 'r') as file:
    for line in file.readlines():
        if line == '\n':
            continue
        if 'Player 1' in line:
            is_player_1 = True
        elif 'Player 2' in line:
            is_player_1 = False
        else:
            num = int(line[:-1])
            if is_player_1:
                player_1.append(num)
            else:
                player_2.append(num)

orig_player_1 = player_1.copy()
orig_player_2 = player_2.copy()

# part 1
while len(player_1) > 0 and len(player_2) > 0:
    draw_1 = player_1.pop(0)
    draw_2 = player_2.pop(0)
    if draw_1 > draw_2:
        player_1.append(max(draw_1, draw_2))
        player_1.append(min(draw_1, draw_2))
    else:
        player_2.append(max(draw_1, draw_2))
        player_2.append(min(draw_1, draw_2))

def compute_score(input):
    return sum([x * y for x, y in zip(reversed(input), range(1, len(input) + 1))])

print(compute_score(player_1))
print(compute_score(player_2))

# part 2
def recursive_combat(deck_1, deck_2):
    played_games = set()
    while len(deck_1) > 0 and len(deck_2) > 0:
        current_cards = (tuple(deck_1), tuple(deck_2))
        if current_cards in played_games:
            return True, deck_1
        played_games.add(current_cards)
        draw_1 = deck_1.pop(0)
        draw_2 = deck_2.pop(0)
        if len(deck_1) >= draw_1 and len(deck_2) >= draw_2:
            player_1_wins, _ = recursive_combat(deck_1[:draw_1].copy(), deck_2[:draw_2].copy())
        else:
            player_1_wins = draw_1 > draw_2
        if player_1_wins:
            deck_1.append(draw_1)
            deck_1.append(draw_2)
        else:
            deck_2.append(draw_2)
            deck_2.append(draw_1)
    if len(deck_1) > 0:
        return True, deck_1
    else:
        return False, deck_2

_, winner_deck = recursive_combat(orig_player_1, orig_player_2)
print(winner_deck)
print(compute_score(winner_deck))
