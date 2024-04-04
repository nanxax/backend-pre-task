import json

from django.conf import settings
from rest_framework.serializers import ModelSerializer, ListSerializer

from apps.models.contact_labels import ContactLabels
from apps.models.labels import Labels
from apps.serializers.label_serializer import LabelSerializer, LabelListSerializer
from apps.services.common_services import CommonService
from apps.services.filters.label_filter import LabelFilter


class LabelService(CommonService):

    queryset = Labels.objects.all()
    serializer_class = LabelSerializer
    serializer_list_class = LabelListSerializer
    filterset_class = LabelFilter

    def add(self, params: dict, path_params: dict = None):

        '''
            라벨 등록 서비스
        Args:
            params: 요청 파라미터
            path_params: path 파라미터

        Returns: 라벨 Serializer

        '''
        if 'labels' not in params:
            raise Exception('라벨을 입력해주세요.')

        return super().add(params, path_params)

    def modify(self, params: dict = None, path_params: dict = None, partial=False):

        '''
            라벨 수정 서비스
        Args:
            params: 요청 파라미터
            path_params: path 파라미터

        Returns: 라벨 Serializer

        '''

        serializer, paging = super().find_default_by_param(params, path_params)
        label = serializer.data
        if len(label) == 0:
            raise Exception('수정할 라벨 정보가 없습니다.')

        serializer = super().modify(params, path_params)
        print(serializer)
        return serializer

    def remove(self, path_params: dict = None):
        '''
            라벨 삭제 서비스
        Args:
            path_params: path 파라미터

        '''

        from apps.services.contact_label_service import ContactLabelService

        print(path_params)

        serializer, paging = super().find_default_by_param({}, path_params)
        label = serializer.data
        if len(label) == 0:
            raise Exception('삭제할 라벨 정보가 없습니다.')

        contact_label_params = {}
        contact_label_params['label_seq'] = path_params['seq']
        contact_label_service = ContactLabelService()
        contact_label_sesializer, contact_label_paging = contact_label_service.find_default_by_param(contact_label_params)

        if len(contact_label_sesializer.data) > 0:
            remove_contact_labels = [data['seq'] for data in contact_label_sesializer.data]
            for remove_contact_label_seq in remove_contact_labels:
                contact_label_params = {}
                contact_label_params['seq'] = remove_contact_label_seq
                contact_label_service.remove(contact_label_params)

        super().remove(path_params)



