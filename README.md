# coin-counter

Práctica para Inteligencia Artifical - S9B

Correr el siguiente comando para instalar requerimientos

    pip install -r requirements.txt
 
O para instalar los paquetes de forma global

    python -m pip install -r requirements.txt
    
Ejecutar
------------
Analizar imagen con
    py practica.py

Analizar video (desde webcam) con
    py tiempo_real.py
    
Las imagenes se encuentran en /images. Se pueden reemplazar por otras pero puede que se requiera modificar los parametros de ***cv.HoughCircles*** y el límite para diferenciar entre monedas de $1 y $10
    
