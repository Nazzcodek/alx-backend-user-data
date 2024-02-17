#!/usr/bin/env python3
"""filter logger module"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """this is a filter datum module"""
    for field in fields:
        regex = "{}=[^{}]*".format(field, re.escape(separator))
        log_msg = re.sub(regex, "{}={}".format(field, redaction), message)

    return log_msg
