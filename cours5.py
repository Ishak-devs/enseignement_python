from multiprocessing import Queue, Process

def envoyer_donnes(queue):
    queue.put(42)

if __name__ == '__main__':

    file = Queue()
    p = Process(target=envoyer_donnes, args=(file,))
    p.start()
    print(f"The result is {file.get()}")
    p.join()