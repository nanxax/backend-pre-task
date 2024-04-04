import django_filters
from apps.models.users import Users


class UserFilter(django_filters.FilterSet):
    """
        사용자 Filter
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
    field = Users.seq.field
    oper_tp = 'exact'
    seq = django_filters.NumberFilter(
        field_name=field.name,
        lookup_expr=oper_tp,
        help_text=field.help_text
    )

