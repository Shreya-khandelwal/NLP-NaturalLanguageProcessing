import re

text  = "The phone number of the agent is 408-555-1234. Call soon!"
print("408-555-1234" in text)

pattern = "phone"
print(re.search(pattern,text))
my_match = re.search(pattern,text)
print(f"Span of the search is {my_match.span()}")
print(f"Start of the span is {my_match.start()}")
print(f"End of the span is {my_match.end()}")

new_text = "My phone is a new phone"
match = re.search(pattern,new_text) #gives only the first instance
print(match)
all_matches = re.findall(pattern,new_text) #gives all the instance
print(all_matches) 
print(f"The pattern is coming {len(all_matches)} times in the text")

#returning iteration of all the matches
for match in re.finditer(pattern,new_text):
    print(f"Match found at {match.span()}")

pattern = "\d{3}-\d{3}-\d{4}"
phone_number = re.search(pattern,text)
print(phone_number.group()) #see the actual match object
print(re.search(pattern,text))

