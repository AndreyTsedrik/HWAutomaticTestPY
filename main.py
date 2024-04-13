import logging
import argparse
from functools import wraps

# Configure logging
logging.basicConfig(level='DEBUG')
logger = logging.getLogger(__name__)

# Configure file handler for errors
handler_error = logging.FileHandler("error.log", encoding='utf-8')
handler_error.setLevel(logging.ERROR)
logger.addHandler(handler_error)


def logging_decorator(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result  # Return the result of the function call
        except Exception as e:
            logger.critical(e)
            raise e
    return wrap


@logging_decorator
def div(a, b):
    return a / b


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Divide two numbers.')
    parser.add_argument('numerator', type=int, help='Numerator')
    parser.add_argument('denominator', type=int, help='Denominator')
    args = parser.parse_args()

    try:
        result = div(args.numerator, args.denominator)
        print("Result:", result)
    except ZeroDivisionError as e:
        print(e)