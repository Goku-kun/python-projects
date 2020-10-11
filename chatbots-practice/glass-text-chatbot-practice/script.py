import re
from looking_glass import looking_glass_full_text
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from collections import Counter

# what the below written regex does is it substitues non word characters (character that aren't A-Za-z0-9_) with empty spaces in the string
cleaned = re.sub(r"\W+", ' ', looking_glass_full_text).lower()
#print(cleaned)
tokens = word_tokenize(cleaned)
# print(tokens)

# Single tokens are being extracted and top 10 most common tokens are being displayed
looking_glass_tokens_frequency = Counter(tokens)
print()
print(looking_glass_tokens_frequency.most_common(10))

# using the ngrams function to extract the bigram tokens since the argument in ngrams function is 2
looking_glass_bigrams = ngrams(tokens, 2)
looking_glass_bigrams_frequency = Counter(looking_glass_bigrams)
print(looking_glass_bigrams_frequency.most_common(10))

# using the ngrams function to extract trigram tokens since the argument in ngrams function is 3
looking_glass_trigrams = ngrams(tokens, 3)
looking_glass_trigrams_frequency = Counter(looking_glass_trigrams)
print(looking_glass_trigrams_frequency.most_common(10))