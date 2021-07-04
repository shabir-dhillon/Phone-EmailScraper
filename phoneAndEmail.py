import re, pyperclip

# phone number regex
phoneRegex = re.compile(r'''
(
((\d\d\d) | (\(\d\d\d\)))? # area code (optional)
(\s|-) # first separator
\d\d\d # first 3 digita
(-) # separator
\d\d\d\d # last 4 digits
(((ext(\.)?\s | x)  # extension word-part (optional)
(\d{2,5})))? # extension number-part (optional)
)
''', re.VERBOSE)

# email regex
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+ # name part
@ # a symbol
[a-zA-Z0-9_.+]+ # domain name part
''', re.VERBOSE)

#get text off the clipboard so copy your entire document using CRTL C and run the program 
text = pyperclip.paste()
# extract phone and email from text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# copy data to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)

print("Done!")
