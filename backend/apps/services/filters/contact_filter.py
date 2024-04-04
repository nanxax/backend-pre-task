import django_filters
from apps.models.contacts import Contacts


class ContactFilter(django_filters.FilterSet):
    """
        연락처 Filter
    """

    # 정렬 기준
    ordering = django_filters.OrderingFilter(
        fields=(
            'seq',
            '-seq',
            'name',
            '-name',
            'email',
            '-email',
            'phone_number',
            '-phone_number',
        ),
        help_text="정렬 기준"
    )

    # 연락처 일련번호
    field = Contacts.seq.field
    oper_tp = 'exact'
    seq = django_filters.NumberFilter(
        field_name=field.name,
        lookup_expr=oper_tp,
        help_text=field.help_text
    )
    # 사용자 일련번호
    field = Contacts.user_seq.field
    oper_tp = 'exact'
    user_seq = django_filters.NumberFilter(
        field_name=field.name,
        lookup_expr=oper_tp,
        help_text=field.help_text
    )

    # 이메일
    field = Contacts.email.field
    oper_tp = 'exact'
    email = django_filters.CharFilter(
        field_name=field.name,
        lookup_expr=oper_tp,
        help_text=field.help_text
    )

    field = Contacts.seq.field
    oper_tp = 'in'
    seq__in = django_filters.NumberFilter(
        method='filter_in_seq',
        help_text='일련번호 검색'
    )

    @staticmethod
    def filter_in_seq(queryset, _, value):
        return queryset.filter(seq__in=value)