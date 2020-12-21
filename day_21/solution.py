food_list = []
with open("input.txt", 'r') as file:
    for line in file.readlines():
        ingredients, allergens = line.split("(")
        ingredients = [x.strip() for x in ingredients.strip().split()]
        allergens = [x.strip() for x in allergens[9:-2].strip().split(",")]
        food_list.append((ingredients, allergens))
print(food_list)


def remove_ing_all(food_list, ingredient, allergen):
    return [
        ([x for x in ingredients if x != ingredient], [x for x in allergens if x != allergen])
        for ingredients, allergens in food_list
    ]

import random

original_food = food_list.copy()

tries = 0
MAX_TRIES = 10000
dang_ing = []
while True:
    # restart search process
    if tries > MAX_TRIES:
        dang_ing = []
        food_list = original_food.copy()
        tries = 0
        continue
    # remove all single ingredients and allergens, insta-matches!
    while any([len(ing) == 1 and len(all) == 1 for ing, all in food_list]):
        only_ing , only_all = [(ing, all) for ing, all in food_list if len(ing) == 1 and len(all) == 1][0]
        food_list = remove_ing_all(food_list, only_ing[0], only_all[0])
    # if there are no more pending allergens
    if all([len(x[1]) == 0 for x in food_list]):
        break
    # pick a random food and select a random ingredient and allergen
    first_food = random.choice(food_list)
    while len(first_food[1]) == 0:
        first_food = random.choice(food_list)
    common_ingredient = random.choice(first_food[0])
    common_allergen = random.choice(first_food[1])
    # if every time the selected allergen is present that ingredient is there, then it's a match!
    appearances = [common_ingredient in x[0] for x in food_list if common_allergen in x[1]]
    tries += 1
    if all(appearances):
        tries = 0
        dang_ing.append((common_ingredient, common_allergen))
        food_list = remove_ing_all(food_list, common_ingredient, common_allergen)
        continue

print(sum([len(x[0]) for x in food_list]))
print([x[0] for x in sorted(dang_ing, key=lambda x: x[1])])


