from models.password_utilitis import password_hash

class User(object):
    _id = None
    username = None
    _hashed_password = None
    email = None

    def __init__(self):
        self._id = -1
        self.username = ""
        self.email = ""
        self._hashed_password = ""

    @property
    def id(self):
        return self._id

    @property
    def hashed_password(self):
        return self._hashed_password

    def set_password(self, password, salt):
        self._hashed_password = password_hash(password, salt)

    def save_to_db(self, cursor):
        if self._id == -1:
            sql = """INSERT INTO Users(username, email, hashed_password)
                    VALUES (%s, %s, %s) RETURNING id"""
            values = (self.username, self.email, self._hashed_password)
            cursor.execute(sql, values)
            self._id = cursor.fetchone()[0]
            return True
        else:
            sql = """UPDATE Users SET username=%s, email=%s, hashed_password=%s
                            WHERE id=%s"""
            values = (self.username, self.email, self._hashed_password, self._id)
            cursor.execute(sql, values)
            return True

    @classmethod
    def load_user_by_id(cls, cursor, user_id):
        sql = "SELECT id, username, email, hashed_password FROM Users WHERE id=%s"
        cursor.execute(sql, (user_id,))  # (user_id, ) - bo tworzymy krotkę
        data = cursor.fetchone()
        if data:
            loaded_user = cls()
            loaded_user._id = data[0]
            loaded_user.username = data[1]
            loaded_user.email = data[2]
            loaded_user._hashed_password = data[3]
            return loaded_user
        else:
            return None

    @classmethod
    def load_all_users(cls, cursor):
        sql = "SELECT id, username, email, hashed_password FROM Users"
        ret = []
        cursor.execute(sql)
        for row in cursor.fetchall():
            loaded_user = cls()
            loaded_user._id = row[0]
            loaded_user.username = row[1]
            loaded_user.email = row[2]
            loaded_user._hashed_password = row[3]
            ret.append(loaded_user)
        return ret

    def delete(self, cursor):
        sql = "DELETE FROM Users WHERE id=%s"
        cursor.execute(sql, (self._id,))
        self._id = -1
        return True


