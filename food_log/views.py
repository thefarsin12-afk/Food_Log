from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Sum
from datetime import datetime

from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework import authentication,permissions
from food_log.permision import IsOwner

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

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):

        auth_user = request.user

        instants = User.objects.get(username=auth_user)

        serialize_instants = UserSerializer(instants)

        return Response(data=serialize_instants.data)

class MealRecordListCreateView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

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

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsOwner]

    def get(self,request,pk=None):

        instance = get_object_or_404(MealRecordModel,id=pk)

        self.check_object_permissions(request,instance)

        serializer_instants = MealRecordSerializer(instance)

        return Response(data=serializer_instants.data)

    def put(self,request,pk=None):

        instance = get_object_or_404(MealRecordModel,id=pk)

        self.check_object_permissions(request,instance)

        form_data = request.data

        serializer_instace = MealRecordSerializer(data=form_data, instance=instance)

        if serializer_instace.is_valid():

            serializer_instace.save()

            return Response(data=serializer_instace.data)

        else:
            return Response(data=serializer_instace.errors)

    def delete(self,request,pk=None):

        instance = get_object_or_404(MealRecordModel,id=pk)

        self.check_object_permissions(request,instance)

        instance.delete()

        return Response(data={"Message:Record Deleted"})   

class SummaryView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):

        response_data = {

            "total":0
        }

        currt_month = datetime.now().month

        currt_year = datetime.now().year

        currt_date = datetime.now().today()

        #monthly_summary

        monthly_summary = MealRecordModel.objects.filter(owner = request.user,created_at__month = currt_month,created_at__year = currt_year)

        if monthly_summary:

            monthly_calorie = monthly_summary.values("calorie").aggregate(total=Sum("calorie")).get("total")

            response_data ["monthly_calorie"] = monthly_calorie



        # today summary

        today_calorie = MealRecordModel.objects.filter(owner=request.user,created_at__date=currt_date)

        if today_calorie:

            today_summary = today_calorie.values("calorie").aggregate(today_total=Sum("calorie")).get("today_total")

            response_data["today_total"] = today_summary

            # category summary

            category_summary = today_calorie.values("meal_type").annotate(details=Sum("calorie"))

            response_data["details"] = category_summary


        return Response(data=response_data)    



    

    

    