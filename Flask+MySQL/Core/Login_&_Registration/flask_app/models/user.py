from flask_app.config.mysqlconnection import connectToMySQL
import re	
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

from flask import flash

class User:
    db = "logindb"
    
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO users (first_name, last_name, email, password) 
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
        """
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db).query_db(query)
        users = [cls(row) for row in results]
        return users

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])

    @staticmethod
    def validate_register(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(User.db).query_db(query, user)
        
        # Check if email is already in use
        if len(results) >= 1:
            flash("Email already in use", "register")
            is_valid = False
        
        # Check if email format is valid
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email format", "register")
            is_valid = False
        
        # Check if first name is at least 2 characters
        if len(user['first_name']) < 2:
            flash("First name must be at least 2 characters", "register")
            is_valid = False
        
        # Check if last name is at least 2 characters
        if len(user['last_name']) < 2:
            flash("Last name must be at least 2 characters", "register")
            is_valid = False
        
        # Check if password meets criteria
        if len(user['password']) < 6:
            flash("Password must be at least 6 characters", "register")
            is_valid = False
        
        if not any(char.isupper() for char in user['password']):
            flash("Password must have at least 1 uppercase letter", "register")
            is_valid = False
        
        if not any(char.isdigit() for char in user['password']):
            flash("Password must contain at least one numeral", "register")
            is_valid = False
        
        # Check if password and confirm password match
        if user['password'] != user['confirm']:
            flash("Passwords do not match", "register")
            is_valid = False
        
        return is_valid
