import re

def get_major_minor_version_from_string(version_string):
    return re.split("[\.-]", version_string.strip())[:2]

def get_correct_semversion(version_string):
    return ".".join(re.split("[\.-]", version_string.strip())[:3])
