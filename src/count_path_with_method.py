from modules.log_formatter import format_logs


def count_path_with_method(path, request):
    logs = format_logs()
    
    count = 0
    for log in logs:
        if request == log['request'][0] and path in log['request'][1]:
            count += 1

    return count