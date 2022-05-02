# By hefei
import time


# 参数：喊话人，频道，喊话内容，喊话次数，间隔时间
def shout(name, word, print_str, num, times):
    for i in range(num):
        countent = str.format("{}--{}：{}；{}次".format(word, name, print_str, i+1))
        print(countent)
        time.sleep(times)  # 时间间隔函数


def auto_add(score):
    score += 10
    return score


if __name__ == '__main__':
    score = 50
    auto_add(score)
    print(score)
    # 位置传参
    shout("张三", "公共频道", "this is a practice", 2, 5)
