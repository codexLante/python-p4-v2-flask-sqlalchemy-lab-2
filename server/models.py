from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin  # For task 3

db = SQLAlchemy()

class Customer(db.Model, SerializerMixin):
    __tablename__ = 'customers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    
    # Relationship to Review
    reviews = db.relationship("Review", back_populates="customer")
    
    # Association Proxy to get items directly
    items = association_proxy('reviews', 'item')
    
    # Serialization rules
    serialize_rules = ('-reviews.customer',)

class Item(db.Model, SerializerMixin):
    __tablename__ = 'items'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Float)
    
    # Relationship to Review
    reviews = db.relationship("Review", back_populates="item")
    
    # Serialization rules
    serialize_rules = ('-reviews.item',)

class Review(db.Model, SerializerMixin):
    __tablename__ = 'reviews'
    
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String)
    
    # Foreign Keys
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    
    # Relationships
    customer = db.relationship("Customer", back_populates="reviews")
    item = db.relationship("Item", back_populates="reviews")
    
    # Serialization rules
    serialize_rules = ('-customer.reviews', '-item.reviews',)