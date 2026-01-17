# 🤖 Telegram Bot - Guía de Uso

## 📋 Requisitos Previos

1. **Python 3.8+** instalado
2. **Cuenta de Telegram**
3. **Token de Bot** de @BotFather

---

## 🚀 Configuración Rápida

### 1️⃣ Crear el Bot en Telegram

1. Abre Telegram y busca **@BotFather**
2. Envía el comando `/newbot`
3. Sigue las instrucciones:
   - Nombre del bot: `Instagram Quote Generator`
   - Username: `tu_nombre_quote_bot` (debe terminar en `bot`)
4. **Guarda el token** que te proporciona (ejemplo: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`)

### 2️⃣ Configurar el Proyecto

```bash
# 1. Copia el archivo de ejemplo
cp .env.example .env

# 2. Edita .env y pega tu token
# TELEGRAM_BOT_TOKEN=tu_token_aquí
```

### 3️⃣ Instalar Dependencias

```bash
# Opción 1: Usando el script (recomendado)
# Windows:
start_telegram_bot.bat

# Linux/Mac:
chmod +x start_telegram_bot.sh
./start_telegram_bot.sh

# Opción 2: Manual
pip install -r requirements.txt
python telegram_bot.py
```

---

## 💬 Cómo Usar el Bot

### Comandos Disponibles

| Comando | Descripción |
|---------|-------------|
| `/start` | Mensaje de bienvenida |
| `/help` | Ayuda y guía de uso |
| `/styles` | Ver estilos disponibles |

### Crear un Quote

1. **Envía tu frase** al bot
   ```
   La vida es bella
   ```

2. **Agrega autor (opcional)** con `|`
   ```
   La vida es bella | Roberto Benigni
   ```

3. **Selecciona un estilo**
   - 🎯 Minimal
   - 🌈 Gradient
   - ✨ Elegant
   - 🚀 Modern
   - 🌿 Nature
   - 🌅 Sunset

4. **Recibe tu imagen** lista para Instagram (1080x1080px)

---

## 🎨 Estilos Disponibles

### 🎯 Minimal
- Fondo blanco limpio
- Tipografía serif elegante
- Ideal para frases profesionales

### 🌈 Gradient
- Degradados coloridos
- Vibrante y llamativo
- Perfecto para contenido motivacional

### ✨ Elegant
- Fondo oscuro sofisticado
- Tipografía dorada/plateada
- Para frases inspiradoras

### 🚀 Modern
- Diseño contemporáneo
- Colores corporativos
- Ideal para negocios

### 🌿 Nature
- Tonos verdes y naturales
- Sensación orgánica
- Para contenido wellness

### 🌅 Sunset
- Colores cálidos (naranja, rosa)
- Atmosférico y emocional
- Para frases románticas

---

## 🔧 Personalización

### Añadir Nuevos Estilos

Edita `telegram_bot.py` y añade en el diccionario `STYLES`:

```python
STYLES = {
    'minimal': '🎯 Minimal',
    'tu_estilo': '🎨 Tu Estilo',  # Añadir aquí
}
```

Luego implementa el estilo en `image_generator.py`.

### Cambiar Formato de Imagen

En `image_generator.py`:

```python
# Cambiar dimensiones
width, height = 1080, 1350  # Para posts verticales

# Cambiar formato
image.save(output_path, 'JPEG', quality=95)  # Para JPEG
```

---

## 🐛 Solución de Problemas

### Error: "TELEGRAM_BOT_TOKEN no configurado"

✅ **Solución:** 
1. Verifica que `.env` existe y contiene tu token
2. Asegúrate de que el formato es correcto: `TELEGRAM_BOT_TOKEN=tu_token_sin_espacios`

### Error: "ModuleNotFoundError: No module named 'telegram'"

✅ **Solución:**
```bash
pip install python-telegram-bot==20.7
```

### Bot no responde

✅ **Verificar:**
1. El token es correcto
2. El script está ejecutándose sin errores
3. Tienes conexión a internet
4. El bot no fue bloqueado por Telegram

### Imágenes no se generan

✅ **Verificar:**
1. La carpeta `output/` existe
2. Tienes permisos de escritura
3. Pillow está instalado correctamente

---

## 📊 Características

- ✅ Generación instantánea de imágenes
- ✅ 6 estilos predefinidos
- ✅ Soporte para autor opcional
- ✅ Formato Instagram optimizado (1080x1080px)
- ✅ Interfaz de botones interactiva
- ✅ Manejo de errores robusto
- ✅ Logging detallado

---

## 🔐 Seguridad

⚠️ **IMPORTANTE:**
- **NUNCA** compartas tu `TELEGRAM_BOT_TOKEN`
- No subas `.env` a repositorios públicos
- El archivo `.gitignore` ya incluye `.env`

---

## 📈 Mejoras Futuras

Ideas para expandir el bot:

- [ ] Más estilos de fondos
- [ ] Personalización de fuentes
- [ ] Múltiples tamaños (Stories, Posts, etc.)
- [ ] Emojis en los quotes
- [ ] Preview antes de generar
- [ ] Historial de quotes generados
- [ ] Compartir directamente en Instagram
- [ ] Modo batch (múltiples frases)

---

## 🆘 Soporte

¿Problemas o preguntas?

1. Revisa esta guía
2. Verifica los logs en la consola
3. Comprueba que todas las dependencias están instaladas

---

## 📄 Licencia

Este proyecto es de código abierto. Úsalo libremente para tus proyectos.

---

**¡Disfruta creando quotes para Instagram! 🎨✨**
