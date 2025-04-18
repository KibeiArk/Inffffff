'''(Е. Джобс) Назовём маской числа последовательность цифр, в которой также могут встречаться
следующие символы:
— символ «?» означает ровно одну произвольную цифру;
— символ «*» означает любую последовательность цифр произвольной длины; в том числе «*»
может задавать и пустую последовательность.
Например, маске 123*4?5 соответствуют числа 123405 и 12300425.
Найдите все числа, меньшие 10^12, соответствующие маске 123?4*5679 и делящиеся без остатка на
4013. В качестве ответа приведите все найденные числа в порядке возрастания, справа от каждого
числа выведите результат его деления на 4013.'''
from itertools import*
com=[]
ans=[]
for l in range(0,4):
    for i in product('0123456789',repeat=l):
        com.append(''.join(i))
for a1 in '0123456789':
    for a2 in com:
        x = int(f'123{a1}4{a2}5679')
        if x >10**12: break
        if x%4013==0:
            ans.append([x,x//4013])
ans.sort()
for i in ans:
    print(*i)
'''
123240365679 30710283
123441015679 30760283
123641665679 30810283
123842315679 30860283
'''