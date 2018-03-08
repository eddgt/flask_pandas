## Aplicacion que lee archivos xlsx y crea un Data Frame html, tambien contiene un tema de material design integrado

## Step to install

# 1  crear un entorno virtual para python:

    # on linux
    1.1 virtualenv nombre_entorno
        
    # on windows    
    1.2 virtualenv -p C:\Python27\python.exe nombre_entorno

# iniciar el entorno virtual de python
2. source nombre_entorno/bin/activate

# instalar Flask
3. pip install Flask

# instalar pandas
4. pip install pandas

# install lector de xlsx
5. pip install xlrd

# clonar repositorio
3. git clone https://github.com/eddgt/flask_pandas.git

# levantar aplicacion
4. sh run.sh or ./run.sh

    debe mostrar lo siguiente en consola
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 326-808-704
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

# Listo!