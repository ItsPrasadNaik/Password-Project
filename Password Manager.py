class BasePasswordmanager:
    old_passwords = []
    users = {}

    def __init__(self,username,password):
        self.username = username
        self.password = password
        BasePasswordmanager.users[self.username] = self.password
        BasePasswordmanager.old_passwords.append(self.password)

    def get_password():
        return BasePasswordmanager.old_passwords[-1]

    def is_correct(pass1):
        if pass1 == BasePasswordmanager.old_passwords[-1]:
            return True
        else:
            return False

class PasswordManager(BasePasswordmanager):
    SpecialSym = ['$', '@', '#', '%']

    def set_method(user, new_password,pos):
        if any(j in PasswordManager.SpecialSym for j in new_password) and any(j.islower() for j in new_password) \
        and any(j.isupper() for j in new_password) and any(j.isdigit() for j in new_password) and len(new_password)>=6 \
        and len(new_password) > len(BasePasswordmanager.old_passwords[pos-1]):
            BasePasswordmanager.old_passwords[pos-1] = new_password
            BasePasswordmanager.users[user] = new_password

            # self.password = new_password
            return 'Password is set'
        else:
            return 'Levels are not satified'

    def get_level(p1):

        if p1.isalpha() or p1.isdigit():
            return 'Password Level is 0'
        elif p1.isalnum():
            return 'Password Level is 1'
        elif any(j in PasswordManager.SpecialSym for j in p1) and any(j.islower() for j in p1) \
                and any(j.isupper() for j in p1) and any(j.isdigit() for j in p1) and len(p1) >= 6:
            return 'Password Level is 2'
        else:
            return 'Password is not able to determine'

user1 = BasePasswordmanager('Prasad','Prasad@123')
user2 = BasePasswordmanager('bharath','Bharath@123')
user3 = BasePasswordmanager('yashavanth','Yashu@123')


print('Passwords list is ',BasePasswordmanager.old_passwords)

print('Getting the current Password', BasePasswordmanager.get_password())

print('Changing the user Password ', PasswordManager.set_method('Bharath' , 'Nagendra@12345',1))


print('security Level of current password', PasswordManager.get_level(BasePasswordmanager.old_passwords[1]))


print('security Level of General password', PasswordManager.get_level('Prasad@123'))

print('Updated Passwords list is ', BasePasswordmanager.old_passwords)

print('Usernames and their Password is ', BasePasswordmanager.users)