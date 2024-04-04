import django_filters
from apps.models.contact_labels import ContactLabels


class ContactLabelFilter(django_filters.FilterSet):
    """
        연락처 라벨 Filter
    """

    # 정렬 기준
    ordering = django_filters.OrderingFilter(
        fields=(
            'seq',
            '-seq'
        ),
        help_text="정렬 기준"
    )

    # 사용자 일련번호
    field = ContactLabels.contact_seq.field
    oper_tp = 'exact'
    contact_seq = django_filters.NumberFilter(
        field_name=field.name,
        lookup_expr=oper_tp,
        help_text=field.help_text
    )

    # 사용자 일련번호
    field = ContactLabels.label_seq.field
    oper_tp = 'exact'
    label_seq = django_filters.NumberFilter(
        field_name=field.name,
        lookup_expr=oper_tp,
        help_text=field.help_text
    )


