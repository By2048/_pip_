from werkzeug.local import LocalStack, LocalProxy

user_stack = LocalStack()
user_stack.push({'name': 'Bob'})
user_stack.push({'name': 'John'})


def get_user():
    return user_stack.pop()


user = get_user()
print(user['name'])
print(user['name'])

# print()
#
proxy_user = LocalProxy(get_user)
print(proxy_user['name'])
print(proxy_user['name'])
# #
proxy_user = LocalProxy(get_user)
print(proxy_user['name'])
