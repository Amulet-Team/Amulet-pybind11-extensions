def get_include() -> str:
    import os
    return os.path.join(__path__[0], "include")
