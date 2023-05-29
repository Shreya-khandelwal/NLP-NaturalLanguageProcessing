import spacy
from spacy.matcher import Matcher

nlp = spacy.load('en_core_web_sm')

matcher = Matcher(nlp.vocab)

#solarPower 
pattern_1 = [{'LOWER':'solarpower'}]
#solar-power 
pattern_2 = [{'LOWER':'solar'},{'IS_PUNCT':True},{'LOWER':'power'}]
# Solar power
pattern_3 = [{'LOWER':'solarpower'}, {'LOWER':'power'}]

patterns = [pattern_1, pattern_2, pattern_3]

#add a pattern in a matcher
matcher.add('SolarPower',patterns)
doc = nlp(u"The Solar Power in the industry continues to grow a solarpower increases. Solar-power is amazing.")

found_matches = matcher(doc)

print(found_matches)

#remove a pattern from a matcher
matcher.remove('SolarPower')

#solarpower
pattern_1 = [{'LOWER':'solarpower'}]

#Solar--power, solar..power (any punctuatuin for any number of times)
pattern_2 = [{'LOWER':'solar'},{'IS_PUNCT':True, 'OP':'*'},{'LOWER':'power'}]

patterns = [pattern_1, pattern_2]
matcher.add('SolarPower',patterns)
doc_2 = nlp(u"The Solar--Power is a solarpower yay!")

found_matches = matcher(doc_2)

print(found_matches)

