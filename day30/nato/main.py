import pandas

data = pandas.read_csv("day30/nato/nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

# ----------------------------------------------------

## as code
# while True:
#     try:
#         word = input("Enter a word: ").upper()
#         output_list = [phonetic_dict[letter] for letter in word]
#         print(output_list)
#         break
#     except KeyError as e:
#         print("Sorry, only letter in alphabet")

# ----------------------------------------------------
## as function

def gen_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError as e:
        print("Sorry, only letter in alphabet")
        gen_phonetic()
    else:
        print(output_list)
        
gen_phonetic()

