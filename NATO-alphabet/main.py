# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
import pandas as pd

nato = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato.iterrows()}
# print(df_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

input_word = input("Enter a word : ").upper()

new_nato_list = [nato_dict[letter] for letter in input_word]

print(new_nato_list)
