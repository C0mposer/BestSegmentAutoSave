def time_string_to_seconds(time_str):
    minutes, seconds = time_str.split(":")
    total_seconds = int(minutes) * 60 + float(seconds)
    return total_seconds