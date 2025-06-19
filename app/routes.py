from flask import Flask, jsonify, request
from .models import db, Hero, Power, HeroPower

app = Flask('api', __name__)

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([{'id': h.id, 'name': h.name, 'super_name': h.super_name} for h in heroes])

