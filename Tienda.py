import os
import random
import time

eventos = [
    ## Eventos neutros
    {"evento": "\033[1;37mUn trabajador está bailando arriba de la caja.",                       "dinero": 0, "animo": 0},
    {"evento": "\033[1;37mSemana tranquila. Todo va bien.",                                      "dinero": 0, "animo": 0},
    {"evento": "\033[1;37mDía lluvioso.",                                                        "dinero": 0, "animo": 0},
    {"evento": "\033[1;37mUn trabajador está bailando arriba de la caja.",                       "dinero": 0, "animo": 0},
    {"evento": "\033[1;37mSemana tranquila. Todo va bien.",                                      "dinero": 0, "animo": 0},
    {"evento": "\033[1;37mDía lluvioso.",                                                        "dinero": 0, "animo": 0},
    {"evento": "\033[1;37mUn cliente se queja del servicio.",                                    "dinero": 0, "animo": 0},

    ## Eventos buenos   
    {"evento": "\033[1;37mSubida de precios en bebidas. \033[1;32m+110€ \033[1;37m",             "dinero": 110, "animo": 5},
    {"evento": "\033[1;37mSubida de precios en la panadería. \033[1;32m+150€ \033[1;37m",        "dinero": 150, "animo": 5},
    {"evento": "\033[1;37mSubida de precios en lacteos. \033[1;32m+135€ \033[1;37m",             "dinero": 135, "animo": 5},
    {"evento": "\033[1;37mSubida de precios en carnes y pescado. \033[1;32m+175€ \033[1;37m",    "dinero": 175, "animo": 5},
    {"evento": "\033[1;37mSubida de precios en la frutería. \033[1;32m+90€ \033[1;37m",          "dinero": 90, "animo": 5},
    {"evento": "\033[1;37mSubida de precios en limpieza. \033[1;32m+45€ \033[1;37m",             "dinero": 45, "animo": 5},
    {"evento": "\033[1;37mFiesta local. \033[1;32m+80€ \033[1;37m",                              "dinero": 80, "animo": 10},
        
    ## Eventos malos
    {"evento": "\033[1;37mUn cliente roba. \033[1;31m-30€\033[1;37m",                            "dinero": -50, "animo": 0},
    {"evento": "\033[1;37mUn trabajador recibe una queja. \033[1;31m-15€\033[1;37m",             "dinero": -15, "animo": 0},
    {"evento": "\033[1;37mUn trabajador renuncia. \033[1;31m-100€\033[1;37m",                    "dinero": -750, "animo": -5},
    {"evento": "\033[1;37mInspección sanitaria. \033[1;31m-500€\033[1;37m",                      "dinero": -500, "animo": -10},
    {"evento": "\033[1;37mUn trabajador se enferma.",                                            "dinero": 0, "animo": -5},
    {"evento": "\033[1;37mUn trabajador tiene un accidente. \033[1;31m-200€\033[1;37m",          "dinero": -450, "animo": -10},
    {"evento": "\033[1;37mMulta grave. \033[1;31m-300€\033[1;37m",                               "dinero": -1200, "animo": 0},   

    ## {"evento": "\033[1;37m ",             "dinero": 0, "animo": 0},   
]

acciones = [
    {"accion": "Hacer promoción",              "dinero":  50, "animo": 15,  "desc": "\033[1;32m+50€\033[1;37m"},
    {"accion": "Hacer publicidad",             "dinero": 220, "animo": 25,  "desc": "\033[1;32m+220€\033[1;37m"},
    {"accion": "Abrir el fín de semana",       "dinero": 350, "animo": -25,  "desc": "\033[1;32m+350€\033[1;37m"},
    {"accion": "Destacar productos",           "dinero": 130, "animo": 2,  "desc": "\033[1;32m+130€\033[1;37m"},

    {"accion": "Día libre extra",              "dinero": -60, "animo": 50, "desc": "\033[1;31m-60€\033[1;37m"},
    {"accion": "Comprar stock",                "dinero": -300, "animo": 15,  "desc": "\033[1;31m-300€\033[1;37m"},
    {"accion": "Pagar más a los trabajadores", "dinero": -500, "animo": 45, "desc": "\033[1;31m-200€\033[1;37m"},
    {"accion": "Contratar un nuevo trabajador","dinero": -750, "animo": 25, "desc": "\033[1;31m-750€\033[1;37m"},
    
]

for indice, accion in enumerate(acciones):
    print(f"- [{indice}] {accion["accion"]} - {accion["desc"]}")

def limpiar_interfaz():
    os.system("cls")

