 Create schema in any Database script or any ORM (Object Relational Mapping).
    SQL Schema
    Here's the schema for the product and product category tables in SQL:

    CREATE TABLE ProductCategory (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    deleted_at DATETIME DEFAULT NULL
  );
  
  CREATE TABLE Product (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    SKU VARCHAR(50) UNIQUE,
    quantity INT,
    category_id INT NOT NULL,
    FOREIGN KEY (category_id) REFERENCES ProductCategory(id) ON DELETE RESTRICT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    modified_at DATETIME DEFAULT NULL,
    deleted_at DATETIME DEFAULT NULL,
    price DECIMAL(10,2) NOT NULL,
    discount_id INT DEFAULT NULL,
    discount_percent DECIMAL(5,2) DEFAULT NULL,
    active BOOLEAN DEFAULT TRUE
  );


This schema creates two tables:

ProductCategory:
id: (INT) Primary key for the table, auto-increments.
name: (VARCHAR(255)) Name of the product category, not null.
description: (TEXT) Optional description of the category.
created_at: (DATETIME) Timestamp of when the category was created, set to current timestamp by default.
deleted_at: (DATETIME) Timestamp of when the category was deleted, null by default (soft delete).
Product:
id: (INT) Primary key for the table, auto-increments.
name: (VARCHAR(255)) Name of the product, not null.
description: (TEXT) Optional description of the product.
SKU: (VARCHAR(50)) Unique stock keeping unit for the product.
quantity: (INT) Current quantity of the product in stock.
category_id: (INT) Foreign key referencing the "id" field of the "ProductCategory" table, not null. Enforces referential integrity.
created_at: (DATETIME) Timestamp of when the product was created, set to current timestamp by default.
modified_at: (DATETIME) Timestamp of when the product was last modified, null by default.
deleted_at: (DATETIME) Timestamp of when the product was deleted, null by default (soft delete).
price: (DECIMAL(10,2)) Price of the product, not null.
discount_id: (INT) Foreign key referencing a discount table (not shown here), null by default.
discount_percent: (DECIMAL(5,2)) Discount percentage applied to the product, null by default.
active: (BOOLEAN) Flag indicating if the product is active or not (default: true).
This schema enforces the one-to-many relationship between product categories and products through the foreign key constraint.

ORM Example (Python with SQLAlchemy)
Here's an example of how this schema could be implemented using SQLAlchemy, a popular ORM for Python:
    from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class ProductCategory(Base):
  __tablename__ = 'product_category'

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(255), nullable=False)
  description = Column(String)
  created_at = Column(DateTime, default=datetime.datetime.utcnow)
  deleted_at = Column(DateTime, default=None)

  products = relationship("Product", backref="category")

class Product(Base):
  __tablename__ = 'product'

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(255), nullable=False)
  description = Column(String)
  sku = Column(String(50), unique=True)
  quantity = Column(Integer)
  category_id = Column(Integer, ForeignKey('product_category.id'), nullable=False)
  created_at = Column(DateTime, default=datetime.datetime.utcnow)
  modified_at = Column(DateTime, default=None)
  deleted_at = Column(DateTime, default=None)
  price = Column(Decimal(10, 2), nullable=False)

