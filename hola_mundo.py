texto = 'mrttaqrhknsw ih puggrur'
custom_key = 'python'

def vigenere(mensaje, llave, direccion=1):
    llave_index = 0
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    mensaje_final = ''

    '''
    index = alfabeto.find(mensaje[0].lower())
    print (index)
    shifted = alfabeto[index+shift]
    print (shifted)
    '''

    for char in mensaje.lower():
        #no encripta caracteres que no sean letras
        if not char.isalpha():
            mensaje_final += char
        else:
            #encuentra el caracter clave correcto para codificar
            llave_char = llave[llave_index%len(llave)]
            llave_index += 1
            #define el desplazamiento y la letra cifrada
            offset = alfabeto.index(llave_char)
            index = alfabeto.find(char)
            new_index = (index + offset*direccion) % len(alfabeto)
            mensaje_final += alfabeto[new_index]

    return mensaje_final

def encriptar (mensaje, llave):
    return vigenere(mensaje, llave)

def desencriptar(mensaje, llave):
    return vigenere(mensaje, llave, -1)

print(f'texto encriptado: {texto}')
print(f"llave: {custom_key}" )
#desencriptacion = desencriptar(encriptacion, custom_key)
#print(desencriptacion)

