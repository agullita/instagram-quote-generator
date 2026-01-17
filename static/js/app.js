/**
 * Instagram Quote Generator - Frontend Application
 */

// Estado de la aplicación
const appState = {
    templates: {},
    selectedTemplate: 'minimal',
    currentFilename: null,
    mode: 'single' // 'single' o 'carousel'
};

// Inicialización
document.addEventListener('DOMContentLoaded', () => {
    loadTemplates();
    setupEventListeners();
});

/**
 * Cargar plantillas disponibles desde el backend
 */
async function loadTemplates() {
    try {
        const response = await fetch('/api/templates');
        const data = await response.json();
        
        if (data.success) {
            appState.templates = data.templates;
            renderTemplates();
        } else {
            showMessage('Error al cargar plantillas', 'error');
        }
    } catch (error) {
        console.error('Error loading templates:', error);
        showMessage('Error de conexión con el servidor', 'error');
    }
}

/**
 * Renderizar las plantillas en la interfaz
 */
function renderTemplates() {
    const container = document.getElementById('templateSelector');
    container.innerHTML = '';
    
    // Colores de preview para cada plantilla
    const previewColors = {
        'minimal': '#FFFFFF',
        'dark': '#14141E',
        'vibrant': '#FF5733',
        'ocean': '#3498DB',
        'sunset': '#FF6F61',
        'forest': '#27AE60',
        'geometric1': '#FFF8F0',
        'geometric2': '#FFFFFF'
    };
    
    // Iconos para cada plantilla
    const previewIcons = {
        'minimal': '✨',
        'dark': '🌙',
        'vibrant': '🎨',
        'ocean': '🌊',
        'sunset': '🌅',
        'forest': '🌲',
        'geometric1': '🔶',
        'geometric2': '📐'
    };
    
    for (const [key, template] of Object.entries(appState.templates)) {
        const templateDiv = document.createElement('div');
        templateDiv.className = 'template-option';
        if (key === appState.selectedTemplate) {
            templateDiv.classList.add('active');
        }
        
        templateDiv.innerHTML = `
            <div class="template-preview" style="background-color: ${previewColors[key] || '#ccc'}">
                ${previewIcons[key] || '🎨'}
            </div>
            <div class="template-name">${template.name}</div>
            <div class="template-description">${template.description}</div>
        `;
        
        templateDiv.addEventListener('click', () => selectTemplate(key));
        container.appendChild(templateDiv);
    }
}

/**
 * Seleccionar una plantilla
 */
function selectTemplate(templateKey) {
    appState.selectedTemplate = templateKey;
    
    // Actualizar UI
    document.querySelectorAll('.template-option').forEach(el => {
        el.classList.remove('active');
    });
    event.currentTarget.classList.add('active');
}

/**
 * Configurar event listeners
 */
function setupEventListeners() {
    // Selector de modo (Imagen única vs Carrusel)
    const modeButtons = document.querySelectorAll('.mode-btn');
    modeButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            const mode = btn.getAttribute('data-mode');
            switchMode(mode);
        });
    });
    
    // Contador de caracteres
    const quoteTextarea = document.getElementById('quote');
    const charCount = document.getElementById('charCount');
    
    quoteTextarea.addEventListener('input', () => {
        const count = quoteTextarea.value.length;
        charCount.textContent = count;
        
        if (count > 450) {
            charCount.style.color = 'var(--danger-color)';
        } else {
            charCount.style.color = 'var(--text-light)';
        }
    });
    
    // Submit del formulario
    const form = document.getElementById('quoteForm');
    form.addEventListener('submit', handleFormSubmit);
    
    // Botón de descarga
    const downloadBtn = document.getElementById('downloadBtn');
    downloadBtn.addEventListener('click', downloadImage);
}

/**
 * Cambiar entre modo imagen única y carrusel
 */
function switchMode(mode) {
    appState.mode = mode;
    
    // Actualizar botones activos
    document.querySelectorAll('.mode-btn').forEach(btn => {
        btn.classList.remove('active');
        if (btn.getAttribute('data-mode') === mode) {
            btn.classList.add('active');
        }
    });
    
    // Mostrar/ocultar campos de carrusel
    const carouselFields = document.getElementById('carouselFields');
    if (mode === 'carousel') {
        carouselFields.style.display = 'block';
    } else {
        carouselFields.style.display = 'none';
    }
}

/**
 * Manejar el envío del formulario
 */
async function handleFormSubmit(event) {
    event.preventDefault();
    
    if (appState.mode === 'carousel') {
        await handleCarouselSubmit();
    } else {
        await handleSingleImageSubmit();
    }
}

/**
 * Manejar envío para imagen única
 */
async function handleSingleImageSubmit() {
    const quote = document.getElementById('quote').value.trim();
    const author = document.getElementById('author').value.trim();
    const highlightWords = document.getElementById('highlightWords').value.trim();
    const template = appState.selectedTemplate;
    
    // Validaciones
    if (!quote) {
        showMessage('Por favor, escribe una frase', 'error');
        return;
    }
    
    // Procesar palabras a destacar
    let highlightArray = null;
    if (highlightWords) {
        highlightArray = highlightWords
            .split(',')
            .map(word => word.trim())
            .filter(word => word.length > 0);
    }
    
    // Mostrar estado de carga
    const generateBtn = document.getElementById('generateBtn');
    const btnText = generateBtn.querySelector('.btn-text');
    const btnLoading = generateBtn.querySelector('.btn-loading');
    
    generateBtn.disabled = true;
    btnText.style.display = 'none';
    btnLoading.style.display = 'flex';
    
    try {
        // Enviar petición al backend
        const response = await fetch('/api/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                quote: quote,
                author: author || null,
                template: template,
                highlight_words: highlightArray
            })
        });
        
        const data = await response.json();
        
        if (data.success) {
            // Guardar nombre del archivo
            appState.currentFilename = data.filename;
            
            // Mostrar imagen
            displayImage(data.filename);
            
            // Mostrar mensaje de éxito
            showMessage('✨ ¡Imagen generada exitosamente!', 'success');
        } else {
            showMessage(data.error || 'Error al generar la imagen', 'error');
        }
        
    } catch (error) {
        console.error('Error:', error);
        showMessage('Error de conexión con el servidor', 'error');
    } finally {
        // Restaurar botón
        generateBtn.disabled = false;
        btnText.style.display = 'inline';
        btnLoading.style.display = 'none';
    }
}

