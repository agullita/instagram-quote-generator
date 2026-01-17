"""
Generador de Carruseles para Instagram
Crea múltiples imágenes conectadas para posts de carrusel
"""
from PIL import Image, ImageDraw, ImageFont
import os
from datetime import datetime
from image_generator import InstagramQuoteGenerator


class CarouselGenerator:
    """Genera carruseles de Instagram con múltiples slides"""
    
    # Tamaños de Instagram
    SQUARE = (1080, 1080)
    VERTICAL = (1080, 1350)
    HORIZONTAL = (1080, 566)
    
    def __init__(self, output_dir='output/carousels'):
        """
        Inicializa el generador de carruseles
        
        Args:
            output_dir: Directorio donde se guardarán los carruseles
        """
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        self.image_generator = InstagramQuoteGenerator()
        
    def _get_font(self, size=60):
        """Obtiene una fuente del sistema"""
        return self.image_generator._get_font(size)
    
    def _draw_slide_number(self, image, current, total, template_config):
        """
        Dibuja el número de slide en la esquina
        
        Args:
            image: Imagen PIL
            current: Número de slide actual
            total: Total de slides
            template_config: Configuración de la plantilla
        """
        draw = ImageDraw.Draw(image)
        font = self._get_font(30)
        
        text = f"{current}/{total}"
        bbox = font.getbbox(text)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        # Posición en la esquina superior derecha
        x = image.size[0] - text_width - 30
        y = 30
        
        # Fondo semi-transparente
        padding = 10
        bg_img = Image.new('RGBA', image.size, (255, 255, 255, 0))
        bg_draw = ImageDraw.Draw(bg_img)
        bg_draw.rounded_rectangle(
            [x - padding, y - padding, x + text_width + padding, y + text_height + padding],
            radius=15,
            fill=(*template_config['accent_color'], 180)
        )
        
        image.paste(bg_img, (0, 0), bg_img)
        draw = ImageDraw.Draw(image)
        draw.text((x, y), text, font=font, fill=template_config['text_color'])
        
    def _draw_swipe_indicator(self, image, template_config):
        """
        Dibuja un indicador de 'desliza para más'
        
        Args:
            image: Imagen PIL
            template_config: Configuración de la plantilla
        """
        draw = ImageDraw.Draw(image)
        font = self._get_font(24)
        
        text = "← Desliza →"
        bbox = font.getbbox(text)
        text_width = bbox[2] - bbox[0]
        
        # Posición en la parte inferior central
        x = (image.size[0] - text_width) // 2
        y = image.size[1] - 60
        
        draw.text((x, y), text, font=font, fill=template_config['accent_color'])
        
    def create_cover_slide(self, title, subtitle=None, template='minimal', size=SQUARE):
        """
        Crea un slide de portada
        
        Args:
            title: Título principal
            subtitle: Subtítulo (opcional)
            template: Plantilla de diseño
            size: Tamaño de la imagen
            
        Returns:
            Imagen PIL
        """
        template_config = self.image_generator.TEMPLATES[template]
        
        # Crear imagen de fondo
        if template_config.get('bg_image'):
            try:
                image = Image.open(template_config['bg_image'])
                if image.size != size:
                    image = image.resize(size, Image.Resampling.LANCZOS)
                if image.mode != 'RGB':
                    image = image.convert('RGB')
            except:
                image = Image.new('RGB', size, template_config['bg_color'])
        else:
            image = Image.new('RGB', size, template_config['bg_color'])
        
        draw = ImageDraw.Draw(image)
        
        # Título grande y centrado
        title_font = self._get_font(100)
        
        # Dividir título en líneas si es necesario
        max_width = size[0] - 160
        words = title.split()
        lines = []
        current_line = []
        
        for word in words:
            test_line = ' '.join(current_line + [word])
            bbox = title_font.getbbox(test_line)
            if bbox[2] - bbox[0] <= max_width:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]
        if current_line:
            lines.append(' '.join(current_line))
        
        # Calcular posición vertical
        line_height = 120
        total_height = len(lines) * line_height
        if subtitle:
            total_height += 100
        
        y = (size[1] - total_height) // 2
        
        # Dibujar título
        for line in lines:
            bbox = title_font.getbbox(line)
            text_width = bbox[2] - bbox[0]
            x = (size[0] - text_width) // 2
            draw.text((x, y), line, font=title_font, fill=template_config['text_color'])
            y += line_height
        
        # Dibujar subtítulo
        if subtitle:
            y += 40
            subtitle_font = self._get_font(40)
            bbox = subtitle_font.getbbox(subtitle)
            text_width = bbox[2] - bbox[0]
            x = (size[0] - text_width) // 2
            draw.text((x, y), subtitle, font=subtitle_font, fill=template_config['accent_color'])
        
        return image
    
    def create_content_slide(self, text, slide_number, total_slides, template='minimal', 
                            highlight_words=None, size=SQUARE):
        """
        Crea un slide de contenido
        
        Args:
            text: Texto del slide
            slide_number: Número de este slide
            total_slides: Total de slides en el carrusel
            template: Plantilla de diseño
            highlight_words: Palabras a destacar
            size: Tamaño de la imagen
            
        Returns:
            Imagen PIL
        """
        template_config = self.image_generator.TEMPLATES[template]
        
        # Crear imagen de fondo
        if template_config.get('bg_image'):
            try:
                image = Image.open(template_config['bg_image'])
                if image.size != size:
                    image = image.resize(size, Image.Resampling.LANCZOS)
                if image.mode != 'RGB':
                    image = image.convert('RGB')
            except:
                image = Image.new('RGB', size, template_config['bg_color'])
        else:
            image = Image.new('RGB', size, template_config['bg_color'])
        
        draw = ImageDraw.Draw(image)
        
        # Calcular tamaño de fuente adaptativo
        max_width = size[0] - 160
        max_height = size[1] - 300
        
        adaptive_font_size = self.image_generator._calculate_adaptive_font_size(
            text, 60, max_width, max_height
        )
        
        font = self._get_font(adaptive_font_size)
        lines = self.image_generator._wrap_text(text, font, max_width)
        
        # Calcular posición
        line_height = adaptive_font_size + 20
        total_text_height = len(lines) * line_height
        y = (size[1] - total_text_height) // 2
        
        # Preparar palabras destacadas
        highlight_set = set()
        if highlight_words:
            highlight_set = {word.lower().strip() for word in highlight_words}
        
        # Dibujar texto
        for line in lines:
            bbox = font.getbbox(line)
            text_width = bbox[2] - bbox[0]
            x = (size[0] - text_width) // 2
            
            if not highlight_set:
                draw.text((x, y), line, font=font, fill=template_config['text_color'])
            else:
                current_x = x
                words = line.split()
                for word in words:
                    word_clean = word.strip('.,;:!?¡¿"\'()[]{}').lower()
                    color = template_config['accent_color'] if word_clean in highlight_set else template_config['text_color']
                    draw.text((current_x, y), word, font=font, fill=color)
                    word_bbox = font.getbbox(word + ' ')
                    current_x += word_bbox[2] - word_bbox[0]
            
            y += line_height
        
        # Añadir número de slide
        self._draw_slide_number(image, slide_number, total_slides, template_config)
        
        # Añadir indicador de deslizar (solo si no es el último)
        if slide_number < total_slides:
            self._draw_swipe_indicator(image, template_config)
        
        return image
    
    def create_closing_slide(self, text, cta_text=None, template='minimal', size=SQUARE):
        """
        Crea un slide de cierre con call to action
        
        Args:
            text: Texto principal
            cta_text: Texto del call to action (ej: "Sígueme para más")
            template: Plantilla de diseño
            size: Tamaño de la imagen
            
        Returns:
            Imagen PIL
        """
        template_config = self.image_generator.TEMPLATES[template]
        
        # Crear imagen de fondo
        if template_config.get('bg_image'):
            try:
                image = Image.open(template_config['bg_image'])
                if image.size != size:
                    image = image.resize(size, Image.Resampling.LANCZOS)
                if image.mode != 'RGB':
                    image = image.convert('RGB')
            except:
                image = Image.new('RGB', size, template_config['bg_color'])
        else:
            image = Image.new('RGB', size, template_config['bg_color'])
        
        draw = ImageDraw.Draw(image)
        
        # Texto principal
        main_font = self._get_font(80)
        bbox = main_font.getbbox(text)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        x = (size[0] - text_width) // 2
        y = (size[1] - text_height) // 2 - 50
        
        draw.text((x, y), text, font=main_font, fill=template_config['text_color'])
        
        # Call to action
        if cta_text:
            y += text_height + 80
            cta_font = self._get_font(40)
            bbox = cta_font.getbbox(cta_text)
            cta_width = bbox[2] - bbox[0]
            cta_height = bbox[3] - bbox[1]
            
            x = (size[0] - cta_width) // 2
            
            # Dibujar botón/caja para el CTA
            padding = 20
            draw.rounded_rectangle(
                [x - padding, y - padding, x + cta_width + padding, y + cta_height + padding],
                radius=25,
                fill=template_config['accent_color']
            )
            
            # Color de texto invertido para el CTA
            cta_text_color = (255, 255, 255) if sum(template_config['accent_color']) < 400 else (30, 30, 30)
            draw.text((x, y), cta_text, font=cta_font, fill=cta_text_color)
        
        return image
    
    def generate_carousel(self, content, carousel_type='auto', template='minimal',
                         title=None, subtitle=None, cta_text=None, 
                         highlight_words=None, size=SQUARE):
        """
        Genera un carrusel completo
        
        Args:
            content: Contenido del carrusel (puede ser texto largo o lista de textos)
            carousel_type: Tipo de carrusel ('auto', 'manual', 'list')
            template: Plantilla de diseño
            title: Título para slide de portada
            subtitle: Subtítulo para slide de portada
            cta_text: Call to action para slide final
            highlight_words: Palabras a destacar
            size: Tamaño de las imágenes
            
        Returns:
            Lista de rutas de archivos generados
        """
        images = []
        
        # 1. Slide de portada (si hay título)
        if title:
            cover = self.create_cover_slide(title, subtitle, template, size)
            images.append(cover)
        
        # 2. Slides de contenido
        if carousel_type == 'auto':
            # Dividir texto largo automáticamente
            if isinstance(content, str):
                # Dividir por longitud aproximada
                max_chars_per_slide = 150
                sentences = content.replace('!', '.').replace('?', '.').split('.')
                
                slides_text = []
                current_slide = []
                current_length = 0
                
                for sentence in sentences:
                    sentence = sentence.strip()
                    if not sentence:
                        continue
                    
                    if current_length + len(sentence) <= max_chars_per_slide:
                        current_slide.append(sentence)
                        current_length += len(sentence)
                    else:
                        if current_slide:
                            slides_text.append('. '.join(current_slide) + '.')
                        current_slide = [sentence]
                        current_length = len(sentence)
                
                if current_slide:
                    slides_text.append('. '.join(current_slide) + '.')
                
                content = slides_text
        
        elif carousel_type == 'list':
            # Contenido ya es una lista
            if not isinstance(content, list):
                content = [content]
        
        # Calcular total de slides
        total_slides = len(images) + len(content)
        if cta_text:
            total_slides += 1
        
        # Crear slides de contenido
        for i, text in enumerate(content, start=len(images) + 1):
            slide = self.create_content_slide(
                text, i, total_slides, template, highlight_words, size
            )
            images.append(slide)
        
        # 3. Slide de cierre (si hay CTA)
        if cta_text:
            closing = self.create_closing_slide("¡Gracias!", cta_text, template, size)
            images.append(closing)
        
        # Guardar imágenes
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_paths = []
        
        for i, img in enumerate(images, start=1):
            filename = f'carousel_{template}_{timestamp}_{i}.png'
            output_path = os.path.join(self.output_dir, filename)
            img.save(output_path, 'PNG', quality=95)
            output_paths.append(output_path)
        
        return output_paths


# Ejemplo de uso
if __name__ == '__main__':
    generator = CarouselGenerator()
    
    # Ejemplo 1: Carrusel automático con texto largo
    long_text = """
    La vida es una aventura maravillosa. Cada día trae nuevas oportunidades. 
    No importa cuántos obstáculos encuentres. Lo importante es seguir adelante. 
    La perseverancia es la clave del éxito. Nunca te rindas ante las dificultades.
    """
    
    paths = generator.generate_carousel(
        content=long_text,
        carousel_type='auto',
        template='minimal',
        title='5 Lecciones de Vida',
        subtitle='Aprende y crece',
        cta_text='Sígueme para más contenido',
        highlight_words=['vida', 'oportunidades', 'éxito']
    )
    
    print(f"Carrusel generado: {len(paths)} imágenes")
    for path in paths:
        print(f"  - {path}")
