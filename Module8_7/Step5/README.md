# Задача на программирование: калькулятор

У вас есть примитивный калькулятор, который умеет выполнять всего три операции с текущим числом <code>x</code>: заменить <code>x</code> на <code>2&nbsp;×&nbsp;x</code>, <code>3&nbsp;×&nbsp;x</code> или <code>x&nbsp;+&nbsp;1</code>. По данному целому числу <code>1&nbsp;≤&nbsp;n&nbsp;≤&nbsp;10<sup>5</sup></code> определите минимальное число операций <code>k</code>, необходимое, чтобы получить <code>n</code> из <code>1</code>. Выведите <code>k</code> и последовательность промежуточных чисел.

## Примеры

Sample Input 1:

```
1
```

Sample Output 1:

```
0
1
```

<hr/>

Sample Input 2:

```
5
```

Sample Output 2:

```
3
1 2 4 5
```

<hr/>

Sample Input 3:

```
96234
```

Sample Output 3:

```
14
1 3 9 10 11 22 66 198 594 1782 5346 16038 16039 32078 96234
```
