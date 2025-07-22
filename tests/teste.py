db = [
    {
        'username': 'leandro',
        'password': '0611',
    },
    {
        'username': 'Joao',
        'password': 'ola'
    }
]

for user in db:
    print(user)
    print(user['username'] == 'leandro' and user['password'] == '0611')

# print(len(users))

