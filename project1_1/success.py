from sklearn.feature_extraction.text import TfidfVectorizer
import docx

# doc = docx.Document('trbyme.docx')
# print(doc)
with open('trbyme.txt', 'r', encoding='utf-8') as made_file:
    doc1 = [made_file.read()]
#print(doc1)
with open('trbygoogle.txt', 'r', encoding='utf-8') as made_file:
    doc2 = [made_file.read()]
#documents = [open(f) for f in ["trbygoogle.txt", "trbyme.txt"] ]
#print(documents)
tfidf = TfidfVectorizer().fit_transform(doc1, doc2)
print(tfidf)
# # no need to normalize, since Vectorizer will return normalized tf-idf
pairwise_similarity = tfidf * tfidf.T
print(pairwise_similarity)

# if you have a string and you want to create a raw text there are two main methods I know of:
# raw_text = [str_text]
# and
# str_text = "%r"%str_text
# raw_text = str_text[1:-1].