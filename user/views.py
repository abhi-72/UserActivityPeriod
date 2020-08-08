from rest_framework import ( viewsets,
                             serializers,
                             response )
from user.models import ( User, 
                          Activity )

class ActivitySerializer(serializers.ModelSerializer):
    start_time = serializers.DateTimeField(format='%Y-%m-%d %I:%M %p')
    end_time = serializers.DateTimeField(format='%Y-%m-%d %I:%M %p')
    class Meta:
        model = Activity
        fields = ('start_time', 'end_time')

class UserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='ref_id')
    real_name = serializers.CharField(source='name')
    tz = serializers.CharField(source='timezone')
    activity_periods = ActivitySerializer(source="user",read_only=True, many=True)
    class Meta:
        model = User
        fields = ('id', 'real_name', 'tz', 'activity_periods')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        try:
            resp = UserSerializer(self.queryset, many=True)
            return response.Response(resp.data)
        except Exception as e:
            print(str(e))

