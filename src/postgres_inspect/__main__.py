import sqlalchemy
import sqlalchemy.dialects.postgresql

from . import db

metadata = sqlalchemy.MetaData()
metadata.reflect(bind=db.engine())


def main():
    for table in metadata.sorted_tables:
        print(sqlalchemy.schema.CreateTable(table).compile(dialect=sqlalchemy.dialects.postgresql.dialect()))


if __name__ == '__main__':
    main()
