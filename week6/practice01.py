# By hefei
# 循环大于26个大写字母的ASKII码
i = 0
x = 65
while i < 26:
    if i % 4 == 0:
        print("")
    print("{}的ASCII码是{}".format(chr(x), x), end="\t")
    x += 1
    i += 1
print("\n===========================================")
# 改进
char = "A"
for i in range(0, 26):
    print("{}的ASCII码是{}".format(char, ord(char)), end="\t")
    char = chr(ord(char) + 1)  # 来回转换
    if (i + 1) % 5 == 0:
        print("")
print("\n===========================================")
char01 = input("请输入查询单词:")
if "A" <= char <= "Z":            #ord(char01) > 90 or ord(char01) < 65:
    print("输入字符不符合要求！")
else:
    print("{}的小写是{}".format(char01, chr(ord(char01) + 32)))
