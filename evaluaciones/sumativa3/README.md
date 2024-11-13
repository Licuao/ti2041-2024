Crear Modelos que permitan la gestión de los datos de una aplicación Django.
Crear Plantillas para la interacción con el usuario y el despliegue de información que viene desde los modelos.
Crear Vistas para mantener la lógica de negocio de la aplicación, permitiendo la realización de las funciones básicas para operar con cada uno de los modelos creados (crear, actualizar, eliminar y listar elementos de los modelos).
Objetivos de la Evaluación
Evaluar la habilidad de los estudiantes en estructura un modelo de datos dentro de una aplicación Django.
Comprobar el uso adecuado de formularios, tablas de datos y manipulación de datos con los modelos creados.
Valorar la capacidad de los estudiantes para aplicar estilos CSS y templates en Django para la presentación visual.
Descripción del Problema
Luego de confeccionar el prototipo para los datos de "Gestión de Productos S.A.", ahora se desea construir una aplicación que utilice elementos reutilizables de Django, como es el administrador del proyecto y el uso de vistas que sean adecuadas para una funcionalidad. Es por eso que se le solicitan las siguientes características para la aplicación: 

Crear los modelos necesarios que le permitan administrar los productos, considerando que: 
El producto tiene código, nombre, y precio.
El  producto tiene un conjunto de características (tamaño, peso, etc).
El producto puede tener una categoría.
El producto debe tener una marca (y que se puede repetir entre productos).
Permitir que toda la administración de Categorías, Marcas y Características (solo los tipos) sean parte del administrador de Django.
Crear la parte de administración de productos y características a través de formularios y vistas en la misma aplicación (no utilizar a través del administrador de Django).
Crear una pantalla de despliegue general de productos, que permita la aplicación de filtros por diferentes parámetros, como marca, característica y categoría.
Incorporar estilos CSS para mejorar la presentación visual de las pantallas.
Instrucciones para la Actividad
Creación del Proyecto
Crea un nuevo proyecto de Django y una aplicación llamada productos, o utiliza la que ya creó para la primera evaluación.
Configura los archivos necesarios (settings.py, urls.py) para asegurar que la aplicación funcione correctamente en un entorno local.
Crear una cuenta de administrador "admin", con una contraseña "inacap2024" para poder acceder al administrador de Django.
Creación de Modelos
Crear un modelo para Producto.

Crear modelos relacionados de Marca, Categoría y Característica.

Implementación de Pantallas
Pantalla de Lista de Productos, donde se presente la lista de productos existentes en el modelo (index.html).
Pantalla con Formulario para la creación de un producto (regiter.html).
Pantalla para el Resultado de la creación del producto (result.html).
Procesamiento de Formularios
Implementa vistas en Django que manejen el envío de formularios utilizando el método POST.
Valida los datos ingresados (asegurando que los campos estén completos y el correo tenga el formato correcto).
Almacena en el modelo correspondiente los datos procesados.
Aplicación de Estilos
Utiliza archivos CSS para estilizar las pantallas de la aplicación, asegurando una presentación coherente y profesional.
Entrega
El proyecto debe entregarse en el repositorio Git creado para el curso, dentro de la carpeta "evaluaciones/sumativa2".
La carpeta debe tener un archivo README.md con instrucciones claras sobre cómo instalar y ejecutar la aplicación.
En la entrega, usted debe especificar: 
Nombre de Usuario GitHub
Número de Commit
Se descontarán puntos si no se cumple con esta condición.
Plazo de Entrega: Domingo 21 de octubre, 23:59 horas.