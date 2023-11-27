import logging.config
import argparse
import re
import sqlalchemy as sa
import sqlalchemy.dialects.postgresql as sa_postgresql


logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {'format': '[%(levelname)s] %(asctime)s - %(name)s - %(message)s'},
    },
    'handlers': {
        'console': {'class': 'logging.StreamHandler', 'level': 'DEBUG', 'formatter': 'default'},
    },
    'loggers': {
        'postgres_inspect': {'level': 'DEBUG', 'handlers': ['console']},
        'sqlalchemy': {'level': 'INFO', 'handlers': ['console']},
    },
})


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', help='DB URL like postgresql://{username}:{password}@{host}:{port}/{database}', required=True)
    parser.add_argument('--schema', help='Schema name')
    parser.add_argument('--exclude', help='Exclude tables in regexp')

    return parser.parse_args()


def main():
    args = parse_args()

    engine: sa.Engine = sa.create_engine(args.url)
    metadata = sa.MetaData(schema=args.schema)
    metadata.reflect(bind=engine)

    for table in metadata.sorted_tables:
        if args.exclude and re.search(args.exclude, table.name):
            continue

        ddl = str(sa.schema.CreateTable(table).compile(dialect=sa_postgresql.dialect()))
        print('\n'.join([elm.rstrip() for elm in ddl.splitlines()]) + ";")


if __name__ == '__main__':
    main()
