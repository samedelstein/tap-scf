"""Stream type classes for tap-rickandmorty."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_scf.client import SCFStream

from datetime import datetime, timedelta

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")
time_diff = datetime.now() - timedelta(7)
updated_at_after = datetime.strftime(time_diff, '%Y-%m-%dT00:00:00-04:00')

class IssuesStream(SCFStream):
    """Define custom stream."""
    name = "issues"
    path = "/issues?search=syracuse,%20ny&updated_at_after="+updated_at_after
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "issues.json"


    

