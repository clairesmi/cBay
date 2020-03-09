# pylint: disable=no-member,arguments-differ
from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt
from items.serializers import PopulatedUserSerializer, ItemSerializer
from .serializers import UserSerializer
from items.models import Item
User = get_user_model()

class ProfileView(APIView):

    def get(self, request):
        # user = User.objects.get(pk=pk)
        #  ADD VIEW IN FOR ITEMS ADDED BY USER - POPULATE ITEMS ON USER
        user = request.user
        serialized_user = PopulatedUserSerializer(user)
        # print(serialized_user)
        return Response(serialized_user.data)

class ListingView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request):
        user = request.user.id
        print(user)
        items = Item.objects.all().filter(owner=user)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=200)


class ProfileDetailView(APIView):
    def get(self, _request, pk):
        user = User.objects.get(pk=pk)
        serialized_user = PopulatedUserSerializer(user)
        return Response(serialized_user.data)


class RegisterView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registration Successful'})
        return Response(serializer.errors, status=422)

        # Django doesn't set an expiry time for the token by default so you have to import packages
        # from datetime (as above) to get Auth in navbar to work properly IF USING THE SAME CODE FROM
        # AN AUTH FILE IN EXPRESS
        # date and time is set with the dt variable to 'now' and time delta is set to 1 day
        # (token expires after 1 day) This needs to be set in the main post function as well as the
        # 'if not user' part

class LoginView(APIView):

    def get_user(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            raise PermissionDenied({'message': 'Invalid Credentials'})
    def post(self, request):

        email = request.data.get('email')
        password = request.data.get('password')

        user = self.get_user(email)

        dt = datetime.now() + timedelta(days=1)
        token = jwt.encode({'sub': user.id, 'exp': int(dt.strftime('%s'))}, settings.SECRET_KEY, algorithm='HS256')

        if not user.check_password(password):
            raise PermissionDenied({'message': 'Invalid Credentials'})

        return Response({'token': token, 'message': f'Hello again {user.username}'})
