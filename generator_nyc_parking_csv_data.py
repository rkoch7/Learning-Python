from collections import namedtuple
from datetime import datetime
from collections import defaultdict

file_name = 'nyc_parking_tickets_extract.csv'
with open(file_name) as f:
    column_headers = next(f).strip('\n').split(',')


column_headers = [headers.replace(' ', '_').lower()
                    for headers in column_headers]

Ticket = namedtuple('Ticket', column_headers)

def read_data():
    with open(file_name) as f:
        next(f)
        yield from f

def parse_int(value, *, default=None):
    try:
        return int(value)
    except ValueError:
        return default

def parse_date(value, *, default=None):
    date_format = '%m/%d/%Y'

    try:
        return datetime.strptime(value, date_format).date()
    except ValueError:
        return default

def parse_str(value, *, default=None):

    try:
        cleaned = value.strip()
        if not cleaned:
            return default
        else:
            return cleaned
    except ValueError:
        return default


column_parsers = (parse_int,
                 parse_str,
                 lambda x : parse_str(x, default=''),
                 lambda x: parse_str(x, default=''),
                 parse_date,
                 parse_int,
                 lambda x: parse_str(x, default=''),
                 parse_str,
                 lambda x: parse_str(x, default='')
)
def parse_row(row, *, default=None):
    fields = row.strip('\n').split(',')
    parsed_data = [func(field)
                    for func, field in zip(column_parsers, fields)]

    if all(item is not None for item in parsed_data):
        return Ticket(*parsed_data)
    else:
        return default

def parsed_data():
    for row in read_data():
        parsed = parse_row(row)
        if parsed:
            yield parsed

make_counts = defaultdict(int)

for data in parsed_data():
    make_counts[data.vehicle_make] += 1

print(make_counts)

