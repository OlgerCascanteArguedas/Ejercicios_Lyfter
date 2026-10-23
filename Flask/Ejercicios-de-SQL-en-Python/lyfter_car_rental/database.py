
import os
from contextlib import contextmanager

import psycopg
from psycopg import sql
from psycopg.rows import dict_row


SCHEMA = "lyfter_car_rental"


@contextmanager
def db():
    with psycopg.connect(
        os.environ["DATABASE_URL"],
        row_factory=dict_row
    ) as conn:
        yield conn


def fetch_all(table, allowed_fields, filters):
    unknown = set(filters.keys()) - set(allowed_fields)

    if unknown:
        raise ValueError(
            "Filtros no permitidos: "
            + ", ".join(sorted(unknown))
        )

    query = sql.SQL(
        "SELECT * FROM {}.{}"
    ).format(
        sql.Identifier(SCHEMA),
        sql.Identifier(table)
    )

    values = []

    if filters:
        conditions = []

        for field, value in filters.items():
            conditions.append(
                sql.SQL("{} = %s").format(
                    sql.Identifier(field)
                )
            )
            values.append(value)

        query += sql.SQL(" WHERE ")
        query += sql.SQL(" AND ").join(conditions)

    query += sql.SQL(" ORDER BY id")

    with db() as conn:
        return conn.execute(query, values).fetchall()
