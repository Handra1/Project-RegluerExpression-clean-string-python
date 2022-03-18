import re
pattern = re.compile('\$\d*\.\d{2}')
result = pattern.match('$17.89')
print(bool(result))
