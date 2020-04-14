# pylint: disable=no-member,arguments-differ
from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_422_UNPROCESSABLE_ENTITY, HTTP_204_NO_CONTENT
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt
from items.serializers import PopulatedUserSerializer, PopulatedItemSerializer, NestedItemSerializer
from items.models import Item
from .serializers import UserSerializer
User = get_user_model()

class ProfileView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request):
        # user = User.objects.get(pk=pk)
        #  ADD VIEW IN FOR ITEMS ADDED BY USER - POPULATE ITEMS ON USER
        user = request.user
        serialized_user = PopulatedUserSerializer(user)
        # print(serialized_user)
        return Response(serialized_user.data)

    def put(self, request):
        user = request.user
        # set the context to edit so password & confirmation are not needed & set partial
        # to true so that the user can edit their chose fields without editing every field on the object
        updated_user = UserSerializer(user, data=request.data, context={'is_edit': True}, partial=True)
        if updated_user.is_valid():
            updated_user.save()
            return Response(updated_user.data)
        return Response(updated_user.errors, status=HTTP_422_UNPROCESSABLE_ENTITY)

class ListingView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request):
        user = request.user
        print(user)
        items = Item.objects.all().filter(owner=user.id)
        serializer = PopulatedItemSerializer(items, many=True)
        return Response(serializer.data, status=200)


class ProfileDetailView(APIView):
    def get(self, _request, pk):
        user = User.objects.get(pk=pk)
        items = Item.objects.all().filter(owner=user)
        serializer = PopulatedItemSerializer(items, many=True)
        return Response(serializer.data, status=200)


class RegisterView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data, context={'is_edit': False})
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
