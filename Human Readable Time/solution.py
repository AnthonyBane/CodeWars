from time import strftime, gmtime

def make_readable(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return strftime(f"{h:02d}:{m:02d}:{s:02d}")