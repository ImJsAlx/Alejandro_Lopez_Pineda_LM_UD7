# Proyecto de Conversión y Visualización de Datos - Vehículos y Motos de Alta Gama

Este repositorio contiene una práctica de **conversión y visualización de datos** utilizando **JSON, XML, Python, XSLT, HTML, CSS y JavaScript**. El proyecto tiene como temática **vehículos y motos de alta gama**, mostrando un conjunto de datos estructurados que se transforman y visualizan de varias formas.

---

## Objetivos del Proyecto

- Aprender a trabajar con formatos de datos estructurados (**JSON y XML**).  
- Convertir datos entre JSON y XML utilizando **Python**.  
- Transformar XML a **HTML** mediante **XSLT**.  
- Visualizar datos de manera dinámica en el navegador usando **JavaScript** y **CSS**.  
- Presentar los datos de forma clara y atractiva para el usuario.

---

## Temática

- **Coches de alta gama:** 37 vehículos de marcas como Tesla, Ferrari, Lamborghini, McLaren, Koenigsegg, Aston Martin, entre otros.  
- **Motos de alta gama:** 14 motocicletas de marcas como Ducati, Kawasaki, BMW, Yamaha, Honda, MV Agusta, Aprilia, KTM y más.

---

## Estructura del Repositorio

Alejandro_Lopez_Pineda_LM_UD7/
│
├─ datos/
│ ├─ datos.json # Archivo original en JSON
│ ├─ datos.xml # Archivo original en XML
│ └─ conversion.py # Script de Python para convertir entre JSON y XML
│
├─ xslt/
│ ├─ plantilla.xslt # Hoja de estilos XSLT para generar HTML
│ ├─ transformar.py # Script Python para aplicar la transformación XSLT
│ └─ salida.html # HTML generado a partir de XML
│
├─ js/
│ ├─ index.html # Página HTML para mostrar datos dinámicos
│ ├─ app.js # Script JavaScript para cargar JSON
│ ├─ styles.css # Hoja de estilos CSS para la visualización
│ └─ datos.json # Copia del JSON para uso en JS
│
└─ README.md 


---

## Tecnologías Utilizadas

- **Python 3**: Para conversión de JSON ↔ XML y aplicación de XSLT.  
- **xmltodict & lxml**: Librerías Python para manipulación de XML.  
- **XSLT**: Transformación de XML a HTML.  
- **HTML, CSS, JavaScript**: Visualización dinámica y estilizada de los datos.  

---

## Uso del Proyecto

### 1. Configuración del entorno

```powershell
# Crear entorno virtual
python -m venv venv

# Activar entorno en Windows
.\venv\Scripts\activate

# Instalar librerías necesarias
pip install xmltodict lxml

# Ejecutar script para convertir datos
python datos\conversion.py

# Ejecutar transformación XSLT
python xslt\transformar.py

Esto genera xslt/salida.html con la visualización de los coches y motos.

Abrir js/index.html en un navegador moderno.
Se mostrará una cuadrícula de tarjetas con coches y motos de alta gama, cargando los datos desde js/datos.json.

Este repositorio fue desarrollado como práctica de conversión y visualización de datos para la unidad didáctica 7.
- Alejandro López Pineda
