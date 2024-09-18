import logging

def log_event(username: str, status: str):
    if status == 'success':
        logging.info(f"User '{username}' logged in successfully.")
    elif status == 'expired':
        logging.warning(f"User '{username}' password expired, needs to change.")
    elif status == 'failed':
        logging.error(f"User '{username}' failed to log in due to incorrect password.")
    else:
        raise ValueError(f"Invalid status: {status}")