import json
import redis
from django.core.management import BaseCommand

from position.settings import SUBSCRIBE_CHANNEL

from api.models import EmployeeId, Position


class Command(BaseCommand):
    def handle(self, *args, **options):
        r = redis.StrictRedis(host='localhost', port=6379, db=1)
        p = r.pubsub()
        p.psubscribe(SUBSCRIBE_CHANNEL)
        for message in p.listen():
            data = message.get('data')
            if type(data) == bytes:
                e = json.loads(data)
                new_obj = EmployeeId.objects.create(
                    employee_id=e['employee_id'],
                    position_id=Position.objects.get(pk=e['position_id'])
                )
