from rest_framework import routers
from app import views

router = routers.DefaultRouter()

router.register(r'day-stats', views.DayStatsViewset, basename='day-stats')
