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
