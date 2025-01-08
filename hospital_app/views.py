from rest_framework import viewsets, generics, status
from rest_framework.generics import *
from rest_framework.permissions import *
from .filters import *
from .models import *
from .pagination import *
from .permissions import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView



# class RegisterView(generics.CreateAPIView):
#     serializer_class = ProfileSerializer
#
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# class CustomLoginView(TokenObtainPairView):
#     serializer_class = LoginSerializer
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         try:
#             serializer.is_valid(raise_exception=True)
#         except Exception:
#             return Response({'detail': 'Неверные учетные данные'}, status=status.HTTP_401_UNAUTHORIZED)
#
#         user = serializer.validated_data
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# class LogoutView(generics.GenericAPIView):
#     def post(self, request, *args, **kwargs):
#         try:
#             refresh_token = request.data['refresh']
#             token = RefreshToken(refresh_token)
#             token.blacklist()
#             return Response(status=status.HTTP_205_RESET_CONTENT)
#         except Exception:
#             return Response(status=status.HTTP_400_BAD_REQUEST)

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer

class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    permission_classes = [CheckHospitalOwner]

class HospitalImageViewSet(viewsets.ModelViewSet):
    queryset = HospitalImage.objects.all()
    serializer_class = HospitalImageSerializer

class DepartmentCategoryViewSet(viewsets.ModelViewSet):
    queryset = DepartmentCategory.objects.all()
    serializer_class = DepartmentCategorySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['department_name']



class DoctorListViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = DoctorFilter
    ordering_fields = ['price']
    pagination_class = DoctorPagination
    permission_classes = [CheckDoctor]

class DoctorDetailViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorDetailSerializer

class PatientProfileListCreateView(ListCreateAPIView):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientProfileSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class MedicalRecordListAPIView(ListCreateAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    permission_classes = [CheckMedicalRecords]

class MedicalRecordDetailListAPIView(ListCreateAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordDetailSerializer
    permission_classes = [CheckMedicalRecords]

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
