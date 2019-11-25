import re
p = "nutanix sdfdgh Nutanix ghshs nutanix"
r = re.findall("[nN]utanix", p)
print(r.count("nutanix"))