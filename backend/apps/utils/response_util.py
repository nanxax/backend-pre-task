from django.core.exceptions import ObjectDoesNotExist

class ResponseData:

    @staticmethod
    def response(success: bool, data: object = None, paging: dict = None) -> dict:
        """응답 데이터(dict)를 반환합니다.
        Args:
          success: 요청 결과
          data: 응답 데이터
          paging: 페이징 데이터
        Returns:
          응답 데이터(dict)
        """

        res = {}

        if success:
            # 정상 응답
            res['success'] = success
            res['data'] = data
        else:
            # 에러
            res['success'] = success
            res['error'] = data

        if paging:
            res['paging'] = paging

        return res
