# Portfolio Simple en Django

## Autor

Desarrollado por Rafael Deacon(https://github.com/Rafa2626).
Este proyecto se presenta como una solución elegante y eficiente para aquellos que buscan exhibir sus trabajos o proyectos de manera profesional y concisa. Desarrollado utilizando el poderoso framework de Django, junto con un conjunto de tecnologías complementarias como HTML, CSS, Bootstrap, y un toque de JavaScript, este portfolio asegura una experiencia de usuario fluida y una interfaz amigable.

## Características Principales

- **Gestión de Proyectos:** Permite a los usuarios añadir, editar y eliminar proyectos de forma intuitiva a través de paneles de administración. Esto facilita la actualización constante del portfolio sin requerir conocimientos avanzados de programación.
- **Edición de Perfil de Usuario:** Los usuarios registrados pueden editar la información de su cuenta, proporcionando así un nivel de personalización que mejora la experiencia de usuario.
- **Registro de Usuarios:** El sistema incluye una funcionalidad para registrar nuevos usuarios, ampliando la interacción dentro del sitio y permitiendo una gestión detallada de accesos y permisos.
- **Sección de Contacto Inteligente:** Con solo presionar un botón, los visitantes pueden copiar la dirección de email del propietario del portfolio, facilitando un primer contacto rápido y eficiente.
- **Responsive Design:** Gracias al uso de Bootstrap, el diseño es totalmente responsive, asegurando que el portfolio se vea bien en cualquier dispositivo, desde smartphones hasta desktops.

## Tecnologías y Lenguajes Utilizados

- **Backend:** Django (Python), proporcionando una base sólida y escalable para el desarrollo del proyecto.
- **Frontend:** HTML, CSS, y JavaScript, para una interfaz de usuario dinámica y estéticamente agradable.
- **Estilización:** Bootstrap, para garantizar un diseño responsivo y moderno.
- **Base de Datos:** SQLite3, ofreciendo un sistema de gestión de base de datos ligero y eficaz para proyectos de esta envergadura.


## Cómo Empezar

Para ejecutar este proyecto en tu máquina local, sigue estos pasos:

1. **Clona este repositorio**
   ```bash
   git clone https://github.com/Rafa2626/django-porfolio-simple.github.io
   ```

2. **Crea un entorno virtual**
   ```bash
   python -m venv entornoVi
   ```

3. **Activa el entorno virtual**
   - En Windows:
     ```bash
     entornoVi\Scripts\activate
     ```
   - En Mac/Linux:
     ```bash
     source entornoVi/bin/activate
     ```

4. **Instala las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

5. **Realiza las migraciones**
   ```bash
   python manage.py migrate
   ```

6. **Crea un superusuario**
   ```bash
   python manage.py createsuperuser
   ```

7. **Ejecuta el servidor de desarrollo**
   ```bash
   python manage.py runserver
   ```

8. **Visita http://127.0.0.1:8000/ en tu navegador para ver el proyecto.**


Este portfolio no solo destaca por su funcionalidad y facilidad de uso, sino también por su enfoque en la accesibilidad y la interactividad, haciendo que sea una excelente elección para profesionales y creativos que deseen presentar sus trabajos al mundo de manera eficaz y moderna.
