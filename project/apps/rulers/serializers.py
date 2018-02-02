from rest_framework import serializers

from project.apps.rulers.models import Ruler


class RulerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruler
        fields = ['id', 'name', 'url']


class RulerWithRelatedSerializer(serializers.ModelSerializer):
    successor = RulerSerializer()
    predecessor = RulerSerializer()

    class Meta:
        model = Ruler
        fields = ['id', 'name', 'url', 'successor', 'predecessor']


class RulerWithAllSuccessorsSerializer(serializers.ModelSerializer):
    successor = RulerSerializer()
    predecessor = RulerSerializer()
    all_successors = RulerWithRelatedSerializer(many=True)

    class Meta:
        model = Ruler
        fields = ['id', 'name', 'url', 'successor', 'predecessor', 'all_successors']
