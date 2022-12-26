task = int(input('введите номер залачи от 1 до 5:'))
match task:
    case 1:
#     
        print(int(sum))

    case 2:
#       
            print(factorial, end=' ')
    case 3:
# 
        print("Сумма элементов",sum)

    case 4:
       def binary (n):
        result = ''
        while n != 0:
            result += str(n % 2)
            n //= 2
        return result[::-1]
        print(result)
        
    case 5:
       
        print("Вот что получилось: ",arr)
        
    case _:
        print('Это нам не задавали')