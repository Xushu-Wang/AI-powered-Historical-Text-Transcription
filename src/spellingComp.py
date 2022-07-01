import pkg_resources
from symspellpy import SymSpell

sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
dictionary_path = pkg_resources.resource_filename(
    "symspellpy", "frequency_dictionary_en_82_765.txt"
)
bigram_path = pkg_resources.resource_filename(
    "symspellpy", "frequency_bigramdictionary_en_243_342.txt"
)
# term_index is the column of the term and count_index is the
# column of the term frequency
sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)
sym_spell.load_bigram_dictionary(bigram_path, term_index=0, count_index=2)

# lookup suggestions for multi-word input strings (supports compound
# splitting & merging)

teststr = "Can yu readthis messa ge despite thehorible sppelingmsitakes"


# max edit distance per lookup (per single word, not per whole input string)
suggestions = sym_spell.lookup_compound(teststr, max_edit_distance=2)

test = ""
for suggestion in suggestions:
    test += suggestion.term
    

def side_by_side(a, b, size=40, space=4):
    while a or b:
        print(a[:size].ljust(size) + " " * space + b[:size])
        a = a[size:]
        b = b[size:]


print(side_by_side(teststr, test))
