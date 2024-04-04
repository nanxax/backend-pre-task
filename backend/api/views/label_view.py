from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from api.views.swagger.label_serializer import LabelSerializer02
from apps.utils.logging_util import LoggingUtil
from apps.utils.response_util import ResponseData
from apps.services.label_service import LabelService


NM = '라벨'
RES_LIST_NM = 'labels'
RES_DETAIL_NM = 'label'

class LabelView(APIView):

    label_service = LabelService()
    logger = LoggingUtil()

    """
    라벨 View
    """
    @swagger_auto_schema(
        tags=[NM],
        operation_summary="{} 목록".format(NM),
        operation_description="{} 목록".format(NM),
        query_serializer=LabelSerializer02.GetParam(),
        responses={status.HTTP_200_OK: LabelSerializer02.GetResponse()}
    )
    def get(self, request: Request, **kwargs: dict) -> Response:
        """요청에 대한 라벨 리스트를 반환합니다.
        Args:
            request: 요청
            kwargs: path param
        Returns: 라벨 리스트 응답
        """
        data = []
        try:
            self.logger.info("사용자 라벨 목록")
            self.logger.info(request.query_params)
            self.logger.info(kwargs)

            serializer, paging = self.label_service.find_default_by_param(request.query_params.dict(), kwargs)
            data = serializer.data
        except Exception as e:
            return Response(ResponseData().response(False, str(e)))

        return Response(ResponseData().response(True, data, paging))

    @swagger_auto_schema(
        tags=[NM],
        operation_summary="{} 등록".format(NM),
        operation_description="{} 등록".format(NM),
        request_body=LabelSerializer02.PostRequest(),
        responses={status.HTTP_200_OK: LabelSerializer02.PostResponse()}
    )
    def post(self, request: Request, **kwargs: dict) -> Response:
        """요청에 대한 라벨을 등록합니다.
        Args:
            request: 요청
        Returns: 라벨 응답
        """
        data = []
        try:
            self.logger.info(request.data)
            self.logger.info(kwargs)

            serializer = self.label_service.add(request.data, kwargs)
            data = serializer.data
        except Exception as e:
            return Response(ResponseData().response(False, str(e)))

        return Response(ResponseData().response(True, data))

class LabelDetailView(APIView):

    label_service = LabelService()
    logger = LoggingUtil()

    """
    라벨 상세 View
    """
    @swagger_auto_schema(
        tags=[NM],
        operation_summary="{} 삭제".format(NM),
        operation_description="{} 삭제".format(NM),
        responses={status.HTTP_200_OK: LabelSerializer02.DeleteResponse()}
    )
    def delete(self, request: Request, **kwargs: dict) -> Response:
        """요청으로 전달 받은 라벨울 삭제합니다.
        Args:
          kwargs: path 파라미터
        Returns:
          라벨 삭제 응답
        """
        try:
            self.label_service.remove(kwargs)
        except Exception as e:
            return Response(ResponseData().response(False, str(e)))

        return Response(ResponseData().response(True))
