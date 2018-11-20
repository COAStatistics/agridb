from rest_framework.validators import (
    UniqueTogetherValidator,
)
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
)
from livestock.models import (
    Livestock,
    Investigation,
    InvestigationType,
    CountType,
    Field,
    Profile,
)


class LivestockSerializer(ModelSerializer):
    full_code = SerializerMethodField()

    def get_full_code(self, ins):
        return ins.full_code()

    class Meta:
        model = Livestock
        fields = '__all__'

    validators = [
        UniqueTogetherValidator(
            queryset=Livestock.objects.all(),
            fields=('parent', 'name', 'code'),
        )
    ]


class InvestigationTypeSerializer(ModelSerializer):
    class Meta:
        model = InvestigationType
        fields = '__all__'


class InvestigationSerializer(ModelSerializer):
    full_season = SerializerMethodField()

    def get_full_season(self, ins):
        return ins.full_season()

    class Meta:
        model = Investigation
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Investigation.objects.all(),
                fields=('type', 'year', 'season'),
            )
        ]


class CountTypeSerializer(ModelSerializer):
    class Meta:
        model = CountType
        fields = '__all__'


class FieldSerializer(ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Field.objects.all(),
                fields=('name', 'member'),
            )
        ]


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Profile.objects.all(),
                fields=('investigation', 'field', 'livestock', 'count_type', 'value'),
            )
        ]
