import re
import sys
import argparse
from collections import Counter

# Using argparse for reading arguments is pretty cool.
# We get defualt help, argument types, and a lot more done :-)
# Refer = http://docs.python.org/dev/library/argparse.html

def format_logs():
  parser = argparse.ArgumentParser(description='A very simple Apache access log parser')

  # A readable log file is a required argument and the file is automagically read too.
  parser.add_argument('log_file', metavar='LOG_FILE', type=argparse.FileType('r'), help='Path to the Apache log file')

  # Regex for the common Apache log format.
  parts = [
      r'(?P<host>\S+)',                   # host
      r'\S+',                             # indent
      r'(?P<user>\S+)',                   # user
      r'\[(?P<time>.+)\]',                # time
      r'"(?P<request>.*)"',               # request
      r'(?P<status>[0-9]+)',              # status
      r'(?P<size>\S+)',                   # size
      r'"(?P<referrer>.*)"',              # referrer
      r'"(?P<agent>.*)"',                 # user agent
  ]
  pattern = re.compile(r'\s+'.join(parts)+r'\s*\Z')

  # Initiazlie required variables
  args = parser.parse_args()
  log_data = []

  # Get components from each line of the log file into a structured dict
  for line in args.log_file:
    log_data.append(pattern.match(line).groupdict())
    
  for log in log_data:
      log['request'] = log['request'].split()

  return log_data

