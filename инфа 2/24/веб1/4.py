'''Текстовый файл 24-157.txt состоит не более чем из 
10^6 символов и содержит только заглавные буквы латинского 
алфавита (A..Z). 
Определите максимальное количество идущих подряд 
символов, среди которых нет сочетания символов QW.'''
s = open('4.txt').readline()
s =s.replace('QW','Q W')
print(max(len(x) for x in s.split()))
#5267