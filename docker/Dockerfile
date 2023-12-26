# Utiliza una imagen base de Jupyter Notebook
FROM jupyter/base-notebook:python-3.8.8

WORKDIR /home/jovyan
RUN mkdir samuel

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt /home/jovyan/samuel

# Instala las dependencias desde requirements.txt
RUN pip install --no-cache-dir -r samuel/requirements.txt


# Comando para iniciar Jupyter Notebook
CMD ["jupyter", "lab", "--ServerApp.token=''"]
