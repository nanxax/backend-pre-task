import json

from django.conf import settings
from rest_framework.serializers import ModelSerializer, ListSerializer

from apps.models.contacts import Contacts
from apps.services.common_services import CommonService
from apps.serializers.contact_serializer import ContactSerializer, ContactNoneSerializer, ContactListSerializer
from apps.services.filters.contact_filter import ContactFilter


class ContactService(CommonService):

    queryset = Contacts.objects.all()
    serializer_class = ContactSerializer
    serializer_none_class = ContactNoneSerializer
    serializer_list_class = ContactListSerializer
    filterset_class = ContactFilter

    def add(self, params: dict, path_params: dict = None):
        '''
            연락처 등록 서비스
        Args:
            params: 요청 파라미터
            path_params: path 파라미터

        Returns: 연락처 Serializer

        '''
        if 'name' not in params:
            raise Exception('이름을 입력해 주세요.')
        params['update_by'] = params['name']
        params['create_by'] = params['name']

        return super().add(params, path_params)

    def modify(self, params: dict = None, path_params: dict = None, partial=False):
        '''
            연락처 수정 서비스
        Args:
            params: 요청 파라미터
            path_params: path 파라미터
            partial: 부분 수정 여부

        Returns: 연락처 serializer

        '''

        sesializer, paging = super().find_list_by_param({}, path_params)
        contact = sesializer.data
        if len(contact) == 0:
            raise Exception('수정할 연락처 정보가 없습니다.')
        sesializer = super().modify(params, path_params, partial=True)
        return sesializer


    def remove(self, path_params: dict = None):
        '''
            연락처 삭제 서비스
        Args:
            path_params: path 파라미터

        '''
        from apps.services.contact_label_service import ContactLabelService

        sesializer, paging = super().find_list_by_param({}, path_params)
        contact = sesializer.data
        if len(contact) == 0:
            raise Exception('삭제할 연락처 정보가 없습니다.')

        contact_label_params = {}
        contact_label_params['contact_seq'] = path_params['seq']
        contact_label_service = ContactLabelService()
        contact_label_sesializer, contact_label_paging = contact_label_service.find_default_by_param(contact_label_params)

        if len(contact_label_sesializer.data) > 0:
            remove_contact_labels = [data['seq'] for data in contact_label_sesializer.data]
            for remove_contact_label_seq in remove_contact_labels:
                contact_label_params = {}
                contact_label_params['seq'] = remove_contact_label_seq
                contact_label_service.remove(contact_label_params)

        super().remove(path_params)

    def find_list_by_param(self, params: dict = None, path_params: dict = None):
        '''
            연락처 목록 조회 서비스
        Args:
            params: 요청 파라미터
            path_params: path 파라미터

        Returns: 연락처 목록 Serializer

        '''
        from apps.services.contact_label_service import ContactLabelService

        serializer, paging = super().find_list_by_param(params, path_params)
        if len(serializer.data) > 0:
            contacts = list(serializer.data)
            for contact in contacts:
                contact_label_params = {}
                contact_label_params['contact_seq'] = contact['seq']
                contact_label_service = ContactLabelService()
                contact_label_sesializer, contact_label_paging = contact_label_service.find_list_by_param(contact_label_params)

                contact_labels = list(contact_label_sesializer.data)
                contact['labels'] = contact_labels
        return contacts, paging

    def find(self, path_params: dict = None):
        '''
            연락처 조회 서비스
        Args:
            params: 요청 파라미터
            path_params: path 파라미터

        Returns: 연락처 Serializer

        '''

        from apps.services.contact_label_service import ContactLabelService

        serializer = super().find(path_params)
        if len(serializer.data) > 0:
            contact = serializer.data
            contact_label_params = {}
            contact_label_params['contact_seq'] = contact['seq']
            contact_label_service = ContactLabelService()
            contact_label_sesializer, contact_label_paging = contact_label_service.find_list_by_param(contact_label_params)

            contact_labels = list(contact_label_sesializer.data)
            contact['labels'] = contact_labels
        return contact
