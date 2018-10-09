#CalBMI.py
height, weight = eval(input("请输入身高（米）和体重（公斤）【逗号隔开】："))
bmi = weight / pow(height, 2)
print("BMI 数值：{:.2f}".format(bmi))
who, nat = "", ""
if bmi < 18.5:
    who, nat = "偏瘦", "偏瘦"
elif 18.5 <= bmi < 24:
    who, nat = "正常", "正常"
print("BMI指标为：国际{0},国内{1}".format(who, nat))