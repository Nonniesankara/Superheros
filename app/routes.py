from flask import Blueprint, jsonify, request
from .models import db, Hero, Power, HeroPower

bp = Blueprint('api', __name__)

@bp.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([{'id': h.id, 'name': h.name, 'super_name': h.super_name} for h in heroes])

# Add other routes as needed
