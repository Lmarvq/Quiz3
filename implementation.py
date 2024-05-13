from clases import *
def main():
    while True:
        print("Bienvenido al sistema X!\nDestinado para la manipulación de imágenes y archivos DICOM")
        menu = int(input("Acciones a ejecutar:\n 1.Carga de datos de un paciente(DICOM)\n 2.Carga de imágenes JPG o PNG\n 3.Rotación de imágenes\n 4.Binarización de imágenes\n 5.Salir\n Usted escogió: "))
        if menu == 1:
            Leer_Asignar_Info()
            continue
        if menu == 2:
            Asignar_Im()
            continue
        if menu == 3:
            pass
        if menu == 4:
            pass
        if menu == 5:
            op1_5 = int(input("¿Desea cerrar el programa?:\n 1.Si\n 2.No\n Usted eligió: "))
            if op1_5 == 1: 
                break
            if op1_5 == 2:
                continue
            else:
                print("Por favor ingrese una opción válida")
                continue
            
main()