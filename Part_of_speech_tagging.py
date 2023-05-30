import spacy

nlp = spacy.load('en_core_web_sm')

doc = nlp(u'The quick brown fox jumped over the lazy dog\'s back')

print(doc.text)
print(doc[4].pos_)
print(doc[4].tag_)

for token in doc:
    print(f"{token.text:{10}} {token.pos_:{10}} {token.tag_:{10}} {spacy.explain(token.tag_):{10}}")
    #print(token.text, token.pos_, token.tag_, spacy.explain(token.tag_))

doc_2 = nlp(u"I read books on NLP.")
word = doc_2[1]
print(word.text)

token = word
print(f"{token.text:{10}} {token.pos_:{10}} {token.tag_:{10}} {spacy.explain(token.tag_):{10}}")

doc_3 = nlp(u'I read a book on NLP.')
word = doc_3[1]
token = word
print(f"{token.text:{10}} {token.pos_:{10}} {token.tag_:{10}} {spacy.explain(token.tag_):{10}}")

#get parts of speech count
doc = nlp(u'The quick brown fox jumped over the lazy dog\'s back')
POS_counts = doc.count_by(spacy.attrs.POS)
print(POS_counts)

print(doc.vocab[84].text)
# for token in doc:
#     print(token.pos)

for k,v in sorted(POS_counts.items()):
    print(f"{k}. {doc.vocab[k].text:{5}} {v:{2}}")

TAG_counts = doc.count_by(spacy.attrs.TAG)
print(TAG_counts)
for k,v in sorted(TAG_counts.items()):
    print(f"{k}. {doc.vocab[k].text:{5}} {v:{2}}")

print(len(doc.vocab))

DEP_counts = doc.count_by(spacy.attrs.DEP)
print(DEP_counts)
for k,v in sorted(DEP_counts.items()):
    print(f"{k}. {doc.vocab[k].text:{5}} {v:{2}}")