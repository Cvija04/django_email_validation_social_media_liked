from rest_framework.views import APIView
from .EmailCheckApi import EmailChecker
from rest_framework.response import Response
from rest_framework import status
from validate_email import validate_email

class CheckEmailView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        if email:
            email_checker = EmailChecker(email)
            data = email_checker.send_data()
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)
        
class CheckEmailValidationView(APIView):
    def post(self, request):
        email = request.data.get('email', None)
        if email is None:
            return Response({'error': 'Please provide an email address'}, status=status.HTTP_400_BAD_REQUEST)
        is_valid = validate_email(email)
        if is_valid:
            return Response({'message': 'Email address is valid'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Email address is not valid'}, status=status.HTTP_400_BAD_REQUEST)