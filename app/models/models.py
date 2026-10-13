from datetime import datetime
from sqlalchemy import CheckConstraint,UniqueConstraint
from app import db

class User(db.Model):
    __tablename__='users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    full_name = db.Column(db.String(100))
    email = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String(255))
    phone = db.Column(db.String(20))
    user_role = db.Column(db.String(20), default='customer')
    is_active = db.Column(db.Boolean, default=0)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow, onupdate=datetime.utcnow)

class Food_Items(db.Model):
    __tablename__ = 'food_items'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    food_name = db.Column(db.String(100))
    category = db.Column(db.String(50))
    price = db.Column(db.Numeric(10,2))
    is_available = db.Column(db.Boolean, default=1)
    image_url = db.Column(db.String(300))
    stock_quantity = db.Column(db.Integer, default=0)

class Auth_Sessions(db.Model):
    __tablename__ = 'auth_sessions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    refresh_token_hash = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime)
    revoked_at = db.Column(db.DateTime)

class Guest_Sessions(db.Model):
    __tablename__ = 'guest_sessions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    session_token_hash = db.Column(db.String(255), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime)
    last_activity_at = db.Column(db.DateTime)

class Carts(db.Model):
    __tablename__ = 'carts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    guest_id = db.Column(db.Integer, db.ForeignKey('guest_sessions.id'))
    cart_status = db.Column(db.String(20), default='active')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime)

    __table_args__ = (
        CheckConstraint( '(user_id is null and guest_id is not null) or (user_id is not null and guest_id is null)', name = 'check_only_one_active'),
    )

class Cart_Items_Table(db.Model):
    __tablename__ = 'cart_items'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('carts.id'))
    food_item_id = db.Column(db.Integer, db.ForeignKey('food_items.id'))
    quantity = db.Column(db.Integer)

    __table_args__ = (
        CheckConstraint('quantity>0', name = 'check_quantity'),
        UniqueConstraint('cart_id', 'food_item_id')
    )

class Orders(db.Model):
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    order_number = db.Column(db.String(40), unique=True)
    order_status = db.Column(db.String(30), default='pending')
    subtotal = db.Column(db.Numeric(10,2))
    total_amount = db.Column(db.Numeric(10,2))
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow, onupdate=datetime.utcnow)

    __table_args__ = (
        CheckConstraint('subtotal>0')
    )

class Orders_Items(db.Model):
    __tablename__ = 'order_items'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    food_item_id = db.Column(db.Integer, db.ForeignKey('food_items.id'))
    food_name = db.Column(db.String(150))
    unit_price = db.Column(db.Numeric(10,2))
    line_total = db.Column(db.Numeric(10,2))
    quantity = db.Column(db.Integer)

    __table_args__ = (
        CheckConstraint('quantity>0')
    )

class Payments(db.Model):
    __tablename__ = 'payments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    payment_method = db.Column(db.String(10))
    amount = db.Column(db.Numeric(10,2))
    payment_status = db.Column(db.String(30))
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow, onupdate=datetime.utcnow)

    __table_args__ = (
        CheckConstraint("payment_method in ('razorpay','cash')"),
        CheckConstraint('amount>0')
    )

