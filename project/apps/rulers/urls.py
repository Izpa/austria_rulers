from rest_framework import routers

from project.apps.rulers.views import RulerViewSet, RulerWithAllSuccessorsViewSet

ruler_router = routers.SimpleRouter()
ruler_with_all_successors_router = routers.SimpleRouter()


ruler_router.register(r'items', RulerViewSet)
ruler_with_all_successors_router.register(r'items_with_all_successors', RulerWithAllSuccessorsViewSet)


urlpatterns = []

urlpatterns += ruler_router.urls
urlpatterns += ruler_with_all_successors_router.urls
