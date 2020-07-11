from .models import User, UserProfile
from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('id', 'url', 'first_name', 'last_name', 'gender', 'phone', 'date_of_birth', 'address', 'country', 'city', 'zip')


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(required=False)

    class Meta:
        model = User
        fields = ('id','url', 'email', 'password', 'profile') #'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')

        password = validated_data.pop('password')
        print('---------{}'.format(password))
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.first_name = profile_data.get('first_name', profile.first_name)
        profile.last_name = profile_data.get('last_name', profile.last_name)
        profile.gender = profile_data.get('gender', profile.gender)
        profile.phone = profile_data.get('phone', profile.phone)
        profile.date_of_birth = profile_data.get('dob', profile.date_of_birth)
        profile.address = profile_data.get('address', profile.address)
        profile.country = profile_data.get('country', profile.country)
        profile.city = profile_data.get('city', profile.city)
        profile.zip = profile_data.get('zip', profile.zip)
        profile.save()

        return instance
