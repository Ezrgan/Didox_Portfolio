# Guía de Despliegue en PythonAnywhere (SQLite)

Esta guía asume que crearás una **Cuenta Nueva** en PythonAnywhere para evitar el límite de 1 app web.

## Paso 0: Crear Cuenta Nueva
1. Ve a [pythonanywhere.com](https://www.pythonanywhere.com).
2. Regístrate con un **correo diferente** al que usas en tu otra cuenta.
3. Elige el plan "Beginner" (Gratis).

---

## Paso 1: Configuración Inicial (Consola Bash)
1. Ve a la pestaña **Consoles** y abre una **Bash** console.
2. Clona tu repositorio:
   ```bash
   git clone https://github.com/Ezrgan/Didox_Portfolio.git
   ```
3. Entra en la carpeta:
   ```bash
   cd Didox_Portfolio
   ```

---

## Paso 2: Crear Entorno Virtual
Ejecuta estos comandos uno por uno en la consola:

1. Crear el entorno:
   ```bash
   python3 -m venv myenv
   ```
2. Activarlo:
   ```bash
   source myenv/bin/activate
   ```
3. Si no coinciden, es más fácil borrar el entorno (`rm -rf myenv`) y crearlo de nuevo especificando la versión: `python3.12 -m venv myenv` (o la versión que tengas seleccionada en la Web).
4. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

---

## Paso 3: Base de Datos y Superusuario
1. Migrar la base de datos (creará `db.sqlite3`):
   ```bash
   python manage.py migrate
   ```
2. Recolectar estáticos:
   ```bash
   python manage.py collectstatic
   ```
   *(Escribe `yes` si pregunta).*
3. Crear usuario administrador:
   ```bash
   python manage.py createsuperuser
   ```

---

## Paso 4: Configurar la Web App
1. Ve a la pestaña **Web** -> **Add a new web app**.
2. Dale **Next** -> Selecciona **Manual configuration** (¡NO Django automático!) -> Selecciona **Python 3.12** (o la versión que uses).
3. **Virtualenv**:
   - Busca la sección "Virtualenv".
   - Escribe la ruta: `/home/TU_USUARIO/Didox_Portfolio/myenv`
   *(Reemplaza `TU_USUARIO` por tu usuario real).*

### Configurar Rutas del Código (Code)
Justo encima de la sección WSGI, verás dos campos importantes. Llénalos así:

- **Source code**: `/home/TU_USUARIO/Didox_Portfolio`
- **Working directory**: `/home/TU_USUARIO/Didox_Portfolio`

*(Esto le dice a PythonAnywhere dónde está tu `manage.py`)*.

---

## Paso 5: Configurar Código (WSGI)
1. En la sección **Code**, haz clic en el archivo **WSGI configuration file** (el enlace que termina en `_wsgi.py`).
2. **BORRA TODO** su contenido y pega esto:

```python
import os
import sys

# RUTA A TU PROYECTO (Cambia TU_USUARIO)
path = '/home/TU_USUARIO/Didox_Portfolio'
if path not in sys.path:
    sys.path.append(path)

# VARIABLES DE ENTORNO
os.environ['DJANGO_SETTINGS_MODULE'] = 'portfolio_didox.settings'
os.environ['SECRET_KEY'] = 'pon-aqui-una-clave-larga-y-aleatoria-hazme-caso' 
os.environ['DEBUG'] = 'False'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```
*(Importante: Asegúrate de reemplazar `TU_USUARIO` en la variable `path` por tu nombre de usuario exacto de PythonAnywhere).*
3. Dale a **Save** (arriba a la derecha).

---

## Paso 6: Archivos Estáticos
Vuelve a la pestaña **Web** y baja a la sección **Static files**. Añade estas dos filas:

(Debes escribir la URL a la izquierda y el directorio a la derecha)

| URL | Directory |
|-----|-----------|
| `/static/` | `/home/TU_USUARIO/Didox_Portfolio/staticfiles` |
| `/media/` | `/home/TU_USUARIO/Didox_Portfolio/media` |

*(Recuerda reemplazar `TU_USUARIO` por tu usuario real).*

---

## Paso 7: ¡Lanzar!
1. Sube arriba del todo en la pestaña **Web**.
2. Dale al botón verde **Reload**.
3. Abre tu enlace (`tu-usuario.pythonanywhere.com`).
