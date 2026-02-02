from typing import Any

responses: list[Any] = [
    {"status_code": 200, "response_time": 320},
    {"status_code": 500, "response_time": 100},
    {"status_code": 201, "response_time": 650},
    {"status_code": 200},
    {"status_code": 201, "response_time": 450}
]

counter = {
    "VALID": 0,
    "INVALID": 0
}

for response in responses:
    if "status_code" in response and "response_time" in response:
        code = response["status_code"]
        time = response["response_time"]

        if isinstance(code, int) and isinstance(time, int):
            if code in (200, 201) and time <= 500:
                counter["VALID"] += 1
            else:
                counter["INVALID"] += 1
        else:
            counter["INVALID"] += 1
    else:
        counter["INVALID"] += 1

print(counter)