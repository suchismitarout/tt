import re

phone = "2004-959-559 # This is Phone Number"

num = re.sub(r'#.*$', "", phone)
num1 = re.sub(r'\D', "", phone)
print(num)
print(num1)