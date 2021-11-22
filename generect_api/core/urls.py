from rest_framework import routers

from core import views


app_name = "core"


router = routers.SimpleRouter()
router.register(r"companies", views.CompanyViewSet, basename="company")
router.register(r"persons", views.PersonViewSet, basename="person")

urlpatterns = router.urls
