
import os

path = "/data/final_data/Checked_cars"
b = []
count = 0

# revisa cada carpeta (cambia el 20 para aumentar el numero de carpetas a revisar)
for c,each_class_name in zip([0]*20,os.listdir(path)):

    # informativo: imprime cada carpeta a la que se esta entrando
    print(each_class_name)
    a = each_class_name.split("_")
    
    # valida que no cambia la raiz de la carpeta
    if b != a[0:2]:

        # si cambia, cambia el nombre de la raiz
        b = a[0:2]
        print("cambio la ruta donde se guardara: "+"_".join(b))

        # y pones el contador a cero para que comienze de 0 desde esta nueva raiz
        count = 0

    # revisa cada archivo
    for mi_file in os.listdir(path +"/"+ each_class_name):
    
        # maximo 5 archivos por carpeta raiz (en teoria este valor lo deberia de modificar la red. Si encuentra una imagen que corresponde deberia aumentar este valor.)
        count = count + 1 
        if count < 5:

            # aplica la red neuronal para la inferencia
            print(mi_file)

