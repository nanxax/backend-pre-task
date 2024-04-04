import json

from django.conf import settings
from rest_framework.serializers import ModelSerializer, ListSerializer

from apps.models.users import Users
from apps.serializers.user_serializer import UserSerializer, UserNoneSerializer
from apps.services.common_services import CommonService


class UserService(CommonService):

    queryset = Users.objects.all()
    serializer_class = UserSerializer
    serializer_none_class = UserNoneSerializer
    filterset_class = None

    def add(self, params: dict, path_params: dict = None):
        '''
            사용자 등록 서비스
        Args:
            params: 요청 파라미터
            path_params: path 파라미터

        Returns: 사용자 Serializer

        '''
        if 'name' not in params:
            raise Exception('이름을 입력해주세요.')
        params['created_by'] = params['name']
        params['updated_by'] = params['name']
        return super().add(params, path_params)

    def find(self, path_params: dict = None):
        '''
            사용자 조회 서비스
        Args:
            params: 요청 파라미터
            path_params: path 파라미터

        Returns: 사용자 Serializer

        '''

        if 'seq' not in path_params:
            raise Exception('잘못된 요청입니다. : not exist [seq]')

        return super().find(path_params)

    def remove(self, path_params: dict):
        '''
            사용자 삭제 서비스
        Args:
            path_params: path 파라미터

        '''

        from apps.services.contact_label_service import ContactLabelService
        from apps.services.contact_service import ContactService
        from apps.services.label_service import LabelService

        print(path_params)
        user = self.find(path_params)

        if len(user.data) == 0:
            raise Exception('삭제할 사용자가 없습니다.')

        contact_params = {}
        contact_params['user_seq'] = path_params['seq']
        contact_service = ContactService()
        contacts_sesializer, contacts_paging = contact_service.find_list_by_param(contact_params)

        if len(contacts_sesializer) > 0:
            remove_contacts = [data['seq'] for data in contacts_sesializer]
            for remove_contact_seq in remove_contacts:

                contact_label_params = {}
                contact_label_params['contact_seq'] = remove_contact_seq
                contact_label_service = ContactLabelService()
                contact_label_sesializer, contact_label_paging = contact_label_service.find_default_by_param(contact_label_params)

                if len(contact_label_sesializer.data) > 0:
                    remove_contact_labels = [data['seq'] for data in contact_label_sesializer.data]
                    for remove_contact_label_seq in remove_contact_labels:

                        contact_label_params = {}
                        contact_label_params['seq'] = remove_contact_label_seq
                        contact_label_service.remove(contact_label_params)

                contact_params = {}
                contact_params['seq'] = remove_contact_seq
                contact_service.remove(contact_params)

        label_params = {}
        label_params['user_seq'] = path_params['seq']
        label_service = LabelService()
        label_sesializer, label_paging = label_service.find_default_by_param(label_params)

        if len(label_sesializer.data) > 0:
            remove_labels = [data['seq'] for data in label_sesializer.data]
            for remove_label_seq in remove_labels:
                label_params = {}
                label_params['seq'] = remove_label_seq
                label_service.remove(label_params)

        super().remove(path_params)
