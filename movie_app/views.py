from rest_framework import generics
from django.db.models import Count, Avg
from .models import Director, Movie
from .serializers import DirectorSerializer, MovieSerializer


class DirectorListWithMovieCount(generics.ListAPIView):
    queryset = Director.objects.annotate(movies_count=Count('movies'))
    serializer_class = DirectorSerializer


class MovieReviewList(generics.ListAPIView):
    queryset = Movie.objects.prefetch_related('reviews').annotate(
        rating=Avg('reviews__stars')
    )
    serializer_class = MovieSerializer


from .models import Review
from .serializers import ReviewSerializer


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
