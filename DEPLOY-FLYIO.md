# 🚀 Deploy en Fly.io - Instagram Quote Generator

## ✨ Por qué Fly.io es Excelente para este Proyecto

- ✅ **3 VMs gratis** (siempre activas)
- ✅ **No se duerme** (24/7 disponible)
- ✅ **Soporta bot de Telegram** perfectamente
- ✅ **Deploy global** (múltiples regiones)
- ✅ **256MB RAM gratis** por VM
- ✅ **3GB almacenamiento persistente** gratis

---

## 📋 PRERREQUISITOS

### 1. Instalar Fly CLI

#### Windows (PowerShell):
```powershell
iwr https://fly.io/install.ps1 -useb | iex
```

#### macOS/Linux:
```bash
curl -L https://fly.io/install.sh | sh
```

#### Verificar instalación:
```bash
fly version
```

### 2. Crear cuenta en Fly.io
```bash
fly auth signup
```

O si ya tienes cuenta:
```bash
fly auth login
```

**⚠️ IMPORTANTE:** Necesitas agregar tarjeta de crédito (NO se cobra si no excedes el plan free)

---

## 🚀 DEPLOYMENT PASO A PASO

### PASO 1: Preparar el Proyecto

Asegúrate de estar en la carpeta del proyecto:
```bash
cd instagram-quote-generator
```

Verifica que existen estos archivos:
- ✅ `Dockerfile` (creado)
- ✅ `fly.toml` (creado)
- ✅ `.dockerignore` (creado)
- ✅ `requirements.txt` (ya existía)

---

### PASO 2: Lanzar la Aplicación en Fly.io

```bash
fly launch --no-deploy
```

**Preguntas que te hará:**

1. **"Choose an app name"**: 
   - Presiona Enter para usar `instagram-quote-generator`
   - O escribe un nombre personalizado

2. **"Choose a region"**:
   - Selecciona la región más cercana a ti:
     - `mad` - Madrid (España)
     - `mia` - Miami (USA)
     - `ams` - Amsterdam (Países Bajos)
     - `syd` - Sydney (Australia)

3. **"Would you like to set up a Postgresql database?"**:
   - **NO** - Presiona `n`

4. **"Would you like to set up an Upstash Redis database?"**:
   - **NO** - Presiona `n`

5. **"Would you like to deploy now?"**:
   - **NO** - Presiona `n` (configuraremos secretos primero)

---

### PASO 3: Configurar Variables de Entorno (Secretos)

#### Para Bot de Telegram:
```bash
fly secrets set TELEGRAM_BOT_TOKEN="tu_token_aqui"
```

Reemplaza `tu_token_aqui` con tu token real.

#### Verificar secretos:
```bash
fly secrets list
```

---

### PASO 4: Configurar Región y Memoria

#### Editar fly.toml si es necesario:
```toml
# Cambiar región (si no elegiste la correcta)
primary_region = "mad"  # Madrid

# Ajustar memoria (256MB es suficiente)
[[vm]]
  cpu_kind = "shared"
  cpus = 1
  memory_mb = 256
```

---

### PASO 5: Hacer el Deploy

```bash
fly deploy
```

**Esto tomará 3-5 minutos**. Verás:
1. 📦 Construyendo imagen Docker
2. 🚀 Subiendo a Fly.io
3. 🌍 Desplegando en región seleccionada
4. ✅ Verificando health checks

---

### PASO 6: Verificar el Deploy

```bash
fly status
```

Deberías ver:
```
Status
  Name     = instagram-quote-generator
  State    = running
  Hostname = instagram-quote-generator.fly.dev
```

---

### PASO 7: Abrir la Aplicación

```bash
fly open
```

Esto abrirá tu navegador en: `https://instagram-quote-generator.fly.dev`

---

## 🤖 DEPLOY DEL BOT DE TELEGRAM

### Opción A: Solo Bot (sin web)

1. **Editar Dockerfile**, cambiar la última línea:
```dockerfile
# Cambiar de:
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]

# A:
CMD ["python", "telegram_bot.py"]
```

2. **Editar fly.toml**, cambiar:
```toml
# Comentar o eliminar sección [http_service]
# [http_service]
#   internal_port = 8080
#   ...

# Agregar:
[[services]]
  protocol = "tcp"
  internal_port = 8080
```

3. **Deploy**:
```bash
fly deploy
```

---

### Opción B: Web + Bot (2 apps separadas)

#### App 1: Aplicación Web
```bash
# Ya está desplegada
fly status
```

#### App 2: Bot de Telegram
```bash
# Crear segunda app
fly launch --name instagram-quote-bot --no-deploy

# Configurar
fly secrets set TELEGRAM_BOT_TOKEN="tu_token" -a instagram-quote-bot

# Editar Dockerfile para bot (cambiar CMD)
# Deploy
fly deploy -a instagram-quote-bot
```

---

## 📊 COMANDOS ÚTILES

### Ver logs en tiempo real:
```bash
fly logs
```

### Ver estado:
```bash
fly status
```

### Escalar (aumentar memoria):
```bash
fly scale memory 512
```

### SSH a la máquina:
```bash
fly ssh console
```

### Ver métricas:
```bash
fly dashboard
```

### Reiniciar:
```bash
fly apps restart
```

### Detener:
```bash
fly apps stop
```

### Eliminar app:
```bash
fly apps destroy instagram-quote-generator
```

---

## 🔐 ALMACENAMIENTO PERSISTENTE (Opcional)

Si necesitas que las imágenes persistan entre deployments:

### Crear volumen:
```bash
fly volumes create data --size 1 --region mad
```

