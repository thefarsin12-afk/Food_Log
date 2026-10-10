from django.urls import path

from food_log.views import UserView,GetMeView
from food_log.views import MealRecordListCreateView,MealRecordRetrieveUpdateDeleteView

urlpatterns = [

    #==== user section ====
    path("signup/",UserView.as_view()),

    path('me/',GetMeView.as_view()),

    # ==== meal record list,creat section ====
    path('meal/',MealRecordListCreateView.as_view()),

    # ==== meal record retrieve,update,delete section ====
    path('meal/<int:pk>/',MealRecordRetrieveUpdateDeleteView.as_view()),
]