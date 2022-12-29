from library.models import Books
from library import db
import csv
with open('google_books_dataset.csv', 'r') as f:
    reader = csv.reader(f)
    rows = list(reader)

for row in rows[1:]:
    book = Books(title=row[0], authors=row[1], language=row[2], categories=row[3],
                 avg_rate=int(float(row[4])) if row[4] != '' else row[4])
    db.session.add(book)
db.session.commit()
