materias = ["Matemáticas", "Física", "Química","Química", "Biología", "Historia", "Geografía", "Literatura"]
materias.append("Inglés")
materias.insert(2, "Educación Física")
print(materias[2])

docente = ("Juan Pérez", "Fulanito Perez", "Perecila Sanchez")
print(docente[0])

conjunto = {1, 2, 3, 4, 5}
conjunto.add(6)
conjunto.add(6)
print(conjunto)

alumno = {"nombre": "Carlos", "edad": 20, "carrera": "Ingeniería"}
print(alumno["nombre"])
print(alumno["edad"])

print(materias)
lista_conjunto = list(conjunto) #convirtiendo el conjunto a una lista
conjunto_materias = set(materias) #convirtiendo la lista de materias a un conjunto
print(conjunto_materias)