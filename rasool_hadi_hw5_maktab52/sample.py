from person import Person
import logging

logger_sample = logging.getLogger("sample_logger")
file_handler1 = logging.FileHandler('sample.log', 'a')


log_format_1 = logging.Formatter("%(asctime)s-%(name)s.10s-%(levelname).16s-%(msecs)s-%(message)s")
log_format_output = logging.Formatter("%(asctime)-%(levelname)-%(message)")
stream_handler1 = logging.StreamHandler()
file_handler1.setFormatter(log_format_1)
stream_handler1.setFormatter(log_format_1)

stream_handler1.setLevel(logging.INFO)
logger_sample.addHandler(stream_handler1)
logger_sample.addHandler(file_handler1)
def sub(a, b):
    if b != 0:
        logger_sample.log(logging.DEBUG, "a/b=" + str(a / b))
        return a / b
    logger_sample.info("Divide by zero!")


print(sub(2, 3))
print(sub(2, 0))

p1 = Person("ali", "alavi", 23)
p2 = Person("gholi", "gholami", -23)
