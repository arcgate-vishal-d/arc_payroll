from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response


class TestProject(APIView):
    def get(self, resquest):
        return Response({"msg": "Project setup"})


class trigger_error(APIView):
    def get(self, request):
        division_by_zero = 1 / 0
        return Response({"msg": "Error"})
