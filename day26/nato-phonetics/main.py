import pandas

# {"A": "Alfa", "B": "Bravo"}


df_phonetics = pandas.read_csv("day26/nato-phonetics/nato_phonetic_alphabet.csv")
# df_phonetics = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(df_phonetics)

## for loop
# for idx,row in df_phonetics.iterrows():
#     dict_phonetics = df_phonetics.set_index('letter')['code'].to_dict()
    # print(f"{row.letter}:{row.code}")

## dict comprehension
dict_phonetics = {row.letter:row.code for idx,row in df_phonetics.iterrows()}    

print(dict_phonetics)

print("-------------------------------------")

input_name = input("Enter a word:").upper()
# print(type(input_name))

output_list =[dict_phonetics[letter] for letter in input_name]
print(output_list)



# ---------------------------------------------------- 

### way#2 longer

# input_name = input("Enter a word:")
# # list_input_name = input_name.split()  # put in list separate by separator
# # list_input_name = [a.split() for a in input_name]  # list of list
# characters = list(input_name.upper())


# # print(character)
# # for n in character

# # print(dict_phonetics["A"])
# list_result = [dict_phonetics[character] for character in characters if character in dict_phonetics]
# print(list_result)