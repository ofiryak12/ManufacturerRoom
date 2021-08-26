from .models import pt
from rest_framework import serializers


class ptSerializer(serializers.ModelSerializer):
    class Meta:
        model = pt
        fields = ['wiring', 'wiring_detail', 'assembly', 'assembly_detail','assembly_qa', 'assembly_qa_detail', 'technosoft', 'technosoft_detail',
                  'captrack','captrack_detail','final_qa', 'final_qa_detail']
