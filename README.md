# 🇪🇸 Ondas viajeras en ecuaciones de ondas inhomogéneas 

- __Víctor González García__
- __Universidad de Granada__
- Grado en Matemáticas

## Motivación
El modelo de __Shallow Waters__ (Aguas poco profundas) es un conjunto de ecuaciones en derivadas parciales (EDP) que describen el movimiento de un fluido cuando el recipiente que lo contiene es poco profundo.

$$
\begin{align}
  \frac{\partial \eta}{\partial t}+\frac{\partial}{\partial x}[h(x)u]&=0 \\
  \frac{\partial u}{\partial t}+g\frac{\partial \eta}{\partial x}&=0
\end{align}
$$

<img width="1.3132*200" height="200" alt="model-sketch" src="https://github.com/user-attachments/assets/6b2c3d6f-d85b-4ea7-9285-9cf9af79e102" />
  

## Resumen
El modelo de __Shallow Waters__ (Aguas poco profundas) es un conjunto de ecuaciones en derivadas parciales (EDP) que describen el movimiento de un fluido cuando el recipiente que lo contiene es poco profundo. Este trabajo aborda lo que se conoce en la literatura como el _problema directo_: ¿se transfieren las propiedades sobre el perfil del fondo del recipiente a las ondas viajeras en la superficie? Zhang ofrece una respuesta a esta pregunta, denominada en el trabajo como el __teorema de Zhang__, y es parcialmente afirmativa: bajo ciertas hipótesis, un perfil periódico genera ondas viajeras periódicas en su superficie. La última parte del trabajo consiste en la implementación de un __algoritmo numérico en Python__ para calcular esta solución periódica que establece el teorema, visualizando la dinámica de las ondas y validando los resultados teóricos.

## Instalación

1. Descargar el repositorio.
2. Cada programa de la carpeta `src` está configurado con los parámetros correctos. Si quiere cambiarlos porque esté buscando
otra solución siga las instrucciones de la última sección del TFG en /docs/"Ondas viajeras en ecuaciones de ondas inhomogéneas.pdf".
3. Instalar librerías usando `pip install -r requirements.txt`.
4. Ejecutar y visualizar!.

## 📥 Descarga del TFG
Puedes leer la memoria completa [haciendo clic aquí](./docs/Ondas%20viajeras%20en%20ecuaciones%20de%20ondas%20inhomogéneas.pdf). También están disponibles las [transparencias](docs/Presentacion_TFG.pdf) usadas el día de la defensa. 

## ⚖️ Licencia y Derechos de Uso

Este repositorio utiliza un esquema de **licencia dual** para proteger los diferentes tipos de contenido:

### 💻 Código Fuente (`/src`)
Todo el código fuente desarrollado para este proyecto (archivos `.py`, scripts, algoritmos) se encuentra bajo la **Licencia MIT**.
> Eres libre de usar, modificar y distribuir el código, siempre que se mantenga la atribución al autor original. Consulta el archivo `LICENSE` para más detalles.

### 📄 Memoria del TFG (`/docs`)
El documento de texto de la memoria ("Ondas viajeras en ecuaciones...") está protegido bajo una licencia **Creative Commons Atribución-NoComercial-SinDerivadas 4.0 Internacional (CC BY-NC-ND 4.0)**.
> Puedes descargar y leer el documento libremente. Sin embargo, **no está permitido** modificar el texto, usarlo con fines comerciales ni distribuirlo sin atribuir la autoría original.

# 🇬🇧 Travelling waves in inhomogeneous wave equations

- __Víctor González García__
- __Universidad de Granada__
- BSc in Mathematics

## Abstract
The __Shallow Waters__ model is a set of partial differential equations (PDE) which describe the motion of a fluid when the container in which the fluid is in is shallow. The thesis tackles what is known in the literature as the \textit{direct problem}: do properties about the profile of the bottom of the container transfer to travelling waves in the surface? A solution to this question is given by Zhang which is called in the thesis as the __Zhang theorem__ and it is partially affirmative: under certain assumptions a periodic profile generates periodic travelling waves on its surface. The last part of the work is an implementation of a __numerical algorithm in Python__ to calculate this periodic solution the theorem states, visualizing wave dynamics and validating theoretical results.


## Installation
1. Download the repository.
2. Each program in `src` folder is already configured with some parameters. If you desire to change them because you want another periodic solution follow the instructions on the thesis' last section in /docs/"Ondas viajeras en ecuaciones de ondas inhomogéneas.pdf" (It is in Spanish).
3. Install libraries using `pip install -r requirements.txt`
4. Run and visualize!

## 📥 Donwload thesis
You can read the thesis [clicking here](./docs/Ondas%20viajeras%20en%20ecuaciones%20de%20ondas%20inhomogéneas.pdf). [Slides](docs/Presentacion_TFG.pdf) used at defense day are also available. (Both in Spanish)

## ⚖️ License and Usage Rights

This repository uses a **dual licensing** scheme to protect different types of content:

### 💻 Source Code (`/src`)
All source code developed for this project (`.py` files, scripts, algorithms) is licensed under the **MIT License**.
> You are free to use, modify, and distribute the code, provided that attribution to the original author is maintained. See the `LICENSE` file for more details.

### 📄 Thesis Document (`/docs`)
The thesis document ("Ondas viajeras en ecuaciones...") is protected under a **Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)** license.
> You may freely download and read the document. However, you are **not permitted** to modify the text, use it for commercial purposes, or distribute it without attributing the original authorship.
