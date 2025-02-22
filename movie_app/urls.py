from django.urls import path
from .views import RegisterUser, ConfirmUser, LoginUser, DirectorList, DirectorDetail, MovieList, MovieDetail, ReviewList, ReviewDetail, MovieWithReviewsList

urlpatterns = [
    path('api/v1/directors/', DirectorList.as_view(), name='director-list'),
    path('api/v1/directors/<int:id>/', DirectorDetail.as_view(), name='director-detail'),
    path('api/v1/movies/', MovieList.as_view(), name='movie-list'),
    path('api/v1/movies/<int:id>/', MovieDetail.as_view(), name='movie-detail'),
    path('api/v1/movies/reviews/', MovieWithReviewsList.as_view(), name='movie-with-reviews-list'),
    path('api/v1/reviews/', ReviewList.as_view(), name='review-list'),
    path('api/v1/reviews/<int:id>/', ReviewDetail.as_view(), name='review-detail'),
    path('api/v1/users/register/', RegisterUser.as_view(), name='user-register'),
    path('api/v1/users/login/', LoginUser.as_view(), name='user-login'),
    path('api/v1/users/confirm/', ConfirmUser.as_view(), name='user-confirm'),
]
