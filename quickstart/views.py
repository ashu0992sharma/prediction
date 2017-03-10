from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions, renderers


from . import models, serializers


class HostelView(APIView):
    def post(self, request):
        """

        :param request:
        :return:
        """

        models.Hostel.objects.create(**(request.data))
        return Response({'message': 'success'}, status=status.HTTP_201_CREATED)


class TestView(APIView):
    """
    Story read api
    """
    template_name = 'hello.html'

    def get(self, request):
        """
        GET api for test
        :return: Room object
        """
        rooms = models.Room.objects.all()
        serializer = serializers.RoomSerializer(rooms, many=True)
        if serializer.is_valid:
            return render(request, self.template_name, {'data': serializer.data})
        return render(request, self.template_name, {'data': []})

    def post(self, request):
        """
        :param request:
        :return:
        """
        hostel = get_object_or_404(models.Hostel, pk=request.data['hostel'])
        serializer = serializers.RoomCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(hostel=hostel)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


