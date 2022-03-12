# uniacco-django
Uniacco assignment for Django based user creation and token generation

# To Set Up the Project
Firstly install the requirements.txt to setup the environment
``` pip install -r requirements.txt ```

Run MakeMigrations to run the model

``` python3 manage.py makemigations uniacco_api ```

Then migrate the application

``` python3 manage.py migrate ```

To run the project locally

``` python3 manage.py runserver ```

It will automatically run the application over 
http://127.0.0.1:8000/

Certain urls can be accessed to get familiarized by the api are
To register the user to the database
http://127.0.0.1:8000/uniacco/register

For jwt token generation or to get user authenctication check
http://127.0.0.1:8000/uniacco/signin

For checking all of the users present in our db
http://127.0.0.1:8000/uniacco/users

To get the login history with the ip of users
http://127.0.0.1:8000/uniacco/userhistory








