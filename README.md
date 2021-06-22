# Proyecto de Lenguaje de Programación: Intérprete de Ruby

## Integrantes
- David Alarcón Galeas
- Manuel Loor Macías

## Comentarios:

Aviso importante. En caso de que desee evitar descargar todo el proyecto con librerías adicionales incluídas y solo requiera del archivo.py, lo que debe hacer es ingresar a la carpeta *Interprete_Ruby*, luego ingresar a *venv* y posteriormente a *Include* y encontrará el archivo *interpreteRuby.py*.

A continuación, se procede a detallar los aportes realizados por *Manuel Loor Macías*:

- Definición del diccionario /*reserved*/ que contiene las palabras reservadas escogidas para ser válidadas por el Analizador Léxico, tales como: puts/print (salida de datos), gets (entrada de datos), if, else, elsif, while, for, end, true, false, and, or, not, break, nil (palabra reservada que representa el valor nulo en Ruby).
- Definición del diccionario /*symbols*/ que contiene los símbolos y carácteres especiales utilizados con mayor frecuencia en Ruby, tales como: @,#,=,$,<,>,!,',"
- Definición del diccionario /*tokens*/ que contiene todos los tokens que implementaremos, por ejemplo, INTEGER (números enteros), STRING (Cadenas de carácteres), FLOAT (coma flotante), LBRACKET/RBRACKET ([]), lPAREN/RPAREN (), MODULUS (%), ADD (+), SUBSTRACT (-), MULTIPLY (*), DIVIDE (/). Y Además se adiccionó los tokens respectivos de cada símbolo o carácter especial al diccionario de Tokens.
- Creación de los módulos correspondientes para los tokens más generales.
-   t_STRING (valida cadenas de carácteres)
-   t_INTEGER (valida números enteros)
-   t_FLOAT (valida números decimales)
-   t_SYMBOLS (valida símbolos o carácteres especiales)

A continuación, se procede a detallar los aportes realizados por *David Alarcon Galeas*:

- Adicion al diccionario /*reserved*/ de las palabras reservadas escogidas para ser válidadas por el Analizador Léxico, tales como: in, do, then, class, alias, begin, def.
- Se desplazo ademas, del diccionario de tokens simples al diccionario de símbolos para una mejor distribución:
- Se removieron del diccionario /*tokens*/ LBRACKET/RBRACKET ([]), lPAREN/RPAREN (), MODULUS (%), ADD (+), SUBSTRACT (-), MULTIPLY (*), DIVIDE (/). Y Además se adiccionó los tokens respectivos de cada símbolo o carácter especial al diccionario de Tokens.
- - Se añadieron al diccionario /*symbols*/ los caracteres: [,],(,),%,+,-,*,/
