#!/usr/bin/env python
'''
1) based on
https://gist.github.com/micktwomey/606178
'''

import multiprocessing as mp
from multiprocessing import Pool
import socket
import math
import time
import Queue
import numpy as np
import ctypes


def foo(n):
    startT = time.time()
    total = 0
    for x in xrange(n):
        total += math.factorial(x)
    #return total
    endT = time.time()
    #print("{} to {} = {:.3f} seconds".format(startT, endT, endT - startT))
    return [startT, endT]

def handle(connection, address, jobID, jobTimingTable, target_dev):
    import logging
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger("process-%r" % (address,))
    ##
    ## create pool of child processes
    ##
    #cpu_num = mp.cpu_count()
    #pool = Pool(processes = cpu_num * 2)

    ##
    ## create a shared table for each process
    ##
    #job_q = Queue.Queue()
    try:
        #logger.debug("Connected %r at %r", connection, address)
        logger.debug("Connected")
        while True:
            data = connection.recv(1024)
            if data == "":
                logger.debug("Socket closed remotely")
                break
            logger.debug("Received data %r", data)

            foo_input = int(data) * 2000
            [startT, endT] = foo(foo_input)
            print("{} to {} = {:.3f} seconds".format(startT, endT, endT - startT))

            jobTimingTable[jobID, 0] = 1  # done
            jobTimingTable[jobID, 1] = startT
            jobTimingTable[jobID, 2] = endT

            

            #job_q.put(int(data))

            #for elem in list(job_q.queue):
            #    print elem

            #print("current queue size : {}".format(job_q.qsize()))
            #
            ## 1) as we receive data, we put into the queue 
            ## (don't work on that asap)
            #job_param = None
            #if not job_q.empty():
            #    job_param = job_q.get()
            #    print("work on {}".format(job_param))

            #print("after dequeue size : {}".format(job_q.qsize()))

            # 2) start a new process
            #newjob = mp.Process(target=foo, args=(int(data),))
            #newjob.start()

            #run_job()

            #result = pool.apply_async(foo, (2000 * int(data), ))
            #[startT, endT] = result.get()


            #connection.sendall(data) # send feedback
            #logger.debug("Sent data")
    except:
        logger.exception("Problem handling request")
    finally:
        logger.debug("Closing socket")
        connection.close()

class Server(object):
    def __init__(self, hostname, port):
        import logging
        self.logger = logging.getLogger("server")
        self.hostname = hostname
        self.port = port
        self.gpuNum = 8  # gpus in cluster

    def monitor(self, jobTimingTable, jobID):
        self.logger.debug("(Monitoring)")
        target_dev = 0

        # round-robin
        target_dev = jobID % self.gpuNum

        return target_dev


    def start(self):
        self.logger.debug("listening")
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # resue socket address
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.hostname, self.port))
        self.socket.listen(1)

    
        #
        # global workload table
        #
        # rows: different application
        # cols: 1) status(0/1)
        # cols: 2) startT(s)
        # cols: 3) endT(s)

        rows, cols = 10,3
        d_arr = mp.Array(ctypes.c_double, rows*cols)
        arr = np.frombuffer(d_arr.get_obj())
        jobTimingTable = arr.reshape((rows,cols))
        #self.logger.debug("%r ", jobTimingTable[:])
        #print jobTimingTable[:]
        #print jobTimingTable[0,1]

        #
        # gpu_table: list of list 
        #
        # rows: gpu_id
        # cols: 1) running_jobs
        # cols: 2)  
        rows, cols = self.gpuNum,2
        d_arr = mp.Array(ctypes.c_double, rows*cols)
        arr = np.frombuffer(d_arr.get_obj())
        gpuTable = arr.reshape((rows,cols))
        #self.logger.debug("%r ", type(gpuTable))
        #self.logger.debug("%r ", gpuTable.dtype)
        #self.logger.debug("%r ", gpuTable[:])
        

        jobID= -1

        while True:
            target_gpu = 0
            conn, address = self.socket.accept()
            jobID = jobID + 1
            self.logger.debug("Got connection : %r at %r ( job %r )", conn, address, jobID)
            #self.logger.debug("Got connection at %r", address)

            if jobID > 0:
                target_gpu = self.monitor(jobTimingTable, jobID)

            self.logger.debug("Target GPU-%r ", target_gpu)
            #print gpuTable[target_gpu, :]

            # add jobs
            gpuTable[target_gpu, 0] = gpuTable[target_gpu, 0] + 1
            self.logger.debug("%r ", gpuTable[:])

            process = mp.Process(target=handle, args=(conn, address, 
                jobID, jobTimingTable, target_gpu))

            process.daemon = False 
            process.start()
            self.logger.debug("Started process %r", process)


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.DEBUG)
    server = Server("0.0.0.0", 9000)
    try:
        logging.info("Listening")
        server.start()
    except:
        logging.exception("Unexpected exception")
    finally:
        logging.info("Shutting down")
        for process in mp.active_children():
            logging.info("Shutting down process %r", process)
            process.terminate()
            process.join()
    logging.info("All done")
