import spacy
from spacy import displacy

nlp = spacy.load('en_core_web_sm')

mystring = '"We\'re moving to L.A.!"'
print(mystring)

doc = nlp(mystring)
print("Tokenization for first string:")
for token in doc:
    print(token.text)
print("\n")

doc_2 = nlp(u"We're here to help! Send snail-mail, email support@oursite.com or visit us at http://www.oursite.com!")
print("Tokenization for second string:")
for token in doc_2:
    print(token.text)
print("\n")

doc_3 = nlp(u"A 5km NYC cab ride costs $10.30")
print("Tokenization for third string:")
for token in doc_3:
    print(token.text)
print("\n")

doc_4 = nlp(u"Let's visit St. Louis in the U.S. next year.")
print("Tokenization for fourth string:")
for token in doc_4:
    print(token.text)
print("\n")

print(f"Number of tokens in the fourth string {len(doc_4)}")

doc_5 = nlp(u'Apple to build a Hong kong factory for $6 million')
print("Tokenization for fifth string:")
for token in doc_5:
    print(token.text,end=' | ')

print("\n") 

for entity in doc_5.ents:
    print(entity)
    print(entity.label_)
    print(str(spacy.explain(entity.label_)))
    print("\n")

#noun chunks
doc_6 = nlp(u'Autonomous cars shift insurance liability towards manufacturers.')
for chunk in doc_6.noun_chunks:
    print(chunk)

doc_7 = nlp(u'Apple is going to build a U.K. factory for $6 million.')
print(displacy.render(doc_7, style='dep'))

doc_8 = nlp(u"Over the last quarter Apple sold nearly 20 thousand iPods fir a profit of $6 million")
print(displacy.render(doc_8,style='ent'))

doc_9 = nlp(u"This is a sentence.")
displacy.serve(doc_9,style='dep')

