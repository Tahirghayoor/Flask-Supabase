from flask import request, jsonify
from app import app, supabase

# CREATE
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    try:
        response = supabase.table('users').insert({
            'name': data['name'],
            'email': data['email'],
            'phone': data['phone']
        }).execute()
        
        # Debug: Check response structure
        print("CREATE Response type:", type(response))
        print("CREATE Response data:", response.data)
        
        return jsonify(response.data[0]), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# READ ALL
@app.route('/users', methods=['GET'])
def get_users():
    try:
        response = supabase.table('users').select('*').execute()
        
        # Debug: Check response structure
        print("GET ALL Response type:", type(response))
        print("GET ALL Response data:", response.data)
        
        return jsonify(response.data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# READ ONE
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        response = supabase.table('users').select('*').eq('id', user_id).execute()
        
        # Debug: Check response structure
        print("GET ONE Response type:", type(response))
        print("GET ONE Response data:", response.data)
        
        if response.data:
            return jsonify(response.data[0]), 200
        return jsonify({'error': 'user not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# UPDATE
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    try:
        response = supabase.table('users').update({
            'name': data.get('name'),
            'email': data.get('email'),
            'phone': data.get('phone')
        }).eq('id', user_id).execute()
        
        # Debug: Check response structure
        print("UPDATE Response type:", type(response))
        print("UPDATE Response data:", response.data)
        
        if response.data:
            return jsonify(response.data[0]), 200
        return jsonify({'error': 'user not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# DELETE
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        response = supabase.table('users').delete().eq('id', user_id).execute()
        
        # Debug: Check response structure
        print("DELETE Response type:", type(response))
        print("DELETE Response data:", response.data)
        
        if response.data:
            return jsonify({'message': 'user deleted'}), 200
        return jsonify({'error': 'user not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500