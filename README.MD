Python скрипт для добавления регулярного выражения для каждого project_id,
исходя из доменов, находящихся в таблице domains.

1. Из-за ограничения по времени выполнения задания было решено использовать фильтрацию
по длине символов в домене верхнего уровня (длины не валидных доменов были одинаковы)
2. Стоит уточнить, допустимы ли различные домены второго уровня, так как есть домены,
которые отличаются от yyy.com в строках 124, 126 и 128. Если это не допускается,
тогда в конец регулярного выражения необходимо будет передавать валидный домен
второго уровня для дополнительной проверки.
3. Как вариант более универсальной проверки (не вписывается во временные рамки), возможно
использование встроенной библиотеки zxcvbn (https://github.com/dwolfhub/zxcvbn-python), 
для проверки энтропии строки. Для валидных доменов урвоень энтропии должен быть ниже,
соответственно регулярное выражение можно составлять из or условий, где будут перечислены
валидные случаи (стоит оценить производительность)
4. Скорее всего самым работоспособным способом будет обучение нейросети для поиска невалидных
доменов, после чего использовать уже обученную легковесную модель на сервере. 