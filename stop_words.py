import spacy

nlp = spacy.load('en_core_web_sm')

print(nlp.Defaults.stop_words)
print(len(nlp.Defaults.stop_words))
print(nlp.vocab['is'].is_stop)
print(nlp.vocab['mystery'].is_stop)
nlp.Defaults.stop_words.add('btw')

#add any word in default stop words
nlp.Defaults.stop_words.add('btw')
print(nlp.vocab['btw'].is_stop)
print(len(nlp.Defaults.stop_words))

#remove any word from default stop words
nlp.Defaults.stop_words.remove('beyond')
print(nlp.vocab['beyond'].is_stop)
print(len(nlp.Defaults.stop_words))
