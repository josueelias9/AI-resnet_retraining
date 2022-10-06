# - `AI-resnet_retraining`
- https://keras.io/api/applications/
- https://www.tensorflow.org/tutorials/images/transfer_learning
- https://hub.docker.com/_/python
- https://docs.docker.com/engine/reference/commandline/run/#full-container-capabilities---privileged

```bash
cd (ruta de repo)

docker-compose up -d

docker run -t -i --privileged django-image bash
```

- ssh -i ~.ssh\id_ed25519.pub josueelias9@ec2-18-218-105-152.us-east-2.compute.amazonaws.com
- clave aaa

# - `Conexion remota`
Seguir [este](https://code.visualstudio.com/docs/remote/troubleshooting#_improving-your-security-with-a-dedicated-key) tutorial oficial para usar _remote ss_. Primero tienes que crear tu servicio en AWS.

- Agregar nuevo host al costado de _SSH TARGETS_ hay un _+_. Poner mouse encima y aparece el mensaje _Add new_. Dar click. ([fuente](https://code.visualstudio.com/docs/remote/ssh#_remember-hosts-and-advanced-settings))
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