from rest_framework import routers
from django.urls import path, include
from accounts import views as accounts_views
from employees import views as employees_views
from structure import views as structure_views
from positions import views as positions_views
from contacts import views as contacts_views
from events import views as events_views
from reports import views as reports_views

router = routers.DefaultRouter()
router.register(r'roles', accounts_views.RoleViewSet)
router.register(r'users', accounts_views.UserViewSet)
router.register(r'employees', employees_views.EmployeeViewSet)
router.register(r'subdivisions', structure_views.SubdivisionViewSet)
router.register(r'types_division', structure_views.TypeDivisionViewSet)
router.register(r'locations', structure_views.LocationViewSet)
router.register(r'posts', positions_views.PostViewSet)
router.register(r'employee_divisions', contacts_views.EmployeeDivisionViewSet)
router.register(r'types_event', events_views.TypeEventViewSet)
router.register(r'events', events_views.EventViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
