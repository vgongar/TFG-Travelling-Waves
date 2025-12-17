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
<div align="center">
  <img width="1.29*300" height="300" alt="model-sketch" src="https://github.com/user-attachments/assets/b67851c4-ea59-4d44-a6bd-eff265779970" />
</div>

Este trabajo aborda lo que se conoce en la literatura como el __problema directo__: ¿pueden propiedades sobre el perfil del fondo del recipiente transferirse a las ondas viajeras en la superficie?

Para encontrar respuestas sobre este problema nos adentraremos en la __teoría de Floquet__ para ecuaciones lineales con coeficientes periódicos, la __ecuación de Hill__ y usaremos trabajos científicos de investigación en la actualidad.
  
## Resumen

Para entender el problema se dispone de una primera sección sobre la __teoría de Floquet__ (matriz de monodromía, Teorema de Floquet, análisis de estabilidad, etc.) y su aplicación a la __ecuación de Hill__: $(py)'+qy=0$, donde $p,q$ son funciones del mismo periodo. 

En la segunda sección se introduce el concepto de onda viajera, que en forma compleja adopta la forma: $\eta(t,x)=A(x)\exp(i(\omega t-\psi(x))$. Posteriormente, se encuentran condiciones necesarias y suficientes que deben cumplir los coeficientes de la onda para que esta se encuentre como solución del modelo y se demuestra lo que se denomina en el trabajo como el __teorema de Zhang__. Viene a responder de forma parcial a nuestra pregunta: bajo ciertas hipótesis, un perfil periódico genera ondas viajeras de amplitud periódica en la superficie. 

El teorema de Zhang demuestra la existencia de una onda viajera periódica dadas ciertas condiciones, pero no dice como encontrarla. La última sección del trabajo consiste en la implementación de un __algoritmo numérico en Python__, basado en los puntos fijos de la aplicación de Poincaré, para calcularla, visualizando la dinámica de las ondas y validando los resultados teóricos. La __aplicación de Poincaré__ es una aplicación que dadas unas condiciones iniciales, $X_0$, y un instante de tiempo, $t$, evalúa la única solución del PVI correspondiente a tiempo $t$. Cuando la ecuación es autónoma, como la que encontramos en el trabajo asociada a la amplitud de onda, encontrar una solución periódica equivale a encontrar un punto fijo de la aplicación de Poincaré.

## Instalación

1. Descargar el repositorio.
2. Cada programa de la carpeta `src` está configurado con los parámetros correctos. Si quiere cambiarlos porque esté buscando
otra solución siga las instrucciones de la última sección del TFG en /docs/"Ondas viajeras en ecuaciones de ondas inhomogéneas.pdf".
3. Instalar librerías usando `pip install -r requirements.txt`.
4. Ejecutar y visualizar!.

## Descarga del TFG
Puedes leer la memoria completa [haciendo clic aquí](./docs/Ondas%20viajeras%20en%20ecuaciones%20de%20ondas%20inhomogéneas.pdf). También están disponibles las [transparencias](docs/Presentacion_TFG.pdf) usadas el día de la defensa. 

## Licencia y Derechos de Uso

Este repositorio utiliza un esquema de **licencia dual** para proteger los diferentes tipos de contenido:

### Código Fuente (`/src`)
Todo el código fuente desarrollado para este proyecto (archivos `.py`, scripts, algoritmos) se encuentra bajo la **Licencia MIT**.
> Eres libre de usar, modificar y distribuir el código, siempre que se mantenga la atribución al autor original. Consulta el archivo `LICENSE` para más detalles.

### Memoria del TFG (`/docs`)
El documento de texto de la memoria ("Ondas viajeras en ecuaciones...") está protegido bajo una licencia **Creative Commons Atribución-NoComercial-SinDerivadas 4.0 Internacional (CC BY-NC-ND 4.0)**.
> Puedes descargar y leer el documento libremente. Sin embargo, **no está permitido** modificar el texto, usarlo con fines comerciales ni distribuirlo sin atribuir la autoría original.

# 🇬🇧 Travelling waves in inhomogeneous wave equations

- __Víctor González García__
- __Universidad de Granada__
- BSc in Mathematics

- ## Motivation
The __Shallow Waters__ model is a set of partial differential equations (PDE) which describe the motion of a fluid when the container is shallow.

$$
\begin{align}
  \frac{\partial \eta}{\partial t}+\frac{\partial}{\partial x}[h(x)u]&=0 \\
  \frac{\partial u}{\partial t}+g\frac{\partial \eta}{\partial x}&=0
\end{align}
$$
<div align="center">
  <img width="1.29*300" height="300" alt="model-sketch" src="https://github.com/user-attachments/assets/b67851c4-ea59-4d44-a6bd-eff265779970" />
</div>

The thesis tackles what is known in the literature as the \textit{direct problem}: can properties about the bottom profile of the container transfer to travelling waves in the surface?

To find answers about this, we will delve into __Floquet Theory__ for periodic linear differential equations, __Hill's Equation__ and review recent research papers.
  
## Abstract

For understanding the problem, the first section of the work consists of an introduction to __Floquet Theory__ (monodormy matrix, Floquet's Theorem, stability analysis, etc.) and its application to __Hill's Equation__: $(py)'+qy=0$, where $p,q$ are functions with the same period.  

In the second section we introduce the concept of __travelling wave__, which, in complex notation, takes the form: $\eta(t,x)=A(x)\exp(i(\omega t-\psi(x))$. Subsequently, we derive sufficient and necessary conditions the wave's coefficient must satisfy to be a solution and we prove what we denominate __Zhang's theorem__. It provides a partial affirmative answer to our question: under certain extra hypotheses, a periodic profile generates travelling waves with periodic amplitude on the surface.

While Zhang's theorem proves the existence of a periodic travelling wave, given certain conditions, it doesn't give a constructive method to find it. The last section of the thesis consists of implementation of a __numerical algorithm in Python__ from scratch, based on fixed points of the __Poincaré application__, to compute these waves, visualizing wave dynamics and validating theoretical results. The __Poincaré map__ is defined as a function that given certain initial conditions, $X_0$ and an instant $t$, evaluates the unique solution corresponding with the Initial Value Problem (IVP) at time $t$. For autonomous equations, such as the one we derived for wave amplitude, finding a periodic solution is equivalent to computing a fixed point of the __Poincaré map.

## Abstract
 The thesis tackles what is known in the literature as the \textit{direct problem}: do properties about the profile of the bottom of the container transfer to travelling waves in the surface? A solution to this question is given by Zhang which is called in the thesis as the __Zhang theorem__ and it is partially affirmative: under certain assumptions a periodic profile generates periodic travelling waves on its surface. The last part of the work is an implementation of a __numerical algorithm in Python__ to calculate this periodic solution the theorem states, visualizing wave dynamics and validating theoretical results.


## Installation
1. Download the repository.
2. Each program in `src` folder is already configured with some parameters. If you desire to change them because you want another periodic solution follow the instructions on the thesis' last section in /docs/"Ondas viajeras en ecuaciones de ondas inhomogéneas.pdf" (It is in Spanish).
3. Install libraries using `pip install -r requirements.txt`
4. Run and visualize!

## Donwload thesis
You can read the thesis [clicking here](./docs/Ondas%20viajeras%20en%20ecuaciones%20de%20ondas%20inhomogéneas.pdf). [Slides](docs/Presentacion_TFG.pdf) used at defense day are also available. (Both in Spanish)

## License and Usage Rights

This repository uses a **dual licensing** scheme to protect different types of content:

### Source Code (`/src`)
All source code developed for this project (`.py` files, scripts, algorithms) is licensed under the **MIT License**.
> You are free to use, modify, and distribute the code, provided that attribution to the original author is maintained. See the `LICENSE` file for more details.

### Thesis Document (`/docs`)
The thesis document ("Ondas viajeras en ecuaciones...") is protected under a **Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)** license.
> You may freely download and read the document. However, you are **not permitted** to modify the text, use it for commercial purposes, or distribute it without attributing the original authorship.
