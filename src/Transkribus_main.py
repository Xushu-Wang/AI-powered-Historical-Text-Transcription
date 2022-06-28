from asrtoolkit import cer, wer
from thefuzz import fuzz
from striprtf.striprtf import rtf_to_text
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
result = ("1846 3 to seek it with real earnestness, and before the meeting closed I attached my-self to the Baptist church. Before this I never lasted frue and lasting happiness. My whole thoughts were centred upon this one subject Religion. This happi-nes lasted for several weeks but my Mind began to be token up by things of this world and of late I enjoy very little religion. I arrived at home on the 30th of November- since which I have enjoyed myself among my friends and cousins. MarchSrs Father arrived from Mobile consequently a good deal of company. I have felt tolerably melancholy all day I do not know any reason for it, except my disposition. Why can I not be abrrays cheerful and happy like those arcrind me? It as merely because I will not be happy. and because I am so quick tem pered- have so onany bad qualities, and because I neg" )

# max edit distance per lookup (per single word, not per whole input string)
suggestions = sym_spell.lookup_compound(result, max_edit_distance=2, transfer_casing=True)

result_after = ""
# display suggestion term, edit distance, and term frequency
for suggestion in suggestions:
    result_after += suggestion.term


file = open("/Users/andywang/Desktop/Data+/Martha Foster Crawford diary, 1846-1850 and 1867/wtddy11001/wtddy11001-9/wtddy11001-9.rtf")
content = file.read()
ground_truth = rtf_to_text(content)

print(ground_truth)
print(result_after)

print("CER: ", cer(result_after, ground_truth))
print("WER: ", wer(result_after, ground_truth))
print("levenshtein distance: ", fuzz.ratio(result_after, ground_truth))