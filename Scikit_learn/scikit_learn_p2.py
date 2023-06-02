import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC

df = pd.read_csv("C:\\Users\\002CL0744\\Documents\\NLP-NaturalLanguageProcessing\\Scikit_learn\\smsspamcollection.tsv", sep='\t')

X = df[['length', 'punct']]
#y is label data
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=42)
print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)

#logistic regression
lr_model = LogisticRegression(solver='lbfgs') #building object
lr_model.fit(X_train,y_train)  #for the model to the tarining data 

#testing accuracy of the model
#create prediction set
predictions = lr_model.predict(X_test) 
print(predictions)
print(y_test)

#print confusion matrix
print(metrics.confusion_matrix(y_test,predictions))

#adding labels to the confusion matrix
df = pd.DataFrame(metrics.confusion_matrix(y_test, predictions), index=['ham','spam'], columns=['ham', 'spam'])
print(df)

print(metrics.classification_report(y_test, predictions))

print(metrics.accuracy_score(y_test,predictions))

#naive bayes algo
nb_model = MultinomialNB() #building object
nb_model.fit(X_train,y_train)
predictions = nb_model.predict(X_test)
print(metrics.confusion_matrix(y_test, predictions))
df = pd.DataFrame(metrics.confusion_matrix(y_test, predictions), index=['ham','spam'], columns=['ham', 'spam'])
print(df)
print(metrics.classification_report(y_test, predictions))

print(metrics.accuracy_score(y_test,predictions))

#vector machine model
svc_model = SVC(gamma='auto')
svc_model.fit(X_train,y_train)
predictions = svc_model.predict(X_test)
print(metrics.confusion_matrix(y_test, predictions))
df = pd.DataFrame(metrics.confusion_matrix(y_test,predictions), index=['ham','spam'], columns=['ham','spam'])
print(df)
print(metrics.classification_report(y_test,predictions))
print(metrics.accuracy_score(y_test,predictions))