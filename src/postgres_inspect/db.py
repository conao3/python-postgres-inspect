import logging
from typing import Any

import sqlalchemy
import psycopg2
import psycopg2.extras
import psycopg2.extensions

from . import settings


logger = logging.getLogger(__name__)
logger_db = logging.getLogger(f'{__name__}/db')

engine_ = None


class LoggingConnection(psycopg2.extras.LoggingConnection):
    """Logging 'after' query execution"""

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.initialize(logger_db)

    def _logtologger(self, msg: str | bytes, cur: psycopg2.extensions.cursor) -> None:
        msg = self.filter(msg, cur)
        if msg:
            if isinstance(msg, bytes):
                msg = msg.decode('utf-8')

            # sqlparse is not a good formatter
            # msg: str = sqlparse.format(msg, reindent=True, keyword_case='upper')

            self._logobj.info(msg)


def db_url():
    return 'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}'.format(
        user=settings.settings.postgres_user,
        password=settings.settings.postgres_password,
        host=settings.settings.postgres_host,
        port=settings.settings.postgres_port,
        db=settings.settings.postgres_db,
    )


def engine() -> sqlalchemy.Engine:
    global engine_
    if engine_ is None:
        engine_ = sqlalchemy.create_engine(
            db_url(),
            client_encoding='utf8',
            connect_args={
                'connection_factory': LoggingConnection,
                'connect_timeout': 5,
                'application_name': __name__,
            }
        )

    return engine_
