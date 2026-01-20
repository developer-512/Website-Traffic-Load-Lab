def parse_slow_log(path):
    if not path:
        return []

    slow = []
    try:
        with open(path) as f:
            for line in f:
                if line.startswith("# Time:"):
                    slow.append(line.strip())
    except FileNotFoundError:
        pass

    return slow
