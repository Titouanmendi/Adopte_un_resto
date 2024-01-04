import ast

word_to_emoji_mapping = {
    "VEGE": "🌱",
    "VEGAN": "🌱🚫🥛🍗",
    "HALLAL": "🚫🐷",
    "LACTOSE_FREE": "🚫🥛",
    "GLUTEN_FREE": "🚫🍞",
    "SUSHI": "🍣",
    "PIZZA": "🍕",
    "BURGER": "🍔",
    "BISTROT": "🍽️",
    "SANDWICH": "🥪",
    "SALADE": "🥗",
}

word_to_better_word = {
    "VEGE": "Vegetarien",
    "VEGAN": "Vegan",
    "HALLAL": "Halal",
    "LACTOSE_FREE": "Sans lactose",
    "GLUTEN_FREE": " Sans gluten",
    "SUSHI": "Sushi",
    "PIZZA": "Pizza",
    "BURGER": "Burger",
    "BISTROT": "Bistrot",
    "SANDWICH": "Sandwich",
    "SALADE": "Salade",
}


def convert_words_to_emojis(input_string):
    if type(input_string) == str:
        words = ast.literal_eval(input_string)
    else:
        words = input_string

    emojis = [word_to_emoji_mapping.get(word, word) for word in words]

    return emojis
