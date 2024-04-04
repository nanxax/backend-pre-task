from rest_framework import serializers

from apps.models.contact_labels import ContactLabels
from apps.services.filters.contact_label_filter import ContactLabelFilter


class ContactLabelSerializer01:
    class Default(serializers.ModelSerializer):
        """
        연락처 라벨 Swagger Serializer
        """

        class Meta:
            model = ContactLabels
            fields = '__all__'
            ref_name = __qualname__

    class List(serializers.ModelSerializer):
        """
        연락처 라벨 목록 Swagger Serializer
        """

        class Meta:
            model = ContactLabels
            fields = '__all__'
            ref_name = __qualname__

    class Detail(serializers.ModelSerializer):
        """
        연락처 라벨 상세 Swagger Serializer
        """

        class Meta:
            model = ContactLabels
            fields = '__all__'
            ref_name = __qualname__

    class Field(serializers.Serializer):
        """
        연락처 라벨 필드 Swagger Serializer
        """

        @staticmethod
        def seq(required=False):
            seq = serializers.IntegerField(
                required=required,
                help_text=ContactLabels.seq.field.help_text
            )
            return seq

        @staticmethod
        def label_seq(required=True):
            label_seq = serializers.IntegerField(
                required=required,
                help_text=ContactLabels.label_seq.field.help_text
            )
            return label_seq

        @staticmethod
        def contact_seq(required=False):
            contact_seq = serializers.IntegerField(
                required=required,
                help_text=ContactLabels.contact_seq.field.help_text
            )
            return contact_seq

        @staticmethod
        def ordering(required=False):
            ordering = serializers.ChoiceField(
                choices=list(ContactLabelFilter.base_filters['ordering'].param_map.values()),
                required=required,
                help_text=ContactLabelFilter.base_filters['ordering'].field.help_text
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


class ContactLabelSerializer02:
    class GetParam(serializers.Serializer):
        """
            연락처 라벨 목록 조회 파라미터 Serializer
        """

        page = ContactLabelSerializer01.Field.page()
        page_size = ContactLabelSerializer01.Field.page_size()
        ordering = ContactLabelSerializer01.Field.ordering()

        class Meta:
            ref_name = __qualname__

    class GetResponse(serializers.Serializer):
        """
        연락처 라벨 목록 조회 응답 Serializer
        """

        class GetPagingData(serializers.Serializer):
            page = ContactLabelSerializer01.Field.page()
            page_count = ContactLabelSerializer01.Field.page_count()
            page_size = ContactLabelSerializer01.Field.page_size()
            total_count = ContactLabelSerializer01.Field.total_count()

        success = serializers.BooleanField(
            required=False,
            help_text="응답 성공 여부"
        )

        data = serializers.ListField(
            child=ContactLabelSerializer01.List(),
            required=False,
            help_text="연락처 라벨 목록"
        )
        paging = GetPagingData(
            required=False,
            help_text="페이징 데이터"

        )

        class Meta:
            ref_name = __qualname__

    class PostRequest(serializers.Serializer):
        """
        연락처 라벨 등록 요청 Serializer
        """

        label_seq = ContactLabelSerializer01.Field.label_seq(True)

        class Meta:
            ref_name = __qualname__

    class PostResponse(serializers.Serializer):
        """
        연락처 라벨 등록 응답 Serializer
        """

        success = serializers.BooleanField(
            required=False,
            help_text="응답 성공 여부"
        )
        data = serializers.ListField(
            child=ContactLabelSerializer01.List(),
            required=False,
            help_text="연락처 라벨 목록"
        )

        class Meta:
            ref_name = __qualname__


    class DeleteRequest(serializers.Serializer):
        """
        연락처 라벨 삭제 요청 Serializer
        """

        class Meta:
            ref_name = __qualname__

    class DeleteResponse(serializers.Serializer):
        """
        연락처 라벨 삭제 응답 Serializer
        """


        success = serializers.BooleanField(
            required=False,
            help_text="응답 성공 여부"
        )
        class Meta:
            ref_name = __qualname__