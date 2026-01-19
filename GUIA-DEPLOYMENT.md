# 🌍 Guía de Deployment - Instagram Quote Generator

## 📋 Opciones de Deployment

El proyecto está listo para desplegarse en múltiples plataformas. Aquí están tus opciones:

---

## 🚀 Opción 1: Render (Recomendado para principiantes)

### ✅ Ventajas:
- Gratis (plan Free)
- Fácil configuración
- SSL automático
- Soporte para aplicaciones Python
- Se duerme después de 15 min de inactividad (plan Free)

### 📝 Pasos:
1. Crea cuenta en [Render.com](https://render.com)
2. Conecta tu repositorio de GitHub
3. Crea un nuevo "Web Service"
4. Configura:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Environment**: Python 3

### 📄 Documentación incluida:
- `DEPLOY-WEB-RENDER.md`
- `RENDER-FIX.md`
- `RENDER-MANUAL-DEPLOY.md`
- `CHECKLIST-DEPLOY-RENDER.md`

---

## 🚄 Opción 2: Railway

### ✅ Ventajas:
- Muy rápido
- Despliegue automático desde Git
- Plan gratuito con $5 de crédito mensual
- Excelente para desarrollo

### 📝 Pasos:
1. Crea cuenta en [Railway.app](https://railway.app)
2. "New Project" → "Deploy from GitHub repo"
3. Selecciona el repositorio
4. Railway detecta automáticamente Python
5. Agrega variables de entorno (si usas bot de Telegram)

### 📄 Documentación incluida:
- `DEPLOY_RAILWAY.md`
- `railway.json` (configuración automática)

---

## ⚡ Opción 3: Vercel

### ✅ Ventajas:
- Despliegue instantáneo
- Gratis para proyectos personales
- CDN global
- **Limitación**: No soporta websockets (el bot de Telegram no funcionará)

### ⚠️ Notas:
- Solo para la aplicación web
- El bot de Telegram requiere otro servidor

### 📄 Documentación incluida:
- `VERCEL-INFO.md`

---

## 🐳 Opción 4: Docker + VPS

### ✅ Ventajas:
- Control total
- Sin limitaciones
- Puede correr 24/7
- Ideal para bot de Telegram

### 📝 Requisitos:
- VPS (DigitalOcean, Linode, AWS EC2, etc.)
- Docker instalado
- Conocimientos básicos de Linux

### 🛠️ Setup básico:
```dockerfile
# Dockerfile (crear en la raíz del proyecto)
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
```

```bash
# Construir y ejecutar
docker build -t instagram-quote-bot .
docker run -d -p 5000:5000 instagram-quote-bot
```

---

## 🤖 Deployment del Bot de Telegram

### Opción A: Junto con la aplicación web
- Render o Railway pueden correr ambos
- Usa `Procfile` con dos procesos:
```
web: gunicorn app:app
worker: python telegram_bot.py
```

### Opción B: Separado
- Web en Vercel/Render
- Bot en Railway/VPS (usando `worker` dyno)

---

## 🔐 Variables de Entorno

Configura estas variables en tu plataforma de deployment:

```bash
# Para Bot de Telegram (opcional)
TELEGRAM_BOT_TOKEN=tu_token_de_botfather

# Para producción (opcional)
FLASK_ENV=production
PORT=5000
```

---

## 📦 Archivos Importantes para Deployment

### Ya incluidos en el proyecto:
- ✅ `requirements.txt` - Dependencias Python
- ✅ `Procfile` - Para Heroku/Render/Railway
- ✅ `runtime.txt` - Versión de Python
- ✅ `render.yaml` - Configuración para Render
- ✅ `railway.json` - Configuración para Railway

---

## 🔍 Checklist Pre-Deployment

- [ ] ✅ Código funciona localmente
- [ ] ✅ Dependencias en `requirements.txt` están actualizadas
- [ ] ✅ Variables de entorno configuradas
- [ ] ✅ `.gitignore` incluye archivos sensibles
- [ ] ✅ Carpeta `output/` existe (o se crea automáticamente)
- [ ] ✅ Imágenes de backgrounds incluidas

---

## 🧪 Testing en Producción

Una vez desplegado, verifica:

1. **Health Check**: `https://tu-app.com/health`
2. **Templates API**: `https://tu-app.com/api/templates`
3. **Generar imagen**: Usa la interfaz web
4. **Bot de Telegram**: Envía `/start` a tu bot

---

## 📊 Monitoreo

### Logs:
- **Render**: Dashboard → Logs
- **Railway**: Project → Deployments → View Logs
- **Vercel**: Dashboard → Deployment → Function Logs

### Métricas importantes:
- Tiempo de respuesta de API
- Errores de generación de imágenes
- Uso de memoria (Pillow consume bastante)

---

## 💰 Costos Estimados

| Plataforma | Plan Free | Plan Pago |
|------------|-----------|-----------|
| **Render** | ✅ Gratis (con límites) | $7/mes |
| **Railway** | $5 crédito mensual | Pay-as-you-go |
| **Vercel** | ✅ Gratis (hobby) | $20/mes (Pro) |
| **VPS** | - | $5-10/mes |

---

## 🎯 Recomendación Según Caso de Uso

### Solo App Web (sin bot):
- 🥇 **Vercel** - Más rápido y gratis
- 🥈 **Render** - Alternativa sólida

### App Web + Bot de Telegram:
- 🥇 **Railway** - Mejor para ambos servicios
- 🥈 **Render** - Con worker dyno

### Uso profesional/comercial:
- 🥇 **VPS con Docker** - Control total
- 🥈 **Railway Pro** - Balance precio/facilidad

---

## 🆘 Solución de Problemas Comunes

### Error: "Module not found"
```bash
# Verifica que requirements.txt esté completo
pip freeze > requirements.txt
```

### Error: "Out of memory"
```bash
# Pillow consume mucha RAM al procesar imágenes
# Aumenta el plan o reduce el tamaño de imágenes
```

### Bot no responde
```bash
# Verifica que TELEGRAM_BOT_TOKEN esté configurado
# Asegúrate que el proceso worker está corriendo
```

### Timeout en generación
```bash
# Aumenta el timeout del servidor
gunicorn --timeout 120 app:app
```

---

## 📚 Recursos Adicionales

- [Guía oficial de Render](https://render.com/docs)
- [Documentación de Railway](https://docs.railway.app)
- [Vercel Python Guide](https://vercel.com/docs/functions/serverless-functions/runtimes/python)
- [Telegram Bot API](https://core.telegram.org/bots/api)

---

## ✅ Próximos Pasos

1. **Elige tu plataforma** según tus necesidades
2. **Sigue la guía específica** (archivos DEPLOY_*.md)
3. **Configura variables de entorno**
4. **Haz tu primer deployment**
5. **Prueba todas las funcionalidades**
6. **Monitorea y optimiza**

---

**¿Listo para desplegar? Consulta las guías específicas en la carpeta del proyecto.**

¡Éxito con tu deployment! 🚀
