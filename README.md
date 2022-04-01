Игру «Жизнь» изобрел математик Джон Хортон Конвей в 1970 году. 

Правила игры «Жизнь» достаточно простые:

«Жизнь» разыгрывается на бесконечном клеточном поле.
У каждой клетки 8 соседних клеток.
В каждой клетке может жить существо.
Существо с двумя или тремя соседями выживает в следующем поколении, иначе погибает от одиночества или перенаселённости.
В пустой клетке с тремя соседями в следующем поколении рождается существо [1].


These rules, which compare the behavior of the automaton to real life, can be condensed into the following:

Any live cell with two or three live neighbours survives.
Any dead cell with three live neighbours becomes a live cell.
All other live cells die in the next generation. Similarly, all other dead cells stay dead.


try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk


[[3,1], [4,3], [4,2], [5,4], [5,3], [6,4]]