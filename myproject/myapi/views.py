from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status, viewsets
from .models import Item,Doctor
from .serlializers import ItemSerializer,DoctorSerializer

@api_view(['GET'])
def ApiOverview(request):
    return Response(
		{
			'status':'ok'
		}
	)
    
# @api_view(['POST'])
# def add_item(request):
#     item=ItemSerializer(request.data)
    
#     i
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import DoctorSerializer

class DoctorOverview(viewsets.ViewSet):
    def create(self, request):
        serializer = DoctorSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        queryset = Doctor.objects.all()
        serializer =DoctorSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)




    # validating for already existing data
    # if Item.objects.filter(**request.data).exists():
    #     raise serializers.ValidationError('This data already exists')