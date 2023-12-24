import re
import sqlite3

from sqlite3 import Cursor, Connection

def get_db_connection() -> Connection:
    return sqlite3.connect("domains.db")

def get_db_cursor(connection: Connection) -> Cursor:
    return connection.cursor()

def get_project_ids(domains_cur: Cursor) -> list[str]:
    project_ids = []
    res = domains_cur.execute("SELECT DISTINCT project_id FROM domains")
    for row in res:
        project_ids.append(row[0])
    return project_ids

def get_domains_by_id(domains_cur: Cursor, project_id: str) -> list[str]:
    domains = []
    res = domains_cur.execute(f"SELECT DISTINCT name FROM domains WHERE project_id = '{project_id}'")
    for row in res:
        domains.append(row[0])
    return domains

def insert_rules(domains_cur: Cursor, project_id: str, rule: str) -> None:
    res = domains_cur.execute(f"INSERT INTO rules VALUES ('{project_id}', '{rule}')")

def get_non_valid_domain_len(domains: list) -> int:
    domain_lens = {}
    for domain in domains:
        length = len(domain.split('.')[0])
        domain_lens[length] = domain_lens.get(length, 0) + 1
    return max(domain_lens, key=domain_lens.get)


def add_regexes_to_rules_table() -> str:
    domains_con = get_db_connection()
    domains_cur = get_db_cursor(domains_con)
    project_ids = get_project_ids(domains_cur)
    output = "Added new rules for:\n"
    for project_id in project_ids:
        domains = get_domains_by_id(domains_cur, project_id)
        non_valid_len = get_non_valid_domain_len(domains)
        regex = "^.{" + str(non_valid_len) + "}\..*$"
        insert_rules(domains_cur, project_id, regex)
        output += f"{project_id=}: {regex=}\n"
    domains_con.commit()
    return output


if __name__ == '__main__':
    print(add_regexes_to_rules_table())
