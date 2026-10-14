from django.urls import path

from food_log.views import UserView,GetMeView
from food_log.views import MealRecordListCreateView,MealRecordRetrieveUpdateDeleteView
from food_log.views import SummaryView

from rest_framework.authtoken.views import ObtainAuthToken


urlpatterns = [

    #==== user section ====
    path("signup/",UserView.as_view()),

    path('me/',GetMeView.as_view()),

    # ==== meal record list,creat section ====
    path('meal/',MealRecordListCreateView.as_view()),

    # ==== meal record retrieve,update,delete section ====
    path('meal/<int:pk>/',MealRecordRetrieveUpdateDeleteView.as_view()),

    # ==== summary ====
    path('meal/summary/',SummaryView.as_view()),

    # ==== token authentication ====
    path('token/',ObtainAuthToken.as_view()),
]