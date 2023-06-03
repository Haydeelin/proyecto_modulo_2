# Proyecto modulo 2 

palabra= input( "Enter a word that contains 4 to 8 characters: ")
longitud= len(palabra)

# Validar que la longitud sea la correcta

if longitud >= 4 and longitud <= 8:
    print("The word and its length are correct")

# Si la palabra tiene menos de 4 letras, indicar un mensaje que diga: su palabra es incorrecta tiene "N" letras. Faltan letras

if longitud < 4:
    print(f"Letters are needed. You only have {longitud} letters")

# Si la palabra tiene mas de 8 letras, indicar un mensaje que diga: su palabra es incorrecta tiene "N" letras. Sobran letras


if longitud >  8:
    print(f"Too many letters. Have {longitud} letters")
    


