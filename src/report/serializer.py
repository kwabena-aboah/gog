from django.core.files.base import ContentFile
import base64 
import six
import uuid
import imghdr
import vidhdr
from django.db.models import fields
from rest_framework import serializers
from .models import District, Region, NationalReport


class Base64ImageField(serializers.ImageField):
    """ handles image-uploads through  raw post data. 
    It uses base64 for encoding and decoding the contents of the file"""

    def to_internal_value(self, data):
        #check if this is a base64 string
        if instance(data, six.string_types):
            # check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64' in data:
                # break out the header from the base64 content
                header, data = data.split(';base64')

            # Trying to decode the file. Return validation error if it fails
            try:
                decode_file = base64.b64decode(data)
            except TypeError:
                self.fail("invalid_image")

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] #call out up to 12 characters
            # get the file name extention
            file_extension = self.get_file_extension(file_name, decode_file)

            complete_file_name = "%s.%s" % (file_name, file_extension,)

            data = ContentFile(decode_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self,file_name, decode_file):
        extension = imghdr.what(file_name, decode_file)
        extension = "jpg" if extension == "jpeg" else extension
        return extension


class Base64VideoField(serializers.FileField):
    """ handles video-uploads through  raw post data. 
    It uses base64 for encoding and decoding the contents of the file"""

    def to_internal_value(self, data):
        #check if this is a base64 string
        if instance(data, six.string_types):
            # check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64' in data:
                # break out the header from the base64 content
                header, data = data.split(';base64')

            # Trying to decode the file. Return validation error if it fails
            try:
                decode_file = base64.b64decode(data)
            except TypeError:
                self.fail("invalid_file")

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] #call out up to 12 characters
            # get the file name extention
            file_extension = self.get_file_extension(file_name, decode_file)

            complete_file_name = "%s.%s" % (file_name, file_extension,)

            data = ContentFile(decode_file, name=complete_file_name)

        return super(Base64VideoField, self).to_internal_value(data)

    def get_file_extension(self,file_name, decode_file):
        extension = vidhdr.what(file_name, decode_file)
        extension = "mp4" if extension == "x-m4v" else extension
        return extension
        

# class PublicAuthoritySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PublicAuthority
#         fields = '__all__'
        
class DistrictSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(many=False)
    class Meta:
        model = District
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region 
        fields = '__all__'

class NationalReportSerializer(serializers.ModelSerializer):
    picture = Base64ImageField(
        max_length=None, use_url=True,
    )
    videos = Base64VideoField(
        max_length=None, use_url=True,
    )
    class Meta:
        model = NationalReport
        fields = ("id", "public_authority", "picture", "videos", "location", "date", "title", "is_active")