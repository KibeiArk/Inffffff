'''(ЕГЭ-2022) Текстовый файл 24-212.txt содержит строку из набора A, B, C, D, O, всего не более чем из 106 символов. 
Определите максимальное количество идущих подряд пар символов вида «согласная + гласная».'''
s =open('8.txt').readline()
s =s.replace('O','A')
s =s.replace('C','B').replace('D','B')
s =s.replace('BA','*')
s = s.replace('B',' ').replace('A',' ')
print(max(len(x) for x in s.split()))
#202