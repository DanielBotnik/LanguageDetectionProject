import re

with open('site.html',encoding='utf8') as file:
    content = file.readlines()

content = [x.strip() for x in content if '</td><td class="alt3">' in x]
content = [x for x in content if re.match('<tr class="alt1"><td>\t\d+\t<\/td><td>\t[a-zA-Z]',x)]

words = [content[i].split('\t')[7] for i in range(len(content))]

with open('hebrew_words.txt', 'w',encoding='utf8') as f:
    for item in words:
        f.write("%s\n" % item)