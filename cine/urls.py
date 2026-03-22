from django.urls import path
from .viewsets import MovieViewSet, ReserveSeatView, SeatMapViewSet

urlpatterns = [
    path("movies/", MovieViewSet.as_view({"get": "list", "post": "create"}), name="movie-list"),
    path("movies/<int:pk>/", MovieViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), name="movie-detail"),
    path("reserve-seat/", ReserveSeatView.as_view()),
    path("sessions/<int:session_id>/seats/", SeatMapViewSet.as_view()),
]