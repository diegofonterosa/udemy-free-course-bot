# 🎓 Udemy Free Course Telegram Bot

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Telegram](https://img.shields.io/badge/Telegram-Bot_API-26A5E4?style=flat-square&logo=telegram&logoColor=white)](https://core.telegram.org/bots/api)
[![RSS](https://img.shields.io/badge/RSS-discudemy.com-FFA500?style=flat-square&logo=rss&logoColor=white)]()

Bot en Python que monitoriza el feed RSS de **[discudemy.com](https://www.discudemy.com)** para detectar cursos gratuitos de Udemy y enviar notificaciones automáticas a Telegram. Con **scheduling interno** que revisa cada 5 minutos sin necesidad de cron.

---

## 📂 Estructura del Proyecto

```
udemy-free-course-bot/
├── bot.py                          # Script principal (con scheduling)
├── requirements.txt                # Dependencias
├── sent.txt                        # Registro de cursos notificados (auto-generado)
├── .env                            # Variables de entorno (no subir)
├── .gitignore
├── README.md
├── setup_startup.sh                # Helper para registrar en cron
└── udemy-free-course-bot.service   # Plantilla systemd
```

---

## ⚙️ Cómo Funciona

```
discudemy.com/feed (RSS)
        │
        ▼
feedparser — parsea hasta 10 entradas
        │
        ▼
sent.txt — ¿ya fue notificado?
        │
   NO ──┘
        ▼
Telegram Bot API — envía mensaje
        │
        ▼
sent.txt — registra para evitar duplicados
```

1. Lee el feed RSS de `discudemy.com/feed`
2. Filtra cursos nuevos (no en `sent.txt`)
3. Envía notificación por Telegram
4. Registra el enlace para no volver a notificarlo
5. **Repite automáticamente cada 5 minutos** ✨

---

## 🚀 Tecnologías

| Librería | Uso |
|---|---|
| **feedparser** | Parseo del RSS |
| **requests** | HTTP a Telegram API |
| **python-dotenv** | Credenciales desde `.env` |
| **schedule** | Ejecución periódica cada 5 min |

---

## ⚙️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/diegofonterosa/udemy-free-course-bot.git
cd udemy-free-course-bot
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

O manualmente:

```bash
pip install feedparser requests python-dotenv schedule
```

### 3. Crear el archivo `.env`

Crea un `.env` con tus credenciales:

```env
TELEGRAM_TOKEN=tu_token_del_bot
TELEGRAM_CHAT_ID=tu_chat_id
```

**Cómo obtener:**
- **Token**: Habla con [@BotFather](https://t.me/BotFather), crea un bot
- **Chat ID**: Habla con [@userinfobot](https://t.me/userinfobot)

> ⚠️ **Nunca subas `.env` a Git** (está en `.gitignore`)

### 4. Ejecutar el bot

```bash
python bot.py
```

El bot arrancará e **imprimirá logs cada 5 minutos**. Para detenerlo, usa `Ctrl+C`.

---

## 📩 Ejemplo de Notificación

Cuando detecta un curso nuevo, envía:

```
🎓 CURSO GRATIS DETECTADO

The Complete Python Bootcamp From Zero to Hero in Python
https://www.discudemy.com/...
```

---

## 🔒 Seguridad

- ✅ Credenciales en `.env`, nunca hardcodeadas
- ✅ Validación temprana de variables de entorno
- ✅ Manejo de errores en HTTP y RSS
- ✅ `sent.txt` como caché local para evitar duplicados

---

## 🚀 Ejecución Automática al Arrancar

El bot incluye **scheduling interno** — revisa cada 5 minutos. Solo necesitas que se inicie al arrancar tu portátil.

### Opción 1: Cron `@reboot` (simple)

Edita el crontab:

```bash
crontab -e
```

Añade:

```cron
@reboot cd /ruta/al/proyecto && /usr/bin/python3 bot.py
```

O usa el script incluido:

```bash
./setup_startup.sh /ruta/al/proyecto
```

### Opción 2: Servicio systemd (recomendado)

Copia la plantilla a `/etc/systemd/system/`:

```bash
sudo cp /ruta/al/proyecto/udemy-free-course-bot.service /etc/systemd/system/
```

Edita el fichero y reemplaza `TU_USUARIO` y las rutas:

```bash
sudo nano /etc/systemd/system/udemy-free-course-bot.service
```

Luego:

```bash
sudo systemctl daemon-reload
sudo systemctl enable udemy-free-course-bot.service
sudo systemctl start udemy-free-course-bot.service
```

Verifica:

```bash
sudo systemctl status udemy-free-course-bot
journalctl -u udemy-free-course-bot -f   # ver logs
```

---

## 🔮 Variables de Entorno Opcionales

Además de `TELEGRAM_TOKEN` y `TELEGRAM_CHAT_ID`, puedes usar:

```env
RSS_URL=https://www.discudemy.com/feed    # fuente RSS (por defecto)
SENT_FILE=sent.txt                         # fichero de cursos enviados (por defecto)
```

---

## 🎯 Habilidades Demostradas

- ✅ Automatización de tareas con Python
- ✅ Consumo de feeds RSS con `feedparser`
- ✅ Integración con Telegram Bot API
- ✅ Scheduling periódico interno
- ✅ Gestión segura de credenciales
- ✅ Sistema de deduplicación con persistencia
- ✅ Logging y manejo de errores

---

## 🔮 Mejoras Futuras

- [ ] Filtrado de cursos por categoría o palabras clave
- [ ] Sustituir `sent.txt` por SQLite/MongoDB
- [ ] Soporte para múltiples fuentes RSS
- [ ] Panel web de estadísticas
- [ ] Docker para despliegue en la nube

---

## 📋 Requisitos

- Python 3.8+
- Cuenta de Telegram
- Bot creado con [@BotFather](https://t.me/BotFather)

---

## 👨‍💻 Autor

**Diego Pérez Fonterosa**

[![GitHub](https://img.shields.io/badge/GitHub-diegofonterosa-181717?style=flat-square&logo=github)](https://github.com/diegofonterosa)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Diego%20Pérez-0A66C2?style=flat-square&logo=linkedin)](https://linkedin.com/in/diegofonterosa)

---

## 📄 Licencia

Proyecto educativo. Usa, modifica y distribuye libremente mencionando al autor original.
