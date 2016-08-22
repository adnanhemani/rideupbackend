from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^login/", views.login, name='login'),
    url(r"^register/", views.register, name="register"),
    url(r"^groups/", views.groups, name="groups"),
    url(r"^ridesessions/", views.ridesessions, name="ridesessions"),
    url(r"^groupsinfo/", views.groupsinfo, name="groupsinfo"),
    url(r"^requestride/", views.requestride, name="requestride"),
    url(r"^addgroup/", views.addgroup, name="addgroup"),
    url(r"^removefromgroup/", views.removefromgroup, name="removefromgroup"),
    url(r"^admingroups/", views.admingroups, name="admingroups"),
    url(r"^adminmakenewevent/", views.adminmakenewevent, name="adminmakenewevent"),
    url(r"^whichuser/", views.whichuser, name="whichuser"),
    url(r"^groupmembers/", views.groupmembers, name="groupmembers"),
]