### Editar fly.toml:
```toml
[mounts]
  source = "data"
  destination = "/app/output"
```

### Redeploy:
```bash
fly deploy
```

---

## 💰 COSTOS - PLAN GRATUITO

### Incluye (GRATIS):
- ✅ 3 VMs shared-cpu-1x (256MB RAM c/u)
- ✅ 160GB bandwidth saliente/mes
- ✅ 3GB almacenamiento persistente
- ✅ Certificados SSL automáticos
- ✅ Deploy en múltiples regiones

### Tu configuración actual:
```
1 VM x 256MB RAM = GRATIS ✅
Bandwidth < 160GB = GRATIS ✅
Sin almacenamiento persistente = GRATIS ✅
```

**Total: $0/mes** 🎉

---

## ⚠️ LIMITACIONES Y CONSIDERACIONES

### Plan Free:
- 3 VMs máximo
- 256MB RAM por VM (suficiente)
- 1 shared CPU
- No autoescalado

### Recomendaciones:
- Usa 1 VM para web + bot (para ahorrar)
- O 2 VMs separadas (1 web, 1 bot)
- Monitorea uso de RAM
- Optimiza generación de imágenes

---

## 🔧 SOLUCIÓN DE PROBLEMAS

### Error: "Could not resolve host"
```bash
# Verifica conexión a internet
ping fly.io

# Reintenta
fly deploy
```

### Error: "Not enough memory"
```bash
# Aumentar RAM
fly scale memory 512
```

### Error: "Health check failed"
```bash
# Ver logs
fly logs

# Verificar que /health endpoint funciona
curl https://tu-app.fly.dev/health
```

### App no responde:
```bash
# Ver status
fly status

# Reiniciar
fly apps restart

# Ver logs
fly logs
```

### Build falla:
```bash
# Limpiar cache
fly deploy --no-cache

# Verificar Dockerfile
cat Dockerfile
```

---

## 🌍 MÚLTIPLES REGIONES (Avanzado)

Para deploy global (3 VMs en diferentes regiones):

```bash
# Agregar región
fly regions add ams  # Amsterdam
fly regions add mia  # Miami

# Escalar a 3 VMs
fly scale count 3

# Ver distribución
fly status
```

Ahora tendrás:
- 1 VM en Madrid
- 1 VM en Amsterdam  
- 1 VM en Miami

**Usuarios globales tendrán baja latencia** 🌎

---

## 📈 MONITOREO

### Dashboard web:
```bash
fly dashboard
```

### Métricas:
- CPU usage
- Memory usage
- Request rate
- Response times

### Alertas:
Configurar en el dashboard de Fly.io

---

## 🔄 CI/CD - Deploy Automático desde GitHub

### Crear GitHub Action:

Archivo: `.github/workflows/fly.yml`

```yaml
name: Deploy to Fly.io

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - uses: superfly/flyctl-actions/setup-flyctl@master
      
      - run: flyctl deploy --remote-only
        env:
          FLY_API_TOKEN: ${{ secrets.FLY_API_TOKEN }}
```

### Obtener token:
```bash
fly tokens create deploy
```

### Agregar a GitHub Secrets:
1. Ir a repo → Settings → Secrets
2. New secret: `FLY_API_TOKEN`
3. Pegar token

**Ahora cada push a main → deploy automático** 🚀

---

## ✅ CHECKLIST DE DEPLOYMENT

- [ ] Fly CLI instalado
- [ ] Cuenta en Fly.io creada
- [ ] Tarjeta agregada
- [ ] Archivos creados (Dockerfile, fly.toml, .dockerignore)
- [ ] `fly launch` ejecutado
- [ ] Token de Telegram configurado (`fly secrets set`)
- [ ] `fly deploy` ejecutado exitosamente
- [ ] App funcionando (`fly open`)
- [ ] Logs sin errores (`fly logs`)
- [ ] Health check pasando
- [ ] Bot de Telegram respondiendo (si aplica)

---

## 🎯 CONFIGURACIÓN RECOMENDADA

### Para tu proyecto:

**Opción 1: Solo Web (Recomendada para empezar)**
```
1 VM (256MB) en tu región
Web app en puerto 8080
$0/mes
```

**Opción 2: Web + Bot Separados**
```
2 VMs (256MB cada una)
1 para web, 1 para bot
$0/mes (dentro del plan free)
```

**Opción 3: Global (3 regiones)**
```
3 VMs (256MB cada una)
Madrid, Amsterdam, Miami
$0/mes (límite del plan free)
```

---

## 📚 RECURSOS

- [Documentación Fly.io](https://fly.io/docs/)
- [Fly.io Pricing](https://fly.io/docs/about/pricing/)
- [Flask en Fly.io](https://fly.io/docs/languages-and-frameworks/python/)
- [Fly.io Dashboard](https://fly.io/dashboard)

---

## 🆘 SOPORTE

### Fly.io Community:
- [Forum](https://community.fly.io/)
- [Discord](https://fly.io/discord)

### Documentación del proyecto:
- Ver otros archivos DEPLOY_*.md
- README.md principal

---

## 🎉 CONCLUSIÓN

Fly.io es **perfecto para este proyecto** porque:

✅ Bot de Telegram 24/7 activo
✅ Sin sleep/cold starts
✅ Gratis hasta 3 VMs
✅ Deploy global
✅ Fácil de escalar

**¡Ahora estás listo para desplegar en Fly.io!** 🚀

---

**¿Listo para empezar? Ejecuta:** 
```bash
fly auth signup
fly launch --no-deploy
```
