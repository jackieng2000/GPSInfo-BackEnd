from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import GPSLocation
from .serializers import GPSLocationSerializer
from accounts.models import Profile  # Adjust if accounts app is different


# class GPSLocationViewSet(viewsets.ModelViewSet):
#     queryset = GPSLocation.objects.all()
#     serializer_class = GPSLocationSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


class GPSLocationViewSet(viewsets.ModelViewSet):
    queryset = GPSLocation.objects.all()
    serializer_class = GPSLocationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'], url_path='group/(?P<group>\w+)')
    def get_group_records(self, request, group=None):
        # Fetch users in the group
        users_in_group = Profile.objects.filter(userGroup=group).values_list('user', flat=True)
        # Fetch GPS records for those users
        queryset = GPSLocation.objects.filter(user__in=users_in_group).order_by('-timestamp')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
