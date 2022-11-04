# - `Retraining a Model`
__Resumen del proyecto__: 
- Uso del poder de computo de las maquinas de AWS para poder entrenar una red neuronal. 
![](documentation/image.jpeg)
- todo el computo se realizara en un contenedor.
- La red tiene que ser capaz de distinguir:
  - parte interna de un vehiculo 
    ![](documentation/interior.png)
  - parte externa de un vehiculo 
    ![](documentation/exterior.jpg)



Estructura del proyecto:
```
|-- AI-resnet_retraining
    |-- AWS
    |-- documentacion
    |-- machine learning
    |-- README.md
```
## -- `machine learning part`
- Partimos por de [esta](https://www.tensorflow.org/tutorials/images/transfer_learning) plantilla.
- prepara estructura del folder y zipear.
```
|-- carpeta_dataset
    |-- train
        |-- class_1
        |-- class_2
    |-- validation
        |-- class_1
        |-- class_2
    |-- vectorize.py
```
- subir el zip a google colab
- dentro del proyecto ejecutar los siguientes comandos para poder descargar el zip (los comandos demoran en ejecutarse. Ser pacientes.)
```bash
!sudo apt-get install unzip
!unzip /content/carpeta_dataset.zip
```
- modificar asi:
```python
# _URL = 'https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip'
# path_to_zip = tf.keras.utils.get_file('cats_and_dogs.zip', origin=_URL, extract=True)
# PATH = os.path.join(os.path.dirname(path_to_zip), 'cats_and_dogs_filtered')

PATH = '/content/carpeta_dataset' # ubicacion donde esta la carpeta descomprimida

train_dir = os.path.join(PATH, 'train')
validation_dir = os.path.join(PATH, 'validation')

# BATCH_SIZE = 32

BATCH_SIZE = 8 # de 32 lo bajamos a 8 porque tenemos pocos datos

IMG_SIZE = (160, 160)
...
```
- al modificar el batch tambien se tiene que modificar las imagenes:
```python
...
for images, labels in train_dataset.take(1):
  #for i in range(9):
  for i in range(8):
    ax = plt.subplot(3, 3, i + 1)
    ...
```
### --- `Adicionales`
- El algoritmo de machine learning de este proyecto se base en ejemplo oficial de tensorflow. Se usara el modelo _Imagenet_.
![](documentation/imagenet.jpg)
### --- `Links oficiales`
- Ejemplo oficial de transfer learning usando el modelo el algoritmo mobilNet [Link](https://www.tensorflow.org/tutorials/images/transfer_learning)
- Informacion de otra arquitectura similar (Resnet50) [Link](https://keras.io/api/applications/)
- Diferencia entre [modelos secuenciales](https://www.tensorflow.org/guide/keras/sequential_model) y [modelos no secuenciales](https://www.tensorflow.org/guide/keras/functional)
- Paper oficial de MobileNetV2 [Link](https://arxiv.org/pdf/1801.04381.pdf) 
- How to use save only the best weights? (search for _save_best_only_) [Link](https://www.tensorflow.org/guide/keras/train_and_evaluate#checkpointing_models)
- How to dynamically label the group of weights that we save? (search for _val_loss:.2f_) [Link](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint)

ssasdasdasdas


## -- `Infraestructure as a Service`
- ir al servicio _EC2_ de _AWS_ y crear un _key pair_ y llamarle _key-pair-name_.
- Subir el archivo _cloudformation_file.yml_ a _Cloudformation_. Luego crear el stack.
- ir a _EC2_ y buscar la instancia creada. Ejecutar:
```bash
touch initialize_EC2.sh
nano initialize_EC2.sh
```
- copiar el contenido del archivo _initialize_EC2.sh_ y pegarlo en el archivo con el mismo nombre dentro de la instancia _EC2_. Luego ejecutar:
```bash
bash initialize_EC2.sh
```
## -- `Conexion remota`

Seguir [este](https://code.visualstudio.com/docs/remote/troubleshooting#_improving-your-security-with-a-dedicated-key) tutorial oficial para usar _Remote - SSH_. Primero tienes que crear tu servicio en AWS.

- En _Remote Explorer_ (al costado de _SSH TARGETS_) hay un _+_. Poner mouse encima y aparece el mensaje _Add new_. Dar click. ([fuente](https://code.visualstudio.com/docs/remote/ssh#_remember-hosts-and-advanced-settings))
- poner lo siguiente _nombre@dominio_. Ejemplo:
```
ubuntu@ec2-52-91-214-209.compute-1.amazonaws.com
```
- seleccionar la ruta _/home/josue/.ssh/config_ ([fuente](https://code.visualstudio.com/docs/remote/troubleshooting#_improving-your-security-with-a-dedicated-key))
- _Abrir configuracion_
- Agregar lo siguiente
```
IdentityFile /(ruta donde esta el public key)
```
- hay que modificar los permisos (asi lo recomienda AWS).
```
chmod 400 _path de key_
```
- Usar el icono del la extension y conectar directamente.

## -- `docker`
- https://hub.docker.com/_/python
- https://docs.docker.com/engine/reference/commandline/run/#full-container-capabilities---privileged
```bash
cd (ruta de repo)

docker-compose up -d

docker run -t -i --privileged django-image bash
```
- ssh -i ~.ssh\id_ed25519.pub josueelias9@ec2-18-218-105-152.us-east-2.compute.amazonaws.com
- clave aaa

## -- `observacion`
- primero levantar servidor linux con docker y docker compose
- levantar imagen y contenedor con todas las dependencias
- dentro de contenedor instalar git para descargar proyecto