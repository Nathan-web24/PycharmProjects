# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = int(weight) / (float(height)*float(height))

print(weight + "/" + "(" + height + "*" + height + ")" + "=" + str(BMI))
BMI = round(BMI)

print(BMI)








