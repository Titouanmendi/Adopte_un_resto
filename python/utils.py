import ast

word_to_emoji_mapping = {
    "VEGE": ":pousse:",
    "VEGAN": ":pousse::interdit::verre_de_lait::cuisse_de_volaille:",
    "HALAL": ":interdit::cochon2:",
    "LACTOSE_FREE": ":interdit::verre_de_lait:",
    "GLUTEN_FREE": ":interdit::pain:",
    "SUSHI": ":sushi:",
    "PIZZA": ":pizza:",
    "BURGER": ":hamburger:",
}

word_to_better_word = {
    "VEGE": "Vegetarien",
    "VEGAN": "Vegan",
    "HALAL": "Halal",
    "LACTOSE_FREE": "Sans lactose",
    "GLUTEN_FREE": " Sans gluten",
    "SUSHI": "Sushi",
    "PIZZA": "Pizza",
    "BURGER": "Burger",
}


def convert_words_to_emojis(input_string):
    words = ast.literal_eval(input_string)

    emojis = [word_to_emoji_mapping.get(word, word) for word in words]

    return emojis
