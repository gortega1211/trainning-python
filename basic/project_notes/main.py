def run():
    students = list()
    students_qty = int(input("Ingrese la cantidad de Alumnos: "))
    notes_qty = int(input("Ingrese la cantidad de notas por Alumno: "))
    for i in range (0, students_qty):
        print(f"\nPara el 'Alumno {i+1}', ingrese los siguientes datos:")
        first_name = input("Nombre: ")
        last_name = input("Apellido: ")
        section = input("Sección: ")
        grade = input("Grado: ")
        notes = list()
        for j in range(0, notes_qty):
            flag = True
            while flag:
                note = input(f"Nota {j + 1} [0 - 20]: ")
                if int(note) and 0 <= int(note) <= 20:
                    flag = False
                else:
                    print("\nERROR:\nEl valor de la nota no pertenece a un rango válido.\nIngrese una nota dentro del rango [0 - 20]\n")
            notes.append(int(note))
        promedio = round(sum(notes) / len(notes), 2)
        print(f"El alumno {first_name} {last_name}, tiene un promedio de {promedio}.")
        print("Ha desaprobado el curso." if promedio < 10.5 else "Felicitaciones, aprobó el curso.")
        print(f"Su nota mayor es {max(notes)}.")
        print(f"Su nota menor es {min(notes)}.")

if __name__ == "__main__":
    run()