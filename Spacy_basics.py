#spacy can grab a lot of information from string
import spacy

nlp = spacy.load('en_core_web_sm') #model loading
#parse string into tokens
doc = nlp(u'Tesla is . looking at buying U.S. startup for $6 million') #u is for unicode
for token in doc:
    print(token.text,token.pos, token.pos_, token.dep_) 
    
#pipeline object
print(nlp.pipeline)
print(nlp.pipe_names)

#Tokenization
doc_2 = nlp(u"Tesla isn't     looking into startuos anymore.")
for token in doc_2:
    print(token.text,token.pos_,token.dep_)

#accessing tokens through index
print(f"part of speech is {doc_2[0].pos_}") #pos is part of speech
print(f"syntactic dependency is {doc_2[0].dep_}") #dep is syntactic dependency

#print particular setence
doc_3 = nlp(u"This is the first sentence. This is the seocnd sentence. This is the third sentence")
for sentence in doc_3.sents:
    print(sentence)

print(doc_3[0])
print(doc_3[4].is_sent_start) #is this start of the sentence