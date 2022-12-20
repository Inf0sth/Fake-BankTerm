"""
Reto personal para aplicar lo aprendido:
Terminal de banco
Joel Araiza
"""
#Librerias a usar:
import time
import pickle
import os

#Codigo a probar para "PICKLE":

#Varialbes Globales:
#Voy a probar con está variable
balance = 2000.0

#Code to check if the file exist:
if not os.path.exists('balance.pkl'):
    # Guarda el valor de la variable en un archivo
    with open('balance.pkl', 'wb') as f:
        pickle.dump(balance, f)


#Variable para la barra de cargado.
limite = 30
#Función para una barra de cargado (Modelo básico)
def progress_bar(segmento, total, long):
    porcentaje = segmento/total
    completado = int(porcentaje * long)
    restante = long - completado
    #Creamos la barra a nuestro gusto:
    bar = f"[{'$' * completado}{'-' * restante}{porcentaje:.2%}]"
    return bar

#Funciones para las operaciones:
def consult_balance(balance):
    # Carga el valor de la variable desde el archivo
    with open('balance.pkl', 'rb') as f:
        balance = pickle.load(f)
    print("Consulta de saldo.\n")
    print(f"El saldo disponible es: ${balance:.2f}")

def out_balance(balance):
    # Carga el valor de la variable desde el archivo
    with open('balance.pkl', 'rb') as f:
        balance = pickle.load(f)
    print("Retiro de efectivo.\n")
    output_balance = float(input("Ingrese la cantidad a retirar: "))
    while output_balance >= balance:
        print("Saldo insuficiente.\n")
        print(f"El saldo disponible es: ${balance:.2f}")
        output_balance = float(input("Ingrese la cantidad a retirar nuevamente: "))
    
    if output_balance <= balance or output_balance == balance:
        print("Operación exitosa")
        balance = balance - output_balance
        # Guarda el valor de la variable en un archivo
        with open('balance.pkl', 'wb') as f:
            pickle.dump(balance, f)
        # Carga el valor de la variable desde el archivo
        with open('balance.pkl', 'rb') as f:
            balance = pickle.load(f)
        print(f"""
        Salida: ${output_balance:.2f}
    
        Restante: ${balance:.2f}
        """)


def enter_balance(balance):
    print("Deposito de efectivo.\n")
    # Carga el valor de la variable desde el archivo
    with open('balance.pkl', 'rb') as f:
        balance = pickle.load(f)
    deposit = float(input("Ingrese el deposito:\n--> "))
    balance = balance + deposit
    # Guarda el valor de la variable en un archivo
    with open('balance.pkl', 'wb') as f:
        pickle.dump(balance, f)
    # Carga el valor de la variable desde el archivo
    with open('balance.pkl', 'rb') as f:
        balance = pickle.load(f)    
    print(f"""\n
    El saldo en la cuenta ahora es: {balance:.2f}
    """)
    return balance

#Usando la barra de carga:
for i in range(limite + 1):
    time.sleep(0.05)
    print(progress_bar(i, limite, 40), end= "\r")

#Simulando un cajero:
#Codigo para el login y un banner:
print ("""\n
███████╗ █████╗ ██╗  ██╗███████╗              ██████╗  █████╗ ███╗   ██╗██╗  ██╗
██╔════╝██╔══██╗██║ ██╔╝██╔════╝              ██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝
█████╗  ███████║█████╔╝ █████╗      █████╗    ██████╔╝███████║██╔██╗ ██║█████╔╝ 
██╔══╝  ██╔══██║██╔═██╗ ██╔══╝      ╚════╝    ██╔══██╗██╔══██║██║╚██╗██║██╔═██╗ 
██║     ██║  ██║██║  ██╗███████╗              ██████╔╝██║  ██║██║ ╚████║██║  ██╗
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝              ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
                                                                                
\n""")

user = str(input("\nIngrese su usuario: "))
psswd = int(input("\nIngrese su contraseña: "))

#Variable estatica para el contador de intentos_
login_num = 0

while login_num !=2 and psswd != 4231:
    print("La contraseña es incorrecta")
    psswd = int(input("Ingrese su contraseña: "))
    login_num= login_num + 1

#Mensaje para notificar al usuario y cerrar terminar el programa
if login_num == 2 and psswd != 4231:
    print("""
    ¡DEMASIADOS INTENTOS!
             ⚠️
     ..CUENTA BLOQUEADA..
    """)
    exit()

#Menú definitión:
menu_terminal = (f"""
Bienvenid@ {user}

Menu:

1->Consutar saldo.
2->Retirar efectivo.
3->Depositar efectivo.
4->Salir.    
""")

#NOTAS: Agregar una barra de carga en a traves de un función donde corresoponda.
if psswd == 4231:
    log_user_term = 1

while log_user_term == 1:
    #Barra de carga:
    for i in range(limite + 1):
        time.sleep(0.07)
        print(progress_bar(i, limite, 40), end= "\r")
        
    print(menu_terminal)
    user_operation = int(input("Ingrese la opción a ejecutar \n--> "))

    if user_operation == 1:
        consult_balance(balance)
        log_user_term = int(input("\nDesea realizar otra operación?\n1-->SÍ\n0-->NO\n: "))
    elif user_operation == 2:
        balance = out_balance(balance)
        log_user_term = int(input("\nDesea realizar otra operación?\n1-->SÍ\n0-->NO\n: "))
    elif user_operation == 3:
        balance = enter_balance(balance)
        log_user_term = int(input("\nDesea realizar otra operación?\n1-->SÍ\n0-->NO\n: "))
    elif user_operation == 4:
        log_user_term = 0
    else:
        print("Operación no valida.")
        log_user_term = int(input("\nDesea realizar otra operación?\n1-->SÍ\n0-->NO\n: "))

if log_user_term == 0:
    print("\nOperación finalizada.")
else:
    print("\nOperación no valida.")
    log_user_term = int(input("\nDesea realizar otra operación?\n1-->\n0-->\n: "))