import json
import traceback

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.db.models import Model, QuerySet
from django_filters import FilterSet, utils
from rest_framework.serializers import ListSerializer, ModelSerializer, BaseSerializer

from apps.models.users import Users
from apps.serializers.user_serializer import UserSerializer, UserNoneSerializer
from apps.utils.logging_util import LoggingUtil


class GsReadType:
    NONE = 'none'
    LIST = 'list'
    DEFAULT = 'default'
    DETAIL = 'detail'


class CommonService:

    queryset = None
    serializer_class = None
    serializer_none_class = None
    serializer_list_class = None
    filterset_class = None

    logger = LoggingUtil()
    def add(self, params: dict, path_params: dict = None) -> ModelSerializer:
        """지정된 모델을 등록합니다.
        Args:
            params: 등록할 모델 params(dict)
        Returns: 지정된 모델 serializer
        """

        try:
            if path_params:
                params.update(path_params)
            print(params)
            print("생성")

            serializer = self.get_serializer(GsReadType.DEFAULT, data=params)
            if serializer.is_valid(raise_exception=True):
                serializer.save()

            return serializer
        except Exception:
            self.logger.error(traceback.format_exc())
            raise Exception('데이터 추가에 실패하였습니다.')

    def find(self, path_params: dict) -> ModelSerializer:
        """지정된 모델을 조회합니다.
        Args:
            path_params: 조회할 모델 pk params(dict)
        Returns: 지정된 모델 serializer
        """

        try:
            instance = self.get_object(path_params)
            serializer = self.get_serializer(GsReadType.DEFAULT, instance)

            return serializer
        except Exception as e:
            if 'not exist' in str(e):
                serializer = self.get_serializer(GsReadType.NONE)
                return serializer
            self.logger.error(traceback.format_exc())
            raise Exception('한 개 데이터 조회에 실패하였습니다.')

    def find_all(self, params: dict = None, path_params: dict = None) -> ListSerializer:
        """지정된 모델 리스트를 조회합니다.
        Args:
            params: 조회할 모델 params(dict)
            path_params: 조회할 모델 pk params(dict)
        Returns: 지정된 모델 list serializer
        """
        """지정된 모델 리스트를 조회합니다.
        Args:
            params: 조회할 모델 params(dict)
            path_params: 조회할 모델 pk params(dict)
        Returns: 지정된 모델 list serializer
        """
        try:
            paging = None
            instance = self.queryset
            if 'page' in params and 'page_size' in params :
                paginator = Paginator(instance, params['page_size'])
                serializer = self.get_serializer(GsReadType.DEFAULT, paginator.page(params['page']), many=True)
                paging = {}
                paging['page_size'] = params['page_size']
                paging['page'] = params['page']
                paging['total_count'] = instance.count()
                paging['total_pages'] = paginator.num_pages
            else:
                serializer = self.get_serializer(GsReadType.DEFAULT, instance, many=True)
                paging = {}
                paging['total_count'] = instance.count()

            return serializer, paging
        except Exception:
            self.logger.error(traceback.format_exc())
            raise Exception('데이터 전체 조회에 실패하였습니다.')

    def find_default_by_param(self, params: dict = None, path_params: dict = None) -> ListSerializer:
        """지정된 모델 리스트를 조회합니다.
        Args:
            params: 조회할 모델 params(dict)
            path_params: 조회할 모델 pk params(dict)
        Returns: 지정된 모델 list serializer
        """
        try:
            if path_params:
                params.update(path_params)
            kwargs = {
                'data': params,
                'queryset': self.queryset
            }

            paging = None
            filterset = self.filterset_class(**kwargs)
            filter_query_set = filterset.qs
            if 'page' in params and 'page_size' in params :
                paginator = Paginator(filter_query_set, params['page_size'])
                serializer = self.get_serializer(GsReadType.DEFAULT, paginator.page(params['page']), many=True)
                paging = {}
                paging['page_size'] = params['page_size']
                paging['page'] = params['page']
                paging['total_count'] = filter_query_set.count()
                paging['total_pages'] = paginator.num_pages
            else:
                serializer = self.get_serializer(GsReadType.DEFAULT, filter_query_set, many=True)
                paging = {}
                paging['total_count'] = filter_query_set.count()

            return serializer, paging
        except Exception:
            self.logger.error(traceback.format_exc())
            raise Exception('데이터 조회에 실패하였습니다.')

    def find_list_by_param(self, params: dict = None, path_params: dict = None) -> ListSerializer:
        """지정된 모델 리스트를 조회합니다.
        Args:
            params: 조회할 모델 params(dict)
            path_params: 조회할 모델 pk params(dict)
        Returns: 지정된 모델 list serializer
        """
        try:
            if path_params:
                params.update(path_params)
            kwargs = {
                'data': params,
                'queryset': self.queryset
            }

            paging = None
            filterset = self.filterset_class(**kwargs)
            filter_query_set = filterset.qs
            if 'page' in params and 'page_size' in params :
                paginator = Paginator(filter_query_set, params['page_size'])
                serializer = self.get_serializer(GsReadType.LIST, paginator.page(params['page']), many=True)
                paging = {}
                paging['page_size'] = params['page_size']
                paging['page'] = params['page']
                paging['total_count'] = filter_query_set.count()
                paging['total_pages'] = paginator.num_pages
            else:
                serializer = self.get_serializer(GsReadType.LIST, filter_query_set, many=True)
                paging = {}
                paging['total_count'] = filter_query_set.count()

            return serializer, paging
        except Exception:
            self.logger.error(traceback.format_exc())
            raise Exception('데이터 조회에 실패하였습니다.')



    def get_serializer(self, read_type, *args: tuple, **kwargs: dict) -> BaseSerializer:
        """지정된 모델 list serializer를 반환합니다.
        Args:
            *args: 지정된 모델을 담은 튜플
            **kwargs: serializer 옵션 딕셔너리
        Returns: 지정된 모델 list serializer
        """
        try:
            if read_type == GsReadType.NONE:
                return self.serializer_none_class(*args, **kwargs)

            if read_type == GsReadType.LIST:
                return self.serializer_list_class(*args, **kwargs)

            return self.serializer_class(*args, **kwargs)
        except Exception as e:
            read_type = e

    def get_object(self, path_params: dict) -> Model:
        """지정된 모델을 조회합니다.
        Args:
            path_params: 조회할 모델 pk params(dict)
        Returns: 지정된 모델
        """
        try:
            obj = self.queryset.get(**path_params)

        except Exception as e:
            raise Exception(e)

        return obj

    def modify(self, params: dict = None, path_params: dict = None, partial=False) -> ModelSerializer:
        """지정된 모델을 수정합니다.
        Args:
            path_params: 수정할 모델 pk params(dict)
            params: 수정할 모델 params(dict)
            partial: 부분 수정 여부
        Returns: 모델 serializer
        """
        try:
            if path_params:
                params.update(path_params)
            instance = self.get_object(path_params)
            serializer = self.get_serializer(GsReadType.DEFAULT, instance, data=params, partial=partial)
            serializer.is_valid()
            serializer.save()
            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}

            return serializer
        except Exception:
            self.logger.error(traceback.format_exc())
            raise Exception('데이터 수정에 실패하였습니다.')

    def remove(self, path_params: dict):
        """지정된 모델을 삭제합니다.
        Args:
            path_params: 삭제할 모델 pk params(dict)
        Returns:
        """
        try:
            instance = self.get_object(path_params)
            instance.delete()
        except Exception:
            self.logger.error(traceback.format_exc())
            raise Exception('데이터 삭제에 실패하였습니다.')
