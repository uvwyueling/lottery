import random

# 限制用户只能输入100以下的整数
total = int(input("请输入总题数"))


remaining = list(range(1,total+1))  # 还没被抽到的数字
drawn = []                          # 已经被抽到的数字

# 随机抽取
def draw():
    pick_up = random.choice(remaining)
    drawn.append(pick_up)
    remaining.remove(pick_up)

    return remaining, drawn

# 一键还原
def reset():
    global total, remaining, drawn
    total = None
    remaining = []
    drawn = []
    return total, remaining, drawn


