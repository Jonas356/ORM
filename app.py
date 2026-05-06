from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tienda.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"<Product(name={self.name}, price={self.price}, stock={self.stock})>"
    
def init_db():
    with app.app_context():
        db.create_all()
        print("base de datos creado con satisfaccion")


def create_data():
    with app.app_context():
        p1 = Product(name="Teclado Mecánico", price=85.50, stock=15)
        p2 = Product(name="Mouse Inalámbrico", price=25.00, stock=30)
        p3 = Product(name="Monitor 24'", price=150.00) 
        db.session.add_all([p1,p2,p3])
        db.session.commit()
        print("Base de datos creada y productos insertados")

# Consultas a la base de datos
def query_products():
    with app.app_context():
        print("\n Listado de todos los productos:")
        products =Product.query.all()
        for p in products:
            print(f"ID: {p.id} Nombre: {p.name} Precio: ${p.price} Stock: {p.stock}")

# Obtener un producto por id
def queryone_product():
    with app.app_context():
        product = Product.query.filter_by(id=1).first()
        if product:
            print(f"\nProducto encontrado: {product.name}")
            return product
        else:
            print("\nProducto no encontrado")

# Actualizar precio y stock
def update_product():
    with app.app_context():
        product = Product.query.filter_by(id=1).first()
        if product:
            product.price= 3
            product.stock= 4
            db.session.commit()
            print(f"\n Producto actualizado exitosamente")
        else:
            print("\n Producto no existe")

# Eliminar producto
def delete_product():
    with app.app_context():
        product = Product.query.filter_by(id=2).first()
        if product:
            db.session.delete(product)
            db.session.commit()
            print(f"\n Producto eliminado")
        else:
            print("\n Producto no encontrado")

if __name__ == "__main__":
    #init_db()
    #create_data()       
    #query_products()   
    #queryone_product()   
    #update_product() 
    delete_product()     
