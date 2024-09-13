from django.urls import path
from django.http import JsonResponse
from rest_framework.routers import DefaultRouter
from core.views import SectionViewSet, ParentViewSet, ChildViewSet

router = DefaultRouter()
router.register(r'sections', SectionViewSet)
router.register(r'parents', ParentViewSet)
router.register(r'children', ChildViewSet)

urlpatterns = [
    path('health/', lambda request: JsonResponse({"status": "ok"})),
]

urlpatterns += router.urls
