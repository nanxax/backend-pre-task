from django.db import models

from apps.models.users import Users


class Labels(models.Model):

    seq = models.BigAutoField(
        name='seq',
        primary_key=True,
        help_text='일련번호(PK)'
    )
    labels = models.CharField(
        max_length=256,
        help_text="라벨"
    )
    user_seq = models.ForeignKey(
        Users,
        on_delete=models.PROTECT,
        db_column='user_seq',
        db_constraint=False,
        help_text='사용자 일련번호(FK)',
    )
    create_at = models.DateTimeField(
        auto_now_add=True,
        help_text='생성일시'
    )

    class Meta:
        db_table = 'labels'
        ordering = ['-seq']