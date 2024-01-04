import ast

import pandas as pd


def convert_words_to_emojis(input_string):
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

    words = ast.literal_eval(input_string)

    emojis = [word_to_emoji_mapping.get(word, word) for word in words]

    return emojis
