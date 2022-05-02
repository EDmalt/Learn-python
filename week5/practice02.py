# By hefei

import  random
#洗牌程序练习
list_num=[i for i in range(0,51)]
list_Cards=["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
list_decks=[]#存放打乱的牌组
random.shuffle(list_num)#打乱牌组
for i in list_num:
    Card=list_num[i]%13#求的牌面
    f_color=list_num[i]//13#求的花色
    # print(Card,"\t",f_color)
    if f_color==0:
        list_decks.append("黑桃{}".format(list_Cards[Card-1]))
    elif f_color==1:
        list_decks.append("红心{}".format(list_Cards[Card - 1]))
    elif f_color==2:
        list_decks.append("方块{}".format(list_Cards[Card - 1]))
    else:
        list_decks.append("梅花{}".format(list_Cards[Card - 1]))
print(list_decks)

# 改版
cards=[card for card in range(52)]
types=["黑桃","红心","方块","梅花"]
values=["A"]+[str(value) for value in range(2,11)]+["J","Q","K"]
random.shuffle(cards)
for i in range(len(cards)):
    type=types[cards[i]//13]#花色
    value=values[cards[i]%13]#牌面
    print("{}:{}-{:6}".format(cards[i],type,value),end="")
    if (i+1)%13==0:
        print()
    else:
        print(end="\t")