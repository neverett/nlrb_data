from common import db_config, sql


if __name__ == '__main__':
    """Confirm cases table exists."""

    query = f"""
            SELECT * FROM pg_tables
            WHERE tablename = 'cases';
            """

    try:
        with sql.db_cnx() as cnx, cnx.cursor() as c:
            c.execute(query)
            if not c.fetchone():
                raise Exception(f'Expected {db_config.cases} to exist, '
                                'but table does not exist')
    except Exception as e:
        raise Exception(f'Could not test for existence of {db_config.cases} table') from e
    else:
        print(f'{db_config.cases} table exists')
    finally:
        cnx.close()
