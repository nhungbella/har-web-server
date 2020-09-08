from django.urls import path

from . import views

urlpatterns = [
    path('', views.render_connection_view, name='login'),    
    path('logout/', views.logoutUser, name='logout'),
    path('reports/', views.render_reports_view, name='reports'),    
    path('report/', views.render_report_creation_view, name='report'),
    path('report/<int:number_report>/', views.render_report_update_view, name='update'),
    path('report/<int:number_report>/deletion', views.render_report_deletion_view, name='delete'),
]