import datetime

unix_time = 1625280000  # Replace this with your Unix time

# Convert Unix time to a datetime object
timestamp = datetime.datetime.fromtimestamp(unix_time)

# Convert datetime object to a readable string
readable_time = timestamp.strftime('%Y-%m-%d %H:%M:%S')

print(readable_time)
