class DepartamentoEntity():
    def __init__(self, dpto_codigo, dpto_descricao):
        self.__dpto_codigo = dpto_codigo
        self.__dpto_descricao = dpto_descricao
    
    @property
    def dpto_codigo(self):
        return self.__dpto_codigo

    @dpto_codigo.setter
    def dpto_codigo(self, dpto_codigo):
        self.__dpto_codigo = dpto_codigo

    @property
    def dpto_descricao(self):
        return self.__dpto_descricao

    @dpto_descricao.setter
    def dpto_descricao(self, dpto_descricao):
        self.__dpto_descricao = dpto_descricao
