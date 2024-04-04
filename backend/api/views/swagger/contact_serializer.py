from rest_framework import serializers

from apps.models.contact_labels import ContactLabels
from apps.models.contacts import Contacts
from apps.serializers.label_serializer import LabelSerializer, LabelListSerializer
from apps.services.filters.contact_filter import ContactFilter


class ContactSerializer01:
    class Default(serializers.ModelSerializer):
        """
        연락처 Swagger Serializer
        """

        class Meta:
            model = Contacts
            fields = '__all__'
            ref_name = __qualname__

    class List(serializers.ModelSerializer):
        """
        연락처 목록 Swagger Serializer
        """
        labels = LabelListSerializer(
            many=True,
            required=True
        )
        class Meta:
            model = Contacts
            fields = ['seq', 'image_url', 'name', 'email','phone_number', 'company', 'position', 'labels']
            ref_name = __qualname__

    class Detail(serializers.ModelSerializer):
        """
        연락처 상세 Swagger Serializer
        """

        class Meta:
            model = Contacts
            fields = '__all__'
            ref_name = __qualname__

    class Field(serializers.Serializer):
        """
        연락처 필드 Swagger Serializer
        """

        @staticmethod
        def seq(required=False):
            seq = serializers.IntegerField(
                required=required,
                help_text=Contacts.seq.field.help_text
            )
            return seq

        @staticmethod
        def user_seq(required=False):
            user_seq = serializers.IntegerField(
                required=required,
                help_text=Contacts.user_seq.field.help_text
            )
            return user_seq

        @staticmethod
        def name(required=False):
            name = serializers.CharField(
                required=required,
                help_text=Contacts.name.field.help_text
            )
            return name

        @staticmethod
        def image_url(required=False):
            image_url = serializers.CharField(
                required=required,
                help_text=Contacts.image_url.field.help_text
            )
            return image_url

        @staticmethod
        def email(required=False):
            email = serializers.CharField(
                required=required,
                help_text=Contacts.email.field.help_text
            )
            return email

        @staticmethod
        def phone_number(required=False):
            phone_number = serializers.CharField(
                required=required,
                help_text=Contacts.phone_number.field.help_text
            )
            return phone_number

        @staticmethod
        def address(required=False):
            address = serializers.CharField(
                required=required,
                help_text=Contacts.address.field.help_text
            )
            return address
        @staticmethod
        def web_site(required=False):
            web_site = serializers.CharField(
                required=required,
                help_text=Contacts.web_site.field.help_text
            )
            return web_site
        @staticmethod
        def company(required=False):
            company = serializers.CharField(
                required=required,
                help_text=Contacts.company.field.help_text
            )
            return company
        @staticmethod
        def position(required=False):
            position = serializers.CharField(
                required=required,
                help_text=Contacts.position.field.help_text
            )
            return position
        @staticmethod
        def birthday(required=False):
            birthday = serializers.CharField(
                required=required,
                help_text=Contacts.birthday.field.help_text
            )
            return birthday
        @staticmethod
        def memo(required=False):
            memo = serializers.CharField(
                required=required,
                help_text=Contacts.memo.field.help_text
            )
            return memo

        @staticmethod
        def create_by(required=False):
            create_by = serializers.CharField(
                required=required,
                help_text=Contacts.create_by.field.help_text
            )
            return create_by

        @staticmethod
        def create_at(required=False):
            create_at = serializers.DateTimeField(
                required=required,
                help_text=Contacts.create_at.field.help_text
            )
            return create_at

        @staticmethod
        def update_by(required=False):
            update_by = serializers.CharField(
                required=required,
                help_text=Contacts.update_by.field.help_text
            )
            return update_by

        @staticmethod
        def update_at(required=False):
            update_at = serializers.DateTimeField(
                required=required,
                help_text=Contacts.update_at.field.help_text
            )
            return update_at

        @staticmethod
        def ordering(required=False):
            ordering = serializers.ChoiceField(
                choices=list(ContactFilter.base_filters['ordering'].param_map.values()),
                required=required,
                help_text=ContactFilter.base_filters['ordering'].field.help_text
            )
            return ordering

        @staticmethod
        def page_count(required=False):
            page_count = serializers.IntegerField(
                required=required,
                help_text='최대 페이지 수'
            )
            return page_count

        @staticmethod
        def page(required=False):
            page = serializers.IntegerField(
                required=required,
                help_text='페이지 번호'
            )
            return page

        @staticmethod
        def page_size(required=False):
            page_size = serializers.IntegerField(
                required=required,
                help_text='페이지당 row 수'
            )
            return page_size

        @staticmethod
        def total_count(required=False):
            total_count = serializers.IntegerField(
                required=required,
                help_text='총 row 수'
            )
            return total_count


