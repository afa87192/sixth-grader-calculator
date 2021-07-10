y=input('language?')
if y =="Русский"or "русский" or"руский"  or 'Russian ':
     print ( '''
                ______________________
               |                     |
               | Калькулятор v1.03   |
               | ____________________|
      поддержка знаков (*,+,-,**)  и расчёт площади , периметра ''' )   
     what  =  input ( 'что нужно геометрия , арифметика, скорость  ? ')
     if what ==  "арифметика" :
          what  =  input ( "Знак действия (*,:,+,-,**)" )
          if what == '*' or ':' or '+' or '-' or '**':
               if what ==  "+" :
                    a  =  float ( input ( "Первое слогаемое " ))
                    b  =  float ( input ( "Второе слогаемое " )) 
                    print ( "Результат :", a  +  b (sep = ''))
               elif what ==  "-" :
                    a  =  float ( input ( "Уменьшаймое" ))
                    b  =  float ( input ( "Вычитаймое" ))  
                    print ( " Результат:"  +  str ( a  -  b ))
               elif what  ==  "*" :
                    a  =  float ( input ( "Первый множитель " ))
                    b  =  float ( input ( "Второй множитель " )) 
                    print ( "Результат :"  +  str ( a  * b ))
               elif what  ==  ":" :
                    a  =  float ( input ( "делимое " ))
                    b  =  float ( input ( "делитель" )) 
                    print ( "Результат :"  +  str ( a  / b ))
               elif what  ==  "**" :
                    a  =  float ( input ( "Первое число " ))
                    b  =  float ( input ( "Второе число " )) 
                    print ( "Результат :"  +  str ( a  **  b ))
          else:
               print ( "Неверная операция !!" )
     if what == 'геометрия':
          what=input( '3д или 2д фигуры?')
          if what == '2д':
               what  =  input ( 'какая фигура (прямоугольник, квадрад, окружность')
               if what ==  "прямоугольник" :
                    a  =  float ( input ( "Первая сторона" ))
                    b  =  float ( input ( "Вторая сторона" )) 
                    print ( "Результат периметр  :", a  +  b,'см плошадь:',a*b," см2"(sep = ''))
               elif what ==  "квадрад" :
                    a  =  float ( input ( " сторона" ))
                    print (  "Результат периметр  :", a  +  a,'см плошадь:',a*a," см2"(sep = ''))
                    
               elif what  ==  "окружность" :
                    a  =  float ( input ( "радиус" ))  
                    print ( "Результат периметр  :",  a*2*3.14,'см плошадь:',a**2*3.14," см2"(sep = ''))
          if what == '3д':
               what  =  input ( 'какая фигура (куб, шар,цилиндр, параллелепипед)')
               if what ==  "шар" :
                    r=int(input ('радиус'))
                    print ( "Результат плошадь:'", 4* 3.14*r**2," см2 объём ",3/4*3.14*r**3 (sep = ''))  
               if what ==  " куб" :
                    a  =  float ( input ( "Сторона" ))
                    print ( "Результат периметр  :",  4*(a + a + a) ,'см плошадь:', 2*( a* a +   a*a +  a*a)," см2 объём ",a **3(sep = '') )
               if what ==  " параллелепипед" :
                    a  =  float ( input ( "Первая сторона" ))
                    b  =  float ( input ( "Вторая сторона" ))
                    с = float ( input ( "Третья сторона" ))
                    print ( "Результат периметр  :",  4*(a + b + с) ,'см плошадь:', 2*( a* b +   b*с +  a*с)," см2 объём ",a * b * с (sep = ''))
          else:
               print ( "Неверная операция !! " )     
     if what == 'скорость':
          x= input( 'что ищем? время? скорость? растояние?')
          if x=='время':
               s=int(input( 'растояние?'))
               v=int(input( 'скорость?'))
               print(s/v)
          if x==' растояние':
               v=int(input( 'скорость?'))
               t=int(input( 'время?'))
               print(v*t)
          if x==' скорость':
               s=int(input( 'растояние?'))
               t=int(input( 'время?'))
               print(s/t)  
if y =="English ":
     print ('''
                     ______________________
                    |                      |
                    | Calculator v1.03     |
                    | ____________________ |
           support for signs (*, +, -, **) and calculation of area, perimeter ''')
     what = input ('what do you need geometry, arithmetic, speed?')
     if what == "arithmetic":
          what = input ("Action sign (*,:, +, -, **)")
          if what == '*' or ':' or '+' or '-' or '**':
               if what == "+":
                    a = float (input ("First syllable"))
                    b = float (input ("Second syllable"))
                    print ("Result:" + str (a + b))
               elif what == "-":
                    a = float (input ("Reduced"))
                    b = float (input ("Subtracted"))
                    print ("Result:" + str (a - b))
               elif what == "*":
                    a = float (input ("First factor"))
                    b = float (input ("Second factor"))
                    print ("Result:" + str (a * b))
               elif what == ":":
                    a = float (input ("dividend"))
                    b = float (input ("divisor"))
                    print ("Result:" + str (a / b))
               elif what == "**":
                    a = float (input ("First number"))
                    b = float (input ("Second number"))
                    print ("Result:" + str (a ** b))
               else:
                    print ("Invalid operation !!")
     if what == 'geometry':
          what = input ('3d or 2d shapes?')
          if what == '2d':
               what = input ('what shape (rectangle, square, circle')
               if what == "rectangle":
                    a = float (input ("First side"))
                    b = float (input ("Second side"))
                    print ("Result perimeter:", a + b, 'cm area:', a * b, "cm2"(sep = ''))
               elif what == "quadrad":
                    a = float (input ("side"))
                    print ("Result perimeter:", a + a, 'cm area:', a * a, "cm2"(sep = ''))
                    
               elif what == "circle":
                    a = float (input ("radius"))
                    print ("Result perimeter:", a * 2 * 3.14, 'cm area:', a ** 2 * 3.14, "cm2"(sep = ''))
          if what == '3d':
               what = input ('what shape (cube, ball, cylinder, parallelepiped)')
               if what == "ball":
                    r = int (input ('radius'))
                    print ("Result area: '", 4 * 3.14 * r ** 2, "cm2 volume", 3/4 * 3.14 * r ** 3(sep = ''))
               if what == "cube":
                    a = float (input ("Side"))
                    print ("Result perimeter:", 4 * (a + a + a), 'cm area:', 2 * (a * a + a * a + a * a), "cm2 volume", a ** 3(sep = ''))
               if what == "box":
                    a = float (input ("First side"))
                    b = float (input ("Second side"))
                    c = float (input ("third party"))
                    print ("Result perimeter:", 4 * (a + b + c), 'cm area:', 2 * (a * b + b * c + a * c), "cm2 volume", a * b * c (sep = ''))
          else:
                    print ("Invalid operation !!")
     if what == 'speed':
          x = input ('what are we looking for? time? speed? distance?')
          if x == 'time':
               s = int (input ('distance?'))
               v = int (input ('speed?'))
               print (s / v)
          if x == 'distance':
               v = int (input ('speed?'))
               t = int (input ('time?'))
               print (v * t)
          if x == 'speed':
               s = int (input ('distance?'))
               t = int (input ('time?'))
               print (s / t)     
     
