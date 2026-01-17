# ⚡ Quick Start - Telegram Bot

## 🚀 En 3 minutos

### 1. Crear Bot en Telegram (1 min)

1. Abre Telegram → Busca `@BotFather`
2. Envía: `/newbot`
3. Dale un nombre: `Mi Quote Bot`
4. Dale un username: `mi_quote_bot` (debe terminar en "bot")
5. **Copia el token** que te da

### 2. Configurar (30 segundos)

```bash
# Crear archivo .env
copy .env.example .env

# Editar .env y pegar tu token
# TELEGRAM_BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
```

### 3. Ejecutar (30 segundos)

**Windows:**
```bash
start_telegram_bot.bat
```

**Linux/Mac:**
```bash
chmod +x start_telegram_bot.sh
./start_telegram_bot.sh
```

## ✅ ¡Listo!

Abre Telegram, busca tu bot y envíale una frase 🎉

---

## 📱 Ejemplo de Uso

1. **Abrir tu bot en Telegram**
2. **Enviar:** `/start`
3. **Escribir tu frase:**
   ```
   La vida es bella | Roberto Benigni
   ```
4. **Seleccionar estilo:** Tap en 🌈 Gradient
5. **Recibir imagen** lista para Instagram

---

## 🎨 Estilos Disponibles

- 🎯 **Minimal** - Fondo blanco limpio
- 🌈 **Gradient** - Degradados coloridos
- ✨ **Elegant** - Fondo oscuro elegante
- 🚀 **Modern** - Diseño moderno
- 🌿 **Nature** - Tonos naturales
- 🌅 **Sunset** - Colores cálidos

---

## ❓ Problemas Comunes

### "Token no configurado"
→ Verifica que `.env` tiene tu token sin espacios

### "ModuleNotFoundError"
→ Ejecuta: `pip install -r requirements.txt`

### Bot no responde
→ Verifica que el script está corriendo sin errores

---

Para más detalles, ver [TELEGRAM_BOT_GUIDE.md](TELEGRAM_BOT_GUIDE.md)
