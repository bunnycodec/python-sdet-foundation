# from typing import Any
# raw_ids = [" #ID-99 ", "id-102", " ID-500 ", "i d - 20 "]

# clean_ids: list[Any] = []

# for id in raw_ids:
#     clean_ids.append(id.strip().replace("#", "").replace(" ", "").upper())

# print(clean_ids)

import re

log = "CRITICAL: Error 404 at 10:00 AM. WARNING: Error 502 at 10:05 AM. INFO: All good. Error 999 detected."
numbers = re.findall(r"Error (\d+)", log)
print(numbers)