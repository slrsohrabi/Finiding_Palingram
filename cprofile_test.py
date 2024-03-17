import cProfile
import palingrams
from load_dictionary import load
dict_words = load('3of6game.txt')
cProfile.run(f'palingrams.find_palingrams({dict_words})')