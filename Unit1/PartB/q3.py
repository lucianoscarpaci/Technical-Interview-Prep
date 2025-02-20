def remove_name(people, secret_identity):
    while secret_identity in people:
        people.remove(secret_identity)
    return people

people = ['Batman', 'Superman', 'Bruce Wayne', 'The Riddler', 'Bruce Wayne']
secret_identity = 'Bruce Wayne'
print(remove_name(people, secret_identity))
