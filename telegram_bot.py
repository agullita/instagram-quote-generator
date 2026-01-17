"""
🤖 Instagram Quote Generator - Telegram Bot
Genera imágenes de quotes para Instagram directamente desde Telegram
"""

import os
import logging
import zipfile
import io
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters
)
from image_generator import InstagramQuoteGenerator
from carousel_generator import CarouselGenerator

# Configurar logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Configuración
from dotenv import load_dotenv
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', 'YOUR_BOT_TOKEN_HERE')

# Plantillas disponibles (con iconos)
TEMPLATE_ICONS = {
    'minimal': '🎯',
    'dark': '🌙',
    'vibrant': '🎨',
    'ocean': '🌊',
    'sunset': '🌅',
    'forest': '🌲',
    'geometric1': '🔶',
    'geometric2': '📐'
}

# Almacenar el estado del usuario
user_state = {}


class TelegramQuoteBot:
    """Bot de Telegram para generar quotes de Instagram"""
    
    def __init__(self, token: str):
        self.token = token
        self.generator = InstagramQuoteGenerator(output_dir='output')
        self.carousel_generator = CarouselGenerator(output_dir='output/carousels')
        
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /start - Bienvenida"""
        welcome_text = """
🎨 **Instagram Quote Generator Bot**

¡Bienvenido! Puedo ayudarte a crear imágenes y carruseles para Instagram.

**Cómo usar:**
1️⃣ Envíame una frase
2️⃣ Elige: Imagen única o Carrusel
3️⃣ Selecciona una plantilla
4️⃣ Recibe tu contenido listo para Instagram

**Comandos disponibles:**
/start - Ver este mensaje
/templates - Ver plantillas disponibles
/carousel - Crear un carrusel
/help - Ayuda

**Nuevas funcionalidades:**
✨ Palabras destacadas
🎨 8 plantillas (incluyendo fondos personalizados)
📱 Generación de carruseles

