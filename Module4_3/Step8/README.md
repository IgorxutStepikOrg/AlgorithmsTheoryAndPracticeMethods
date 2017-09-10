# Задача на программирование: очередь с приоритетами

Первая строка входа содержит число операций <code>1&nbsp;≤&nbsp;n&nbsp;≤&nbsp;10<sup>5</sup></code>. Каждая из последующих <code>n</code> строк задают операцию одного из следующих двух типов:

- <code>Insert x</code>, где <code>0&nbsp;≤&nbsp;x&nbsp;≤&nbsp;10<sup>9</sup></code> — целое число;
- <code>ExtractMax</code>.

Первая операция добавляет число <code>x</code> в очередь с приоритетами, вторая — извлекает максимальное число и выводит его.

## Примеры

Sample Input:

```
6
Insert 200
Insert 10
ExtractMax
Insert 5
Insert 500
ExtractMax
```

Sample Output:

```
200
500
```
