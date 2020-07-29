import json
import os


def load_data(dir="."):
    meta = _load_meta(dir)
    _try_update_guild_flags(meta)
    data = _load_data(dir)
    return data, meta


def _load_meta(dir):
    return json.load(open(os.path.join(dir, "meta.json")))


def _try_update_guild_flags(meta):
    try:
        from guild import _api as gapi
    except ImportError:
        pass
    else:
        run = gapi.current_run()
        flags = run.get("flags") or {}
        flags.update(meta)
        run.write_attr("flags", flags)


def _load_data(dir):
    return open(os.path.join(dir, "data.csv")).readlines()
