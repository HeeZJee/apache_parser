from modules.log_formatter import format_logs


def count_ip():
    logs = format_logs()
    
    count = 0
    for log in logs:
        if '-' != log['host'] or '' != log['host'] or '127.0.0.1' != log['host']:
            count += 1
    
    return count