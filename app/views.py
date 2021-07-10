from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class UplaodTextAPIView(APIView):
    def get(self, request, *args, **kwargs):
        text = request.data['text']

        return Response(status=status.HTTP_200_OK)
