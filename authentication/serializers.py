from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from authentication.models import Account, UserImage
from crediblysite import settings

class UserImageSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    #image_url = serializers.SerializerMethodField()

    #def get_image_url(self, obj):
        #return '%s%s' % (settings.MEDIA_URL, obj.image.url)
        #return obj.image.url

    class Meta:
        model = UserImage
        fields = ('url','id','image','owner','label')
        owner = serializers.Field(source='owner.username')
        readonly_fields = ('url', 'image')

class AccountSerializer(serializers.ModelSerializer):
   password = serializers.CharField(write_only=True, required=False)
   confirm_password = serializers.CharField(write_only=True, required=False)
   full_name = serializers.SerializerMethodField()

   #image = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='userimage-detail')
   image = UserImageSerializer(many=True,read_only=True)

   def get_full_name(self, instance):
       return instance.get_full_name()

   class Meta:
      model = Account
      fields = ('id', 'email', 'username', 'created_at', 'updated_at',
                'first_name', 'last_name', 'full_name', 'tagline', 'password',
                'confirm_password','address_street','address_city',
                'address_state','personal_website', 'image', 'job_title')
      read_only_fields = ('created_at', 'updated_at',)

      def create(self, validated_data):
          #user_image = validated_data.pop('image')
          #UserImage.objects.create(user_image)
          return Account.objects.create(**validated_data)

      def update(self, instance, validated_data):
          instance.username = validated_data.get('username', instance.username)
          instance.tagline = validated_data.get('tagline', instance.tagline)
     
          instance.save()

          password = validated_data.get('password', None)
          confirm_password = validated_data.get('confirm_password', None)
 
          if password and confirm_password and password == confirm_password:
              instance.set_password(password)
              instance.save()

          update_session_auth_hash(self.context.get('request'), instance)

          return instance