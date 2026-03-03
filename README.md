# 🎓 Udemy Free Course Telegram Bot

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Telegram](https://img.shields.io/badge/Telegram-Bot_API-26A5E4?style=flat-square&logo=telegram&logoColor=white)](https://core.telegram.org/bots/api)
[![RSS](https://img.shields.io/badge/RSS-discudemy.com-FFA500?style=flat-square&logo=rss&logoColor=white)]()
[![Estado](https://img.shields.io/badge/Estado-Completado-brightgreen?style=flat-square)]()

Bot en Python que monitoriza el feed RSS de **[discudemy.com](https://www.discudemy.com)** para detectar cursos gratuitos de Udemy y enviar notificaciones automáticas a Telegram. Incluye un sistema de deduplicación mediante archivo local para evitar notificaciones repetidas.

---

## 📂 Estructura del Proyecto

```
udemy-free-course-bot/
│
├── 📄 bot.py          # Script principal del bot
├── 📄 sent.txt        # Registro de cursos ya notificados (auto-generado)
├── 📄 .env            # Variables de entorno con credenciales (no subir)
├── 📄 .gitignore
└── 📄 README.md
```

---

## ⚙️ Cómo Funciona

```
discudemy.com/feed (RSS)
        │
        ▼
feedparser — parsea hasta 10 entradas del feed
        │
        ▼
Comprueba sent.txt — ¿ya fue notificado este enlace?
        │
   NO ──┘
        ▼
Telegram Bot API — envía mensaje con título + enlace
        │
        ▼
sent.txt — registra el enlace para evitar duplicados
```

1. Lee el feed RSS de `discudemy.com/feed` con `feedparser`
2. Comprueba los últimos **10 cursos** del feed
3. Filtra los que ya fueron enviados consultando `sent.txt`
4. Envía un mensaje de Telegram por cada curso nuevo con título y enlace
5. Guarda el enlace en `sent.txt` para no volver a notificarlo

---

## 🚀 Tecnologías Utilizadas

| Librería | Uso |
|---|---|
| **feedparser** | Parseo del feed RSS de discudemy.com |
| **requests** | Llamadas HTTP a la Telegram Bot API |
| **python-dotenv** | Carga de credenciales desde `.env` |
| **os** | Gestión de archivos y variables de entorno |

---

## ⚙️ Instalación y Configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/diegofonterosa/udemy-free-course-bot.git
cd udemy-free-course-bot
```

### 2. Instalar dependencias

```bash
pip install feedparser requests python-dotenv
```

### 3. Crear el archivo `.env`

Crea un archivo `.env` en la raíz del proyecto con tus credenciales de Telegram:

```env
TELEGRAM_TOKEN=tu_token_del_bot
TELEGRAM_CHAT_ID=tu_chat_id
```

> ⚠️ **Nunca subas el archivo `.env` a un repositorio público.** Ya está incluido en el `.gitignore`.

#### ¿Cómo obtener las credenciales?

- **`TELEGRAM_TOKEN`** — Habla con [@BotFather](https://t.me/BotFather) en Telegram, crea un bot y copia el token
- **`TELEGRAM_CHAT_ID`** — Habla con [@userinfobot](https://t.me/userinfobot) para obtener tu Chat ID

### 4. Ejecutar el bot

```bash
python bot.py
```

La primera vez que se ejecute se creará automáticamente el archivo `sent.txt` donde se registran los cursos ya notificados.

---

## 📩 Ejemplo de Notificación

Cuando se detecta un curso nuevo, el bot envía en Telegram:

```
🎓 CURSO GRATIS DETECTADO

The Complete Python Bootcamp From Zero to Hero in Python
https://www.discudemy.com/...
```

---

## 🔒 Seguridad

- Las credenciales se cargan desde `.env` con `python-dotenv`, **nunca hardcodeadas** en el código
- Al arrancar, el script valida que `TELEGRAM_TOKEN` y `TELEGRAM_CHAT_ID` estén definidas; si no, lanza un `ValueError` y detiene la ejecución
- El archivo `sent.txt` actúa como caché local para prevenir notificaciones duplicadas

---

## 🔮 Mejoras Futuras

- [ ] Ejecución programada con `cron` o `schedule` para monitoreo continuo
- [ ] Contenedorización con Docker para despliegue en la nube (uptime 24/7)
- [ ] Filtrado de cursos por categoría o palabras clave
- [ ] Sustitución de `sent.txt` por base de datos (SQLite / MongoDB)
- [ ] Soporte para múltiples fuentes RSS
- [ ] Panel web de control

---

## 🎯 Habilidades Demostradas

- ✅ Automatización de tareas con Python
- ✅ Consumo de feeds RSS con `feedparser`
- ✅ Integración con la Telegram Bot API mediante `requests`
- ✅ Gestión segura de credenciales con variables de entorno (`dotenv`)
- ✅ Sistema de deduplicación con persistencia en fichero
- ✅ Manejo de errores HTTP y validación de configuración

---

## 📋 Requisitos

- Python 3.8+
- Cuenta de Telegram y bot creado con [@BotFather](https://t.me/BotFather)

---

## 👨‍💻 Autor

**Diego Pérez Fonterosa**

[![GitHub](https://img.shields.io/badge/GitHub-diegofonterosa-181717?style=flat-square&logo=github)](https://github.com/diegofonterosa)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Diego%20Pérez-0A66C2?style=flat-square&logo=linkedin)](https://linkedin.com/in/diegofonterosa)

> Cursando ASIR y Máster en Ciberseguridad

---

## 📄 Licencia

Este proyecto tiene fines educativos y personales. Puedes usar, modificar y distribuir el código con libertad mencionando al autor original.
