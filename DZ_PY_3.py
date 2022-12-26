from random import uniform

task = int(input('введите номер залачи от 1 до 5:'))
match task:
    case 1:
        print('сумма элементов стоящих на нечетных позициях ')
        my_list = [2, 3, 5, 9, 3]
        print(my_list)
        total = 0     
        for i in range(len(my_list)):
            if i % 2 != 0:
                total += my_list[i]
        
        print("Сумма", total)


    case 2:
        print('Произведение пар чисел ')
        my_list = [2, 3, 5, 9, 3]
        print(my_list)
        product = 1
        while len(my_list) > 0:
            product = my_list[0] * my_list[-1]
            if len(my_list) > 1:
                del my_list[0], my_list[-1]
            else:
                del my_list[0]
            print('Результат ',product)
        

    case 3:
# 
        n = int(input('Введите размер списка '))
        list1 = []
        for i in range(n):
            f = uniform(0, 9)
            list1.append(round(f, 2))

        min = list1[0]
        max = 0
        for i in range(len(list1)):
            
            if max < list1[i]:
                max = list1[i]
            if min > list1[i]:
                min = list1[i]
        dif = (max - int(max)) - (min - int(min))

        print(list1)
        print(max, min)
        print(round(dif,2))

    case 4:
       n= int(input('Введите число для перевода в двоичную систему:  '))
       def binary (n):
            result = ''
            while n != 0:
                result += str(n % 2)
                n //= 2
            return result[::-1]
            
       print(binary(n))
        
        
    case 5:
          
        def ngfb(n):
            if n < 1:
                return - 1
            else:
                return ((- 1) ** (n + 1)) * fibo(n)


        def fibo(n):
            if n < 2:
                return 1
            else:
                return fibo(n - 1) + fibo(n - 2)
            return 
        n = int(input('Введите количество элементов'))
        res = [0] * n
        res_2 = [0] * n
        for i in range(n):
            res[i] = fibo(i)
            res_2[i] = ngfb(i) * (- 1)
        res.insert(0, 0)
        print(res_2[::-1] + res)

        
    case _:
        print('Это нам не задавали')