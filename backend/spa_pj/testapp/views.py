from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

def hello(request):
   return HttpResponse("Hello, World!")


# 인증 오류 발생시 아래 어노테이션 필요
# @api_view(['GET', 'POST'])
# @permission_classes([AllowAny])

@api_view(['GET'])
def hello_rest_api(request):
   data = {'message': 'Hello, REST API!'}
   return Response(data)
