from . import db
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

class Hero(db.Model, SerializerMixin):
    __tablename__ = 'heroes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    super_name = db.Column(db.String(100), nullable=False)

    
    hero_powers = db.relationship('HeroPower', backref='hero')

    
    serialize_rules = ('-hero_powers.hero',)  

    @validates('name', 'super_name')
    def validate_name_fields(self, key, value):
        if not value or not value.strip():
            raise ValueError(f"{key} must not be empty.")
        return value

class Power(db.Model, SerializerMixin):
    __tablename__ = 'powers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)

    
    hero_powers = db.relationship('HeroPower', backref='power')

    serialize_rules = ('-hero_powers.power',)

    @validates('description')
    def validate_description(self, key, value):
        if not value or len(value.strip()) < 10:
            raise ValueError("Description must be at least 10 characters long.")
        return value

class HeroPower(db.Model, SerializerMixin):
    __tablename__ = 'hero_powers'
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String(50), nullable=False)

    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)

    serialize_rules = ('-hero.hero_powers', '-power.hero_powers')

    @validates('strength')
    def validate_strength(self, key, value):
        allowed = ['Strong', 'Weak', 'Average']
        if value not in allowed:
            raise ValueError(f"Strength must be one of: {', '.join(allowed)}")
        return value
