from django.db import models

# Create your models here.

class Group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    admin = models.ForeignKey("User", on_delete=models.CASCADE)

    def __str__(self):
        return self.name + str(self.id)



class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    email_address = models.EmailField(max_length=254)
    password = models.CharField(max_length=16)
    is_driver = models.BooleanField()
    has_own_car = models.BooleanField()
    groups = models.ManyToManyField(Group, blank=True)

    def __str__(self):
        return self.first_name + self.last_name + str(self.id)


class Event(models.Model):
    DEFAULT_GROUP_ID = 0

    id = models.AutoField(primary_key=True)
    date_time_created = models.DateTimeField(auto_now=True, auto_now_add=True)
    name = models.CharField(max_length=100)
    event_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    signup_expiry_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, default=DEFAULT_GROUP_ID)
    active = models.BooleanField()

    def __str__(self):
        return self.name + " " + str(self.event_time) + " " + str(self.id)

class EventRequests(models.Model):
    DEFAULT_EVENT_ID = 4

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    driver_leaving_time = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    driver_car_spaces = models.IntegerField(null=True, blank=True)
    special_requests = models.CharField(max_length=50, null=True, blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, default=DEFAULT_EVENT_ID)

    def __str__(self):
        return str(self.user) + " " + str(self.id) + " " + str(self.event)


class EventRideGroup(models.Model):
    id = models.AutoField(primary_key= True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_requests_assigned')
    riders = models.ManyToManyField("User", related_name='%(class)s_requests_created', blank=True)
    time_leaving = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.event + str(self.id)



