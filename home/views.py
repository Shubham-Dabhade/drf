from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializers import PeopleSerializer
from rest_framework.views import APIView
from rest_framework import viewsets


@api_view(['GET'])
def index(request):
    courses = {
        'course_name':'python',
        'learn':['django','fast-api','tornado'],
        'course_provider':'scaler'
    }

    return Response(courses)


class PersonAPI(APIView):

    def get(self,request):
        return Response({"message":'This is a get request'})
    def post(self,request):
        return Response({"message":'This is a post request'})
    def put(self,request):
        return Response({"message":'This is a put request'})
    def patch(self,request):
        return Response({"message":'This is a patch request'})

@api_view(['GET','POST','PUT','PATCH'])
def people(request):
    if request.method == "GET":
        objs = Person.objects.all()
        serializer = PeopleSerializer(objs,many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        data = request.data
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    elif request.method == 'PUT':
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PeopleSerializer(obj,data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    elif request.method == 'PATCH':
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PeopleSerializer(obj,data = data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class PeopleViewSet(viewsets.ModelViewSet):
    serializer_class = PeopleSerializer
    queryset = Person.objects.all()
