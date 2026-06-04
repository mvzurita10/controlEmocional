<div align="center">

<img src="https://ute.edu.ec/wp-content/uploads/2021/08/LogoUteTrans.png" alt="UTE - Escuela de Tecnologías" width="250"/>

</div>

<hr>
<br>

<div style="border-left: 4px solid #1e88e5; padding-left: 15px; margin-top: 20px;">

<p><strong>Universidad Tecnológica Equinoccial</strong></p>

<p><strong>Escuela de Tecnologías</strong></p>

<p><strong>Carrera:</strong> Desarrollo de Software</p>

<p><strong>Asignatura:</strong> Programación IV</p>

</div>

<br><br>

<p><strong>Tema:</strong> SEMINARIO DE INTEGRACIÓN - Construcción de Backend Django.</p>

<br>

<p><strong>Fecha:</strong> 03/06/2026</p>

<p><strong>Presentado por:</strong></p>

<ul>
  <li>Zurita Mikaela</li>
</ul>

<p><strong>Docente:</strong> Francisco Javier Higuera González </p>

<hr>

# Control Emocional - API (TherAppy)

TherAppy (Control-Emocional) es una API REST desarrollada con Django REST Framework que proporciona servicios para la gestión integral de la salud emocional. Permite administrar usuarios, psicólogos, citas, historiales clínicos, registros de emociones, perfiles psicológicos, recomendaciones personalizadas y sistemas de mensajería, facilitando la comunicación entre pacientes y profesionales de la salud mental.

## Instalación y Ejecución del Backend

Sigue estos pasos para levantar el entorno de desarrollo en tu máquina local:

1. **Clonar el repositorio:**
   ```bash
   https://github.com/mvzurita10/controlEmocional.git
   cd controlEmocional
   ```

2. **Crear y configurar postgres:**

    En Windows: abrir pgAdmin o usar la consola psql desde el menú de inicio

   ```bash
    CREATE USER therappy_user WITH PASSWORD 'therappy_pass';
    CREATE DATABASE therappy_db OWNER therappy_user;
    GRANT ALL PRIVILEGES ON DATABASE therappy_db TO therappy_user;
    ALTER USER therappy_user CREATEDB;
   \q
   ```

3. **Crear y activar un entorno virtual:**
   ```bash
   # En Windows:
   python -m venv .venv
   .venv\Scripts\activate
   ```

4. **Instalar dependencias:**
   ```bash
   uv pip install -r requirements.txt
   ```
   

5. **Configurar las variables de entorno:**
   `.env`
   ```bash
   # Django
    SECRET_KEY=django-insecure-change-this-in-production
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1

    # PostgreSQL
    DB_NAME=therappy_db
    DB_USER=therappy_user
    DB_PASSWORD=therappy_pass
    DB_HOST=localhost
    DB_PORT=5432

    # CORS
    CORS_ALLOW_ALL_ORIGINS=True

    # Test database (Django la crea automáticamente)
    TEST_DB_NAME=therappy_test_db
   ```

6. **Aplicar migraciones:**
   ```bash
    python manage.py makemigrations 
    python manage.py migrate
   ```

7. **Crear superusuario (opcional pero recomendado):**
   ```bash
   python manage.py createsuperuser
   ```
    Username: admin |
    Email address: admin@therappy.com |
    Password: Admin1234! 

8. **Ejecutar el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```
   La API estará disponible en `http://localhost:8000`.

---

## Ejemplos de uso de la API (con Token)

El sistema utiliza **JSON Web Tokens (JWT)** para la autenticación. 

## 1. Obtener el Token (Login)

Para poder acceder a las rutas protegidas, primero necesitas iniciar sesión para obtener tu `access_token`.

1. Abre Postman y crea una nueva petición.
2. Cambia el método a **POST**.
3. Ingresa la URL de login: `http://localhost:8000/api/auth/login/`.
4. Ve a la pestaña **Body**, selecciona **raw** y luego **JSON** en el menú desplegable.
5. Ingresa tus credenciales en el cuerpo de la petición:
   ```json
   {
       "username": "tu_usuario",
       "password": "tu_password"
   }
   ```
6. Haz clic en **Send**.

**Respuesta Exitosa esperada:**
```json
{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6Ik...",
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6Ik...",
    "user_id": 1,
    "username": "tu_usuario",
    "email": "correo@ejemplo.com",
    "is_staff": false
}
```
*Copia el valor que aparece en `"access"`, ese es tu Token JWT.*

## 2. Usar el Token en Endpoints Protegidos

Una vez que tienes tu token de acceso (`access`), debes incluirlo en las peticiones hacia endpoints que requieran estar logueado (por ejemplo, listar usuarios o ver el perfil).

### Usar la pestaña "Authorization" 
1. Crea o selecciona la petición hacia un endpoint protegido.
2. Ve a la pestaña **Authorization** (justo debajo de la barra donde pones la URL en Postman).
3. En el menú desplegable **Type**, selecciona **Bearer Token**.
4. En el campo **Token** que aparece a la derecha, **pega tu token de acceso** (sin comillas).
5. Haz clic en **Send**.

**Ejemplo de Petición (Crear Psicólogo):**
- **Método:** `POST`
- **URL:** `http://localhost:8000/api/psicologos/`
- **Token en Postman (Bearer Token):** `eyJhbGciOiJIUzI1NiIsInR5cCI6Ik...`
- **Body (raw -> JSON):**
  ```json
  {
      "usuario": 1,
      "especialidad": "Psicología Clínica",
      "descripcion": "Especialista en terapia cognitivo-conductual",
      "experiencia": 5,
      "universidad": "UTE",
      "licencia_profesional": "12345678"
  }
  ```

