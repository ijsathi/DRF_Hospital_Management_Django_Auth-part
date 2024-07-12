from rest_framework import serializers
from . import models

class AppointmentSerializer(serializers.ModelSerializer):
    # for disply show
    patient = serializers.StringRelatedField(many=False)
    doctor = serializers.StringRelatedField(many=False)
    time = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.Appointment
        fields = '__all__'
