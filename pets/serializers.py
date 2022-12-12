from rest_framework import serializers
from pets.models import PetSex, Pet

from groups.serializers import GroupSerializer
from traits.serializers import TraitSerializer

from groups.models import Group
from traits.models import Trait

class PetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(
        choices=PetSex.choices,
        default=PetSex.NOT_INFORMED,
    )
    group = GroupSerializer()
    # traits = TraitSerializer(many = True)

    def create(self, validated_data: dict):
        group_dict = validated_data.pop('group')

        pet_obj = Pet.objects.create(**validated_data)
        group = Group.objects.get_or_create(**group_dict, pet = pet_obj)

        return pet_obj
    
    def update(self, instance, validated_data: dict):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance