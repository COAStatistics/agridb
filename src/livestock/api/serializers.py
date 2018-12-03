from rest_framework.validators import (
    UniqueTogetherValidator,
)
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    PrimaryKeyRelatedField,
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
    parent = PrimaryKeyRelatedField(queryset=Livestock.objects.all(), default=None)

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
    field = PrimaryKeyRelatedField(queryset=Field.objects.all(), default=None)

    class Meta:
        model = Profile
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Profile.objects.all(),
                fields=('investigation', 'field', 'livestock', 'count_type', 'value'),
            )
        ]


# api view

class LivestockResultSerializer(ModelSerializer):
    member = SerializerMethodField()
    count_type = SerializerMethodField()
    year = SerializerMethodField()
    season = SerializerMethodField()
    field = SerializerMethodField()
    livestock = SerializerMethodField()

    def get_member(self, ins):
        return ins.member.app_id

    def get_count_type(self, ins):
        return ins.count_type.name

    def get_year(self, ins):
        return ins.investigation.year

    def get_season(self, ins):
        return ins.investigation.full_season()

    def get_field(self, ins):
        if ins.field:
            return ins.field.name
        return None

    def get_livestock(self, ins):
        return ins.livestock.name

    class Meta:
        model = Profile
        fields = ['member', 'field', 'livestock', 'year', 'season', 'count_type', 'value']