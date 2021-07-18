import pickle
import dill
class User:
    def __init__(self, id, first_name, lastname, phone) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = lastname
        self.phone :str = phone

    def __repr__(self):
        return f"{self.id}: {self.first_name} {self.last_name} <{self.phone}>"

    # q5-3
    def fullname(self):
        return f"{self.first_name} {self.last_name}"


#q5-1
def sort_id(user: User):
    return user.id


with open("users.pickled", "rb") as f:
    users: list = pickle.load(f)
users.sort(key=sort_id)
with open("output-q5-1.txt", "wb") as f:
    pickle.dump(users, f)
#q5-2


def filter_phone(user:User) -> bool:
    if user.phone.startswith('0919'):
        return True
    else:
        return False


filterd = list(filter(filter_phone, users))
with open("output-q5-2.txt", "wb") as f:
    pickle.dump(users, f)
#q5-3
with open("output-q5-2.txt", "wb") as f:
    dill.dump(users, f)




