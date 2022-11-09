#!/bin/bash
<<COMENT
# ejecutar desde el mismo lugar de donde se encuentra este archivo:
bash tam.sh

# crear variable de entorno:
export HOLA=10

# busca variable de entorno creado:
env | grep "HOLA"

# llama env variable en linea de comando:
HOLA
COMENT

RUTA=$(pwd)

cd $RUTA/como_debe_ser/train/in
TAM_1=$(ls -1 | wc -l)
cd $RUTA/como_debe_ser/train/out
TAM_2=$(ls -1 | wc -l)
cd $RUTA/como_debe_ser/train/ruedas
TAM_3=$(ls -1 | wc -l)
cd $RUTA/como_debe_ser/validation/in
TAM_4=$(ls -1 | wc -l)
cd $RUTA/como_debe_ser/validation/out
TAM_5=$(ls -1 | wc -l)
cd $RUTA/como_debe_ser/validation/ruedas
TAM_6=$(ls -1 | wc -l)

echo train/in $TAM_1 
echo train/out $TAM_2 
echo train/ruedas $TAM_3 
echo
echo validation/in $TAM_4
echo validation/out $TAM_5 
echo validation/ruedas $TAM_6 

