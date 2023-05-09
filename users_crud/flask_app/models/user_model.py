from flask_app.config.mysqlconnection import connectToMySQL
import pprint

db = 'users_crud'

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name= data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls,data):
        query = 'INSERT INTO users (first_name,last_name,email) VALUES (%(first_name)s,%(last_name)s,%(email)s)'
        return connectToMySQL(db).query_db(query,data)


    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users'
        results = connectToMySQL(db).query_db(query) 
        all_users = []
        pprint.pprint(results)
        for user in results:
            all_users.append(cls(user))
        return all_users

    @classmethod
    def get_one_user(cls,data):
        query = "SELECT * from users where id = %(id)s"
        results = connectToMySQL(db).query_db(query,data)
        return cls(results[0])

    @classmethod
    def update_user(clas,data,id):
        query = f'''
        UPDATE users
        set first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s
        WHERE id = {id}
        '''
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def delete_user(cls,id):
        query = f"DELETE FROM users where id = {id}"
        return connectToMySQL(db).query_db(query)
