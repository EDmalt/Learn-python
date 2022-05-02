# By hefei
# @File : test.py
s=input('请输入内容：asdf 564456=3')
letter=0
space=0
digit=0
other=0
for i in s:
    if i.isalpha():#判断是否是字母
        letter+=1
    elif i.isspace():#判断是否是空格
        space+=1
    elif i.isdigit():#判断是否是数字
        digit+=1
    else:
        other+=1
print('字母个数为{},空格字数为{},数字字数为{},其他字符为{}'.format(letter,space,digit,other))