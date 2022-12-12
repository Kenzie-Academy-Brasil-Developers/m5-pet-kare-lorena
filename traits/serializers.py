from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from traits.models import Trait

class TraitSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    # name = serializers.CharField(
    #     validators = [
    #         UniqueValidator(
    #             queryset=Trait.objects.all(), message='Trait must be unique'
    #         ),
    #     ]
    # )
    name = serializers.CharField(max_length = 20)
    created_at = serializers.DateTimeField(read_only = True)