**Respuesta Exitosa esperada (201 Created):**
```json
{
    "id": 1,
    "usuario": 1,
    "especialidad": "Psicología Clínica",
    "descripcion": "Especialista en terapia cognitivo-conductual",
    "experiencia": 5,
    "universidad": "Universidad Nacional",
    "licencia_profesional": "12345678",
    "disponible": true,
    "valoracion": "0.0"
}
```
---

## Listado de Endpoints

A continuación, se listan las rutas principales de la API. Se asume el prefijo `/api/` antes de cada endpoint.

### Autenticación (`/api/auth/`)
- `POST /register/` - Registrar nuevo usuario.
- `POST /login/` - Iniciar sesión (Obtener JWT).

### Usuarios (`/api/usuarios/`)
- `GET /api/usuarios/` - Listar usuarios.
- `POST /api/usuarios/` - Crear usuario.
- `GET /api/usuarios/{id}/` - Obtener detalle de usuario.
- `PUT /api/usuarios/{id}/` - Actualizar usuario completo.
- `PATCH /api/usuarios/{id}/` - Actualización parcial de usuario.
- `DELETE /api/usuarios/{id}/` - Eliminar usuario.

### Psicólogos (`/api/psicologos/`)
- `GET /api/psicologos/` - Listar psicólogos.
- `POST /api/psicologos/` - Crear psicólogo.
- `GET /api/psicologos/{id}/` - Obtener detalle de psicólogo.
- `PUT /api/psicologos/{id}/` - Actualizar psicólogo completo.
- `PATCH /api/psicologos/{id}/` - Actualización parcial de psicólogo.
- `DELETE /api/psicologos/{id}/` - Eliminar psicólogo.

### Citas (`/api/citas/`)
- `GET /api/citas/` - Listar citas.
- `POST /api/citas/` - Crear cita.
- `GET /api/citas/{id}/` - Obtener detalle de cita.
- `PUT /api/citas/{id}/` - Actualizar cita completa.
- `PATCH /api/citas/{id}/` - Actualización parcial de cita.
- `DELETE /api/citas/{id}/` - Eliminar cita.

### Historiales (`/api/historiales/`)
- `GET /api/historiales/` - Listar historiales.
- `POST /api/historiales/` - Crear historial.
- `GET /api/historiales/{id}/` - Obtener detalle de historial.
- `PUT /api/historiales/{id}/` - Actualizar historial completo.
- `PATCH /api/historiales/{id}/` - Actualización parcial de historial.
- `DELETE /api/historiales/{id}/` - Eliminar historial.

### Emociones (`/api/emociones/`)
- `GET /api/emociones/` - Listar emociones.
- `POST /api/emociones/` - Registrar emoción.
- `GET /api/emociones/{id}/` - Obtener detalle de emoción.
- `PUT /api/emociones/{id}/` - Actualizar emoción completa.
- `PATCH /api/emociones/{id}/` - Actualización parcial de emoción.
- `DELETE /api/emociones/{id}/` - Eliminar emoción.

### Recomendaciones (`/api/recomendaciones/`)
- `GET /api/recomendaciones/` - Listar recomendaciones.
- `POST /api/recomendaciones/` - Crear recomendación.
- `GET /api/recomendaciones/{id}/` - Obtener detalle de recomendación.
- `PUT /api/recomendaciones/{id}/` - Actualizar recomendación completa.
- `PATCH /api/recomendaciones/{id}/` - Actualización parcial de recomendación.
- `DELETE /api/recomendaciones/{id}/` - Eliminar recomendación.

### Perfiles Psicológicos (`/api/perfiles-psicologicos/`)
- `GET /api/perfiles-psicologicos/` - Listar perfiles psicológicos.
- `POST /api/perfiles-psicologicos/` - Crear perfil psicológico.
- `GET /api/perfiles-psicologicos/{id}/` - Obtener detalle de perfil psicológico.
- `PUT /api/perfiles-psicologicos/{id}/` - Actualizar perfil psicológico completo.
- `PATCH /api/perfiles-psicologicos/{id}/` - Actualización parcial de perfil psicológico.
- `DELETE /api/perfiles-psicologicos/{id}/` - Eliminar perfil psicológico.

### Chats (`/api/chats/`)
- `GET /api/chats/` - Listar chats.
- `POST /api/chats/` - Crear chat.
- `GET /api/chats/{id}/` - Obtener detalle de chat.
- `PUT /api/chats/{id}/` - Actualizar chat completo.
- `PATCH /api/chats/{id}/` - Actualización parcial de chat.
- `DELETE /api/chats/{id}/` - Eliminar chat.

### Mensajes (`/api/mensajes/`)
- `GET /api/mensajes/` - Listar mensajes.
- `POST /api/mensajes/` - Enviar mensaje.
- `GET /api/mensajes/{id}/` - Obtener detalle de mensaje.
- `PUT /api/mensajes/{id}/` - Actualizar mensaje completo.
- `PATCH /api/mensajes/{id}/` - Actualización parcial de mensaje.
- `DELETE /api/mensajes/{id}/` - Eliminar mensaje.

### Otros
- `GET /api/health/` - Verificar estado de la API.