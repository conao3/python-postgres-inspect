# python-postgres-inspect

## Usage

### Prepare database

Prepare database. You can use [docker-postgres-dvdrental](https://github.com/conao3-playground/docker-postgres-dvdrental) as a sample.

```bash
$ git clone https://github.com/conao3-playground/docker-postgres-dvdrental.git
$ cd docker-postgres-dvdrental
$ docker-compose up
```

Load sample data.

```bash
$ curl -LO https://www.postgresqltutorial.com/wp-content/uploads/2019/05/dvdrental.zip
$ unzip dvdrental.zip
$ PGPASSWORD=postgres pg_restore -U postgres -h localhost -p 15432 -d dvdrental dvdrental.tar
```

### Run

```bash
$ poetry install
$ poetry run python -m postgres_inspect
```

## Tips

### SQL log

postgres-inspect write SQL log into `/tmp/postgres_inspect_db.log`.

```bash
$ tail -f /tmp/postgres_inspect_db.log
```

### Sample output

[Sample output is available](https://github.com/conao3/python-postgres-inspect/blob/master/sample/dvdrental/ddl.sql) for dvdrental database.
