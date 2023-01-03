from library.models import Books
from library import db
import csv
import random

with open('google_books_dataset.csv', 'r') as f:
    reader = csv.reader(f)
    rows = list(reader)

for row in rows[1:]:
    book = Books(title=row[0], authors=row[1].lstrip('[\'').rstrip('\']'), language=row[2],
                 categories=row[3].lstrip('[\'').rstrip('\']'),
                 avg_rate=int(float(row[4])) if row[4] != '' else row[4], number_of_copies=random.randint(1, 20))
    db.session.add(book)
db.session.commit()
