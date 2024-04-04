from django.db import models

class Users(models.Model):

    seq = models.BigAutoField(
        primary_key=True,
        help_text='일련번호(PK)'
    )
    name = models.CharField(
        max_length=64,
        help_text="이름"
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
        db_table = 'users'
        ordering = ['-seq']