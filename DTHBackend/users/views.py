from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics, filters
from .models import CustomUser, HeroUser, HostUser
from .serializers import CustomUserSerializer, CustomUserDetailSerializer, HostUserSerializer, HeroUserSerializer, HeroUserDetailSerializer, HostUserDetailSerializer, HeroUpgradeSerializer, HostUpgradeSerializer
from .permissions import IsOwnerOrReadOnly


class CustomUserList(APIView):
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class CustomUserDetail(APIView):
    permissions_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try: 
            user = CustomUser.objects.get(pk=pk)
            self.check_object_permissions(self.request, user)
            return user
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        data = request.data
        serializer = CustomUserDetailSerializer(
            instance=user,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(   
            status=status.HTTP_204_NO_CONTENT
        )


class HostUserList(APIView):
    def get(self, request):
        users = HostUser.objects.all()
        serializer = HostUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HostUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class HeroUserList(APIView):
    def get(self, request):
        users = HeroUser.objects.all()
        serializer = HeroUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HeroUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class HeroUpgradeList(APIView):
    permissions_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try: 
            user = CustomUser.objects.get(pk=pk)
            self.check_object_permissions(self.request, user)
            return user
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request):
        user = HeroUser.objects.all()
        serializer = HeroUpgradeSerializer(user, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        data = request.data
        serializer = HeroUpgradeSerializer(data=request.data, context={'user': user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class HostUpgradeList(APIView):
    permissions_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try: 
            user = CustomUser.objects.get(pk=pk)
            self.check_object_permissions(self.request, user)
            return user
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request):
        user = HostUser.objects.all()
        serializer = HostUpgradeSerializer(user, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        data = request.data
        serializer = HostUpgradeSerializer(data=request.data, context={'user': user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class HeroUserDetail(APIView):
    permissions_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try: 
            user = HeroUser.objects.get(pk=pk)
            self.check_object_permissions(self.request, user)
            return user
        except HeroUser.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = HeroUserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        data = request.data
        serializer = HeroUserDetailSerializer(
            instance=user,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(   
            status=status.HTTP_204_NO_CONTENT
        )

class HostUserDetail(APIView):
    permissions_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try: 
            user = HostUser.objects.get(pk=pk)
            self.check_object_permissions(self.request, user)
            return user
        except HostUser.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = HostUserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        data = request.data
        serializer = HostUserDetailSerializer(
            instance=user,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(   
            status=status.HTTP_204_NO_CONTENT
        )

class HeroList(generics.ListAPIView):
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        heroes = CustomUser.objects.filter(is_hero=True)
        return heroes

class HostList(generics.ListAPIView):
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        hosts = CustomUser.objects.filter(is_host=True)
        return hosts

class FeminineHeroList(generics.ListAPIView):
    serializer_class = HeroUserSerializer

    def get_queryset(self):
        feminine = HeroUser.objects.filter(gender='feminine')
        return feminine

class NonGenderHeroList(generics.ListAPIView):
    serializer_class = HeroUserSerializer

    def get_queryset(self):
        gender = HeroUser.objects.filter(gender='prefer not to say')
        return gender