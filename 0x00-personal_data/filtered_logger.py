#!/usr/bin/env python3
"""filter logger module"""
from typing import List
import re
import logging
import mysql.connector

PII_FIELDS = ['password', 'name', 'email','phone', 'ssn']


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """this is a filter datum module"""
    for field in fields:
        regex = "{}=.*?{}".format(field, separator)
        message = re.sub(regex, "{}={}{}".format(field, redaction, separator),
                         message)
    return message


def get_logger() -> logging.Logger:
    """logger getter method"""
    log_user_data = logging.getLogger('user_data')
    log_user_data.setLevel(logging.INFO)
    log_user_data.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    log_user_data.addHandler(stream_handler)

    return log_user_data


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ connect to database"""
    username = environ.get("PERSONAL_DATA_DB_USERNAME", "root")
    password = environ.get("PERSONAL_DATA_DB_PASSWORD", "")
    host = environ.get("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = environ.get("PERSONAL_DATA_DB_NAME")

    cursor = mysql.connector.connection.MySQLConnection(user=username,
                                                        password=password,
                                                        host=host,
                                                        database=db_name)
    return cursor


def main():
    """ main module """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    field_names = [i[0] for i in cursor.description]

    logger = get_logger()

    for row in cursor:
        str_row = ''.join(f'{f}={str(r)}; ' for r, f in zip(row, field_names))
        logger.info(str_row.strip())

    cursor.close()
    db.close()


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """init method"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """format method"""
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)
