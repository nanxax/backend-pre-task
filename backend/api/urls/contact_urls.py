
from django.urls import path

from api.views import contact_label_view
from api.views import contact_view

urlpatterns = [
    path('/<int:seq>', contact_view.ContactDetailView.as_view()),
    path('/<int:contact_seq>/label', contact_label_view.ContactLabelView.as_view()),
    path('/<int:contact_seq>/label/<int:seq>', contact_label_view.ContactLabelDetailView.as_view()),
    ]
