import re
phoneNumber = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumber.search('My phone number is 415-555-4242.')
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))  #不分组电话号码
print(mo.group())  #不分组电话号码

print(mo.groups()) #分组电话号码

areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)


#如果有括号，需要加斜杠

phoneNumber = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
mo = phoneNumber.search('My phone number is (415)-555-4242.')
print(mo.group(1))


#管道匹配多个分组  "|"
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey') #找到第一个
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman ') #找到第一个
print(mo2.group())

batReg = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batReg.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))

# "?"匹配0次或1次，"+"匹配1次和以上，"*"匹配0次或多次
batReg = re.compile(r'Bat(wo)?man')
mo = batReg.search('the adventures of Batman')
print(mo.group())
print(mo.group(1)) #没有


mo2 = batReg.search('the adventures of Batwoman')
print(mo2.group())
print(mo2.group(1)) #没有

#花括号匹配特定次数

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())


# python默认贪心，匹配更长结果，非贪心模型在花括号后面加上"?"
greedHaRegex = re.compile(r'(Ha){3,5}|(ha)*')
mo1 = greedHaRegex.search('HaHaHaHaHaHa')
print(mo1.group())


greedHaRegex = re.compile(r'(Ha){3,5}?')
mo1 = greedHaRegex.search('HaHaHaHaHaHa')
print(mo1.group())

# findall方法：没有分组返回一个匹配字符串列表，有分组返回一个元组列表
phoneNumber = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumber.findall('My phone number is 415-555-4242 and cell number is 444-555-6666.')
print(mo)

phoneNumber = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = phoneNumber.findall('My phone number is 415-555-4242 and cell number is 444-555-6666.')
print(mo)

# 字符分类  \d \D \w \W \s \S
xmasRegex = re.compile(r'\d+\s\w+')  #\w+  字母直到空格
mo = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(mo)

# 通配符 "."通配单位字符,换行符除外
atReg = re.compile(r'.at')
mo = atReg.findall('The cat in the hat sat on the flat mat.')
print(mo)

# (.*)匹配多个字符，贪心模式
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group()) #所有匹配
print(mo.group(1))
print(mo.group(2))
print(mo.groups()) #所有分组

# (.*?)匹配多个字符,非贪心模式
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())


greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())


# re.I  不区分大小写
robocop = re.compile(r'robocop', re.I)
mo = robocop.findall('Robocop roBocop is part man, part machine, all cop.')
print(mo)

namesRegex = re.compile(r'Agent \w+')

agentNamesRegex = re.compile(r'(Agent \w)\w*') # \w 表示单个字母 \w*表示0个或以上的字母
x = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(x)

