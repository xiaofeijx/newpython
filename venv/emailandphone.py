import pyperclip, re


# 电话号码匹配
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?    #区号  123  或者 (123)
    (\s|-|\.)             #空格，连线，点号
    (\d{3})
    (\s|-|\.)             #空格，连线，点号
    (\d{4})
    (\s*(ext|x|ext\.)\s*(\d{2,5}))?
)
''', re.VERBOSE)


# 电子邮件匹配
emailRegex = re.compile(r'''(
    [a-zA-Z0-9.%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
)''', re.VERBOSE)

# 在粘贴板里查找
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phonenum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phonenum += ' X' + groups[8]
    matches.append(phonenum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print("Copied to clipboard:")
    print('\n'.join(matches))
else:
    print('nothing')