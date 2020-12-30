import json
import redis
from django.core.management import BaseCommand

from employee.settings import PUBLISH_CHANNEL


class Command(BaseCommand):
    def handle(self, *args, **options):
        r = redis.StrictRedis(host='localhost', port=6379, db=1)
        p = r.pubsub()
        p.psubscribe(PUBLISH_CHANNEL)
        for message in p.listen():
            data = message.get('data')
            if type(data) == bytes:
                e = json.loads(data)
                print(e)
                print(type(e))
