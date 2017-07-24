recipes = {"hamburger": ["cheese", "buns", "ketchup", 'lettuce', "mayonnaise", "mustard", "pickles", "tomatoes"],
    "pizza": ["mozzarella", "tomato sauce", "pepperoni", "Italian seasoning", "pizza dough"]
}

myIngredients = []

while True:
    print "What do you have? (type 'done' when Done.)"
    have_these_items = raw_input("> ")
    if len(have_these_items) < 1:
        print "You have not entered anything."
    elif have_these_items == "done":
        break
    else:
        myIngredients.append(have_these_items)


while True:
    print "What are you making?"
    making_this_item = raw_input("> ")
    if len(making_this_item) < 1:
        print "You have not entered anything."
    elif making_this_item not in recipes.keys():
        print "Sorry, this item is not registered."
    else:
        break

ingredients_i_need = recipes[making_this_item]

for m in myIngredients:
    if m in ingredients_i_need:
        ingredients_i_need.remove(m)

print "You need: "
for i in ingredients_i_need:
    print i
