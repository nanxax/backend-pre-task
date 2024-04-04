from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from api.views.swagger.user_serializer import UserSerializer02
from apps.utils.logging_util import LoggingUtil
from apps.utils.response_util import ResponseData
from apps.services.user_service import UserService


NM = '사용자'
RES_LIST_NM = 'users'
RES_DETAIL_NM = 'user'

class UserView(APIView):

    user_service = UserService()
    logger = LoggingUtil()

    """
    사용자 View
    """

    @swagger_auto_schema(
        tags=[NM],
        operation_summary="{} 목록".format(NM),
        operation_description="{} 목록".format(NM),
        query_serializer=UserSerializer02.GetParam(),
        responses={status.HTTP_200_OK: UserSerializer02.GetResponse()}
    )
    def get(self, request: Request, **kwargs: dict) -> Response:
        """요청에 대한 사용자 리스트를 반환합니다.
        Args:
            request: 요청
            kwargs: path param
        Returns: 사용자 리스트 응답
        """
        data = []
        try:
            self.logger.info("사용자 목록")
            self.logger.info(request.query_params)
            self.logger.info(kwargs)

            serializer, paging = self.user_service.find_all(request.query_params.dict(), kwargs)
            data = serializer.data
        except Exception as e:
            return Response(ResponseData().response(False, str(e)))

        return Response(ResponseData().response(True, data, paging))

    @swagger_auto_schema(
        tags=[NM],
        operation_summary="{} 등록".format(NM),
        operation_description="{} 등록".format(NM),
        request_body=UserSerializer02.PostRequest(),
        responses={status.HTTP_200_OK: UserSerializer02.PostResponse()}
    )
    def post(self, request: Request) -> Response:
        """요청에 대한 사용자를 등록합니다.
        Args:
            request: 요청
        Returns: 사용자 등록 응답
        """
        data = []
        try:
            self.logger.info(request.data)

            serializer = self.user_service.add(request.data)
            data = serializer.data
        except Exception as e:
            return Response(ResponseData().response(False, str(e)))

        return Response(ResponseData().response(True, data))

class UserDetailView(APIView):

    user_service = UserService()
    logger = LoggingUtil()

    """
    사용자 상세 View
    """

    @swagger_auto_schema(
        tags=[NM],
        operation_summary="{} 상세".format(NM),
        operation_description="{} 상세".format(NM),
        query_serializer=UserSerializer02.GetDetailParam(),
        responses={status.HTTP_200_OK: UserSerializer02.GetDetailResponse()}
    )
    def get(self, request: Request, **kwargs: dict) -> Response:
        """요청에 대한 사용자를 반환합니다.
        Args:
            request: 요청
            kwargs: path param
        Returns: 사용자 응답
        """
        data = []
        try:
            self.logger.info(request.query_params)
            self.logger.info(kwargs)

            serializer = self.user_service.find(kwargs)
            data = serializer.data
        except Exception as e:
            return Response(ResponseData().response(False, str(e)))

        return Response(ResponseData().response(True, data))

    @swagger_auto_schema(
        tags=[NM],
        operation_summary="{} 수정".format(NM),
        operation_description="{} 수정".format(NM),
        request_body=UserSerializer02.PutRequest(),
        responses={status.HTTP_200_OK: UserSerializer02.PutResponse()}
    )
    def put(self, request: Request, **kwargs: dict) -> Response:
        """요청에 대한 사용자 수정 합니다.
        Args:
            request: 요청
        Returns: 사용자 수정 응답
        """
        data = []
        try:
            params = request.data
            serializer = self.user_service.modify(params, kwargs)
            data = serializer.data
        except Exception as e:
            return Response(ResponseData().response(False, str(e)))
        return Response(ResponseData().response(True, data))

    @swagger_auto_schema(
        tags=[NM],
        operation_summary="{} 삭제".format(NM),
        operation_description="{} 삭제".format(NM),
        responses={status.HTTP_200_OK: UserSerializer02.DeleteResponse()}
    )
    def delete(self, request: Request, **kwargs: dict) -> Response:
        """요청으로 전달 받은 사용자를 삭제합니다.
        Args:
          kwargs: path 파라미터
        Returns:
          사용자 삭제 응답
        """
        try:
            self.user_service.remove(kwargs)
        except Exception as e:
            return Response(ResponseData().response(False, str(e)))

        return Response(ResponseData.response(True))
