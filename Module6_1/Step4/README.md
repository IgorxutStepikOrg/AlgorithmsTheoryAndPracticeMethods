# Задача на программирование: двоичный поиск

В первой строке даны целое число <code>1&nbsp;≤&nbsp;n&nbsp;≤&nbsp;10<sup>5</sup></code> и массив <code>A[1…&nbsp;n]</code> из <code>n</code> различных натуральных чисел, не превышающих <code>10<sup>9</sup></code>, в порядке возрастания, во второй — целое число <code>1&nbsp;≤&nbsp;k&nbsp;≤&nbsp;10<sup>5</sup></code> и <code>k</code> натуральных чисел <code>b<sub>1</sub>,&nbsp;…,&nbsp;b<sub>k</sub></code>, не превышающих <code>10<sup>9</sup></code>. Для каждого <code>i</code> от <code>1</code> до <code>k</code> необходимо вывести индекс <code>1&nbsp;≤&nbsp;j&nbsp;≤&nbsp;n</code>, для которого <code>A[j]&nbsp;=&nbsp;b<sub>i</sub></code>, или <code>−1</code>, если такого <code>j</code> нет.

## Примеры

Sample Input:

```
5 1 5 8 12 13
5 8 1 23 1 11
```

Sample Output:

```
3 1 -1 1 -1
```
