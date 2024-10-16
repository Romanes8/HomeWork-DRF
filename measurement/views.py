from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


class ListCreateAPIView(ListAPIView):
    #получение списка датчиков с краткой информацией
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    #создание датчика
    def post(self, request):
        review = SensorSerializer(data=request.data)
        if review.is_valid():
            review.save()
        return Response({'Датчик добавлен': request.data})


class RetrieveUpdateAPIView(RetrieveAPIView):
    #вывод информации по конкретному датчику
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    #изменение информации по датчику
    def patch(self, request, pk):
        sensor = Sensor.objects.get(pk=pk)
        serializer = SensorSerializer(sensor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class CreateAPIView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    #добавление измерения
    def post(self, request):
        review = MeasurementSerializer(data=request.data)
        if review.is_valid():
            review.save()
        return Response({'Добавлена температура': request.data})









