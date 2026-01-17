@echo off
echo 🤖 Iniciando Telegram Quote Generator Bot...
echo.

REM Cargar variables de entorno desde .env
if exist .env (
    for /f "tokens=*" %%a in (.env) do (
        set %%a
    )
)

REM Verificar que existe el token
if "%TELEGRAM_BOT_TOKEN%"=="" (
    echo ❌ ERROR: TELEGRAM_BOT_TOKEN no configurado
    echo.
    echo Por favor:
    echo 1. Copia .env.example a .env
    echo 2. Edita .env y añade tu token de Telegram
    echo 3. Obtén el token desde @BotFather en Telegram
    echo.
    pause
    exit /b 1
)

REM Instalar dependencias si es necesario
if not exist "venv\" (
    echo 📦 Creando entorno virtual...
    python -m venv venv
)

call venv\Scripts\activate.bat

echo 📦 Instalando dependencias...
pip install -q -r requirements.txt

echo.
echo ✅ Bot iniciado correctamente
echo 📱 Abre Telegram y busca tu bot
echo 🛑 Presiona Ctrl+C para detener
echo.

python telegram_bot.py

pause
