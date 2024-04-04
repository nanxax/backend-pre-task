import django_filters
from apps.models.labels import Labels


class LabelFilter(django_filters.FilterSet):
    """
        라벨 Filter
    """

    # 정렬 기준
    ordering = django_filters.OrderingFilter(
        fields=(
            'seq',
            '-seq'
        ),
        help_text="정렬 기준"
    )

    # 일련번호
    field = Labels.seq.field
    oper_tp = 'exact'
    seq = django_filters.NumberFilter(
        field_name=field.name,
        lookup_expr=oper_tp,
        help_text=field.help_text
    )


    # 사용자 일련번호
    field = Labels.user_seq.field
    oper_tp = 'exact'
    user_seq = django_filters.NumberFilter(
        field_name=field.name,
        lookup_expr=oper_tp,
        help_text=field.help_text
    )

