import cattr
from datetime import date, datetime
from uuid import UUID

from dapodik.utils.parser import str_to_date, str_to_datetime


cattr.register_structure_hook(date, lambda d, t: str_to_date(d))
cattr.register_structure_hook(datetime, lambda d, t: str_to_datetime(d))
cattr.register_structure_hook(UUID, lambda d, t: UUID(d))
