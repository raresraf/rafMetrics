# API Login
## ROUTES
### /
#### index():
Sample function for checking the availability of server. Returns "Hello, world!" in case of success

### /add
- POST REQUESTS
#### add_user()
Simple API to add a new user.

Payload must contain the Last Name, First Name, Username, Password and Email of the user:

e.g.
```json
    {
      "last_name": "flask_test_last_name",
      "first_name": "flask_test_first_name",
      "username": "flask_test_username",
      "email": "flask_test_email",
      "pwd" : "flask_test_password"
    }
```

### /users
#### users()
Get details about all users

e.g. GET request
```json
[
    {
    "Created": "Thu, 07 Nov 2019 08:46:20 GMT",
    "Email": "test@email.com",
    "FirstName": "test_first_name",
    "LastName": "test_last_name",
    "Userid": 1,
    "Username": "TestUsername",
    "hashedpassword": "pbkdf2:sha256:150000$3LCL1PDp$dd4ad95d664ce4b6fc0b7c9fe5870e793c3d364160c83fbd67fb1589fc5ab486"
    },
    {
    "Created": "Tue, 12 Nov 2019 12:52:59 GMT",
    "Email": "flask_test_email",
    "FirstName": "flask_test_first_name",
    "LastName": "flask_test_last_name",
    "Userid": 2,
    "Username": "flask_test_username",
    "hashedpassword": "pbkdf2:sha256:150000$ZIYIaFBX$963996e4c5dbd588b4f24f7a08d4bf801fc0c495e22c779ae333a2901e3b1bd3"
    }
]
```

### /user/\<id>
#### user(id)
Get details about user with Username = id 

e.g. GET request /user/flask_test_username
```json
{
"Created": "Tue, 12 Nov 2019 12:52:59 GMT",
"Email": "flask_test_email",
"FirstName": "flask_test_first_name",
"LastName": "flask_test_last_name",
"Userid": 2,
"Username": "flask_test_username",
"hashedpassword": "pbkdf2:sha256:150000$ZIYIaFBX$963996e4c5dbd588b4f24f7a08d4bf801fc0c495e22c779ae333a2901e3b1bd3"
}
```

### /user/\<id>/\<passwd>
(not secured)
#### auth_user(id, passwd)

Authentificate user based on Username and Password

### /update/\<id>
- POST REQUESTS
#### update_user(id)

Update details about a user
e.g.
```json
    {
      "last_name": "flask_test_last_name",
      "first_name": "flask_test_first_name",
      "email": "flask_test_email",
      "pwd" : "new_flask_test_password"
    }
```


### /delete/\<id>
#### delete_user(id)

Simple API to delete a existing user.
