import pyodbc

class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class SingletonConexionDB(metaclass=SingletonMeta):

    __direccion_servidor = 'DESKTOP-D19E7F7'
    __nombre_bd = 'Tienda'
    __nombre_usuario = 'sa'
    __password = 'pato'

    __conexion = None

    def connect_database(self):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """
        try:
            self.__conexion =  pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                                    self.__direccion_servidor+';DATABASE='+
                                    self.__nombre_bd+';UID='+
                                    self.__nombre_usuario+';PWD=' + 
                                    self.__password)
            # OK! conexión exitosa
            print(' # OK! conexión exitosa')
        except Exception as e:
            # Atrapar error
            print("Ocurrió un error al conectar a SQL Server: ", e)
        

    def disconnect_database(self):
        self.__conexion.close()

    def db_conexion(self):
        return self.__conexion.cursor()


