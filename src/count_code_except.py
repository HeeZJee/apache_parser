from modules.log_formatter import format_logs


def count_code_except(code):
    logs = format_logs()
    
    count = 0
    for log in logs:
        if code != log['status']:
            count += 1
    
    return count