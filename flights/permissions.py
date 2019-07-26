from rest_framework.permissions import BasePermission
from datetime import date

class isowner(BasePermission):
    message="only the owner of the booking can access this"

    def has_object_permissions(self, request, view, obj):
        if request.user.is_staff or (obj.user==request.user):
            return True
        else:
            return False

class is_3d_away(BasePermission):
    message="You can not update or cancel any booking 3 days away from your travel date"

    def has_object_permissions(self, request, view, obj):
        today = date.today()
        if (obj.date - today).days >= 3 :
            return True
        else:
            return False