

def get_filename_from_url(url: str) -> str:
    parts = url.split('/')
    filename = parts[-1]
    return filename


def parse_link_to_get_bucket_name(url: str) -> str:
    parts = url.split("/")
    return parts[0]
