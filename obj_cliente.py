

class Cliente:
    """Objeto Cliente, se crea un cliente."""

    __id: int = 0

    def __init__(self):

        Cliente.__id += 1
        self.id_persona = Cliente.__id

        self.__operativo: bool = False
        self.__nombre: str = ""
        self.__apellidos: str = ""
        self.__edad: int = 0
        self.__email: str = ""
        self.__password: str = ""

    def set_operativo(self, activar: bool) -> None:
        self.__operativo = activar

    def set_nombre(self, nombre: str) -> None:
        self.__nombre = nombre

    def set_apellidos(self, apellidos: str) -> None:
        self.__apellidos = apellidos

    def set_edad(self, edad: int) -> None:
        self.__edad = edad
        
    def set_email(self, email: str) -> None:
        self.__email = email
        
    def set_password(self, password: str) -> None:
        self.__password = password

    def get_id(self) -> int:
        return self.id_persona

    def get_nombre(self) -> str:
        return self.__nombre
        
    def get_apellidos(self) -> str:
        return self.__apellidos

    def get_edad(self) -> int:
        return self.__edad
        
    def get_email(self) -> str:
        return self.__email
        
    def get_password(self) -> str:
        return self.__password

    def get_operativo(self) -> bool:
        return self.__operativo

    def __str__(self):
        return 'Usuario: {}, Nombre: {}'.format(self.id_persona, self.get_nombre())
