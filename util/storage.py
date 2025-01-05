import datetime
import time

import google.api_core.exceptions
import orjson
import pendulum
from google.cloud import storage

from util.json_default import default


class GCS:

    def __init__(self):
        self._gcs = None

    def create_folder(self, activity):
        if isinstance(activity.created_at, datetime.datetime):
            activity.created_at = pendulum.instance(activity.created_at)

        _date, _time = activity.created_at.to_rfc3339_string().split("T")
        year, month, day = _date.split("-")
        hour, minute = _time.split(":")[:2]
        return f"{year}/{month}/{day}/{hour}/{minute}"

    def get_bucket(self, filename):
        if not self._gcs:
            self._gcs = storage.Client()
        return self._gcs.get_bucket(filename)

    def save_activity(self, activity):
        folder = self.create_folder(activity)
        filename = f"{folder}/{activity.sqid}.json"
        try:
            self._save_activity(filename, activity.as_dict())
        except google.api_core.exceptions.ServiceUnavailable:
            time.sleep(1)
            self._save_activity(filename, activity.as_dict())

    def _save_activity(self, filename, payload):
        bucket = self.get_bucket("hf-activities")
        blob = bucket.blob(filename)
        blob.upload_from_string(orjson.dumps(payload, default=default))


gcs = GCS()
