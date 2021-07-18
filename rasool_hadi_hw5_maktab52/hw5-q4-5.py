def numberoflog(level, filename):
    with open(filename, "r") as f:
        logs = f.read()
    return logs.count(level)


