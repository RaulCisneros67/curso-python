cadena1 = "hola soy Raul"
cadena2 = "bienvenido gilberto" 

#convierte a mayusculas
mayusc = cadena1.upper()

#convierte a minusculas
minusc = cadena1.lower()

#primera letra en mayuscula
primer_letra_mayusc = cadena1.capitalize()

#buscamos una cadena en otra cadena, si no hay concidencias devuelve -1
busqueda_find = cadena1.find("s")

#buscamos una cadena en otra cadena, si no hay concidencias lanza una excepcion  
busqueda_index = cadena1.index("s")

#si es numerico devuelve True, si no develve False
es_numerico = cadena1.isnumeric()

#si es alpha numerico devolvemos True, si no devolvemos False
es_alphanumerico = cadena1.isalpha()

#buscamos una cadena en otra cadena, devuelve la cantidad de veces que coincida
contar_coincidencias = cadena1.count()

#contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve True
empieza_con = cadena1.startswith()

#verificamos si una cadena Termina con otra cadena dada, si es asi devuelve True
termina_con = cadena1.endswith()

#remplaza un pedazo de la cadena dada, por otra dada
cadena_nueva = cadena1.replace(x, y)

#separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split()