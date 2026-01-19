# 🚀 Comandos Rápidos para Deploy en Fly.io

## ⚡ SETUP INICIAL (Solo 1 vez)

### 1. Instalar Fly CLI
```powershell
# Windows PowerShell (ejecuta como Administrador)
iwr https://fly.io/install.ps1 -useb | iex
```

### 2. Verificar instalación
```powershell
fly version
```

### 3. Crear cuenta / Login
```powershell
# Si no tienes cuenta
fly auth signup

# Si ya tienes cuenta
fly auth login
```

---

## 🚀 DEPLOYMENT (Ejecutar en orden)

### PASO 1: Lanzar app (sin deploy todavía)
```powershell
cd instagram-quote-generator
fly launch --no-deploy
```

**Responde las preguntas:**
- App name: Presiona Enter (usa `instagram-quote-generator`)
- Region: Elige `mad` (Madrid) o la más cercana
- PostgreSQL: **NO** (n)
- Redis: **NO** (n)
- Deploy now: **NO** (n)

---

### PASO 2: Configurar token de Telegram
```powershell
fly secrets set TELEGRAM_BOT_TOKEN="8573033645:AAG7CC8OB7KgymvZDjaTDS-yJKS0M60Wrg8"
```

**Verifica que se guardó:**
```powershell
fly secrets list
```

---

### PASO 3: Deploy
```powershell
fly deploy
```

⏳ **Espera 3-5 minutos** mientras:
- 📦 Construye la imagen Docker
- 🚀 Sube a Fly.io
- ✅ Inicia la aplicación

---

### PASO 4: Verificar
```powershell
# Ver estado
fly status

# Abrir en navegador
fly open

# Ver logs
fly logs
```

---

## ✅ VERIFICACIÓN FINAL

### Tu app estará en:
```
https://instagram-quote-generator.fly.dev
```

### Health check:
```
https://instagram-quote-generator.fly.dev/health
```

### Probar generación:
```
https://instagram-quote-generator.fly.dev
```

---

## 🤖 SI QUIERES BOT 24/7

### Opción 1: Web + Bot en misma VM (Recomendado)

Edita `Dockerfile`, cambia la última línea:
```dockerfile
# De:
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "--timeout", "120", "app:app"]

# A (ejecutar ambos):
CMD gunicorn --bind 0.0.0.0:8080 --workers 1 --timeout 120 app:app & python telegram_bot.py
```

Luego:
```powershell
fly deploy
```

---

### Opción 2: Bot separado (2 VMs)

```powershell
# Crear segunda app para bot
fly launch --name instagram-quote-bot --no-deploy

# Configurar token
fly secrets set TELEGRAM_BOT_TOKEN="tu_token" -a instagram-quote-bot

# Editar Dockerfile para solo bot:
# CMD ["python", "telegram_bot.py"]

# Deploy
fly deploy -a instagram-quote-bot
```

---

## 📊 COMANDOS DE MONITOREO

```powershell
# Ver logs en tiempo real
fly logs -a instagram-quote-generator

# Ver estado detallado
fly status -a instagram-quote-generator

# Abrir dashboard web
fly dashboard

# Ver métricas
fly dashboard metrics

# SSH a la máquina
fly ssh console
```

---

## 🔧 COMANDOS DE MANTENIMIENTO

```powershell
# Reiniciar app
fly apps restart instagram-quote-generator

# Escalar RAM (si necesitas más)
fly scale memory 512 -a instagram-quote-generator

# Escalar VMs (múltiples regiones)
fly scale count 3 -a instagram-quote-generator

# Ver regiones disponibles
fly platform regions

# Agregar región
fly regions add ams -a instagram-quote-generator

# Detener app
fly apps stop instagram-quote-generator

# Iniciar app
fly apps start instagram-quote-generator
```

---

## 🐛 COMANDOS DE DEBUG

```powershell
# Ver logs de error
fly logs --level error

# Ver configuración actual
fly config show

# Ver secretos configurados
fly secrets list

# Verificar health checks
fly checks list

# Probar conexión
fly ping -n 10
```

---

## 🔄 ACTUALIZAR APP

Cuando hagas cambios en el código:

```powershell
# Commit cambios
git add .
git commit -m "Actualización"
git push

# Deploy nueva versión
fly deploy
```

---

## 🗑️ ELIMINAR APP (si quieres empezar de nuevo)

```powershell
fly apps destroy instagram-quote-generator
```

**CUIDADO:** Esto elimina todo (app, configuración, secretos)

---

## 💰 VER COSTOS

```powershell
# Ver uso actual
fly dashboard billing

# Tu configuración actual: $0/mes ✅
# 1 VM x 256MB = Gratis
```

---

## ⚡ RESUMEN DE 4 COMANDOS

Si ya tienes Fly CLI instalado:

```powershell
# 1. Iniciar
fly launch --no-deploy

# 2. Configurar token
fly secrets set TELEGRAM_BOT_TOKEN="tu_token"

# 3. Deploy
fly deploy

# 4. Abrir
fly open
```

**¡Eso es todo!** 🎉

---

## 📱 DESPUÉS DEL DEPLOY

### Para la Web:
```
https://instagram-quote-generator.fly.dev
```

### Para el Bot:
1. El bot está corriendo 24/7 en Fly.io
2. Abre Telegram
3. Busca tu bot
4. Envía `/start`
5. ¡Funciona desde cualquier lugar!

---

## 🆘 PROBLEMAS COMUNES

### "fly: command not found"
```powershell
# Reinicia PowerShell o agrega al PATH
$env:Path += ";$env:USERPROFILE\.fly\bin"
```

### "Error: not authenticated"
```powershell
fly auth login
```

### "Health check failed"
```powershell
# Ver qué está pasando
fly logs

# Verificar endpoint
curl https://tu-app.fly.dev/health
```

### Build muy lento
```powershell
# Primera vez es lento (5-10 min)
# Siguientes builds son más rápidos (2-3 min)
```

---

## ✅ CHECKLIST

Antes de empezar, asegúrate de tener:
- [ ] Fly CLI instalado
- [ ] Cuenta en Fly.io
- [ ] Tarjeta agregada (no se cobra)
- [ ] Estar en carpeta `instagram-quote-generator`
- [ ] Archivos Dockerfile, fly.toml, .dockerignore existen
- [ ] Token de Telegram a mano

---

## 🎯 ORDEN RECOMENDADO

1. ✅ Instalar Fly CLI
2. ✅ Login / Signup
3. ✅ `fly launch --no-deploy`
4. ✅ `fly secrets set TELEGRAM_BOT_TOKEN="..."`
5. ✅ `fly deploy`
6. ✅ `fly open`
7. ✅ Probar web
8. ✅ Probar bot en Telegram

---

**¿Listo? ¡Empieza con el primer comando!** 🚀
