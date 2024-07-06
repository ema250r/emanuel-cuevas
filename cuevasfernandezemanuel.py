def prosesar_lista():
    print("prosesamos la lista de los estudiantes")

def registrar_estudiante():
    print("registrar estudiante")
    print("porfavor ingrese sus datos")
    rut=int(input("porfavor ingrese su rut :"))
    nombre=str(input("ingrese su nombre :"))
    nota1=int(input("ingrese su primer nota :"))
    nota2=int(input("ingrese su segunda nota :"))
    print("resgistro de estudiante")
    registro_deestudiante_nuevo={
        "rut",rut,
        "nombre",nombre,
        "nota1",nota1,
        "nota2",nota2, }
      
    
def modificar_nota():
    calificaciones=[]
    rut=input("ingresa tu rut :")
    for estudiante in calificaciones():
        if estudiante["rut"]==rut:
            nota_a_modificar=(input("ingrese la nota que quiere modificar, nota1 o nota2 "))
            if(nota_a_modificar==1):
                nueva_nota=(input("ingrese la nueva nota 1 :"))
                estudiante["nota1"]=nueva_nota
                print("nota modificada")
            elif(nota_a_modificar==2):
                nueva_nota=(input("ingrese la nueva nota 2 :"))
                estudiante["nota2"]=nueva_nota
                print("nota modificada")




def eliminar_estudiante():
    print("eliminar estudiante")

s
def generar_promedio_de_notas():
    print("")

def generar_acta_de_cierre_de_curso():
    print("")