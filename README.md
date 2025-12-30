# postgres-inspect

A lightweight command-line tool for inspecting PostgreSQL databases and generating DDL (Data Definition Language) statements.

## Features

- Extracts schema definitions from PostgreSQL databases
- Generates clean, readable DDL output
- Supports schema filtering and table exclusion patterns
- Works with PostgreSQL and Redshift

## Installation

```bash
poetry install
```

## Quick Start

```bash
poetry run postgres-inspect --url postgresql://postgres:postgres@localhost:5432/mydb
```

For a sample database to experiment with, check out [docker-postgres-dvdrental](https://github.com/conao3-playground/docker-postgres-dvdrental).

## Options

### `--url <URL>`

**Required.** Database connection URL in the format:

```
postgresql://{username}:{password}@{host}:{port}/{database}
```

### `--schema <SCHEMA>`

Target schema name. Defaults to `public`.

### `--exclude <PATTERN>`

Exclude tables matching a regex pattern (uses `re.search`).

For example, to exclude date-partitioned tables like `user_20231127` or `store_20231127`:

```bash
--exclude '_[0-9]+$'
```

Note: Use single quotes to prevent shell glob expansion.

## Sample Output

See the [sample DDL output](https://github.com/conao3/python-postgres-inspect/blob/master/sample/dvdrental/ddl.sql) generated from the dvdrental database.

## Working with Redshift

For Redshift compatibility, downgrade SQLAlchemy to version 1.x:

```bash
poetry add 'sqlalchemy@^1'
```

See [amundsen-io/amundsen#2105](https://github.com/amundsen-io/amundsen/issues/2105) for details.

## License

Apache-2.0
