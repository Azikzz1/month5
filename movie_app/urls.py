from django.urls import path
from .views import (
    DirectorListWithMovieCount,
    MovieReviewList,
    DirectorList,
    DirectorDetail,
    MovieList,
    MovieDetail,
    ReviewList,
    ReviewDetail,
    RegisterUser,
    ConfirmUser,
    LoginUser
)

urlpatterns = [
    # Director URLs
    path('api/v1/directors/', DirectorListWithMovieCount.as_view(), name='director-list-with-movie-count'),
    path('api/v1/directors/', DirectorList.as_view(), name='director-list'),
    path('api/v1/directors/<int:id>/', DirectorDetail.as_view(), name='director-detail'),

    # Movie URLs
    path('api/v1/movies/', MovieList.as_view(), name='movie-list'),
    path('api/v1/movies/<int:id>/', MovieDetail.as_view(), name='movie-detail'),
    path('api/v1/movies/reviews/', MovieReviewList.as_view(), name='movie-review-list'),

    # Review URLs
    path('api/v1/reviews/', ReviewList.as_view(), name='review-list'),
    path('api/v1/reviews/<int:id>/', ReviewDetail.as_view(), name='review-detail'),

    # User URLs
    path('api/v1/users/register/', RegisterUser.as_view(), name='user-register'),
    path('api/v1/users/confirm/', ConfirmUser.as_view(), name='user-confirm'),
    path('api/v1/users/login/', LoginUser.as_view(), name='user-login'),
]
