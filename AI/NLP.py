import nltk
import string
corpus="Any text can be entered"


lowerc=corpus.lower()
print(lowerc)
puncrem="".join(c for c in lowerc if c not in string.punctuation)
print(puncrem)
tokend=nltk.word_tokenize(puncrem)
print(tokend)


from nltk.corpus import stopwords
stp_wrds=set(stopwords.words("english"))
filter_tokend=[i for i in tokend if i not in stp_wrds]
print(filter_tokend)


from nltk.stem import PorterStemmer
stemmer=PorterStemmer()
stemmed_tokens=[stemmer.stem(token) for token in filter_tokend]
print(stemmed_tokens)


from nltk.tag import pos_tag
pos_tag(stemmed_tokens)
