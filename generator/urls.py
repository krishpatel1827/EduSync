from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('timetable/', views.timetable_view, name='timetable'),
    path('timetable/<int:timetable_id>/', views.timetable_view, name='timetable'),
    path('history/', views.history, name='history'),
    path('add/', views.add_entry, name='add_entry'),
    path('setup/', views.setup_view, name='setup'),
    path('export/excel/<int:timetable_id>/', views.export_excel, name='export_excel'),
    path('export/pdf/<int:timetable_id>/', views.export_pdf, name='export_pdf'),
]
