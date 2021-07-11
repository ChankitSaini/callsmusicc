import hashlib


def md5(_):
    __ = hashlib.md5()
    __.update(_.encode() if isinstance(_, str) else _)
    return __.hexdigest()
