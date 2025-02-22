# movie_app/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from django.db.models import Count, Avg

from .models import Director, Movie, Review, User
from .serializers import (
    DirectorSerializer,
    MovieSerializer,
    ReviewSerializer,
    UserSerializer,
    UserConfirmationSerializer
)


class DirectorListWithMovieCount(generics.ListAPIView):
    queryset = Director.objects.annotate(movies_count=Count('movies'))
    serializer_class = DirectorSerializer


class MovieReviewList(generics.ListAPIView):
    queryset = Movie.objects.prefetch_related('reviews').annotate(rating=Avg('reviews__stars'))
    serializer_class = MovieSerializer


class DirectorList(generics.ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class DirectorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class RegisterUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class ConfirmUser(generics.GenericAPIView):
    serializer_class = UserConfirmationSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        confirmation_code = serializer.validated_data['confirmation_code']

        try:
            user = User.objects.get(email=email, confirmation_code=confirmation_code)
            user.is_active = True
            user.confirmation_code = ''
            user.save()
            return Response({'message': 'User confirmed'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'message': 'Invalid confirmation code'}, status=status.HTTP_400_BAD_REQUEST)


class LoginUser(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            if user.is_active:
                return Response({'message': 'User logged in'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'User is not confirmed'}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response({'message': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)
