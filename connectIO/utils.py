from typing import Any, Callable
from threading import Thread


def threaded(func: Callable) -> Callable:
    """
    A decorator that runs a function on
    a separate thread.
    """
    def wrapper(*args: Any, **kwargs: Any) -> None:
        Thread(
            target=func, 
            args=args,
            kwargs=kwargs,
        ).start()
        
    return wrapper
