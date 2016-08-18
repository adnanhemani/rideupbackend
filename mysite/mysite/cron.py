#Possibly a waste of time; Use Heroku Scheduler instead


from django.conf import settings
#from django.contrib.auth.models import Event
from backend.models import Event

from django_cron import CronJobBase, Schedule
from django.utils import timezone

class MyCronJob(CronJobBase):
    RUN_AT_TIMES = ["8:00", "9:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:01", "16:30", "17:01", 
    "17:30", "18:01", "18:30", "19:01", "19:30", "20:00", "21:00", "22:00", "23:00", "0:00", "1:00"]

    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'my_app.my_cron_job'    # a unique code

    def do(self):
        active_events = Event.objects.filter(active=True)
        for event in active_events:
            if event.signup_expiry_time < timezone.now():
                event.active = False
                event.save()
