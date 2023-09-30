from common import sql


if __name__ == "__main__":
    """Confirm no records require attention."""

    # not all cases have participants
    """
    comparison_query = (
        "select 
            (select count(case_id) from pages) - 
            (select count(distinct case_id) from participants)"
        " as row_diff;"
    )
    """

    text_query = """
                SELECT p.case_id, c.case_number, p.raw_participant
                FROM cases c
                INNER JOIN participants p
                ON c.id = p.case_id
                INNER JOIN error_log e
                on c.id = e.case_id
                WHERE e.participants_parse_error is TRUE
                """

    try:
        with sql.db_cnx() as cnx:
            c = cnx.cursor()
            c.execute(text_query)
            count = len(c.fetchall())
            if count != 0:
                print(f"Expected 0 parse errors, found {count}")
                c.execute(text_query)
                for case_number, raw_text in c.fetchall():
                    print(f"Case: {case_number} Raw text: {raw_text}")
    except Exception as e:
        print("Could not count or summarize participants parse errors")
        raise e
    else:  # no exception
        print("Finished checking participants parse errors.")
    finally:
        c.close()
        cnx.close()
