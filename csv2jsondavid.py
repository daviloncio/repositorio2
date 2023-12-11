import csv;import json;import sys;from pathlib import Path;import ast
#usar ratings
#los vals num que ocurren a nivel superior como el id o revenue se tratan comom cadenas , son cols a evaluar
#con ast literal eval 
#en el json.columns deben estar aquellas columnas con las que vayamos a usar ast_literal eval,
#son las numericas y las que son json

#no hay que hacerlo para los 19 archivos ,que se podria, sino para los originalisimos de la p1
#movies.metedate.csv, su json cols sería id,belong to...,production_comapnies.....

#quiero leer cada una de las columnas del csv y reescribirlas en un json.

#usar ratings small, no es del todo necesario usar links_small porque no es tan pequño

d={'links_small.csv':['movieId','imdbId','tmdbId'],
   'credits.csv':['cast','crew','id'],
   'ratings_small.csv':['userId','movieId','rating','timestamp'],
   'ratings.csv':['userId','movieId','rating','timestamp'],
   'links.csv':['movieId','imdbId','tmdbId'],
   'keywords.csv':['id', 'keywords'],
   'movies_metadata.csv':['belongs_to_collection','budget','genres','id','imdb_id','popularity','production_companies','production_countries','release_date','revenue','runtime','spoken_languages','vote_average','vote_count'],}

def desde_csv_a_json(archivo_name,ruta_entrada_csv='csv',ruta_salida_json='json',json_columns=[]): #directorio 

    
    with open(f"{ruta_entrada_csv}/{archivo_name}", mode='r', encoding='utf-8') as f:  #leemos el archivo nombre_csv que está en el directorio csv
        reader = csv.DictReader(f)
        data = [row for row in reader] #lista de diccionarios


# Evaluate the json columns, which are quoted, to convert them into a dictionary or list of dictionaries
# print(type(data[0]), data[0])
    for row in data:
        for col in json_columns:
            try:
                # evaluate row[col] as dict or list of dicts
                row[col] = ast.literal_eval(row[col]) #convertimos una cadena a json 
                #si se evalua el id, no me lo convierte en string, por eso debo pasarlo por el literal eval
                # print(f"SETTING {col} TO {row[col]}")
            except Exception as e:
                pass  # ignore - not a good practice, in general

    # Write JSON output to file
    json_file = Path(archivo_name).with_suffix('.json')
    with open(f"{ruta_salida_json}/{json_file}", mode='w') as f:
        json.dump(data, f)

'''desde_csv_a_json(archivo_name='links_small.csv',
                 ruta_entrada_csv='c:/Users/juanj/Documents/3ercuatri/modelado/modelado_p1',
                 ruta_salida_json='c:/Users/juanj/Documents/3ercuatri/modelado/modelado_p4/pruebas_json',
                 json_columns = d['links_small.csv'])'''


if __name__ == '__main__' :
    if len(sys.argv)==1: #ejecutamos todo con los args por defecto
        csv_dir,json_dir='c:/Users/juanj/Documents/3ercuatri/modelado/modelado_p1','c:/Users/juanj/Documents/3ercuatri/modelado/modelado_p4/pruebas_json'
    else:
        csv_dir = sys.argv [1]
        json_dir = sys.argv [2]
    
    desde_csv_a_json(archivo_name='link_ids.csv',ruta_entrada_csv=csv_dir,ruta_salida_json=json_dir, json_columns = d['links_small.csv'])
    desde_csv_a_json(archivo_name='ratings_small.csv',ruta_entrada_csv=csv_dir,ruta_salida_json=json_dir, json_columns = d['ratings_small.csv'])
    desde_csv_a_json(archivo_name='movies_metadata.csv',ruta_entrada_csv=csv_dir,ruta_salida_json=json_dir, json_columns = d['movies_metadata.csv'])
    desde_csv_a_json(archivo_name='credits.csv',ruta_entrada_csv=csv_dir,ruta_salida_json=json_dir, json_columns = d['credits.csv'])
    desde_csv_a_json(archivo_name='keywords.csv',ruta_entrada_csv=csv_dir,ruta_salida_json=json_dir, json_columns = d['keywords.csv'])
    
    