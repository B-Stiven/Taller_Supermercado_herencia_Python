
class Producto:
    
    def __init__(self,nombreproduc,codigoproduc,precioproduc,misubcategoria,miproveedor):

        self.nombreproduc=nombreproduc
        self.codigoproduc=codigoproduc
        self.precioproduc=precioproduc
        self.misubcategoria=misubcategoria
        self.miproveedor=miproveedor


    

    def PasarAcadena(self):
        print("")
        return print("--Subcategoria--",self.misubcategoria.nombresub,"--codigo subcategoria--",self.misubcategoria.codigosub,"--proveedor--",self.miproveedor.nombrepro,"--codigo proveedor--",self.miproveedor.codigopro,"--producto--",self.nombreproduc,"--codigo producto--",self.codigoproduc,"--precio producto--",self.precioproduc)
        print("")

    def modificar(self,nombreproduc,codigoproduc,precioproduc):
        self.nombreproduc=nombreproduc
        self.codigoproduc=codigoproduc
        self.precioproduc=precioproduc
        
        print()
        print("registro exitoso")
    def retornar(self):
        return print(self.nombreproduc,self.codigoproduc,self.precioproduc)



    