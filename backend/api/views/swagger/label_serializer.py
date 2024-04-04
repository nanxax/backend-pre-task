from rest_framework import serializers

from apps.models.labels import Labels
from apps.serializers.label_serializer import LabelSerializer, LabelListSerializer
from apps.services.filters.label_filter import LabelFilter


class LabelSerializer01:
    class Default(serializers.ModelSerializer):
        """
        라벨 Swagger Serializer
        """

        class Meta:
            model = Labels
            fields = '__all__'
            ref_name = __qualname__

    class List(serializers.ModelSerializer):
        """
        라벨 목록 Swagger Serializer
        """
        labels = LabelListSerializer(
            many=True,
            required=True
        )
        class Meta:
            model = Labels
            fields = '__all__'
            ref_name = __qualname__

    class Detail(serializers.ModelSerializer):
        """
        라벨 상세 Swagger Serializer
        """

        class Meta:
            model = Labels
            fields = '__all__'
            ref_name = __qualname__

    class Field(serializers.Serializer):
        """
        라벨 필드 Swagger Serializer
        """

        @staticmethod
        def seq(required=False):
            seq = serializers.IntegerField(
                required=required,
                help_text=Labels.seq.field.help_text
            )
            return seq

        @staticmethod
        def user_seq(required=False):
            user_seq = serializers.IntegerField(
                required=required,
                help_text=Labels.user_seq.field.help_text
            )
            return user_seq

        @staticmethod
        def labels(required=False):
            labels = serializers.CharField(
                required=required,
                help_text=Labels.labels.field.help_text
            )
            return labels

        @staticmethod
        def create_at(required=False):
            create_at = serializers.DateTimeField(
                required=required,
                help_text=Labels.create_at.field.help_text
            )
            return create_at


        @staticmethod
        def ordering(required=False):
            ordering = serializers.ChoiceField(
                choices=list(LabelFilter.base_filters['ordering'].param_map.values()),
                required=required,
                help_text=LabelFilter.base_filters['ordering'].field.help_text
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


class LabelSerializer02:
    class GetParam(serializers.Serializer):
        """
            라벨 목록 조회 파라미터 Serializer
        """

        page = LabelSerializer01.Field.page()
        page_size = LabelSerializer01.Field.page_size()
        ordering = LabelSerializer01.Field.ordering()

        class Meta:
            ref_name = __qualname__

    class GetResponse(serializers.Serializer):
        """
        라벨 목록 조회 응답 Serializer
        """

        class GetLabelPagingData(serializers.Serializer):
            page = LabelSerializer01.Field.page()
            page_count = LabelSerializer01.Field.page_count()
            page_size = LabelSerializer01.Field.page_size()
            total_count = LabelSerializer01.Field.total_count()

        success = serializers.BooleanField(
            required=False,
            help_text="응답 성공 여부"
        )

        data = serializers.ListField(
            child=LabelSerializer01.List(),
            required=False,
            help_text="라벨 목록"
        )
        paging = GetLabelPagingData(
            required=False,
            help_text="페이징 데이터"

        )

        class Meta:
            ref_name = __qualname__


    class GetDetailParam(serializers.Serializer):
        """
            라벨 상세 조회 파라미터 Serializer
        """

        class Meta:
            ref_name = __qualname__

    class GetDetailResponse(serializers.Serializer):
        """
        라벨 상세 조회 응답 Serializer
        """

        success = serializers.BooleanField(
            required=False,
            help_text="응답 성공 여부"
        )

        data = LabelSerializer01.Detail()

        class Meta:
            ref_name = __qualname__


    class PostRequest(serializers.Serializer):
        """
        라벨 등록 요청 Serializer
        """

        labels = LabelSerializer01.Field.labels(True)

        class Meta:
            ref_name = __qualname__

    class PostResponse(serializers.Serializer):
        """
        라벨 등록 응답 Serializer
        """

        success = serializers.BooleanField(
            required=False,
            help_text="응답 성공 여부"
        )
        data = LabelSerializer01.Detail()

        class Meta:
            ref_name = __qualname__



    class PutRequest(serializers.Serializer):
        """
        라벨 수정 요청 Serializer
        """

        labels = LabelSerializer01.Field.labels()

        class Meta:
            ref_name = __qualname__

    class PutResponse(serializers.Serializer):
        """
        라벨 수정 응답 Serializer
        """

        success = serializers.BooleanField(
            required=False,
            help_text="응답 성공 여부"
        )
        data = LabelSerializer01.Detail()

        class Meta:
            ref_name = __qualname__


    class DeleteRequest(serializers.Serializer):
        """
        라벨 삭제 요청 Serializer
        """

        class Meta:
            ref_name = __qualname__

    class DeleteResponse(serializers.Serializer):
        """
        라벨 삭제 응답 Serializer
        """

        success = serializers.BooleanField(
            required=False,
            help_text="응답 성공 여부"
        )
        class Meta:
            ref_name = __qualname__