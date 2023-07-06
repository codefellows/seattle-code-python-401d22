import re

# Example log line
log_line = '2023-05-21 10:00:00,001 [main] ERROR org.example.MyApp - Something went wrong!'

# Match date and time
match = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}', log_line)
if match:
    print(f'Date and Time: {match.group()}')  # 2023-05-21 10:00:00,001

# Extract log level
match = re.search(r'INFO|ERROR|WARN|DEBUG', log_line)
if match:
    print(f'Log Level: {match.group()}')  # ERROR

# Extract error message
match = re.search(r' - (.*)', log_line)
if match:
    print(f'Error Message: {match.group(1)}')  # Something went wrong!
