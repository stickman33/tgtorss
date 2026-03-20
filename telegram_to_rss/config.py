import os
from pathlib import Path
from urllib.parse import urlparse
from platformdirs import user_data_dir

api_id = int(os.environ.get("TG_API_ID"))
api_hash = os.environ.get("TG_API_HASH")
password = os.environ.get("TG_PASSWORD")

# Proxy configuration: supports socks5://host:port, socks4://host:port, http://host:port
_proxy_url = os.environ.get("PROXY_URL")
proxy = None
if _proxy_url:
    import socks
    _parsed = urlparse(_proxy_url)
    _proxy_types = {
        "socks5": socks.SOCKS5,
        "socks4": socks.SOCKS4,
        "http": socks.HTTP,
    }
    _proxy_type = _proxy_types.get(_parsed.scheme)
    if _proxy_type is None:
        raise ValueError(f"Unsupported proxy scheme: {_parsed.scheme}")
    proxy = (_proxy_type, _parsed.hostname, _parsed.port)

update_interval_seconds = int(os.environ.get("UPDATE_INTERVAL") or 3600)
feed_size_limit = int(os.environ.get("FEED_SIZE") or 200)
initial_feed_size = int(os.environ.get("INITIAL_FEED_SIZE") or 50)
base_url = os.environ.get("BASE_URL")
bind = os.environ.get("BIND") or "127.0.0.1:3042"
max_video_size_mb = int(os.environ.get("MAX_VIDEO_SIZE_MB", 10))
max_video_size = max_video_size_mb * 1024 * 1024

loglevel = os.environ.get("LOGLEVEL", "INFO").upper()

data_dir = (
    Path(os.environ.get("DATA_DIR"))
    if os.environ.get("DATA_DIR")
    else Path(user_data_dir()).joinpath("telegram_to_rss")
)
session_path = data_dir.joinpath("telegram_to-rss.session")
static_path = data_dir.joinpath("static")
db_path = data_dir.joinpath("feeds.db")

data_dir.mkdir(mode=0o700, parents=True, exist_ok=True)
static_path.mkdir(mode=0o700, exist_ok=True)
