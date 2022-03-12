
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from uniacco_api.models import Account, UserLoginHistory
from uniacco_api.serializers import RegistrationSerializer, AccountSerializer, UserLoginHistorySerializer
from uniacco_api.serializers import UserLoginSerializer

# Create your views here.
@api_view(['POST',])
def reg_user_view(request):
    """
    For adding user to our database and new record is entered to our database using this api
    """
    if request.method == 'POST':
        serializer = RegistrationSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            if account:
                data['response'] = 'Succesfully Registered'
                data['username'] = account.username
            else:
                data['response'] = 'Not able to enter user with same username'
        return Response(data)

@api_view(['GET',])
def get_user_view(request):
    """
    For getting the list of all users present in our database
    """
    if request.method == 'GET':
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)

@api_view(['GET',])
def get_user_login_history_view(request):
    """
    For getting the list of all users which are successfuly logged in
    """
    if request.method == 'GET':
        users = UserLoginHistory.objects.all()
        serializer = UserLoginHistorySerializer(users, many=True)
        return Response(serializer.data)

@api_view(['POST',])
def UserLoginView(request):
    """
    For signing in the user and token generation via Post request
    """
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    response = {
        'success' : 'True',
        'status code' : status.HTTP_200_OK,
        'message': 'User logged in  successfully',
        'token' : serializer.data['token'],
        }
    status_code = status.HTTP_200_OK
    return Response(response, status=status_code)