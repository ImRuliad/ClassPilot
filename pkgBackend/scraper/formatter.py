

def get_name_from_sem_url(url: str) -> str:
    tail = url.rstrip("/").split("/")[-1]
    return tail.replace("-", " ").title()