def mostrar_interfaz(nombre, dinero, ganancia, estado_animo, evento, semana, personas, personas2):
    limpiar_interfaz()
    print ("\033[1;32m /¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨\                     ______  __    __  _______   _______  _______   ____    ____  _______  _______    ____   _______  _______     ______  \n"
           "/                 \              ^    / _____||  |  |  ||   __  \ |   ____||   __  \ |    \  /    ||   ____||   __  \  /  __| /  __   \|   __  \   /  __  \  \n"
           "\033[1;37m|¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨| \033[1;32m            / \   | |____ |  |  |  ||  |__|  ||  |____ |  |__|  ||  |\ \/ /|  ||  |____ |  |__|  |/  /   |  |  |  ||  |  \  \ |  |  |  | \n"
           "\033[1;37m|    __ \033[1;36m|¨¨¨¨¨¨¨¨|\033[1;37m| \033[1;32m           /   \  \____  \|  |  |  ||   ____/ |   ____||   _   / |  | \__/ |  ||   ____||   _   / |  |   |  |__|  ||  |   |  ||  |  |  | \n"
           "\033[1;37m|   |  |\033[1;36m|________|\033[1;37m|  o    o   \033[1;32m /___\   ____| ||  \__/  ||  |      |  |____ |  | \  \ |  |      |  ||  |____ |  | \  \ \  \__ |  ___   ||  |__/  / |  |__|  | \n"
           "\033[1;37m|___|__|__________|  |    |      |  \033[1;32m  |______/ \______/ |__|      |_______||__|  \__\|__|      |__||_______||__|  \__\ \____||__|  |__||_______/   \______/ \033[1;37m(por JavierMGB) ")


    print("\r \033[1;37m==========================================================================                             \n"
       "- \033[1;32m" + f"{nombre}" + "\033[1;37m - \033[1;36mSemana \033[1;37m" + f"{semana}" + " -                                                                   \n"
       "--------------------------------------------------------------------------                                            \n"
       "- \033[1;36mDinero: \033[1;37m" + f"{color_dinero(dinero)}" + " \033[1;37m(\033[1;32m" + f"{ganancia}" + "€/semana\033[1;37m)                                                         \n"
       "- \033[1;36mTrabajadores: \033[1;37m" + f"{estado_animo}" + "                                     \033[1;32m   __________  \033[1;37m                       \n"
       "--------------------------------------------------------------------------  \033[1;32m /..........\    \033[1;37m                         \n"
       "\033[1;33mEvento:                \033[1;37m                                                      |__________|\033[1;36m" + f"{personas}" + "\033[1;37m        \n"
       "- "+ f"{evento["evento"]}" + "                                                                                         \n"
       "--------------------------------------------------------------------------          \033[1;36m" + f"{personas2}" + "\033[1;37m                                   \n"
       "\033[1;33mAcciones:    \033[1;37m                                                                                                          ")
    acciones_semana = random.sample(acciones, 3)
    for indice, accion in enumerate(acciones_semana):
        print(f"- \033[1;37m[\033[1;33m{indice}\033[1;37m] {accion['accion']} - {accion['desc']}")
    
    print("==========================================================================                                           ")

def color_dinero(dinero):
    if dinero < 0:
        return f"\033[1;31m{dinero}€\033[1;37m"  # Rojo para negativo
    else:
        return f"\033[1;32m{dinero}€\033[1;37m"  # Verde para positivo


limpiar_interfaz()
nombre = input("\033[1;37mIntroduce el nombre de tu supermercado: ")
dinero = 500
animo = 50
semana = 1
estado_animo = "\033[1;37m >:( \033[1;37m :( \033[1;36m :| \033[1;37m :) \033[1;37m :3 \033[1;37m "
clientes = "¡ ¡"
clientes2 = ""
contador_semanal = 0

while True:
    evento = random.choice(eventos)
    ganancia = random.randint(80, 150) + evento["dinero"]
    dinero += ganancia
    animo = max(0, min(100, animo + evento["animo"]))
   
    mostrar_interfaz(nombre, dinero, ganancia, estado_animo, evento, semana, clientes, clientes2)

    print("\033[1;37mElige una acción (\033[1;33m0-2\033[1;37m) o (\033[1;31msalir\033[1;37m) para salir:")
    eleccion = input("> ")

    if eleccion == 'salir':
        print("\033[1;32m¡Gracias por jugar!\033[1;37m")
        break

    if eleccion in [0, 1, 2] or eleccion in ["0", "1", "2"]:
        accion = acciones[int(eleccion)]

        dinero += accion["dinero"]

        animo += accion["animo"]

    else:
        print("\033[1;37mOpción no válida. Pulsa Enter para continuar.")
        input("> ")
        continue


    if (animo >= 0 or animo < 0) and animo <= 20:
        estado_animo = "\033[1;31m >:( \033[1;37m :( \033[1;37m :| \033[1;37m :) \033[1;37m :3 \033[1;37m "

    elif animo >= 21 and animo <= 40:
        estado_animo = "\033[1;37m >:( \033[1;33m :( \033[1;37m :| \033[1;37m :) \033[1;37m :3 \033[1;37m "

    elif animo >= 41 and animo <= 60:
        estado_animo = "\033[1;37m >:( \033[1;37m :( \033[1;36m :| \033[1;37m :) \033[1;37m :3 \033[1;37m "

    elif animo >= 61 and animo <= 80:
        estado_animo = "\033[1;37m >:( \033[1;37m :( \033[1;37m :| \033[1;32m :) \033[1;37m :3 \033[1;37m "

    elif animo >= 81 and animo <= 100:
        estado_animo = "\033[1;37m >:( \033[1;37m :( \033[1;37m :| \033[1;37m :) \033[1;35m :3 \033[1;37m "


    if contador_semanal == 5 and animo >= 81:
        clientes += " ¡"
        contador_semanal = 0

    elif contador_semanal == 5 and animo < 81:
        contador_semanal = 0

    elif contador_semanal < 5:
        contador_semanal += 1

    elif clientes >= " ¡"*20 and animo >= 61 and contador_semanal == 5:
        clientes2 += " ¡ ¡"
        contador_semanal = 0

    
    if dinero <= -2000:
        print("\033[1;31mTu supermercado está en banca rota. Fin del juego.\033[1;37m")
        break
    elif dinero >= 10000 and clientes >= " ¡"*20 :
        print("\033[1;32m¡Felicidades! Has alcanzado el objetivo de 10000€. ¡Has ganado el juego!\033[1;37m")
        break
   
    semana += 1
    time.sleep(1)
