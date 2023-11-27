# python-postgres-inspect

## Usage

### Prepare database

Prepare database. You can use [docker-postgres-dvdrental](https://github.com/conao3-playground/docker-postgres-dvdrental) as a sample.

### Run

```bash
$ poetry install
$ poetry run postgres-inspect --url postgresql://postgres:postgres@localhost:15432/dvdrental
```

### Sample output

[Sample output is available](https://github.com/conao3/python-postgres-inspect/blob/master/sample/dvdrental/ddl.sql) for dvdrental database.

## Options

### `--url <URL>`

Required.  DB URL like this `postgresql://{username}:{password}@{host}:{port}/{database}`.

### `--schema <SCHEMA>`

Optional, default is `public`.  Target schema name.

### `--exclude <EXCLUDE>`

Optional.  Exclude table name pattern using regex.

Regex is matched with `re.fullmatch`.

For example, if you want to exclude `user_20231127` and `store_20231127` and somethig like this, you can use `--exclude '.*_[0-9]*'`.
(Single quotes are required to avoid being recognised by the shell as a glob)
