#primero se importa la biblioteca pandas para poder usar el dataframe
import pandas as pd 
#luego se importa el archivo en la variable csvfile
rutaFileCsv = "https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true"

#definicion de la funcion
def listaPeliculas (rutaFileCsv: str):
    #primero verificar que el archivo sea csv
    if rutaFileCsv.split(".")[-1]=='csv?raw=true':
        try:
            #leer el archivo csv 
            csv= pd.read_csv(rutaFileCsv)
            #realizar un subgrupo donde se leera las tres filas necesarias: country language y gross earnings
            subGrupoPeliculas = csv[["Country", "Language", "Gross Earnings"]]
            #se crea la tabla dinamica con pivot_table con country y language
            gananciaPaisLenguaje = subGrupoPeliculas.pivot_table(index=["Country", "Language"])
            #se regresa solo diez registros
            return gananciaPaisLenguaje.head(10)
        except:
            return "Error al leer el archivo de datos."
    else:
        return "Extensión inválida."


print (listaPeliculas(rutaFileCsv))