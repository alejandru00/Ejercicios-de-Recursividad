
#Definimos la tabla y los valores
tabla = [1,2,3,4,5,6,7,8]
n = int(input('Introduzca el valor que desea encontrar:'))
i = 0
j = len(tabla)
m = (i+j)/2


def busqueda_numero():
    if i > j:
      return'No hay ningún valor en la posición seleccionada'
      
    else:
      m = m
      if tabla[m] == n:
        return m
      elif tabla[m] > n:
        print(busqueda_numero())
        return busqueda_numero(m -1)
      else:
        return busqueda_numero(m + 1)
        

resultado = busqueda_numero(tabla,n,j,i)
print(resultado.busqueda_numero())