¡Envíame una frase para empezar! 🚀
        """
        await update.message.reply_text(welcome_text, parse_mode='Markdown')
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /help"""
        help_text = """
📖 **Ayuda - Quote Generator Bot**

**Uso básico:**
Simplemente envía cualquier texto y elige entre imagen única o carrusel.

**Plantillas disponibles:**
🎯 Minimalista - Fondo blanco limpio
🌙 Oscuro - Fondo oscuro elegante
🎨 Vibrante - Colores brillantes
🌊 Océano - Azul relajante
🌅 Atardecer - Tonos cálidos
🌲 Bosque - Verde natural
🔶 Geométrico Naranja - Formas modernas
📐 Geométrico Limpio - Diseño minimalista

**Personalización:**
• Autor: después de | → "Frase | Autor"
• Palabras destacadas: después de # → "Frase | Autor #palabra1,palabra2"
• Ejemplo: "La vida es bella | Roberto #vida,bella"

**Formato de salida:**
• 1080x1080px (formato Instagram)
• PNG de alta calidad
• Tipografía adaptativa

**Para carruseles:**
Usa /carousel para crear múltiples slides
        """
        await update.message.reply_text(help_text, parse_mode='Markdown')
    
    async def templates_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /templates - Mostrar plantillas"""
        templates = self.generator.TEMPLATES
        templates_text = "🎨 **Plantillas disponibles:**\n\n"
        
        for key, config in templates.items():
            icon = TEMPLATE_ICONS.get(key, '🎨')
            templates_text += f"{icon} **{config['name']}**\n"
            templates_text += f"   _{config['description']}_\n\n"
        
        templates_text += "\n💡 Envía una frase para empezar"
        
        await update.message.reply_text(templates_text, parse_mode='Markdown')
    
    async def carousel_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /carousel - Información sobre carruseles"""
        carousel_text = """
📱 **Crear Carruseles para Instagram**

**Formato:**
Envía tu texto con el formato:
```
CAROUSEL: Tu contenido aquí
```

**Opciones adicionales:**
• Título: TITLE: Tu título
• Subtítulo: SUBTITLE: Tu subtítulo  
• CTA: CTA: Sígueme para más
• Palabras destacadas: #palabra1,palabra2

**Ejemplo completo:**
```
CAROUSEL: La vida es bella. Cada día es una oportunidad. Nunca te rindas.
TITLE: 3 Lecciones de Vida
SUBTITLE: Inspiración diaria
CTA: Sígueme para más contenido
#vida,oportunidad
```

El bot generará múltiples imágenes y las enviará como álbum.
        """
        await update.message.reply_text(carousel_text, parse_mode='Markdown')
    
    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Manejar mensajes de texto (frases)"""
        user_id = update.effective_user.id
        message_text = update.message.text
        
        # Verificar si es un carrusel
        if message_text.startswith('CAROUSEL:'):
            await self.handle_carousel_request(update, context)
            return
        
        # Parsear el mensaje: Frase | Autor #palabras,destacadas
        quote_text = message_text
        author = None
        highlight_words = None
        
        # Extraer palabras destacadas
        if '#' in quote_text:
            parts = quote_text.split('#')
            quote_text = parts[0].strip()
            highlight_words = [w.strip() for w in parts[1].split(',')]
        
        # Extraer autor
        if '|' in quote_text:
            parts = quote_text.split('|')
            quote_text = parts[0].strip()
            author = parts[1].strip()
        
        # Guardar la información del usuario
        user_state[user_id] = {
            'quote': quote_text,
            'author': author,
            'highlight_words': highlight_words
        }
        
        # Crear teclado con modo
        keyboard = [
            [
                InlineKeyboardButton("🖼️ Imagen Única", callback_data="mode_single"),
                InlineKeyboardButton("📱 Carrusel", callback_data="mode_carousel")
            ]
        ]
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        # Mostrar preview del texto
        preview_text = f"📝 **Tu frase:**\n_{quote_text}_"
        if author:
            preview_text += f"\n👤 **Autor:** {author}"
        if highlight_words:
            preview_text += f"\n✨ **Palabras destacadas:** {', '.join(highlight_words)}"
        preview_text += "\n\n¿Qué quieres crear?"
        
        await update.message.reply_text(
            preview_text,
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
    
    async def handle_carousel_request(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Manejar solicitud de carrusel"""
        user_id = update.effective_user.id
        message_text = update.message.text
        
        # Parsear el mensaje de carrusel
        content = ""
        title = None
        subtitle = None
        cta = None
        highlight_words = None
        
        lines = message_text.split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith('CAROUSEL:'):
                content = line.replace('CAROUSEL:', '').strip()
            elif line.startswith('TITLE:'):
                title = line.replace('TITLE:', '').strip()
            elif line.startswith('SUBTITLE:'):
                subtitle = line.replace('SUBTITLE:', '').strip()
            elif line.startswith('CTA:'):
                cta = line.replace('CTA:', '').strip()
            elif line.startswith('#'):
                highlight_words = [w.strip() for w in line[1:].split(',')]
        
        # Guardar información
        user_state[user_id] = {
            'mode': 'carousel',
            'content': content,
            'title': title,
            'subtitle': subtitle,
            'cta': cta,
            'highlight_words': highlight_words
        }
        
        # Mostrar opciones de plantillas
        await self.show_template_selection(update, user_id, is_carousel=True)
    
    async def show_template_selection(self, update: Update, user_id: int, is_carousel: bool = False):
        """Mostrar selección de plantillas"""
        templates = self.generator.TEMPLATES
        
        # Crear teclado con plantillas
        keyboard = []
        row = []
        for key, config in templates.items():
            icon = TEMPLATE_ICONS.get(key, '🎨')
            callback_prefix = "carousel_template_" if is_carousel else "template_"
            row.append(InlineKeyboardButton(
                f"{icon} {config['name']}", 
                callback_data=f"{callback_prefix}{key}"
            ))
            if len(row) == 2:
                keyboard.append(row)
                row = []
        if row:
            keyboard.append(row)
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        mode_text = "carrusel" if is_carousel else "imagen"
        await update.message.reply_text(
            f"🎨 Selecciona una plantilla para tu {mode_text}:",
            reply_markup=reply_markup
        )
    
    async def button_callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Manejar clicks en botones"""
        query = update.callback_query
        await query.answer()
        
        user_id = update.effective_user.id
        
        # Verificar que el usuario tiene datos guardados
        if user_id not in user_state:
            await query.message.reply_text("❌ Por favor envía una frase primero.")
            return
        
        callback_data = query.data
        
        # Manejar selección de modo
        if callback_data.startswith('mode_'):
            mode = callback_data.replace('mode_', '')
            user_state[user_id]['mode'] = mode
            
            if mode == 'carousel':
                # Convertir contenido a formato carrusel
                quote = user_state[user_id]['quote']
                user_state[user_id]['content'] = quote
            
            await self.show_template_selection(query, user_id, is_carousel=(mode == 'carousel'))
            return
        
        # Manejar selección de plantilla para imagen única
        if callback_data.startswith('template_'):
            await self.generate_single_image(query, user_id, callback_data.replace('template_', ''))
            return
        
        # Manejar selección de plantilla para carrusel
        if callback_data.startswith('carousel_template_'):
            await self.generate_carousel_images(query, user_id, callback_data.replace('carousel_template_', ''))
            return
    
    async def generate_single_image(self, query, user_id: int, template: str):
        """Generar imagen única"""
        state = user_state[user_id]
        quote = state['quote']
        author = state.get('author')
        highlight_words = state.get('highlight_words')
        
        template_name = self.generator.TEMPLATES[template]['name']
        await query.message.reply_text(f"⏳ Generando imagen con plantilla {template_name}...")
        
        try:
            # Generar la imagen
            output_path = self.generator.generate_image(
                quote=quote,
                template=template,
                author=author,
                highlight_words=highlight_words,
                output_filename=f'telegram_{user_id}_{template}.png'
            )
            
            # Enviar la imagen
            with open(output_path, 'rb') as photo:
                caption = f"✅ **Tu imagen está lista!**\n\n"
                caption += f"🎨 Plantilla: {template_name}\n"
                if highlight_words:
                    caption += f"✨ Palabras destacadas: {', '.join(highlight_words)}\n"
                caption += "\n💡 Envía otra frase para crear más imágenes"
                
                await query.message.reply_photo(
                    photo=photo,
                    caption=caption,
                    parse_mode='Markdown'
                )
            
            # Limpiar archivo temporal
            os.remove(output_path)
            
            logger.info(f"Imagen generada para usuario {user_id} con plantilla {template}")
            
        except Exception as e:
            logger.error(f"Error generando imagen: {e}")
            await query.message.reply_text(
                f"❌ Error al generar la imagen: {str(e)}\n\nPor favor intenta de nuevo."
            )
    
    async def generate_carousel_images(self, query, user_id: int, template: str):
        """Generar carrusel de imágenes"""
        state = user_state[user_id]
        content = state.get('content', state.get('quote'))
        title = state.get('title')
        subtitle = state.get('subtitle')
        cta = state.get('cta')
        highlight_words = state.get('highlight_words')
        
        template_name = self.generator.TEMPLATES[template]['name']
        await query.message.reply_text(f"⏳ Generando carrusel con plantilla {template_name}...\nEsto puede tomar unos segundos...")
        
        try:
            # Generar carrusel
            output_paths = self.carousel_generator.generate_carousel(
                content=content,
                carousel_type='auto',
                template=template,
                title=title,
                subtitle=subtitle,
                cta_text=cta,
                highlight_words=highlight_words
            )
            
            # Enviar las imágenes como álbum (máximo 10 imágenes en Telegram)
            media_group = []
            for i, path in enumerate(output_paths[:10]):  # Telegram permite máx 10 imágenes
                with open(path, 'rb') as photo:
                    media_group.append({
                        'type': 'photo',
                        'media': photo.read()
                    })
            
            caption = f"✅ **Tu carrusel está listo!**\n\n"
            caption += f"📱 Total de slides: {len(output_paths)}\n"
            caption += f"🎨 Plantilla: {template_name}\n"
            if highlight_words:
                caption += f"✨ Palabras destacadas: {', '.join(highlight_words)}\n"
            caption += "\n💡 Sube las imágenes a Instagram en orden"
            
            # Nota: Telegram no soporta media_group directamente con archivos abiertos
            # Enviar imágenes una por una
            for i, path in enumerate(output_paths[:10], 1):
                with open(path, 'rb') as photo:
                    if i == 1:
                        await query.message.reply_photo(photo=photo, caption=caption, parse_mode='Markdown')
                    else:
                        await query.message.reply_photo(photo=photo)
                
                # Limpiar archivo temporal
                os.remove(path)
            
            if len(output_paths) > 10:
                await query.message.reply_text(
                    f"⚠️ Se generaron {len(output_paths)} imágenes, pero Telegram solo permite enviar 10 a la vez.\n"
                    f"Usa la versión web para obtener todas las imágenes."
                )
            
            logger.info(f"Carrusel generado para usuario {user_id} con {len(output_paths)} imágenes")
            
        except Exception as e:
            logger.error(f"Error generando carrusel: {e}")
            import traceback
            logger.error(traceback.format_exc())
            await query.message.reply_text(
                f"❌ Error al generar el carrusel: {str(e)}\n\nPor favor intenta de nuevo."
            )
    
    async def error_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Manejar errores"""
        logger.error(f"Error: {context.error}")
        if update and update.effective_message:
            await update.effective_message.reply_text(
                "❌ Ocurrió un error. Por favor intenta de nuevo."
            )
    
    def run(self):
        """Iniciar el bot"""
        logger.info("Iniciando bot...")
        
        # Verificar token
        if self.token == 'YOUR_BOT_TOKEN_HERE':
            logger.error("⚠️  TELEGRAM_BOT_TOKEN no configurado!")
            logger.error("Por favor configura la variable de entorno TELEGRAM_BOT_TOKEN")
            return
        
        # Crear aplicación
        application = Application.builder().token(self.token).build()
        
        # Registrar handlers
        application.add_handler(CommandHandler("start", self.start))
        application.add_handler(CommandHandler("help", self.help_command))
        application.add_handler(CommandHandler("templates", self.templates_command))
        application.add_handler(CommandHandler("carousel", self.carousel_command))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))
        application.add_handler(CallbackQueryHandler(self.button_callback))
        application.add_error_handler(self.error_handler)
        
        # Iniciar bot
        logger.info("✅ Bot iniciado correctamente")
        logger.info("Presiona Ctrl+C para detener")
        application.run_polling(allowed_updates=Update.ALL_TYPES)


def main():
    """Función principal"""
    bot = TelegramQuoteBot(TELEGRAM_BOT_TOKEN)
    bot.run()


if __name__ == '__main__':
    main()
