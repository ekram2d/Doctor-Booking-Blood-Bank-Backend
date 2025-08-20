from .models import Item,Doctor
from rest_framework import serializers
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields=('category','subcategory','name','amount')
        
class DoctorSerializer(serializers.ModelSerializer):
    # For returning absolute URL
    image_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Doctor
        fields = ['id', 'name', 'title', 'department', 'image', 'image_url']
        # "image" will accept uploads
        # "image_url" will return full URL

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None

