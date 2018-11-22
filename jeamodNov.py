'''модуль основных ф-ийй для initdata, импортируется
в основную программу'''
import re, sys, math
z=print

def ValSum(Dictionary):
    # Сумма одиночных значений Val любого словаря
    qs = 0
    for Key in Dictionary:
        qs += Dictionary[Key]
    return qs
        
def jround( number ):
    '''Ф-ия математического округления( не до четных) до целых'''
    integer = int( number )
    fractional_part = number - integer
    if fractional_part >= 0.5 :
        return integer + 1
    else:
        return integer

def findfp(): # находим подходящий результат умножения целых чисел
    pmax=int( input('Максимальное Подвигание ? : ') )
    fmax=int( input('Максимальный Фронт ? : ') )
    ss=int( input('На какую площадь нужно выйти? : ') )
    delta=int( input('Максимальное отклонение от площади(1-5 кв.м)? : ') )
    for f in reversed(range( fmax )):
        for p in reversed(range( pmax )):
            Sq=f*p
            if Sq==ss:
                print('Фронт= {}   Подвигание= {}   \
Площадь= {} '.format(f,p,ss))
            if abs(Sq-ss)<=delta: # ищем отклонение до delta  метров
                print('Приближенно Фронт: {} Подвигание: {}   \
Площадь: {} Прибл.площ: {} dlt: {}'.format(f,p,ss,Sq,ss-Sq))

def findfp2(): # находим 2 смежные площади, чтобы их f*p были целыми
    #----------------------------------ввод для 1й площ
    pmax1=int( input('Максимальное Подвигание 1 ? : ') )
    fmax1=int( input('Максимальный Фронт 1 ? : ') )
    ss1=int( input('На какую площадь 1 нужно выйти? : ') )
     #----------------------------------ввод для 2й площ
    pmax2=int( input('Максимальное Подвигание 2 ? : ') )
    fmax2=int( input('Максимальный Фронт 2 ? : ') )
    ss2=int( input('На какую площадь 2 нужно выйти? : ') )
    dlt=int( input('Максимальное отклонение между площадями? : ') )
    dev1,dev2 = [ ] , [ ]  # списки списков отклонений
    def qw(pmax, fmax, ss, delta):  #это измененная версия findfp
        dev=[ ] 
        for f in reversed(range( fmax )):
            for p in reversed(range( pmax )):
                Sq=f*p
                if Sq==ss:
                    sms = [ ' Фронт= ', f , ' Подвиг.= ', p , ' Площ.= ', ss , 'dlt = ',  0 ]
                    dev.append(sms)
                if abs(Sq-ss)<=delta: # ищем отклонение до delta  метров
                    sms = [ ' Прибл.: Фронт: ', f , ' Подвиг.: ', p , ' Площадь: ', ss , ' Прибл.площ: ', Sq , ' dlt: ', ss-Sq ]
                    dev.append(sms)
        return dev
    dev1=sorted( qw( pmax1, fmax1, ss1, dlt ) , key = lambda x : x[-1])
    dev2=sorted( qw( pmax2, fmax2, ss2, dlt ) , key = lambda x : x[-1])
    global dev
    dev = [ dev1 , dev2 ]
    return dev
                 
def isq():
    '''Используем  для подбора нужной площади по боковой длине \
    участка'''
    setalon = 4352 # нужная площадь, менять ручками
    print('-----------Внимание !!!---------')
    print('Эталонная площадь, на которую надо выйти = ',setalon)
    print('Если нужна другая, изменить в скрипте jeamod . ')
    s=float(input('\nВвести получившуюся площадь из чертежа : '))
    fr = float(input('Вводим боковую длину (фронт): '))
    print('Подвижка д.б. (+ влево, - вправо) : ', round((setalon - s)/fr, 3) )
    
