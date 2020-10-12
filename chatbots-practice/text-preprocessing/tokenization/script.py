from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

text = """As a member of the Star Wars generation (or Xennial), I more or less missed the Harry Potter craze when it happened.
Sure, I saw all of the movies in the theatre and witnessed the minor miracle of long lines of children outside bookstores every time a new installment came out.
How could fast paced action scenes on flying vehicles, an orphan with hidden powers and a Dark Lord reviving an evil empire as a nemesis compare to Star W — ok, they were similar, but I liked my Space Opera and didn’t internalize any of the excitement about a magic British boarding school.
"""

words = word_tokenize(text)
sentences = sent_tokenize(text)

print(words)
print()
print(sentences)