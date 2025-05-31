import sys

def is_python_version_greater_than_3_11():
    python_version_major = sys.version_info.major
    python_version_minor = sys.version_info.minor
    if python_version_major==3 and python_version_minor >= 11:
        return True
    else:
        return False

if __name__ == "__main__":
    print(is_python_version_greater_than_3_11())