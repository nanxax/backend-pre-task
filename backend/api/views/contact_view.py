from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from api.views.swagger.contact_serializer import ContactSerializer02
from apps.utils.logging_util import LoggingUtil
from apps.utils.response_util import ResponseData
from apps.services.contact_service import ContactService

NM = '연락처'
RES_LIST_NM = 'contacts'
RES_DETAIL_NM = 'contact'


class ContactView(APIView):
    contact_service = ContactService()
    logger = LoggingUtil()

    """
    연락처 View
    """

    @swagger_auto_schema(
        tags=[NM],
        operation_summary="{} 목록".format(NM),
        operation_description="{} 목록".format(NM),
        query_serializer=ContactSerializer02.GetParam(),
        responses={status.HTTP_200_OK: ContactSerializer02.GetResponse()}
    )
    def get(self, request: Request, **kwargs: dict) -> Response:
        """요청에 대한 연락처 리스트를 반환합니다.
        Args:
            request: 요청
            kwargs: path param
        Returns: 연락처 리스트 응답
        """
        data = []
        try:
            self.logger.info(request.query_params)
            self.logger.info(kwargs)

            data, paging = self.contact_service.find_list_by_param(request.query_params.dict(), kwargs)

        except Exception as e:
            return Response(ResponseData().response(False, str(e)))

        return Response(ResponseData().response(True, data, paging))

    @swagger_auto_schema(
        tags=[NM],
        operation_summary="{} 등록".format(NM),
        operation_description="{} 등록".format(NM),
        request_body=ContactSerializer02.PostRequest(),
        responses={status.HTTP_200_OK: ContactSerializer02.PostResponse()}
    )
    def post(self, request: Request, **kwargs: dict) -> Response:
        """요청에 대한 연락처를 등록합니다.
        Args:
            request: 요청
        Returns: 연락처 응답
        """
        data = []
        try:
            self.logger.info(request.data)
            self.logger.info(kwargs)

            serializer = self.contact_service.add(request.data, kwargs)
            data = serializer.data
        except Exception as e:
            return Response(ResponseData().response(False, str(e)))

        return Response(ResponseData().response(True, data))


class ContactDetailView(APIView):
    contact_service = ContactService()
    logger = LoggingUtil()

    """
    연락처 상세 View
    """

    @swagger_auto_schema(
        tags=[NM],
        operation_summary="{} 상세".format(NM),
        operation_description="{} 상세".format(NM),
        query_serializer=ContactSerializer02.GetDetailParam(),
        responses={status.HTTP_200_OK: ContactSerializer02.GetDetailResponse()}
    )
    def get(self, request: Request, **kwargs: dict) -> Response:
        """요청에 대한 연락처를 반환합니다.
        Args:
            request: 요청
            kwargs: path param
        Returns: 연락처 응답
        """
        data = []
        try:
            self.logger.info(request.query_params)
            self.logger.info(kwargs)

            data = self.contact_service.find(kwargs)
        except Exception as e:
            return Response(ResponseData().response(False, str(e)))

        return Response(ResponseData().response(True, data))

    @swagger_auto_schema(
        tags=[NM],
        operation_summary="{} 수정".format(NM),
        operation_description="{} 수정".format(NM),
        request_body=ContactSerializer02.PutRequest(),
        responses={status.HTTP_200_OK: ContactSerializer02.PutResponse()}
    )
    def put(self, request: Request, **kwargs: dict) -> Response:
        """요청에 대한 연락처 수정 합니다.
        Args:
            request: 요청
        Returns: 광고주 응답
        """
        data = []
        try:
            params = request.data
            serializer = self.contact_service.modify(params, kwargs)
            data = serializer.data
        except Exception as e:
            return Response(ResponseData().response(False, str(e)))
        return Response(ResponseData().response(True, data))

    @swagger_auto_schema(
        tags=[NM],
        operation_summary="{} 삭제".format(NM),
        operation_description="{} 삭제".format(NM),
        responses={status.HTTP_200_OK: ContactSerializer02.DeleteResponse()}
    )
    def delete(self, request: Request, **kwargs: dict) -> Response:
        """요청으로 전달 받은 연락처를 삭제합니다.
        Args:
          kwargs: path 파라미터
        Returns:
          관리자 역할 삭제 응답
        """
        try:
            self.contact_service.remove(kwargs)
        except Exception as e:
            return Response(ResponseData().response(False, str(e)))

        return Response(ResponseData.response(True))
