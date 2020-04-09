from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser,JSONParser
from .models import UserAccount
import traceback

class GoToAccount(APIView):
	parser_classes = (JSONParser,)
	def get(self,request):
		return Response({"caution": "please add either 'fetch' or 'create' to the url"},status=403)

	def post(self,request):
		return Response({"caution": "please add either 'fetch' or 'create' to the url"},status=403)

class createUser(APIView):
	parser_classes = (MultiPartParser,)	
	def get(self,request):
		return Response({"status": "GET/ not allowed"},status=403)

	def post(self,request):
		try:
			firstName = request.POST.get('firstName')
			lastName = request.POST.get('lastName')
			email = request.POST.get('email')

			print(firstName)
			print(lastName)
			print(email)			
			if firstName and lastName and email :
				print("hi")
				_ , created = UserAccount.objects.get_or_create(
							   FirstName=firstName,LastName=lastName,Email=email)
				print(created)
				if created:
					user = UserAccount.objects.all().filter(FirstName=firstName,LastName=lastName,Email=email)[:]					
					userJson =user.values()[:]
				else:
					userJson = {"status" : "user already exists"}
			else:
				userJson = {"error": "please send all the required fields"}

			return Response(userJson , content_type='application/json')
		except Exception as e:
			traceback.print_exc()
			print(e)
			return Response({'status': "error while creating user"} , content_type='application/json',status=403)


class fetchUser(APIView):
	parser_classes = (MultiPartParser,)	
	def get(self,request):
		return Response({"status": "GET/ not allowed"},status=403)

	def post(self,request):
		try:
			pk = request.POST.get('pk')
			print("inside")

			if pk:
				try:
					print("inside2")
					user = UserAccount.objects.all().filter(pk=pk)[:]					
					userJson =user.values()[:]
					if len(userJson) == 0:
						userJson = {'error':'pk not found. User does not exist'}
				except Exception as e:
					traceback.print_exc()
					print(e)	
					userJson = {"status" : "user does not exist"}
			else:
				userJson = {"error": "please send the primary key of the user"}

			return Response(userJson , content_type='application/json')
		except Exception as e:
			traceback.print_exc()
			print(e)
			return Response({'status': "error while fetching user"} , content_type='application/json',status=403)