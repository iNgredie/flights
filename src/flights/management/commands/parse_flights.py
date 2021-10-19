import os
from datetime import datetime
from time import time

from django.utils import timezone
import requests
from django.core.management import BaseCommand
from requests.auth import HTTPBasicAuth

from flights.models import Flight


class AddingFlights:
    """Добавление рейсов рейсов для борта UR-82060 за последний месяц"""

    def __init__(self) -> None:
        self.status_code = None
        self.start_time = int(time()) - 30 * 24 * 60 * 60
        self.end_time = int(time())
        self.url = f'https://opensky-network.org/api/flights/' \
                   f'aircraft?icao24=508035&begin={self.start_time}&end={self.end_time}'
        self.auth = HTTPBasicAuth(os.environ.get('USERNAME'), os.environ.get('PASSWORD'))

    def get_flights(self) -> list:
        with requests.get(self.url, auth=self.auth) as r:
            self.status_code = r.status_code
            return r.json()

    def create_flights(self) -> None:
        flights = self.get_flights()
        if self.status_code == 200:
            for item in flights:
                Flight.objects.get_or_create(
                    departure_time=datetime.fromtimestamp(int(item['firstSeen']), tz=timezone.utc),
                    departure_airport=item['estDepartureAirport'],
                    arrival_time=datetime.fromtimestamp(int(item['lastSeen']), tz=timezone.utc),
                    arrival_airport=item['estArrivalAirport']
                )


class Command(BaseCommand):
    help = 'Adding flights'

    def handle(self, *args, **options):
        script = AddingFlights()
        script.create_flights()
        print(f'status code: {script.status_code}')
