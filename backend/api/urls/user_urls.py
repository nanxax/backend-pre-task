
from django.urls import path

from api.views import user_view
from api.views import label_view
from api.views import contact_view


urlpatterns = [
    path('', user_view.UserView.as_view()),
    path('/<int:seq>', user_view.UserDetailView.as_view()),
    path('/<int:user_seq>/label', label_view.LabelView.as_view()),
    path('/<int:user_seq>/label/<int:seq>', label_view.LabelDetailView.as_view()),
    path('/<int:user_seq>/contact', contact_view.ContactView.as_view()),
    # path('/<int:evt_seq>/event-participant/excel-download', event_participant_view.EventParticipantExcelDownloadView.as_view()),
]
