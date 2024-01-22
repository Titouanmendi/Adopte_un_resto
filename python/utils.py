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
    "LEBANESE": "🇱🇧",
    "BISTROT": "🍽️",
    "SANDWICH": "🥪",
    "SALADE": "🥗",
    "ASIATIQUE": "🍜",
    "POKE": "🍱",
    "DONUT": "🍩",
    "COFFEE": "☕️"
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

district_list = [2,3,4,6,9,10,11,18,19,20,92120]
lieu_mapping = {"Partout": "Partout", "Proche de chez Jaz": "chez_jaz", "Proche du taff de Jaz": "taff_jaz"}
lieu_mapping2 = {"Partout": "Partout", "Patisserie": "bakery", "Proche de chez Jaz": "chez_jaz", "Proche du taff de Jaz": "taff_jaz"}



def convert_words_to_emojis(input_string):
    if type(input_string) == str:
        words = ast.literal_eval(input_string)
    else:
        words = input_string

    emojis = [word_to_emoji_mapping.get(word, word) for word in words]

    return emojis
