# #Ejecuta todo
echo "SI NO TIENES LA CARPETA 'data' CON LOS DATOS TE VA A PETAR "
echo "TIENES 10s PARA HACER CTRL-C :D"
sleep 10
cd juntar_database
mkdir diccionarios
echo "Creamos diccionario de links"
python3 crear_dic_links.py
cd ..
cd generos
mkdir diccionarios
echo "Creamos diccionario de generos"
python3 crear_dic_genero.py
cd ..
cd pelicula
mkdir diccionarios
echo "Creamos diccionario de pelicula"
python3 crear_dic_pelicula.py
cd ..
cd cast
mkdir diccionarios
echo "Creamos diccionario cast"
python3 crear_tabla_cast.py
cd ..
cd crew
mkdir diccionarios
echo "Creamos diccionario crew"
python3 crear_tabla_crew.py
cd ..
cd personas
mkdir diccionarios
echo "Creamos diccionario personas"
python3 crear_dic_personas.py
cd ..
cd titulos
mkdir diccionarios
echo "Creamos diccionario titulos"
python3 titulos2dic.py
cd ..
cd votos
mkdir diccionarios
echo "Creamos diccionario votos (Tardara un rato)"
python3 crear_dic_votos.py
cd ..
cd TABLAS
mkdir tablas
echo "Creando tablas"
python3 crear_tablas.py