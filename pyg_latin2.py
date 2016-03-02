# Jeff, I made changes to this code based on your feedback this morning. 

your_word = input('Tell me a word: ')
first_letter = your_word[0]

if first_letter in "aeiouAEIOU":
    new_word = your_word + "say"
else:
    new_word = your_word[1:] + first_letter + "ay"

print(new_word.lower())
