### Text Analytics
# 1. Extract Sample document and apply following document preprocessing methods:
# Tokenization, POS Tagging, stop words removal, Stemming and Lemmatization.
# 2.Create representation of document by calculating Term Frequency and Inverse Document
# Frequency. 

import nltk
from nltk.corpus import stopwords
fromt nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
fromt nltk.tokenize import word_tokenize, sent_tokenize
from sklearn.feature_extraction import TfidVectorizer

text = ""
tok_text = sent_tokenize(text)
print(tok_text)
tok_word = word_tokenize(text)
print(tok_word)

ex_sent = """"""
stop_word = set(stopwords.words('english'))
word_token = word_tokenize(ex_sent)

filtered_text=[]
for w in word_token:
    if w not in stop_word:
        flitered_sentence.append(w)
print(filtered_text)
print(word_token)

ps = PorterStemmer()
word = ["run", "runner", "running", "ran", "runs"]
for w in word:
    print(w,":",ps.stem(w))


lemma = WordNetLemmatizer()
print("rocks :", lemma.lemmatize("rocks"))
print("corpora :", lemma.lemmatize("corpora"))

sent = "Everything is about money"
token = nltk.word_tokenize(sent)
pos_tagging = nltk.pos_tag(token)
print(pos_tagging)

document = ["","",""]
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)
print("TF-IDF Features")
print(vectorizer.get_feature_names_out())
print("TF-IDF Matrix")
print(tfid_matrix.toarray())