class ContactSerializer02:
    class GetParam(serializers.Serializer):
        """
            연락처 목록 조회 파라미터 Serializer
        """

        page = ContactSerializer01.Field.page()
        page_size = ContactSerializer01.Field.page_size()
        ordering = ContactSerializer01.Field.ordering()

        class Meta:
            ref_name = __qualname__

    class GetResponse(serializers.Serializer):
        """
        연락처 목록 조회 응답 Serializer
        """

        class GetContactPagingData(serializers.Serializer):
            page = ContactSerializer01.Field.page()
            page_count = ContactSerializer01.Field.page_count()
            page_size = ContactSerializer01.Field.page_size()
            total_count = ContactSerializer01.Field.total_count()

        success = serializers.BooleanField(
            required=False,
            help_text="응답 성공 여부"
        )

        data = serializers.ListField(
            child=ContactSerializer01.List(),
            required=False,
            help_text="연락처 목록"
        )
        paging = GetContactPagingData(
            required=False,
            help_text="페이징 데이터"

        )

        class Meta:
            ref_name = __qualname__


    class GetDetailParam(serializers.Serializer):
        """
            연락처 상세 조회 파라미터 Serializer
        """
        class Meta:
            ref_name = __qualname__

    class GetDetailResponse(serializers.Serializer):
        """
        연락처 상세 조회 응답 Serializer
        """

        success = serializers.BooleanField(
            required=False,
            help_text="응답 성공 여부"
        )

        data = ContactSerializer01.Detail()

        class Meta:
            ref_name = __qualname__


    class PostRequest(serializers.Serializer):
        """
        연락처 등록 요청 Serializer
        """

        name = ContactSerializer01.Field.name(True)
        image_url = ContactSerializer01.Field.image_url()
        email = ContactSerializer01.Field.email(True)
        phone_number = ContactSerializer01.Field.phone_number(True)
        address = ContactSerializer01.Field.address()
        web_site = ContactSerializer01.Field.web_site()
        company = ContactSerializer01.Field.company()
        position = ContactSerializer01.Field.position()
        birthday = ContactSerializer01.Field.birthday()
        memo = ContactSerializer01.Field.memo()

        class Meta:
            ref_name = __qualname__

    class PostResponse(serializers.Serializer):
        """
        연락처 등록 응답 Serializer
        """

        success = serializers.BooleanField(
            required=False,
            help_text="응답 성공 여부"
        )
        data = ContactSerializer01.Detail()

        class Meta:
            ref_name = __qualname__



    class PutRequest(serializers.Serializer):
        """
        연락처 수정 요청 Serializer
        """

        name = ContactSerializer01.Field.name()
        image_url = ContactSerializer01.Field.image_url()
        email = ContactSerializer01.Field.email()
        phone_number = ContactSerializer01.Field.phone_number()
        address = ContactSerializer01.Field.address()
        web_site = ContactSerializer01.Field.web_site()
        company = ContactSerializer01.Field.company()
        position = ContactSerializer01.Field.position()
        birthday = ContactSerializer01.Field.birthday()
        memo = ContactSerializer01.Field.memo()

        class Meta:
            ref_name = __qualname__

    class PutResponse(serializers.Serializer):
        """
        연락처 수정 응답 Serializer
        """

        success = serializers.BooleanField(
            required=False,
            help_text="응답 성공 여부"
        )
        data = ContactSerializer01.Detail()

        class Meta:
            ref_name = __qualname__


    class DeleteRequest(serializers.Serializer):
        """
        연락처 삭제 요청 Serializer
        """

        class Meta:
            ref_name = __qualname__

    class DeleteResponse(serializers.Serializer):
        """
        연락처 삭제 응답 Serializer
        """


        success = serializers.BooleanField(
            required=False,
            help_text="응답 성공 여부"
        )
        class Meta:
            ref_name = __qualname__