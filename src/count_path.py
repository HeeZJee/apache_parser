from modules.log_formatter import format_logs


def count_path(path):
    logs = format_logs()
    
    count = 0
    for log in logs:
        if path in log['request'][1]:
            count += 1

    return count