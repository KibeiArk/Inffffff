s = open('24_17756.txt').readline()
while '**' in s: s = s.replace('**','* *')
while '++' in s: s = s.replace('++','+ +')
while '+*' in s: s = s.replace('+*','+ *')
while '*+' in s: s = s.replace('*+','* +')
print(max(len(x) for x in s.split()))
#317