# Guía de Despliegue en Render para Portfolio Didox

Sigue estos pasos para poner tu proyecto en producción utilizando Render.com.

## Paso 1: Crear la Base de Datos (PostgreSQL)
Como `db.sqlite3` se borra cada vez que Render reinicia (porque el sistema de archivos es efímero), necesitas una base de datos real.

1. En tu Dashboard de Render, haz clic en **New +** y selecciona **PostgreSQL**.
2. Nombre: `portfolio-db` (o lo que quieras).
3. Región: Elige la misma que usarás para tu Web Service (ej. Ohio o Frankfurt).
4. Plan: Select **Free** (si está disponible) o el plan más barato.
5. Haz clic en **Create Database**.
6. Una vez creada, busca la sección **Internal Database URL** y copia el valor. Se verá como: `postgres://user:password@hostname/dbname`.

## Paso 2: Crear el Web Service
1. Ve al Dashboard y haz clic en **New +** y selecciona **Web Service**.
2. Conecta tu cuenta de GitHub y selecciona el repositorio: `Didox_Portfolio`.
3. Configura los siguientes campos:
   - **Name**: `portfolio-didox`
   - **Region**: La misma que tu base de datos.
   - **Branch**: `main`
   - **Runtime**: `Python 3`
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn portfolio_didox.wsgi`

## Paso 3: Configurar Variables de Entorno
Antes de darle a "Create", baja a la sección **Environment Variables** y añade las siguientes:

| Key | Value | Descripción |
|-----|-------|-------------|
| `DATABASE_URL` | *(Pegar URL Paso 1)* | La conexión a tu base de datos PostgreSQL. |
| `SECRET_KEY` | *(Inventa una larga)* | Ej: `super-secreto-aleatorio-123456...` |
| `DEBUG` | `False` | Para modo producción seguro. |
| `PYTHON_VERSION` | `3.12.0` | Para asegurar que usa la misma versión que tú. |

## Paso 4: Finalizar
1. Haz clic en **Create Web Service**.
2. Render comenzará a construir tu proyecto. Verás los logs.
   - Ejecutará `pip install`.
   - Ejecutará `collectstatic`.
   - Ejecutará `migrate`.
3. Si todo sale bien, verás un mensaje de "Live" y una URL (ej. `https://portfolio-didox.onrender.com`).

## Solución de Problemas Comunes
- **Error en build.sh**: Si dice `permission denied`, Render suele arreglarlo solo, pero asegúrate de que el archivo tenga permisos de ejecución (ya suele tenerlos en git).
- **CSS no carga**: Verifica que `Whitenose` está activo en `settings.py` (ya lo configuramos).
