#Задача на программирование: наибольшая последовательнократная подпоследовательность

Дано целое число <code>1&nbsp;≤&nbsp;n&nbsp;≤&nbsp;10<sup>3</sup></code> и массив <code>A[1…&nbsp;n]</code> натуральных чисел, не превосходящих <code>2&nbsp;×&nbsp;10<sup>9</sup></code>. Выведите максимальное <code>1&nbsp;≤&nbsp;k&nbsp;≤&nbsp;n</code>, для которого найдётся подпоследовательность <code>1&nbsp;≤&nbsp;i<sub>1</sub>&nbsp;<&nbsp;i<sub>2</sub>&nbsp;<&nbsp;…&nbsp;<&nbsp;i<sub>k</sub>&nbsp;≤&nbsp;n</code> длины <code>k</code>, в которой каждый элемент делится на предыдущий (формально: для всех <code>1&nbsp;≤&nbsp;j&nbsp;<&nbsp;k</code>, <code>A[i<sub>j</sub>]&nbsp;|&nbsp;A[i<sub>j+1</sub>]</code>).

## Примеры

Sample Input:

```
4
3 6 7 12
```

Sample Output:

```
3
```
