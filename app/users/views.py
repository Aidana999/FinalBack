from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserModelSerializer


class UserApiView(APIView):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            serializer = UserModelSerializer(request.user)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "User in not logged in"}, status=status.HTTP_401_UNAUTHORIZED)
