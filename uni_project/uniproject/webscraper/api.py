from rest_framework.generics import ListAPIView

from .serializers import Rise_againstSerializer
from .models import Rise_against

class Rise_againstApi(ListAPIView):
	queryset = Rise_against.objects.all()
	serializer_class = Rise_againstSerializer