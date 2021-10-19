from datetime import timedelta
from django.utils import timezone
from django.views.generic import ListView

from .models import Flight


class FlightListView(ListView):
    queryset = Flight.objects.filter(departure_time__gte=timezone.now() - timedelta(days=30))
    template_name = 'flights.html'
    paginate_by = 5
