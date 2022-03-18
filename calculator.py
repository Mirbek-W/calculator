# мой первый калькулятор
from colorama import *

init( autoreset = True) 

print(Fore.BLUE+Back . GREEN+"     Добро пожаловать! на калькулятор \n     не стал до конца добивать но и   \n     так надеюсь сойдёт!              ")

while True:
    try:
        
        iop=float(input("# введите первое число  :"))
        zn=input("\n\n # что нужно делать?\n # * умножение \n # / деление \n # + плюс \n # - минус \n # % остаток при делении \n # * умножение \n #:")
        iop2=float(input("\n\n # введите второе  число  :"))
    except ValueError:
        print(Fore.WHITE+Back .RED+"\n Hе верное значение! введите с начало !\n")
        continue


    if zn =="+": #  плюс
        res=iop+iop2
        print(Fore.RED +"\n # результат :",res)
        input("\n нажмите ENTER")
        continue 

    elif zn == "-":  # минус 
        res= iop-iop2
        print(Fore.RED+ "\n # результат :",res )
        input("\n нажмите ENTER \n")
        continue 

    elif zn =="/":  #деление 
        res=iop/iop2
        print(Fore.RED+ "\n # результат :",res)
        input("\n нажмите ENTER \n")
        continue

    elif zn =="%":    # остаток  при делении 
        res=iop%iop2
        print(Fore.RED+ "\n # результат :",res)
        input("\n нажмите ENTER \n")
        continue

    elif zn =="*":  # умножение 
        res=iop*iop2
        print(Fore.RED +"\n # результат :",res)
        input("\n нажмите ENTER \n")
        continue   
    else:
        print ( Fore.WHITE+Back.RED+ "такой функции нет ! =  ",zn)
        continue
        








