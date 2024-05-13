import pydicom as pyd
import nilearn as nii
import dicom2nifti as d2n



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
        self.__IM_DICOM = d
    def Add_IM_Niftii(self, f):
        self.__IM_Niftii = f

    def ObtenerNombre(self):
        return self.__nombre
    def ObtenerNombre(self):
        return self.__edad
    def ObtenerNombre(self):
        return self.__ID
    def ObtenerNombre(self):
        return self.__IM_DICOM
    def ObtenerNombre(self):
        return self.__IM_Niftii

p = Paciente()
    
def Leer_Info(self):
    dirD = input(r"Ingrese la dirección del directorio Dicom")
    dirN = input(r"Ingrese la dirección donde desea almacenar elementos Niftii")
    ds = pyd.dcmread(dirD)
    n = ds.PatientName
    e = ds.PatientAge
    i = ds.PatientID
    d = ds.pixel_array
    f = d2n.convert_directory(dirD, dirN)
    p.AddNombre(n)
    p.AddEdad(e)
    p.AddID(i)
    p.Add_IM_Dicom(d)
    p.Add_IM_Niftii(f)
    

    


