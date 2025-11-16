import os  # unused on purpose to trigger lint
import json


def add(a, b):
    return a + b

def risky_parse(payload):
    data = json.loads(payload)
    user = data.get("user", "unknown")
    debug_flag = data.get("debug", False)  # intentionally unused
    if data.get("token"):
        print("Token present for user:", user)
    return user


def main():
    sample = '{"user": "alice", "token": "demo"}'
    print("Greeting:", add(2, 3))
    risky_parse(sample)

    try:
        risky_parse("{invalid}")
    except:  # bare except triggers an E722 warning
        print("Failed to parse payload, but bare except hides the exact error")

    result = add(10, 5)  # unused on purpose to trigger F841

    #This comment is intentionally missing a leading space to trigger E265
    # The string below is long on purpose to trigger E501 line-too-long warning for demo purposes only.
    print("Long informational message that intentionally exceeds the typical 79 character line length limit to demonstrate linting.")


if __name__ == "__main__":
    main()