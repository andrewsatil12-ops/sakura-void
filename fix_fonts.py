import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'font-weight:\s*200', 'font-weight: 400', content)
content = re.sub(r'font-weight:\s*300', 'font-weight: 400', content)
content = re.sub(r'font-weight:\s*500', 'font-weight: 700', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Font weights updated!")
