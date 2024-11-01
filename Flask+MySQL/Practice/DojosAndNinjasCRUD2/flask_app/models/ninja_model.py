from flask_app.config.mysqlconnection import db , connectToMySQL
#might need other imports like flash other classes and regex

db = 'dojos_and_ninjas'

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo = data['name']

    @classmethod
    def get_ninjas(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(db).query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas
    
    @classmethod
    def get_dojo_w_ninjas(cls, data):
        query = "SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        print(results)
        new_dojo = []
        for ninja in results:
            new_dojo.append(cls(ninja))
        return new_dojo
    
    @classmethod
    def save_ninjas(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(id)s);"
        result = connectToMySQL(db).query_db(query, data)
        return result
    
    @classmethod
    def get_by_id(cls , data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query , data)

        if results:
            return cls(results[0])
        return None
    
    @classmethod
    def edit_ninja(cls , data):
            query = "UPDATE reviews SET first_name = %(first_name)s , last_name = %(last_name)s ,age = %(age)s  WHERE id = %(id)s;"
            return connectToMySQL(db).query_db(query , data)
        
    @classmethod
    def delete(cls , data):
            query = "DELETE FROM reviews WHERE id = %(id)s;"
            return connectToMySQL(db).query_db(query , data)