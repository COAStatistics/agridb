from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
)
from livestock.models import (
    Field,
    Profile,
)


class ProfileSerializer(ModelSerializer):
    count_type = SerializerMethodField()
    year = SerializerMethodField()
    season = SerializerMethodField()
    livestock = SerializerMethodField()

    def get_count_type(self, ins):
        return ins.count_type.name

    def get_year(self, ins):
        return ins.investigation.year

    def get_season(self, ins):
        return ins.investigation.full_season()

    def get_livestock(self, ins):
        return ins.livestock.name

    class Meta:
        model = Profile
        fields = ['livestock', 'year', 'season', 'count_type', 'value']


class FieldSerializer(ModelSerializer):
    profiles = ProfileSerializer(many=True)

    class Meta:
        model = Field
        fields = ['name', 'profiles']



