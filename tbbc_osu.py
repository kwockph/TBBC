# tbbc_osu.py
import requests

# Constant strings
_API_URL = "https://osu.ppy.sh/api/"
Coni_ID = "2188855" # For testing purposes

_key = ""
with open("osu_api_key.txt","r") as f:
    _key = f.readline().strip()

# #####################
# # osu API functions #
# #####################
# get_beatmaps()
# get_user()
# get_scores()
# get_user_best()
# get_user_recent()
# get_match()
# get_replay()

def get_beatmaps(since = None, s = None, b = None, u = None, type = None,
m = None, a = None, h = None, limit = None, mods = None):
    url = _API_URL + "get_beatmaps"
    params = {
        "k": _key,
        "since": since,
        "s": s,
        "b": b,
        "u": u,
        "type": type,
        "m": m,
        "a": a,
        "h": h,
        "limit": limit,
        "mods": mods
    }
    nones = []
    for key in params:
        if params[key] == None:
            nones.append(key)
    for key_name in nones:
        del params[key_name]
    return requests.post(url, params).json()

def get_user(u, m = None, type = None, event_days = None):
    url = _API_URL + "get_user"
    params = {
        "k": _key,
        "u": u,
        "m": m,
        "type": type,
        "event_days": event_days
    }
    nones = []
    for key in params:
        if params[key] == None:
            nones.append(key)
    for key_name in nones:
        del params[key_name]
    return requests.post(url, params).json()

def get_scores(b, u = None, m = None, mods = None, type = None, limit = None):
    url = _API_URL + "get_scores"
    params = {
        "k": _key,
        "b": b,
        "u": u,
        "m": m,
        "mods": type,
        "type": limit
    }
    nones = []
    for key in params:
        if params[key] == None:
            nones.append(key)
    for key_name in nones:
        del params[key_name]
    return requests.post(url, params).json()

def get_user_best(u, m = None, limit = None, type = None):
    url = _API_URL + "get_user_best"
    params = {
        "k": _key,
        "u": u,
        "m": m,
        "limit": limit,
        "type": type
    }
    nones = []
    for key in params:
        if params[key] == None:
            nones.append(key)
    for key_name in nones:
        del params[key_name]
    return requests.post(url, params).json()

def get_user_recent(u, m = None, limit = None, type = None):
    url = _API_URL + "get_user_recent"
    params = {
        "k": _key,
        "u": u,
        "m": m,
        "limit": limit,
        "type": type
    }
    nones = []
    for key in params:
        if params[key] == None:
            nones.append(key)
    for key_name in nones:
        del params[key_name]
    return requests.post(url, params).json()

def get_match(mp):
    url = _API_URL + "get_match"
    params = {
        "k": _key,
        "mp": mp
    }
    nones = []
    for key in params:
        if params[key] == None:
            nones.append(key)
    for key_name in nones:
        del params[key_name]
    return requests.post(url, params).json()

def get_replay(k, b, u, m = None, s = None, type = None, mods = None):
    url = _API_URL + "get_replay"
    params = {
        "k": _key,
        "b": b,
        "u": u,
        "m": m,
        "s": s,
        "type": type,
        "mods": mods
    }
    nones = []
    for key in params:
        if params[key] == None:
            nones.append(key)
    for key_name in nones:
        del params[key_name]
    return requests.post(url, params).json()
