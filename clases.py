import pydicom as pyd
import nilearn as nii
import dicom2nifti as d2n
import cv2 
import numpy as np
import matplotlib.pyplot as plt
import os


dict__pacientes = {}
dict__imágenes = {}


class Paciente():
    def __init__(self):
        self.__nombre = ""
        self.__edad = 0
        self.__ID = ""
        self.__IM_DICOM = ""
        self.__IM_Niftii = ""
    
    def AddNombre(self, n):
        self.__nombre = n
    def AddEdad(self, e):
        self.__edad = e
    def AddID(self, i):
        self.__ID = i
    def Add_IM_Dicom(self, d):
        self.__IM_DICOM = [d]
    def Add_IM_Niftii(self, f):
        self.__IM_Niftii = f

    def ObtenerNombre(self):
        return self.__nombre
    def ObtenerEdad(self):
        return self.__edad
    def ObtenerID(self):
        return self.__ID
    def Obtener_IM_Dicom(self):
        return self.__IM_DICOM
    def Obtener_IM_Niftii(self):
        return self.__IM_Niftii

p = Paciente()
    
def Leer_Asignar_Info():
    dirD = input(r"Ingrese la dirección del directorio Dicom: ")
    nom = input("Ingrese el nombre de uno de los archivos dicom para extraer la información: ")
    ds = pyd.dcmread(os.path.join(dirD,nom))
    n = ds.PatientName
    e = ds.PatientAge
    i = ds.PatientID
    d = ds.pixel_array
    
    p.AddNombre(n)
    p.AddEdad(e)
    p.AddID(i)
    p.Add_IM_Dicom(d)
    
    dict__pacientes[p.ObtenerID] = p
    dict__imágenes[p.ObtenerID] = [p.Obtener_IM_Dicom]
    op1 = int(input("¿Desea crear un elemento Niftii a partir del archivo anterior?:\n 1.Si\n 2.No\n Usted ingresó: "))
    if op1 ==1:
        dirN = input(r"Ingrese la dirección donde desea almacenar elementos Niftii: ")
        f = d2n.convert_directory(dirD,dirN)
        p.Add_IM_Niftii(f)
    else: 
        pass
    print("Los datos han sido guardados correctamente")


def Asignar_Im():
    dir = input(r"Ingrese la dirección de la imágen JPG o PNG que desea registrar: ")
    llave = input("Ingrese la clave que desea asignar a dicha imágen: ")
    Img = cv2.imread(dir)
    dict__imágenes[llave]= Img
    op2 = int(input("¿Desea visualizar la imágen asociada al paciente?\n 1.Si\n 2.No\n Usted escogió: "))
    if op2 == 1:
        plt.imshow(Img)
        plt.show()
        pass
    if op2 ==2 : 
        pass