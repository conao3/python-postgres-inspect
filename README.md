# python-postgres-inspect

## Usage

### Prepare database

Prepare database. You can use [docker-postgres-dvdrental](https://github.com/conao3-playground/docker-postgres-dvdrental) as a sample.

### Run

```bash
$ poetry install
$ poetry run postgres-inspect --url postgresql://postgres:postgres@localhost:15432/dvdrental
```

DB URL is like this `postgresql://{username}:{password}@{host}:{port}/{database}`.

### Sample output

[Sample output is available](https://github.com/conao3/python-postgres-inspect/blob/master/sample/dvdrental/ddl.sql) for dvdrental database.
