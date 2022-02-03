# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random
x = len(names)
random_names = random.randint(0, x - 1)
person_who_will_pay = names[random_names]
print(f"{person_who_will_pay} is going to buy the meal.")

