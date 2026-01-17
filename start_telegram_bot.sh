#!/bin/bash

echo "🤖 Iniciando Telegram Quote Generator Bot..."
echo ""

# Cargar variables de entorno
if [ -f .env ]; then
    export $(cat .env | xargs)
fi

# Verificar token
if [ -z "$TELEGRAM_BOT_TOKEN" ]; then
    echo "❌ ERROR: TELEGRAM_BOT_TOKEN no configurado"
    echo ""
    echo "Por favor:"
    echo "1. Copia .env.example a .env"
    echo "2. Edita .env y añade tu token de Telegram"
    echo "3. Obtén el token desde @BotFather en Telegram"
    echo ""
    exit 1
fi

# Crear entorno virtual si no existe
if [ ! -d "venv" ]; then
    echo "📦 Creando entorno virtual..."
    python3 -m venv venv
fi

source venv/bin/activate

echo "📦 Instalando dependencias..."
pip install -q -r requirements.txt

echo ""
echo "✅ Bot iniciado correctamente"
echo "📱 Abre Telegram y busca tu bot"
echo "🛑 Presiona Ctrl+C para detener"
echo ""

python telegram_bot.py
