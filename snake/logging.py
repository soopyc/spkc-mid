# logging.py: custom logging facility

def debug(msg, **kwargs):
    print(f'[*] {msg}', **kwargs)


def info(msg, **kwargs):
    print(f'[i] {msg}', **kwargs)
