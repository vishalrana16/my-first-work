import re
r=re.match('\w+@\w+.\w+','abc@gmail.com')
print(r.group())
