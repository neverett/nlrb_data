#!/usr/bin/env python3

from common import db_config, sql


if __name__ == '__main__':
    """Confirm error_log table exists"""

    if db_config.db_type == 'sqlite':
        query = f"""
                SELECT name FROM sqlite_master
                WHERE type='table'
                AND name='error_log';
                """
    elif db_config.db_type == 'postgresql':
        query = f"""
                SELECT * FROM pg_tables
                WHERE tablename = 'error_log';
                """

    try:
        with sql.db_cnx() as cnx:
            c = cnx.cursor()
            print(f'Testing for existence of {db_config.error_log} table...')
            c.execute(query)
    except Exception as e:
        raise Exception(f'Could not test for existence of {db_config.error_log}') from e
    else: # no exception
        if not c.fetchone():
            raise Exception(f'{db_config.error_log} table does not exist')
        print(f'{db_config.error_log} table exists')
    finally:
        c.close()
        cnx.close()
