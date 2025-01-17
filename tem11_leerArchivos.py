from io import open

fichero=open('fichero.txt','r')
texto=fichero.readline()
print(texto) 
print(type(texto))
fichero.close()

for i in texto:
    print(i)

