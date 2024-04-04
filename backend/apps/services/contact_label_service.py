import json

from django.conf import settings
from rest_framework.serializers import ModelSerializer, ListSerializer

from apps.models.contact_labels import ContactLabels
from apps.serializers.contact_label_serializer import ContactLabelSerializer, ContactLabelListSerializer
from apps.services.common_services import CommonService
from apps.services.filters.contact_label_filter import ContactLabelFilter
from apps.services.label_service import LabelService


class ContactLabelService(CommonService):

    queryset = ContactLabels.objects.all()
    serializer_class = ContactLabelSerializer
    serializer_list_class = ContactLabelListSerializer
    filterset_class = ContactLabelFilter

    def add(self, params: dict, path_params: dict = None):
        '''
            연락처 라벨 등록 서비스
        Args:
            params: 요청 파라미터
            path_params: path 파라미터

        Returns: 연락처 라벨 Serializer

        '''
        from apps.services.contact_service import ContactService
        from apps.services.label_service import LabelService

        if 'label_seq' not in params:
            raise Exception('라벨을 선택해 주세요.')
        if 'user_seq' not in params:
            raise Exception('사용자 정보가 없습니다.')

        # 연락처 - 사용자 맵핑 정보 확인.
        contact_params = {}
        contact_params['seq'] = path_params['contact_seq']
        contact_params['user_seq'] = params['user_seq']
        contact_service = ContactService()
        contacts, contact_paging = contact_service.find_list_by_param(contact_params)

        if len(contacts) == 0:
            raise Exception('잘못된 사용자 정보 입니다.')

        # 라벨 - 사용자 맵핑 정보 확인.
        label_params = {}
        label_params['seq'] = params['label_seq']
        label_params['user_seq'] = params['user_seq']
        label_service = LabelService()
        labels, label_paging = label_service.find_default_by_param(label_params)

        if len(labels.data) == 0:
            raise Exception('선택된 라벨 정보가 없습니다.')

        # 중복 확인.
        contact_label_params = {}
        contact_label_params['label_seq'] = params['label_seq']
        contact_label_params['contact_seq'] = path_params['contact_seq']
        contact_labels, contact_label_paging = super().find_default_by_param(contact_label_params)

        if len(contact_labels.data) > 0:
            raise Exception('이미 선택된 라벨입니다.')

        return super().add(params, path_params)


    def remove(self, path_params: dict = None):
        '''
            연락처 라벨 정보 삭제 서비스.
        Args:
            path_params: path 파라미터

        '''

        sesializer, paging = super().find_default_by_param({}, path_params)
        label = sesializer.data
        if len(label) == 0:
            raise Exception('삭제할 라벨 정보가 없습니다.')

        sesializer = super().remove(path_params)



