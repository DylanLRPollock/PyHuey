# PyHuey Debian Forky cockpit override.
# Upstream splash/preloader disabled for Huey.

def _start_preloader(*args, **kwargs):
    """No-op preloader for PyHuey."""
    return None
