
# Ejercicio 2: Palíndromos.

def convertir_a_minusculas(palabra):
    for i in palabra:
        if i.isupper():
            palabra = palabra.lower()
    return palabra

def quitar_espacios(palabra):
    for i in palabra:
        if i == " ":
            palabra = palabra.replace(" ", "")
    return palabra

def quitar_signos(palabra):
    for i in palabra:
        if i == "," or i == "." or i == ";" or i == ":" or i == "?" or i == "¿" or i == "!" or i == "¡":
            palabra = palabra.replace(",", "")
            palabra = palabra.replace(".", "")
            palabra = palabra.replace(";", "")
            palabra = palabra.replace(":", "")
            palabra = palabra.replace("?", "")
            palabra = palabra.replace("¿", "")
            palabra = palabra.replace("!", "")
            palabra = palabra.replace("¡", "")
    return palabra

def quitar_acentos(palabra):
    for i in palabra:
        if i == "á" or i == "é" or i == "í" or i == "ó" or i == "ú":
            palabra = palabra.replace("á", "a")
            palabra = palabra.replace("é", "e")
            palabra = palabra.replace("í", "i")
            palabra = palabra.replace("ó", "o")
            palabra = palabra.replace("ú", "u")
    return palabra

def comprobar_palindromo(palabra):
    palabra = palabra[::-1]
    if palabra == palabra:
        print(palabra,"es un palíndromo. \n")
    else:
        print(palabra,"no es un palíndromo. \n")

def converti_a_polindromos():
    palabra_a_comprovar = input("Introduce una palabra para convertirla a palíndromo: ")

    palabra_a_comprovar = convertir_a_minusculas(palabra_a_comprovar)
    palabra_a_comprovar = quitar_espacios(palabra_a_comprovar)
    palabra_a_comprovar = quitar_signos(palabra_a_comprovar)
    palabra_a_comprovar = quitar_acentos(palabra_a_comprovar)
    comprobar_palindromo(palabra_a_comprovar)

converti_a_polindromos()