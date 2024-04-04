from django.db import models

from apps.models.contacts import Contacts
from apps.models.labels import Labels


class ContactLabels(models.Model):

    seq = models.BigAutoField(
        primary_key=True,
        help_text='일련번호(PK)'
    )
    contact_seq = models.ForeignKey(
        Contacts,
        on_delete=models.PROTECT,
        db_column='contact_seq',
        db_constraint=False,
        help_text='주소록 일련번호(FK)',
    )
    label_seq = models.ForeignKey(
        Labels,
        on_delete=models.PROTECT,
        db_column='label_seq',
        db_constraint=False,
        help_text='라벨 일련번호(FK)',
    )
    class Meta:
        db_table = 'contact_labels'
        ordering = ['-seq']