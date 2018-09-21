#Moneyconvert.py

Money = input()

if Money[0:3] in ["USD", "usd"]:
    RMB = eval(Money[3:])*6.78
    print("RMB{:.2f}".format(RMB))
elif Money[0:3] in ["RMB", "rmb"]:
    USD = eval(Money[3:])/6.78
    print("USD{:.2f}".format(USD))
else:
    print("输入格式有误！")