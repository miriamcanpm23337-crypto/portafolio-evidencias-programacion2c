"""
Control de asistencia   
"""
asistencia = []
materia_fav = {}

opcion = input("¿Desea registrar la asistencia? (s/n): ")
while opcion.lower() == 's':
    nombre = input("Ingrese el nombre del estudiante: ")
    asistencia.append(nombre)
    materia = input("Ingrese la materia favorita del estudiante: ")
    materia_fav[nombre] = materia
    opcion = input("¿Desea registrar la asistencia? (s/n): ")

asistencia_unica = set(asistencia) #convirtiendo la lista de asistencia a un conjunto para eliminar duplicados    
print("Lista de estudiantes presentes:")
for estudiante in asistencia_unica:
    print(estudiante)
print("Materias favoritas:")

for nombre, materia in materia_fav.items():
    print(f"{nombre}: {materia}")

