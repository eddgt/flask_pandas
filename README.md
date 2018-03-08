## Aplicacion que lee archivos xlsx y crea un Data Frame html, tambien contiene un tema de material design integrado

### Pasos para instalar

#### 1  crear un entorno virtual para python (se requiere tener virtualenv instalado):

    1.1 en linux  
    virtualenv nombre_entorno
        
    1.2 en windows (usa la ubicacion y version que tengas instalada en tu windows)   
    virtualenv -p C:\Python27\python.exe nombre_entorno

#### iniciar el entorno virtual de python
    2. source nombre_entorno/bin/activate

#### instalar Flask
    3. pip install Flask

#### instalar pandas
    4. pip install pandas

#### install lector de xlsx
    5. pip install xlrd

#### clonar repositorio
    3. git clone https://github.com/eddgt/flask_pandas.git

#### levantar aplicacion
    4. sh run.sh or ./run.sh

        debe mostrar lo siguiente en consola
        * Restarting with stat
        * Debugger is active!
        * Debugger PIN: 326-808-704
        * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

#### Listo!