# Rocódromo Puente de Roca -- Django

Proyecto de una web para un rocódromo real en Toledo, desarrollada con **Django
(backend + frontend)** y desplegada en **Render**.

El objetivo es tener una base realista y publicable, pensada para
producción, sobre la que ir añadiendo funcionalidades.

------------------------------------------------------------------------

## 🧱 Stack

-   Python 3
-   Django
-   Django Templates (frontend)
-   Whitenoise (static files)
-   Gunicorn (producción)
-   Render (hosting)

------------------------------------------------------------------------

## 📦 Instalación en local (Windows)

### 1️⃣ Clonar el repositorio

``` bash
git clone https://github.com/mororko/rocodromo.git
cd rocodromo
```

### 2️⃣ Crear entorno virtual

``` powershell
python -m venv .venv
```

Activar el entorno virtual:

``` powershell
.\.venv\Scripts\Activate.ps1
```

Debe aparecer `(.venv)` en la terminal.

------------------------------------------------------------------------

### 3️⃣ Instalar dependencias

``` powershell
pip install -r requirements.txt
```

------------------------------------------------------------------------

### 4️⃣ Variables de entorno (local)

En **Windows (PowerShell)**:

``` powershell
$env:DJANGO_DEBUG="True"
$env:DJANGO_ALLOWED_HOSTS="127.0.0.1,localhost"
$env:DJANGO_SECRET_KEY="dev-secret-key"
```

> En producción estas variables se configuran en Render.

------------------------------------------------------------------------

### 5️⃣ Migraciones y usuario admin

``` powershell
python manage.py migrate
python manage.py createsuperuser
```

------------------------------------------------------------------------

### 6️⃣ Lanzar el servidor en local

``` powershell
python manage.py runserver
```

Abrir en el navegador: - Web: http://127.0.0.1:8000/ - Admin:
http://127.0.0.1:8000/admin/

------------------------------------------------------------------------

## 📱 Responsive

La web es responsive: - Desktop y tablet: menú horizontal - Móvil: menú
burger que **empuja el contenido** (no se superpone)

El CSS está en:

    core/static/core/styles.css

------------------------------------------------------------------------

## 🚀 Despliegue en Render

### Variables de entorno en Render

Configurar en el Web Service:

  Variable                      Valor
  ----------------------------- -------------------------------------
  DJANGO_DEBUG                  False
  DJANGO_SECRET_KEY             (clave segura)
  DJANGO_ALLOWED_HOSTS          rocodromo-jhn0.onrender.com
  DJANGO_CSRF_TRUSTED_ORIGINS   https://rocodromo-jhn0.onrender.com

------------------------------------------------------------------------

### Build y Start Command (IMPORTANTE)

En Render → Settings:

**Build Command**

``` bash
pip install -r requirements.txt && python manage.py collectstatic --noinput --clear
```

**Start Command**

``` bash
gunicorn config.wsgi:application
```

> ⚠️ El flag `--clear` es clave para evitar problemas de CSS antiguo en
> producción.

------------------------------------------------------------------------

## 🧯 Problema conocido: CSS no se actualizaba en Render

### Síntoma

-   En local el CSS se veía bien
-   En Render se seguía viendo el CSS antiguo

### Solución

-   Forzar `collectstatic --clear`
-   Evitar `build.sh` (usado anteriormente pero da problema de momento)
-   Verificar `/static/core/styles.css` directamente en el navegador

------------------------------------------------------------------------

## 📂 Estructura principal

    config/        # settings, urls, wsgi
    core/          # páginas públicas
    static/        # CSS
    templates/     # HTML templates

------------------------------------------------------------------------

## 🛣️ Próximos pasos (pendientes)

-   [ ] Formulario de contacto real
-   [ ] Contenido editable desde admin (horarios, precios)
-   [ ] SEO básico
-   [ ] Sistema de reservas (pospuesto)
-   [ ] Dominio propio

------------------------------------------------------------------------

## 📝 Notas

-   El módulo de reservas está planteado pero **no implementado
    todavía**
-   El proyecto está pensado para crecer sin rehacer la base
