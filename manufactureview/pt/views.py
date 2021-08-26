from django.shortcuts import render
from .models import pt
from .serializers import ptSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class ptView(APIView):

    def get(self,request):
        data = pt.objects.all()
        serializer = ptSerializer(data,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ptSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)