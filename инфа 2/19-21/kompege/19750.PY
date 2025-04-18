'''Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит куча камней. Игроки ходят по очереди, первый ход делает Петя. 
За один ход игрок может выполнить любое из следующих действий:
1) убрать из кучи пять камней;
2) если количество камней в куче чётно, уменьшить его в два раза;
3) если количество камней в куче кратно трём, уменьшить его в три раза;
4) если количество камней в куче нечётно и не кратно трём, добавить один камень.
Например, если в куче 12 камней, то за один ход можно получить 7, 6 или 4 камня, а если в куче 11 камней, то за один ход можно получить 6 или 12 камней. Игра завершается, 
когда количество камней в куче становится не более 19. Победителем считается игрок, сделавший последний ход, то есть первым получивший кучу, в которой будет 19 или меньше камней. 
В начале игры в куче было S камней, S > 19
Укажите минимальное значение S, при котором Петя не может выиграть первым ходом, но при любом первом ходе Пети Ваня может выиграть своим первым ходом.
Задание 20.
Для игры, описанной в задании 19, найдите два наименьших значения S, при которых Петя не может выиграть первым ходом, но у 
Пети есть выигрышная стратегия, позволяющая ему выиграть вторым ходом при любой игре Вани.
В ответе запишите найденные значения в порядке возрастания.

Задание 21.
Для игры, описанной в задании 19, найдите минимальное значение S, при котором у Вани есть стратегия, позволяющая ему выиграть 
первым или вторым ходом при любой игре Пети, но у Вани нет стратегии, которая позволила бы ему гарантированно выиграть первым ходом.'''
def f(s, m):
  if s <= 19: return m % 2 == 0
  if m == 0: return 0
  h = []
  if s % 2 == 0:
      h = [f(s - 5, m - 1), f(s // 2, m - 1)]
  if s % 3 == 0:
      h = [f(s - 5, m - 1), f(s // 3, m - 1)]
  if s % 2 != 0 and s % 3 != 0:
      h = [f(s - 5, m - 1), f(s + 1, m - 1)]
  return any(h) if m % 2 != 0 else all(h)

print('19)', [s for s in range(20, 100) if f(s, 2)])
print('20)', [s for s in range(20, 100) if not f(s, 1) and f(s, 3)])
print('21)', [s for s in range(20, 100) if not f(s, 2) and f(s, 4)])
#25
#40 43
#60