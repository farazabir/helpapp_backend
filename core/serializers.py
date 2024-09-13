from rest_framework import serializers
from .models import Section, Parent, Child


class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = ['id', 'name', 'details', 'phone_number', 'location']


class ParentSerializer(serializers.ModelSerializer):
    children = ChildSerializer(
        many=True, read_only=True)

    class Meta:
        model = Parent
        fields = ['id', 'name', 'logo_link', 'children']


class SectionSerializer(serializers.ModelSerializer):
    parents = ParentSerializer(
        many=True, read_only=True)

    class Meta:
        model = Section
        fields = ['id', 'name', 'logo', 'parents']
