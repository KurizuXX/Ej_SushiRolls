import os
import time
def Mostrar_menu():
    print('****************************************')
    print('* selecciona el roll que deseas llevar *')
    print('****************************************')
    print('* [1] Pikachu Roll              $4500  *')
    print('* [2] Otaku Roll                $5000  *')
    print('* [3] Pulpo Venenoso Roll       $5200  *')
    print('* [4] Anguila Eléctrica Roll    $4800  *')
    print('*                                      *')
    print('* [0] Completé mi pedido               *')
    print('****************************************')
def Mostrar_boleta():
    print('******************************')
    print(f"TOTAL PRODUCTOS:{Contprod}")
    print('******************************')
    print(f'Pikachu Roll : {ContPikachu_Roll}')
    print(f'Otaku Roll : {ContOtaku_Roll}')
    print(f'Pulpo Venenoso Roll: {ContPulpo_Roll}')
    print(f'Anguila Eléctrica Roll: {ContAnguila_Roll}')
    print('******************************')
    print(f"Subtotal por pagar: ${totalpedido}")
    if codigo_dcto == "soyotaku":
        print(f"Descuento por codigo: ${dcto_deltotal}\n")
        print(f"TOTAL: ${dcto_aplicado}")
    else:
        print(f"TOTAL: ${totalpedido}")

pikachu_roll=4500
otaku_roll=5000
pulpo_roll=5200
Anguila_roll=4800
Otro_pedido=0

codigo_dcto="null"
dcto="null"

print('****************************************')
print('*             Japan rolls              *')
print('****************************************')
input('\nPresiona una tecla para continuar al menú de Rolls')
while True:
    while True:
        totalpedido, ContPikachu_Roll, ContOtaku_Roll, ContPulpo_Roll, ContAnguila_Roll, Contprod = 0, 0, 0, 0, 0, 0
        dcto_deltotal, dcto_aplicado = 0, 0
        while True:
            os.system('cls')
            Mostrar_menu()
            if Otro_pedido==2:
                break
            try:
                seleccion = int(input('Digite qué va a llevar: '))
                if seleccion == 1:
                    totalpedido += pikachu_roll
                    os.system('cls')
                    Contprod += 1
                    ContPikachu_Roll += 1
                elif seleccion == 2:
                    totalpedido += otaku_roll
                    os.system('cls')
                    Contprod += 1
                    ContOtaku_Roll += 1
                elif seleccion == 3:
                    totalpedido += pulpo_roll
                    os.system('cls')
                    Contprod += 1
                    ContPulpo_Roll += 1
                elif seleccion == 4:
                    totalpedido += Anguila_roll
                    os.system('cls')
                    Contprod += 1
                    ContAnguila_Roll += 1
                elif seleccion == 0 and totalpedido==0:
                    print('No agregaste nada a tu pedido.\n Cerrando...')
                    time.sleep('cls')
                    os.system('cls')
                    break
                else:
                    print('Selección inválida.')
            except ValueError:
                print('ERROR \nIngresa solo números')
                time.sleep(1)
                os.system('cls')
        while codigo_dcto!='soyotaku' or codigo_dcto=='x': 
            try:    
                descuento=int(input('Tienes un codigo de descuento?\n[1] Si\n[2] No\n:'))
                if descuento ==1:
                    while True:
                        codigo_dcto=input('Ingresa tu codigo de descuento \nPara volver al menu anterior ingresa "X"):\n:').upper
                        if codigo_dcto=="SOYOTAKU" or codigo_dcto=="X":
                            os.system("cls")
                            break
                        else:
                            print("ingrese un codigo valido..."),input("")
                            os.system("cls")
                else:
                    os.system("cls")
                    break
            except ValueError:
                print('ERROR \nIngresa solo números')
                time.sleep(1)
                os.system('cls')
            if codigo_dcto=="soyotaku":
                dcto_deltotal= totalpedido*0.1 
                dcto_aplicado = totalpedido-dcto_deltotal
        Mostrar_boleta()
        Otro_pedido=int(input("Desea realizar otro pedido?\n[1]Si\n[2]No\n>>>"))
        if Otro_pedido==2:
            os.system('cls')
            break