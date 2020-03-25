from models.user import User
from models.password_utilitis import generate_salt
from db_utils import create_db_connection


cnx = create_db_connection('warsztaty_db')
cursor = cnx.cursor()

user_1 = User()



print(user_1)

print(user_1.id)
salt = generate_salt()
user_1.set_password('123abc', salt)

print(salt)

user_1.username = 'Karo'
user_1.email = 'ala@o2.pl'

user_2 = User()
user_2.username = 'Adi'
user_2.email = 'adi@02.pl'

user_2.set_password('abs123', salt)
#user_1.save_to_db(cursor)
#user_2.save_to_db(cursor)
a = User.load_user_by_id(cursor, 9)

if a:
    print(a.username)
else:
    print("Błąd")

users = User.load_all_users(cursor)

for u in users:
    print(u.username, u.email)


print('nowe imie')

a.username = "kasia"

a.save_to_db(cursor)

if a:
    print(a.username)
else:
    print("Błąd")

#a.delete(cursor)


cnx.commit()
cursor.close()
cnx.close()