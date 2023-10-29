# Instalacion

La instación de **CPCReady** es muy sencilla, tan solo se necesitan ciertos requisitos para poder instalarlos.

## Requisitos

| Software | URL |Version |
| ------ | ------ | ------ |
| Python | [Descarga](https://www.python.org/downloads/) | 3. 6 o superior (Recomendada =>3.10)|
| Visual Studio Code |[Descarga](https://www.python.org/downloads/) | Latest|

Para ver como instalar Python en todos los sistemas ver [este link ](https://www.ionos.es/digitalguide/paginas-web/desarrollo-web/instalar-python/)

Una vez instalado Python en tu sistema operativo, comprobaremos si tenemos la herramienta **pip** instalada. Esta herramienta nos permitira instalar CPCReady y mas modulos que algun dia podamos necesitar. 

Para ello abriremos un terminal (si no sabes como hacerlo accede a [este link ](https://www.ionos.es/ayuda/correo/solucion-de-problemas-correo-basiccorreo-profesional/abrir-la-linea-de-comandos-terminal/#:~:text=Abrir%20la%20l%C3%ADnea%20de%20comandos%20en%20Windows,entrada%20con%20la%20tecla%20Enter.) para verlo.

Y ejecutaremos

> **NOTA: 
Dependiendo de los sistemas operativos, el comando puede ser pip o pip3**
>
```sh
pip --version
```
Si nos devuelve la versión podremos continuar con la instalacion. Si no consulta [Instalar Pip en tu Sistema Operativo](https://tecnonucleous.com/2018/01/28/como-instalar-pip-para-python-en-windows-mac-y-linux/).

## Instalar CPCReady

Para instalar CPCReady en nuestra maquina, desde un terminal ejecutaremos:

```sh
pip install cpcready
```
Esto nos instalara la ultima version del software que este disponible en los repositorios. Podremos comprobar la version instalada ejecutando

```sh
CPCReady --version
```

## Upgrade CPCReady

Si ya tubieramos una version instalada de **CPCReady** y queremos instalar la ultima ejecutaremos:

```sh
pip install cpcready --upgrade
```

## Instalar Visual Studio Code

Aunque ya tendrias instalado **CPCReady** y podrias empezar a crear tus propios proyectos con Basic, te recomendamos que para una mejor experiencia lo hagas a traves de la herramienta de desarrollo Visual Studio Code.

Para instalarla ve al Software Market de tu sistema operativo, buscala e instalala. Si quieres instalarla manualmente puedes descargarla desde [aqui](https://code.visualstudio.com/downloads/).


## Extensiones en Visual Studio Code

Sera necesario que en Visual Studio Code, instalemos las siguientes extensiones para mayor comodidad en la programación. Las extensiones a instalar son:

- sdkcpc-amstrad-basic-language
- sdkcpc-amstrad-basic-snippet
- sdkcpc-amstrad-ugbasic-language
- ms-vscode.live-server

### Como instalar extensiones

Si no sabes como instalar extensiones, puedes ver el siguiente [video](https://www.youtube.com/watch?app=desktop&v=kY02vXiIkqE/) donde se explica de manera muy sencilla como hacerlo.

