import json
from rest_framework import serializers
from uniacco_api.models import Account, UserLoginHistory
from django.contrib.auth.hashers import make_password, check_password
from rest_framework_jwt.settings import api_settings
import requests
import socket   

"""
RegistrationSerializer

Use: For signing up the user to the application we are fetching username and password and then passing that to the
database for storing the record which can later be used for token generation and signing of the user. It makes sure 
unique username is entered to the database and it's hosted over /uniacco/register via Post request
"""
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'username', 'password')
        extra_kwargs = {
            'password' : {'write_only':True}
        }
    def save(self):
        accounts = Account.objects.all()
        uname =  self.validated_data['username']
        if not any(d.username == uname for d in accounts):
            account = Account(
                username = self.validated_data['username'],
                password = make_password(self.validated_data['password'])
            )
            account.save()
            return account
        else:
            return None

"""
AccountSerializer 

Use :-  For grabbing all the records from the account table and showing that to the user
to our api hosted on /uniacco/users route
"""
class AccountSerializer(serializers.ModelSerializer):
   class Meta:
       model = Account
       fields = ('id', 'username')

"""
UserLoginHistorySerializer 

Use :-  For grabbing all the records from the UserLoginHistory table and showing that to the user
to our api hosted on /uniacco/userhistory route
"""
class UserLoginHistorySerializer(serializers.ModelSerializer):
   class Meta:
       model = UserLoginHistory
       fields = ('id', 'ip_address')



JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER
"""
UserLoginSerializer

Use: For validating the request coming to our api from /api/token route
It is fetching all of the records from the DB and then comparing the ones with the requested username and password
If it exists it's creating a jwt token and sending back to user for logging in

Also for any user who is trying to use our authentication service its sending the ip address to the url as requested
"""
class UserLoginSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        username = data.get("username", None)
        password = data.get("password", None)
        # To send the username and ip address of the user trying to use our authenticate api
        IPAddr = requests.get("https://api.ipify.org").text
        data = {'user':username,'ip':IPAddr}
        cli_res = requests.post("https://encrusxqoan0b.x.pipedream.net/", data= json.dumps(data))
        
        users = Account.objects.all()
        account = None
        for user in users:
            if user.username == username and check_password(password, user.password):
                account = user
                break
            
        if account is None:
            raise serializers.ValidationError(
                'A account with this username and password is not found.'
            )
        try:
            # For successful login generating the jwt token and storing user login history
            user_hist = UserLoginHistory(
                ip_address =  IPAddr
            )
            user_hist.save()
            payload = JWT_PAYLOAD_HANDLER(account)
            jwt_token = JWT_ENCODE_HANDLER(payload)
        except Account.DoesNotExist:
            raise serializers.ValidationError(
                'User with given username and password does not exists'
            )
        return {
            'username':user.username,
            'token': jwt_token
        }
