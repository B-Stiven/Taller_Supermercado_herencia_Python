from categorias import Categoria

class SubCategoria(Categoria):

    def __init__(self,nombresub,codigosub,micategoria):

        self.nombresub=nombresub
        self.codigosub=codigosub
        self.micategoria=micategoria

    def PasarAcadena(self):
        return print("nombre subcategoria--",self.nombresub,"--codigo subcategoria--",self.codigosub,"--categoria--",self.micategoria)

  