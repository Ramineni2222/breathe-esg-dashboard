from django.urls import path

from .views import (
    dashboard,
    delete_record,
    edit_record,
    upload_csv,
    api_records
)

urlpatterns = [

    # DASHBOARD
    path('', dashboard),

    # DELETE RECORD
    path('delete/<int:id>/', delete_record),

    # EDIT RECORD
    path('edit/<int:id>/', edit_record),

    # UPLOAD CSV
    path('upload_csv/', upload_csv),

    # API
    path('api/', api_records),

]