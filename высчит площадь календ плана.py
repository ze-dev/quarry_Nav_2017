z=print

# в главном импортируемом модуле есть другая ф-ия. Использовать ту.
ans = ''
needS = 4367
while ans != 'v':
    realS =float( input('\nВводим получившуюся на плане площадь: ') )
    deltaS = needS - realS
    z('Разница площадей = ', deltaS)
    try:
         dlin =float( input('Вводим длину бока участка : ') )
         d= round(deltaS/dlin,3 )
         z('Двигаем (+ влево, - вправо) на : {}'.format( d ))
    except:
        z('Что-то пошло не так... Проверь ввод.')
    ans = input('Следующая итерация - enter, если выходим - v : ')
    