def square():
    '''Используем для вычисления площади отработки помесячно \
       ,чтобы выйти на целые числа фронт*подвигание=площадь'''
    f=[0,0,0]
    p=[0,0,0]
    s=int(input('Площадь? : '))
    p[1]=int(input('Подвигание? : '))
    p[0]=p[1]-1
    p[2]=p[1]+1
    print('Фронт  Подвигание  Площадь Расхождение')
    for i in range(3):
        f[1]= s//p[i]
        f[0]=f[1]-1
        f[2]=f[1]+1
        for _ in range(3):
            print(f[_], '     ',p[i],'     ',f[_]*p[i],'     ',  f[_]*p[i]-s )

def isVarIn(nn,dd):
    '''Проверяем, чтобы не было совпадений имен переменных
       в исходной и рассчитываемой базах данных.'''
    for i in nn:
        for j in dd:
            if i==j:
                z('\n----Непорядок !-!-!-! \n----Переменная {} есть и в nb и в db !!!-!-!-!-!-!'.format(i)) 

def prizma(ugol1,ugol2,maxHUst):
    from math import tan as mt
    from math import radians as rd
    '''Угол устойчивого,рабочего уступов, максим высота уступа'''
    z ( 1/(mt(rd(ugol1))) )
    z ( 1/(mt(rd(ugol2))) )
    return round( maxHUst*( 1/(mt(rd(ugol1)))-1/(mt(rd(ugol2))) ),2)

def kol_rab_dn(fi,la): 
    ''' Определим количество рабочих дней по номерам месяцов .
        fi,la,ca - номера первого, последнего месяца(2017г). '''
    ca = { 1: 17, 2:18, 3:22, 4:20, 5:20, 6:21, 7:21, 8:23, 9:21, 10:22, 11:21, 12:21}
    krdn=0 
    for m  in range(fi,la+1):
        krdn+=ca[m]
    return krdn

def zlocdb(db, lst):
    '''Печатаем локальные базы данны из пунктов проекта'''
    for _ in lst:
        z(_,' : ', db[_][0], ' = ', db[_][1])

def zloc(*args):
    '''Более усовершенствованная версия zlocdb'''
    #zloc('Ku','zo','yp')            
    arg=list(args)
    for _ in args:
        for x in [db, nb]:
            if _ in x:
                z(_, x[_][0], x[_][1], sep=' : ')
                arg.remove(_)
    if len(arg)>0:
        z('---!!!--Переменная {} не найдена в основных базах данных!!!-------'\
          .format(arg))
       
def zdb(database): # print data base
    '''Печатаем всю базу данных посторочно на экран. Если надо изменить -
    корректируем в iinitdataNov'''
    z('\nОбщие базы данных:')
    for k,v in database.items() :
        z(k,' => ' , v[0], ' = ' , v[1] )

def idb(var_name, description, var_value, database):
    """Запишем описание переменной и ее значение в общую базу данных"""
    if var_name not in database:
        database[ var_name] =  [ description, var_value ]
        return var_value
    else:
        z('\n---Внимание! ---- Переменная {} уже существует в текущей базе данных!---!---!.\
            \nЭто: '.format(var_name), var_name, database[ var_name]  , \
          '\nИнициализация не выполнена. Задайте новое имя.')
        return database[var_name][1]

def Read_File(filename):
    with open ('{}'.format(filename), 'r' ) as f:
        fe=f.readlines()
    return fe

def info_project():
    print("""Модуль jeamod - тут набор только функций и классов =>
База данных с переменными и формулами в initdataNov. Часть описана
и откорректирована в теле вордовского проекта""")
    
def make_db_shelve(db,nb):
    '''Записываем одну общую базу (db+nb) на диск 'base_nonovas'''
    import shelve
    global base
    base = shelve.open('base_nonovas')
    for _ in db:
        if _ in nb:
            print('--!!!---Ahtung! Переменные {} совпадают!'.format(_))
    all_base = {**db, **nb} 
    for key in all_base:
        base[key] = all_base[key]
    print('\n-------В записанной базе  {}  строк----'.format(len( base )))
    base.close()

z('инициализация jeamod  завершена')


