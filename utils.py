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
    "COFFEE": "☕️",
    "COOKIE": "🍪",
    "GAUFRE": "🧇",
    "ICE CREAM": "🍦",
    "CREPE": "🥞"
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

district_list = [2,3,4,6,9,10,11,12,18,19,20,92120]
district_list_Tess = [1,2,3,4,5,6,9,11,12]
lieu_mapping = {"Partout": "Partout", "Proche de la Villette": "chez_jaz", "Montrouge": "taff_jaz"}
lieu_mapping2 = {"Partout": "Partout", "Patisserie": "bakery", "Proche de la Villette": "chez_jaz", "Montrouge": "taff_jaz"}
lieu_mapping3 = {"Partout": "Partout", "Dans le quartier": "proche"}


def convert_words_to_emojis(input_string):
    if type(input_string) == str:
        words = ast.literal_eval(input_string)
    else:
        words = input_string

    emojis = [word_to_emoji_mapping.get(word, word) for word in words]

    return emojis
