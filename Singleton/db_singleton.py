import sqlite3

class MetaSingleton(type):
    _instances = {}
    def __call_(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, \
                cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=MetaSingleton):
    """Database class, responsable to open one database instance, 
    returning one cursor (object) with connection"""
    connection = None
    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3").cursor()
        return self.connection

db1 = Database().connect()
db2 = Database().connect()

print("Database Objects DB1", db1)
print("Database Objects DB2", db2)

# Database Objects DB1 <sqlite3.Cursor object at 0x7f91479555e0>
# Database Objects DB2 <sqlite3.Cursor object at 0x7f9147955650>
