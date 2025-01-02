from django.db.models import DateTimeField as BaseDateTimeField
from pendulum import DateTime, Date
from django.db.models import DateField as BaseDateField


class DateTimeField(BaseDateTimeField):

    def value_to_string(self, obj):
        val = self.value_from_object(obj)

        if isinstance(val, DateTime):
            return val.to_datetime_string()

        return "" if val is None else val.isoformat()


class DateField(BaseDateField):
    def value_to_string(self, obj):
        val = self.value_from_object(obj)

        if isinstance(val, Date):
            return val.to_date_string()

        return "" if val is None else val.isoformat()
