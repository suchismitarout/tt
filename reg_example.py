import re

with open("C:/Users/Ranjitha/PycharmProject/tt/data", "r") as fp:
    for line in fp:
        ip = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$").findall(line)
    print(ip)