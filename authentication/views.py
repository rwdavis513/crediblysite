from django.shortcuts import render

from rest_framework import permissions, viewsets
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from authentication.models import Account, UserImage
from authentication.permissions import IsAccountOwner
from authentication.serializers import AccountSerializer, UserImageSerializer

import json
from django.contrib.auth import authenticate, login, logout
import logging

logger = logging.getLogger(__name__)

class AccountViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    def create(self, request):
       serializer = self.serializer_class(data=request.data)

       if serializer.is_valid():
           Account.objects.create_user(**serializer.validated_data)

           return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

       return Response({
           'status': 'Bad request',
           'message': 'Account could not be created with received data.'
       }, status=status.HTTP_400_BAD_REQUEST)


class LoginView(views.APIView):
    def post(self, request, format=None):
        data = json.loads(request.body)

        email = data.get('email',None)
        password = data.get('password',None)

        account = authenticate(email=email, password=password)

        if account is not None:
            if account.is_active:
                login(request, account)

                serialized = AccountSerializer(account, context={'request': request})

                return Response(serialized.data)
            else:
                return Response({
                    'status': 'Unauthorized',
                    'message': 'This account has been disabled.'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username/password combination invalid.'
            }, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        logout(request)

        return Response({}, status=status.HTTP_204_NO_CONTENT)


class UserImageListView(views.APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAccountOwner)
    parser_classes = (MultiPartParser,)

    def get(self, request, format=None):
        image = UserImage.objects.all()
        serializer = UserImageSerializer(image, many=True, context={'request':self.request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        logger.debug("UserImageListView.post...")

        serializer = UserImageSerializer(data=request.data, context={'request':self.request})

        logger.debug(request.data)
        #logger.debug(serializer.instance)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        #logger.debug(serializer.validated_data)
        logger.debug(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserImageDetailView(views.APIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAccountOwner)  # Need to update to allow read only view
    parser_classes = (MultiPartParser,)

    def get_object(self, pk):
        try:
            return UserImage.objects.get(pk=pk)
        except UserImage.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, format=None):
        image = self.get_object(pk)
        serializer = UserImageSerializer(image, context={'request':self.request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        image = self.get_object(pk)
        serializer = UserImageSerializer(image, data=request.data, context={'request':self.request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        image = self.get_object(pk)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def pre_save(self, obj):
        obj.owner = self.request.user


# class FileUploadView(views.APIView):
#     parser_classes = (MultiPartParser,)
#
#     def post(self, request, format=None):
#         logger.info(self.request.user.username)
#         file_obj = request.data['file']
#
#         #data = json.loads(request.data)
#         #filename = data.get('filename', None)
#         #filename = request.data['filename']
#
#         with open('static/media/images/' + self.request.user.username + '.jpg', 'wb+') as destination:
#             for chunk in file_obj.chunks():
#                 destination.write(chunk)
#
#         return Response(status=status.HTTP_204_NO_CONTENT)
