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
f = open(r"/Users/andywang/Desktop/martha7.ocr.txt")
result = f.read()

# max edit distance per lookup (per single word, not per whole input string)
suggestions = sym_spell.lookup_compound(result, max_edit_distance=2, transfer_casing=True)

result_after = ""
# display suggestion term, edit distance, and term frequency
for suggestion in suggestions:
    result_after += suggestion.term


file = open("/Users/andywang/Desktop/martha7.gt.txt")
ground_truth = file.read()

print(ground_truth)
print(result_after)


print("CER: ", cer(result, ground_truth))
print("WER: ", wer(result, ground_truth))
print("levenshtein distance: ", fuzz.ratio(result, ground_truth))


print("CER: ", cer(result_after, ground_truth))
print("WER: ", wer(result_after, ground_truth))
print("levenshtein distance: ", fuzz.ratio(result_after, ground_truth))

