# Defining a dictionary with fruit names with their calorie counts
fruit_calories = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80,
}

# Prompt the user for input
# lowercase for case-insensitivity
user_input = input("Enter a fruit: ").lower()

# Check if the user's input is in the dictionary
if user_input in fruit_calories:
    calories = fruit_calories[user_input]
    print(f"Calories: {calories}")

