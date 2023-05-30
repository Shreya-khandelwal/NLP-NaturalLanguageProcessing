import spacy
from spacy.language import Language
from spacy.pipeline import SentenceSegmenter

nlp = spacy.load('en_core_web_sm')

doc = nlp(u'This is the first setence. This is the another sentence. This is the last sentence.')

for sent in doc.sents:
    print(sent)

print(list(doc.sents)[0])

doc_2 = nlp('"Management is doing the right things; Leadership is doing the right things." -Peter Drucker')
print(doc_2)
for sent in doc_2.sents:
    print(sent)

#add a sementation rule
@Language.component("set_custom_boundaries")
def set_custom_boundaries(doc):
    for token in doc[:-1]:
        if token.text == ';':
            doc[token.i+1].is_sent_start = True
    return doc

#adding rule before parsing
nlp.add_pipe("set_custom_boundaries", before="parser")
print(nlp.pipe_names)

doc_4 = nlp('"Management is doing the right things; Leadership is doing the right things." -Peter Drucker')

print("\nsegmentation rule added\n")
for sent in doc_4.sents:
    print(sent)
print('\n')
#change segmentation rule
mystring = nlp(u"This is a sentence. This is another.\n\nThis is a \nthird sentence.")
print(mystring)

doc = nlp(mystring)
for sent in doc.sents:
    print(sent)

print('\n')
def split_on_newlines(doc):
    start = 0
    seen_newline = False

    for word in doc:
        if seen_newline:
            yield doc[start:word.i]
            start = word.i
            seen_newline = False
        elif word.text.startswith('\n'):
            seen_newline = True
    
    yield doc[start:]

sbd =  SentenceSegmenter(nlp.vocab, strategy=split_on_newlines)
nlp.add_pipe(sbd)
doc = nlp(mystring)

for sentence in doc.sents:
    print(sentence)

