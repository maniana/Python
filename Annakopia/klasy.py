class User:
    def __init__(self, name, mail, age):
        self.name = name
        self.mail = mail
        self.age = age

    def print_info(self):
        print(f'Name: {self.name}, Email: {self.mail}, Age: {self.age}')

    @classmethod
    def create_and_print_users(cls):
        # Tworzenie obiektów w metodzie klasy
        user = cls(name='Anna', mail='anna@mail.com', age=35)
        user1 = cls(name='Konrad', mail='konrad@kdhg.pl', age=32)

        # Wywołanie metody print_info
        user.print_info()
        user1.print_info()

# Wywołanie metody create_and_print_users, która tworzy obiekty i wywołuje print_info
User.create_and_print_users()


# print(user.name)
# print(user.age)
# print(user1.mail)