# Load dictionary as a list of words
from load_dictionary import load

dict_words = load('3of6game.txt')

def find_palingrams(dict_words):
    dict_words = set(dict_words)  # Convert to set for faster lookup
    palingrams = []
    for word in dict_words:
        rev_word = word[::-1]
        end = len(word)
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in dict_words:
                    palingrams.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-1:] and rev_word[:end-i] in dict_words:
                    palingrams.append((rev_word[:end-i], word))
    return palingrams

palingrams = find_palingrams(dict_words)
sorted_palingrams = sorted(palingrams)

print(f"\nNumber of palingrams:{len(palingrams)}\n")
# for first,second in sorted_palingrams:
#     print(f"{first} {second}")



# palingrams = find_palingrams()
# sorted_palingrams = sorted(palingrams)
# print(f"\nNumber of palingrams:{palingrams}\n")
