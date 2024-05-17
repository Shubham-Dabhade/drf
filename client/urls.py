from home.views import index,people,PersonAPI,PeopleViewSet
from django.urls import path,include

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'peopleViewSet',PeopleViewSet,basename='peopleViewSet')
urlpatterns = router.urls

urlpatterns = [
    path("",include(router.urls)),
    path("index/",index),
    path('person/',people),
    path('persons-api/',PersonAPI.as_view())
]
