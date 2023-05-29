import nltk #natural language toolkit
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer

p_stemmer = PorterStemmer()
words = ['run', 'runner', 'ran', 'runs', 'easily', 'fairly', 'fairness']
print("Porter stemmer")
for word in words:
    print(word + '---->' + p_stemmer.stem(word))
print("\n")

s_stemmer = SnowballStemmer(language='english')
print("Snowball stemmer")
for word in words:
    print(word + '---->' + s_stemmer.stem(word))
print("\n")

words = ['generous', 'generation', 'generously', 'generate']
for word in words:
    print(word + '---->' + s_stemmer.stem(word))
print("\n")

