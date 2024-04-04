from rest_framework import serializers

from apps.models.users import Users
from apps.serializers.user_serializer import UserSerializer
from apps.services.filters.user_filter import UserFilter


class UserSerializer01:
    class Default(serializers.ModelSerializer):
        """
        사용자 Swagger Serializer
        """

        class Meta:
            model = Users
            fields = '__all__'
            ref_name = __qualname__

    class Detail(serializers.ModelSerializer):
        """
        사용자 상세 Swagger Serializer
        """

        class Meta:
            model = Users
            fields = '__all__'
            ref_name = __qualname__

    class Field(serializers.Serializer):
        """
        사용자 필드 Swagger Serializer
        """

        @staticmethod
        def seq(required=False):
            seq = serializers.IntegerField(
                required=required,
                help_text=Users.seq.field.help_text
            )
            return seq

        @staticmethod
        def name(required=False):
            name = serializers.CharField(
                required=required,
                help_text=Users.name.field.help_text
            )
            return name

        @staticmethod
        def create_by(required=False):
            create_by = serializers.CharField(
                required=required,
                help_text=Users.create_by.field.help_text
            )
            return create_by

        @staticmethod
        def create_at(required=False):
            create_at = serializers.DateTimeField(
                required=required,
                help_text=Users.create_at.field.help_text
            )
            return create_at

        @staticmethod
        def update_by(required=False):
            update_by = serializers.CharField(
                required=required,
                help_text=Users.update_by.field.help_text
            )
            return update_by

        @staticmethod
        def update_at(required=False):
            update_at = serializers.DateTimeField(
                required=required,
                help_text=Users.update_at.field.help_text
            )
            return update_at

        @staticmethod
        def ordering(required=False):
            ordering = serializers.ChoiceField(
                choices=list(UserFilter.base_filters['ordering'].param_map.values()),
                required=required,
                help_text=UserFilter.base_filters['ordering'].field.help_text
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


class UserSerializer02:

    class GetParam(serializers.Serializer):
        """
            사용자 목록 조회 파라미터 Serializer
        """

        page = UserSerializer01.Field.page()
        page_size = UserSerializer01.Field.page_size()
        ordering = UserSerializer01.Field.ordering()

        class Meta:
            ref_name = __qualname__

    class GetResponse(serializers.Serializer):
        """
        사용자 목록 조회 응답 Serializer
        """

        class GetUserPagingData(serializers.Serializer):
            page = UserSerializer01.Field.page()
            page_count = UserSerializer01.Field.page_count()
            page_size = UserSerializer01.Field.page_size()
            total_count = UserSerializer01.Field.total_count()

        success = serializers.BooleanField(
            required=False,
            help_text="응답 성공 여부"
        )

        data = serializers.ListField(
            child=UserSerializer01.Default(),
            required=False,
            help_text="사용자 목록"
        )
        paging = GetUserPagingData(
            required=False,
            help_text="페이징 데이터"

        )

        class Meta:
            ref_name = __qualname__


    class GetDetailParam(serializers.Serializer):
        """
            사용자 상세 조회 파라미터 Serializer
        """

        class Meta:
            ref_name = __qualname__

    class GetDetailResponse(serializers.Serializer):
        """
        사용자 상세 조회 응답 Serializer
        """

        success = serializers.BooleanField(
            required=False,
            help_text="응답 성공 여부"
        )

        data = UserSerializer01.Detail()

        class Meta:
            ref_name = __qualname__


    class PostRequest(serializers.Serializer):
        """
        사용자 등록 요청 Serializer
        """

        name = UserSerializer01.Field.name(True)

        class Meta:
            ref_name = __qualname__

    class PostResponse(serializers.Serializer):
        """
        사용자 등록 응답 Serializer
        """

        success = serializers.BooleanField(
            required=False,
            help_text="응답 성공 여부"
        )
        data = UserSerializer01.Detail()

        class Meta:
            ref_name = __qualname__



    class PutRequest(serializers.Serializer):
        """
        사용자 수정 요청 Serializer
        """

        name = UserSerializer01.Field.name()

        class Meta:
            ref_name = __qualname__

    class PutResponse(serializers.Serializer):
        """
        사용자 수정 응답 Serializer
        """

        success = serializers.BooleanField(
            required=False,
            help_text="응답 성공 여부"
        )
        data = UserSerializer01.Detail()

        class Meta:
            ref_name = __qualname__


    class DeleteRequest(serializers.Serializer):
        """
        사용자 삭제 요청 Serializer
        """

        class Meta:
            ref_name = __qualname__

    class DeleteResponse(serializers.Serializer):
        """
        사용자 삭제 응답 Serializer
        """

        success = serializers.BooleanField(
            required=False,
            help_text="응답 성공 여부"
        )
        class Meta:
            ref_name = __qualname__