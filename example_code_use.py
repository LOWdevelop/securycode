import secury_code


FIREBASE_URL = 'FIRE BASE URL'


sc = secury_code.secury_key(FIREBASE_URL)

key = str(input('Your key  ->  '))

response =  sc.check_key(key=key)

if response['registered'] == 'not_registered':

    print('Registering User')

    sc.register_key(response['userid'])

    response = sc.check_key(key=key)


if response['registered'] == 'Key Not Exist':

    print(response['registered'])

else:
    print(response['registered'])


if sc.auth_key(response['userid']):

    print(f'Authenticated , Welcome {response["userid"]}')

else:
    print('Error , user not Authenticated')

