with open('referat.txt', 'r', encoding='utf-8') as myfile:
    content = myfile.read()
    length = len(content)
    print(length)
    print(len(content.split()))

with open('referat.txt', 'r', encoding='utf-8') as myfile1:
    for line in myfile1:
        contentexclamation = line.replace('.','!')

with open('referat2.txt', 'w', encoding='utf-8') as myfile2:
    myfile2.write(contentexclamation)