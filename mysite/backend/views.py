import json
from .models import User, Group, EventRequests, Event, EventRideGroup
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from django.http import JsonResponse, HttpResponse
from django.core import serializers

@csrf_exempt
def login(request):
    retVal = {}
    email = request.GET["email"]
    pw = request.GET["password"]
    user = User.objects.filter(email_address=email)
    if not user:
        retVal = {"logged_in": False, "reason": "User not found"}
        return JsonResponse(retVal)
    if user[0].password == pw:
        retVal = {"logged_in": True, "user": user[0].id}
        return JsonResponse(retVal)
    else:
        retVal = {"logged_in": False, "reason": "User and Password do not match."}
        return JsonResponse(retVal)


@csrf_exempt
def register(request):
    #try:
    group = request.GET["g"]
    if (User.objects.filter(email_address=request.GET["email"])):
        return JsonResponse({"success": False, "reason": "A user already exists with this username"})
    new_user = User(first_name=request.GET["fname"], last_name=request.GET["lname"], phone_number=request.GET["phone_number"], 
        email_address=request.GET["email"], password=request.GET["pw"], is_driver=request.GET["driver"], has_own_car=request.GET["own_car"])
    new_user.save()
    new_user.groups.add(group)
    new_user.save()
    retVal={"success": True}
    return JsonResponse(retVal)
    # except:
    #     return JsonResponse({"success": False, "reason": "whelp"})

@csrf_exempt
def groups(request):
    try:    
        user_id = request.GET["user"]
        user = User.objects.filter(id=user_id)[0]
        #print(user.groups.all())
        group_list = serializers.serialize("json", user.groups.all())
        retVal = {"error": False, "groups": group_list}
        return JsonResponse(retVal) 
    except:
        return JsonResponse({"error": True, "reason": "no user"})

@csrf_exempt
def ridesessions(request):
    try:    
        user_id = request.GET["user"]
        user = User.objects.filter(id=user_id)[0]
        #print(user.groups.all())
        events = []
        for group in user.groups.all():
            for event in Event.objects.filter(group=group.id, active=True):
                events.append(event)
        event_json = serializers.serialize("json", events)
        retVal = {"error": False, "groups": event_json}
        return JsonResponse(retVal) 
    except:
        return JsonResponse({"error": True, "reason": "no user found"})

@csrf_exempt
def groupsinfo(request):
    try:
        group_number = request.GET["group"]
        group = Group.objects.filter(id=group_number)[0]
        group_userbase = 0
        past_events = []
        for user in User.objects.all():
            if user.groups.all().filter(id=group_number):
                group_userbase += 1
        for event in Event.objects.all():
            print(event.group.id==group.id)
            if event.group.id == group.id:
                past_events.append(event)
        event_list = serializers.serialize("json", past_events)
        retVal = {"error": False, "admin": group.admin.first_name + " " + group.admin.last_name, "name": group.name, "users": group_userbase, "past_events": event_list}
        return JsonResponse(retVal)
    except:
        return JsonResponse({"error": True, "reason": "No group found. Oops?!?!"})

@csrf_exempt
def requestride(request):
    try:
        user_id = request.GET["user"]
        user = User.objects.filter(id=user_id)[0]
    except:
        return JsonResponse({"error": True, "reason": "User not found. Oops?!?!"})

    retVal = {}
    event_id=request.GET["event_id"]
    event_obj = Event.objects.filter(id=event_id)[0]
    if user.is_driver:
        new_rr = EventRequests(user=user, driver_leaving_time=request.GET["driver_leaving_time"], driver_car_spaces=request.GET["driver_spaces"], event=event_obj)
    else:
        new_rr = EventRequests(user=user, driver_leaving_time=None, driver_car_spaces=None, event=event_obj)

    try:
        new_rr.save()
    except:
        retVal["error"] = True
        retVal["reason"] = "You are a driver and you have left either your leaving time or spaces in your car blank. Please try again."
        return JsonResponse(retVal)
    retVal["error"] = False
    return JsonResponse(retVal)

@csrf_exempt
def addgroup(request):
    try:
        user_id = request.GET["user"]
        user = User.objects.filter(id=user_id)[0]
    except:
        return JsonResponse({"error": True, "reason": "User not found. Oops?!?!"})

    try:
        group_id = request.GET["group"]
        group = Group.objects.filter(id=group_id)[0]
    except:
        return JsonResponse({"error": True, "reason": "Group not found. Oops?!?!"})

    try:
        user.groups.add(group_id)
    except:
        return JsonResponse({"error": True, "reason": "User is already part of this group."})
    user.save()
    retVal = {"error": False}
    return JsonResponse(retVal)

@csrf_exempt
def removefromgroup(request):
    try:
        user_id = request.GET["user"]
        user = User.objects.filter(id=user_id)[0]
    except:
        return JsonResponse({"error": True, "reason": "User not found. Oops?!?!"})

    try:
        group_id = request.GET["group"]
        group = Group.objects.filter(id=group_id)[0]
    except:
        return JsonResponse({"error": True, "reason": "Group not found. Oops?!?!"})

    user.groups.remove(group_id)
    user.save()
    retVal = {"error": False}
    return JsonResponse(retVal)

@csrf_exempt
def admingroups(request):
    try:    
        user_id = request.GET["user"]
        user = User.objects.filter(id=user_id)[0]
        groupadmin = []
        for group in Group.objects.all():
            print(group.admin.id)
            if group.admin.id == user.id:
                groupadmin.append(group)

        group_list = serializers.serialize("json", groupadmin)
        retVal = {"error": False, "groups": group_list}
        return JsonResponse(retVal) 
    except:
        return JsonResponse({"error": True, "reason": "no user"})

@csrf_exempt
def adminmakenewevent(request):
    group = Group.objects.filter(id=request.GET["group"])[0]
    new_event = Event(name=request.GET["name"], event_time=request.GET["event_time"], 
        signup_expiry_time=request.GET["signup_expiry"], group=group, active=True)

    retVal = {}
    try:
        new_event.save()
    except:
        retVal["error"] = True
        retVal["reason"] = "Some input of yours is wrong. Please try again."
        return JsonResponse(retVal)
    retVal["error"] = False
    return JsonResponse(retVal)

@csrf_exempt
def whichuser(request):
    user_id = request.GET["user_id"]
    user = User.objects.filter(id=user_id)[0]
    user_ser = serializers.serialize("json", [user])
    return JsonResponse({"error": False, "user": user_ser})

@csrf_exempt
def groupmembers(request):
    group_id = request.GET["group"]
    group_members = []
    for user in User.objects.all():
        if user.groups.all().filter(id=group_id):
            group_members.append(user)
    group_members_ser = serializers.serialize("json", group_members)
    return JsonResponse({"error": False, "members": group_members_ser})



