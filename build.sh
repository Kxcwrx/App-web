# Activar el entorno virtual
& "venv\Scripts\Activate.ps1"

# Actualizar pip
pip install --upgrade pip

# Instalar las dependencias
pip install -r requirements.txt

# Inicializar Reflex
reflex init

# Exportar solo el frontend
reflex export --frontend-only

# Eliminar la carpeta public si existe
Remove-Item -Recurse -Force public

# Descomprimir el archivo frontend.zip en la carpeta public
Expand-Archive -Path frontend.zip -DestinationPath public -Force

# Eliminar el archivo frontend.zip
Remove-Item -Force frontend.zip

# Desactivar el entorno virtual
deactivate
