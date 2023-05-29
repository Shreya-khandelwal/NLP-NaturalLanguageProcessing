import spacy

nlp = spacy.load('en_core_web_sm')
doc_1 = nlp(u'I am a runner running in a race because i love to run since i ran today')

for token in doc_1:
    print(token.text, '\t', token.pos, '\t', token.lemma, '\t', token.lemma_)
print('\n')

#function for formatting
def show_lemmas(text):
    for token in text:
        print(f'{token.text:{12}} {token.pos:{6}} {token.lemma:<{22}} {token.lemma_}')

doc_2 = nlp(u"I saw ten mice today!")
show_lemmas(doc_2)
