
# import required module
import os

# rutas padres
como_dan_path = './como_dan'
como_debe_ser_path = './como_debe_ser'

# tamaño del validation
porcentaje = 20

# se itera por cada clase
for each_class_name in os.listdir(como_dan_path):
    
    # todo lo que viene hasta el final es para una sola clase (<clase>)
    each_class_path = como_dan_path + '/' + each_class_name

    # total de archivos que hay en la carpeta <clase>
    each_class_num_archivos = len([entry for entry in os.listdir(
        each_class_path) if os.path.isfile(os.path.join(each_class_path, entry))])

    # definimos el numero de elementos que debe tener la carpeta "como_debe_ser/validation/<clase>"
    each_class_num_validation = round(each_class_num_archivos * porcentaje / 100)
    
    # repartimos los archivos
    for count, given_file_name in enumerate(os.listdir(each_class_path)):
        given_file_path = each_class_path + '/' + given_file_name

        # se envia a la carpeta <clase>/validation/ el porcentaje de archivos que corresponda
        if(count +1 <= each_class_num_validation):
            destination = como_debe_ser_path + '/validation/' + each_class_name
            os.popen('cp ' + given_file_path + ' ' + destination)

        # los demas archivos se envian a la carpeta <clase>/train/
        else:
            destination = como_debe_ser_path + '/train/' + each_class_name
            os.popen('cp ' + given_file_path + ' ' + destination)
