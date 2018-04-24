from rest_framework import serializers

from .models import Rise_against

class Rise_againstSerializer(serializers.ModelSerializer):

	class Meta:
		model = Rise_against