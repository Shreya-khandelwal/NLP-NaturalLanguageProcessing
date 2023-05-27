import re

text  = "The phone number of the agent is 888-555-1234. Call soon!"
pattern = "(\d{3})-(\d{3})-(\d{4})" #individual groups seperated by()
phone_number = re.search(pattern,text)
print(f"First group is {phone_number.group(1)}")
print(f"Second group is {phone_number.group(2)}")
print(f"Third group is {phone_number.group(3)}")

#or operatore
result = re.search(r"man|women","This man was here")
print(result.span())

#wildcard
result = re.findall(r".at","The cat in the hat sat splat")
print(result)

result = re.findall(r"..at","The cat in the at sat splat")
print(result)

result = re.findall(r"^\d", 'this ends with 2')
print (len(result))

result = re.findall(r"^\d", '1 ends with 2')
print (result)

phrase = "there are 3numbers 34 inside 5 this sentence"
print(re.findall(r"[^\d]", phrase)) #exclude digits