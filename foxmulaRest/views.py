from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser,JSONParser

# Create your views here.
class GoToHome(APIView):
	parser_classes = (JSONParser,)
	def get(self,request):
		return Response({"caution": "please add account/ to the url"},status=403)

	def post(self,request):
		return Response({"caution": "please add account/ to the url"},status=403)