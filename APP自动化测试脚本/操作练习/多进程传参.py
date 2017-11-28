import multiprocessing
import random
import time


def producer(queue):
    item = random.randint(0, 256)
    queue.put(item)
    print("Process Producer: item %d appended to queue" % item)


def consumer(queue):
    while True:
        if (queue.empty()):
            print("the queue is empty")
            break
        else:
            time.sleep(2)
            item = queue.get()
            print("Process Consumer: item %d poped from by" % item)


if __name__ == '__main__':
    queue = multiprocessing.Queue()
    process_producer = multiprocessing.Process(target=producer, args=(queue,))
    process_consumer = multiprocessing.Process(target=consumer, args=(queue,))
    process_producer.start()
    process_consumer.start()
    process_producer.join()
    process_consumer.join()
