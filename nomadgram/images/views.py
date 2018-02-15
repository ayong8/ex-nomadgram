from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers

class ListAllImages(APIView):

    def get(self, request, format=None):
        all_images = models.Image.objects.all() # Go and get all images
        # all_images는 그냥 파이썬 오브젝트일 뿐이므로 json으로 바꿔야 한다
        # serialize many images and get an object
        serializer = serializers.ImageSerializer(all_images, many=True)

        # data는 serializer.data에 저장되어 있음
        return Response(data=serializer.data)