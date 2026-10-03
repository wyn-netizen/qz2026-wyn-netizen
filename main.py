import json

def analyze_log(filepath: str) -> dict:
    total = 0
    by_level = {}
    by_user = {}
    last_error = None

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    log = json.loads(line)
                except json.JSONDecodeError:
                    continue

                total += 1
                lv = log["level"]
                usr = log["user"]

                if lv in by_level:
                    by_level[lv] += 1
                else:
                    by_level[lv] = 1

                if usr in by_user:
                    by_user[usr] += 1
                else:
                    by_user[usr] = 1

                if lv == "ERROR":
                    last_error = log["message"]
    except FileNotFoundError:
        pass

    return {
        "total": total,
        "by_level": by_level,
        "by_user": by_user,
        "last_error": last_error
    }
