logs = [
    "INFO: Application started",
    "WARN: Disk usage high",
    "ERROR: Unable to connect to DB",
    "INFO: Retrying connection",
    "INVALID LOG",
    "",
    "ERROR: Timeout occurred"
]

counter = {
    "INFO": 0,
    "WARN": 0,
    "ERROR": 0
}

for log in logs:
    if ":" not in log:
        continue

    severity = log.split(":")[0]

    if severity in counter:
        counter[severity] += 1

print(counter)