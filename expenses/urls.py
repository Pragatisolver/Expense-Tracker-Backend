from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpenseViewSet, RegisterView, register_page

router = DefaultRouter()
router.register("expenses", ExpenseViewSet, basename="expenses")

urlpatterns = [
    path("", include(router.urls)),
    path("register/", RegisterView.as_view(), name="register"),  # API (POST)
    path("register-page/", register_page, name="register_page"),  # HTML page
]
