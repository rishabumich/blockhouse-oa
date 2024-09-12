"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# server/api/urls.py
from django.urls import path, include
from . import views  # Importing views correctly

urlpatterns = [
    path('candlestick-data/', views.candlestick_data, name='candlestick-data'),
    path('line-chart-data/', views.line_chart_data, name='line-chart-data'),
    path('bar-chart-data/', views.bar_chart_data, name='bar-chart-data'),
    path('pie-chart-data/', views.pie_chart_data, name='pie-chart-data'),
]
