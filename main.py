from categorias import Categoria
from subcategoria import SubCategoria
from proveedor import Proveedor
from producto import Producto

listacategorias=[]
listasubcategoria=[]
listaproveedor=[]
listaproductos=[]

class Supermercado:

    def __init__(self,nombresuper):
        self.nombresuper=nombresuper

    

def crear():
    
    global miproducto
    print("**************se habilito la opcion de crear***************")
    print()

    print("ingrese la categoria del producto que desea crear")
    nombreca=input()
    nombreca=str(nombreca)

    print("ingrese el codigo de la categoria ",nombreca)
    codigoca=input()
    codigoca=int(codigoca)

    micategoria=Categoria(nombreca,codigoca)

    print("ingrese la sub categoria ")
    nombresub=input()
    nombresub=str(nombresub)

    print("ingrese el codiigo de la subcategoria ",nombresub)
    codigosub=input()
    codigosub=int(codigosub)

    misubcategoria=SubCategoria(nombresub,codigosub,micategoria)

    print("ingrese el provedor que desee para su producto")
    nombrepro=input()
    nombrepro=str(nombrepro)

    print("ingrese el codigo de ese proveedor ",nombrepro)
    codigopro=input()
    codigopro=int(codigopro)

    miproveedor=Proveedor(nombrepro,codigopro)

    print("ingrese el nombre del producto")
    nombreproduc=input()
    nombreproduc=str(nombreproduc)

    print("ingrese el codigo de ",nombreproduc)
    codigoproduc=input()
    codigoproduc=int(codigoproduc)

    print("ingrese el precio de ",nombreproduc)
    precioproduc=input()
    precioproduc=float(precioproduc)


    miproducto=Producto(nombreproduc,codigoproduc,precioproduc,misubcategoria,miproveedor)


    listaproductos.append(miproducto)




def listar():
    #funcion para listar los clientes
    print()
    print("*******************se habilito la opcion de listar***************")
    print()
    for t in listaproductos:
        t.PasarAcadena()

    menu()

def buscar():
    #funcion para buscar a los clientes en el sistema
    
    print()
    print("******************se habilito la opcion de buscar**********")
    print()
    print("ingrese el codigo del producto que desea buscar")
    codigo=int(input(""))
    longitud=len(listaproductos)-1
    while longitud >=0:
        if codigo==listaproductos[longitud].codigoproduc:
            print("subcategoria",listaproductos[longitud].misubcategoria.nombresub,"nombre",listaproductos[longitud].nombreproduc,"codigo",listaproductos[longitud].codigoproduc)
            break
        longitud=longitud-1

    if longitud==-1:
        print("el codigo no existe")
    menu()

def modificar():
    #funcion para modificar los datos de los clientes
    print()
    print("***************se habilito la opcion de modificar*************")
    print()
    print("ESTOS SON LAS CATEGORIAS QUE PUEDE MODIFICAR")
    print()
    for objeto in listaproductos:
        objeto.PasarAcadena()
    print()
    print("ingrese el codigo de producto  que desea modificar:")
    nombre=input()
    nombre=int(nombre)
    print()
    longitud=len(listaproductos)-1
    while longitud >=0:
        if nombre==listaproductos[longitud].codigoproduc:
            
            print("ingrese el nombre del producto")
            nombreproduc=input()
            nombreproduc=str(nombreproduc)

            print("ingrese el codigo del producto")
            codigoproduc=input()
            codigoproduc=int(codigoproduc)

            print("ingrese el precio del producto")
            precioproduc=input()
            precioproduc=float(precioproduc) 

            miproducto.modificar(nombreproduc,codigoproduc,precioproduc)
            miproducto.PasarAcadena()
            break

        else:
            print("la categoria no se encuentra") 

            menu()


            
       


     

def eliminar():
    #funcion para eliminar clientes del sistema
    print()
    print("***************se habilito la opcion de eliminar*************")
    print()
    print("ESTOS SON LAS CATEGORIAS QUE PUEDE ELIMINAR")
    print(listaproductos)
    print()
    codigo=int(input(""))
    longitud=len(listaproductos)-1
    while longitud >=0:
        if codigo==listaproductos[longitud].codigoproduc:
            listaproductos.pop(longitud)
            break
        menu()
    


def menu():
    #funcion de menu para hecer el llamado a todas las funciones
        print()
        print()
        condision="si"
        while condision=="si":
            print("\n")
            print("|************************|")
            print("|**|     Bienvenidos  |**|")
            print("|**|        Menu      |**|")
            print("|************************|")
            print()
            print("1- para crear un nuevo producto")
            print("2- para listar todos los productos")
            print("3- para buscar un producto ")
            print("4- para modificar un producto")
            print("5- para eliminar un producto ")
            print()

            print("que opcion desea elegir")
            opcion=input()
            opcion=int(opcion)

            if opcion==1:
                crear()
            elif opcion==2:
                listar()
            elif opcion==3:
                buscar()
            elif opcion==4:
                modificar()
            elif opcion==5:
                eliminar()

    

            condision=str(input("quiere hacer algo mas  SI/NO:   "))

menu()