/**
 * Manejar envío para carrusel
 */
async function handleCarouselSubmit() {
    const content = document.getElementById('quote').value.trim();
    const highlightWords = document.getElementById('highlightWords').value.trim();
    const template = appState.selectedTemplate;
    const title = document.getElementById('carouselTitle').value.trim();
    const subtitle = document.getElementById('carouselSubtitle').value.trim();
    const ctaText = document.getElementById('carouselCTA').value.trim();
    const carouselType = document.getElementById('carouselType').value;
    const carouselSize = document.getElementById('carouselSize').value;
    
    // Validaciones
    if (!content) {
        showMessage('Por favor, escribe el contenido del carrusel', 'error');
        return;
    }
    
    // Procesar palabras a destacar
    let highlightArray = null;
    if (highlightWords) {
        highlightArray = highlightWords
            .split(',')
            .map(word => word.trim())
            .filter(word => word.length > 0);
    }
    
    // Procesar contenido según el tipo
    let processedContent = content;
    if (carouselType === 'list') {
        // Dividir por líneas para modo manual
        processedContent = content.split('\n').filter(line => line.trim().length > 0);
    }
    
    // Mostrar estado de carga
    const generateBtn = document.getElementById('generateBtn');
    const btnText = generateBtn.querySelector('.btn-text');
    const btnLoading = generateBtn.querySelector('.btn-loading');
    
    generateBtn.disabled = true;
    btnText.style.display = 'none';
    btnLoading.style.display = 'flex';
    btnLoading.querySelector('span:last-child').textContent = 'Generando carrusel...';
    
    try {
        // Enviar petición al backend
        const response = await fetch('/api/generate-carousel', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                content: processedContent,
                carousel_type: carouselType,
                template: template,
                title: title || null,
                subtitle: subtitle || null,
                cta_text: ctaText || null,
                highlight_words: highlightArray,
                size: carouselSize
            })
        });
        
        if (response.ok) {
            // Descargar el archivo ZIP
            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `carousel_${template}_${Date.now()}.zip`;
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
            document.body.removeChild(a);
            
            // Mostrar mensaje de éxito
            showMessage('🎉 ¡Carrusel generado y descargado exitosamente!', 'success');
            
            // Mostrar información en el área de resultado
            const resultArea = document.getElementById('resultArea');
            resultArea.innerHTML = `
                <div style="text-align: center; padding: 40px;">
                    <div style="font-size: 80px; margin-bottom: 20px;">📱✨</div>
                    <h3 style="margin-bottom: 10px;">¡Carrusel Generado!</h3>
                    <p style="color: var(--text-light);">El archivo ZIP con todas las imágenes se ha descargado.</p>
                    <p style="margin-top: 20px; padding: 15px; background: var(--bg-light); border-radius: 8px;">
                        💡 <strong>Tip:</strong> Descomprime el ZIP y sube las imágenes a Instagram en orden.
                    </p>
                </div>
            `;
        } else {
            const data = await response.json();
            showMessage(data.error || 'Error al generar el carrusel', 'error');
        }
        
    } catch (error) {
        console.error('Error:', error);
        showMessage('Error de conexión con el servidor', 'error');
    } finally {
        // Restaurar botón
        generateBtn.disabled = false;
        btnText.style.display = 'inline';
        btnLoading.style.display = 'none';
        btnLoading.querySelector('span:last-child').textContent = 'Generando...';
    }
}

/**
 * Mostrar la imagen generada
 */
function displayImage(filename) {
    const resultArea = document.getElementById('resultArea');
    const downloadSection = document.getElementById('downloadSection');
    
    // Crear elemento de imagen con timestamp para evitar caché
    const timestamp = new Date().getTime();
    resultArea.innerHTML = `
        <img 
            src="/api/preview/${filename}?t=${timestamp}" 
            alt="Imagen generada" 
            class="result-image"
        >
    `;
    
    // Mostrar sección de descarga
    downloadSection.style.display = 'block';
}

/**
 * Descargar la imagen
 */
function downloadImage() {
    if (!appState.currentFilename) {
        showMessage('No hay imagen para descargar', 'error');
        return;
    }
    
    // Crear enlace de descarga
    const link = document.createElement('a');
    link.href = `/api/download/${appState.currentFilename}`;
    link.download = appState.currentFilename;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    
    showMessage('📥 Descargando imagen...', 'success');
}

/**
 * Mostrar mensaje temporal
 */
function showMessage(text, type = 'success') {
    const container = document.getElementById('messageContainer');
    
    const message = document.createElement('div');
    message.className = `message message-${type}`;
    message.innerHTML = `
        <span class="message-close" onclick="this.parentElement.remove()">×</span>
        ${text}
    `;
    
    container.appendChild(message);
    
    // Auto-eliminar después de 5 segundos
    setTimeout(() => {
        if (message.parentElement) {
            message.remove();
        }
    }, 5000);
}

// Exponer funciones globales para uso en HTML
window.selectTemplate = selectTemplate;
