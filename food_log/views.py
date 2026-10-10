from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework import authentication,permissions

from food_log.serializer import UserSerializer
from food_log.serializer import MealRecordSerializer
from food_log.models import MealRecordModel

class UserView(APIView):

    def post(self,request):

        form_data = request.data

        serializer_instants = UserSerializer(data=form_data)

        if serializer_instants.is_valid():

            cleaned_data = serializer_instants.validated_data

            instans = User.objects.create_user(**cleaned_data)

            serializer_instants = UserSerializer(instans)

            return Response(data=serializer_instants.data)

        else:
            return Response(data=serializer_instants.errors)

class GetMeView(APIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):

        auth_user = request.user

        instants = User.objects.get(username=auth_user)

        serialize_instants = UserSerializer(instants)

        return Response(data=serialize_instants.data)

class MealRecordListCreateView(APIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):

        instance = MealRecordModel.objects.filter(owner = request.user)

        serialize_instance = MealRecordSerializer(instance,many=True)

        return Response(data=serialize_instance.data)

    def post(self,request):

        form_data = request.data

        serializer_instans = MealRecordSerializer(data=form_data)

        if serializer_instans.is_valid():

            serializer_instans.save(owner = request.user)

            return Response(data=serializer_instans.data)

        else:

            return Response(data=serializer_instans.errors)  

class MealRecordRetrieveUpdateDeleteView(APIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,pk=None):

        instance = get_object_or_404(MealRecordModel,id=pk)

        serializer_instants = MealRecordSerializer(instance)

        return Response(data=serializer_instants.data)

    def put(self,request,pk=None):

        instance = get_object_or_404(MealRecordModel,id=pk)

        form_data = request.data

        serializer_instace = MealRecordSerializer(data=form_data, instance=instance)

        if serializer_instace.is_valid():

            serializer_instace.save()

            return Response(data=serializer_instace.data)

        else:
            return Response(data=serializer_instace.errors)

    def delete(self,request,pk=None):

        instance = get_object_or_404(MealRecordModel,id=pk)

        instance.delete()

        return Response(data={"Message:Record Deleted"})        

    

    

    