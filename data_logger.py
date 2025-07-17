import pandas as pd
from datetime import datetime

def log_command(command):
    now = datetime.now()
    log_entry = {
        'command': command,
        'hour': now.hour,
        'day': now.strftime("%A")
    }

    try:
        df = pd.read_csv("command_log.csv")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["command", "hour", "day"])

    df = pd.concat([df, pd.DataFrame([log_entry])], ignore_index=True)
    df.to_csv("command_log.csv", index=False)