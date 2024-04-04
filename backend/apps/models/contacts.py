from django.db import models

from apps.models.users import Users


class Contacts(models.Model):

    seq = models.BigAutoField(
        primary_key=True,
        help_text='일련번호(PK)'
    )
    user_seq = models.ForeignKey(
        Users,
        on_delete=models.PROTECT,
        db_column='user_seq',
        db_constraint=False,
        help_text='사용자 일련번호(FK)',
    )
    name = models.CharField(
        max_length=256,
        help_text="이름"
    )
    image_url = models.CharField(
        null=True,
        max_length=256,
        help_text="이미지 URL"
    )
    email = models.CharField(
        max_length=256,
        help_text="이메일"
    )
    phone_number = models.CharField(
        max_length=256,
        help_text="전화번호"
    )
    address = models.CharField(
        null=True,
        max_length=256,
        help_text="주소"
    )
    web_site = models.CharField(
        null=True,
        max_length=256,
        help_text="웹사이트"
    )
    company = models.CharField(
        null=True,
        max_length=256,
        help_text='회사'
    )
    position = models.CharField(
        null=True,
        max_length=256,
        help_text='직책'
    )
    birthday = models.DateTimeField(
        null=True,
        auto_now_add=True,
        help_text='생일'
    )
    memo = models.CharField(
        null=True,
        max_length=1000,
        help_text='메모'
    )
    create_by = models.CharField(
        max_length=64,
        help_text='생성자'
    )
    create_at = models.DateTimeField(
        auto_now_add=True,
        help_text='생성일시'
    )
    update_by = models.CharField(
        max_length=64,
        help_text='수정자'
    )
    update_at = models.DateTimeField(
        auto_now=True,
        help_text='수정일시'
    )

    class Meta:
        db_table = 'contacts'
        ordering = ['-seq']