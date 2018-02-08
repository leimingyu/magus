#!/usr/bin/env python
'''
1) based on
https://gist.github.com/micktwomey/606178
'''

import multiprocessing as mp
import socket
import math
import time
import Queue
import numpy as np
import ctypes

from multiprocessing import Pool, Value, Lock

def foo(n):
    startT = time.time()
    total = 0
    for x in xrange(n):
        total += math.factorial(x)
    #return total
    endT = time.time()
    #print("{} to {} = {:.3f} seconds".format(startT, endT, endT - startT))
    return [startT, endT]


class Server(object):
    def __init__(self, hostname, port):
        import logging
        self.logger = logging.getLogger("server")
        self.hostname = hostname
        self.port = port
        self.gpuNum = 8  # gpus in cluster

    def monitor(self, jobTimingTable, jobID, scheme = 'rr'):
        self.logger.debug("(Monitoring)")
        target_dev = 0

        # round-robin
        if scheme == 'rr':
            target_dev = jobID % self.gpuNum

        return target_dev

    
    def PrintGpuJobTable(self, GpuJobTable, total_jobs):
        #--------------------------------------------------------------
        # gpu job table : 5 columns
        #    jobid      gpu     status      starT       endT 
        #--------------------------------------------------------------
        print("JobID\tGPU\tStatus\tStart\t\t\tEnd\t\t\tDuration")
        for row in xrange(total_jobs):
            print("{}\t{}\t{}\t{}\t\t{}\t\t{}".format(GpuJobTable[row, 0],
            GpuJobTable[row, 1],
            GpuJobTable[row, 2],
            GpuJobTable[row, 3],
            GpuJobTable[row, 4],
            GpuJobTable[row, 4] - GpuJobTable[row, 3]))


    #--------------------------------------------------------------------------
    # run gpu job 
    #--------------------------------------------------------------------------
    def handleWorkload(self, connection, address, jobID, GpuJobTable, jobTimingTable, 
            target_dev):
        '''
        schedule workloads on the gpu
        '''
        import logging
        logging.basicConfig(level=logging.DEBUG)
        logger = logging.getLogger("process-%r" % (address,))


        try:
            #logger.debug("Connected %r at %r", connection, address)
            logger.debug("Connected")
            while True:
                #------------------------------------------------------------------
                # receive data
                #------------------------------------------------------------------
                data = connection.recv(1024)
                if data == "":
                    logger.debug("Socket closed remotely")
                    break

                if data == "end_simulation":
                    RunServer = False

                logger.debug("Received data %r", data)


                #------------------------------------------------------------------
                # work on the job 
                #------------------------------------------------------------------
                foo_input = int(data) * 2000
                [startT, endT] = foo(foo_input)
                #print("{} to {} = {:.3f} seconds".format(startT, endT, endT - startT))
                self.logger.debug("(Job {}) {} to {} = {:.3f} seconds".format(jobID, startT, endT, endT - startT))

                #------------------------------------------------------------------
                # update job timing table 
                #------------------------------------------------------------------
                ##jobTimingTable[jobID, 0] = 1  # done
                ##jobTimingTable[jobID, 1] = startT
                ##jobTimingTable[jobID, 2] = endT
                ##self.logger.debug("%r ", jobTimingTable[:])


                #--------------------------------------------------------------
                # update gpu job table 
                # 5 columns:
                #    jobid      gpu     status      starT       endT 
                #--------------------------------------------------------------
                GpuJobTable[jobID, 2] = 1  # done
                GpuJobTable[jobID, 3] = startT 
                GpuJobTable[jobID, 4] = endT 

                #self.logger.debug("%r ", GpuJobTable[:5,:])



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


    #--------------------------------------------------------------------------
    # server start
    #--------------------------------------------------------------------------
    def start(self):
        self.logger.debug("listening")
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # resue socket address
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.hostname, self.port))
        self.socket.listen(1)

        #-----------------------
        # 1) gpu job table : 5 columns
        #
        #    jobid      gpu     status      starT       endT 
        #       0       0           1       1           2
        #       1       1           1       1.3         2.4
        #       2       0           0       -           -
        #       ...
        #-----------------------
        maxJobHist = 10000
        rows, cols = maxJobHist,5 # note: init with a large prefixed table
        d_arr = mp.Array(ctypes.c_double, rows*cols)
        arr = np.frombuffer(d_arr.get_obj())
        GpuJobTable = arr.reshape((rows,cols))

    
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
        # gpu_status_table: list of list 
        #
        # rows: gpu_id
        # cols: 1) running_jobs
        # cols: 2)  
        rows, cols = self.gpuNum,2
        d_arr = mp.Array(ctypes.c_double, rows*cols)
        arr = np.frombuffer(d_arr.get_obj())
        gpuStatusTable = arr.reshape((rows,cols))
        #self.logger.debug("%r ", type(gpuTable))
        #self.logger.debug("%r ", gpuTable.dtype)
        #self.logger.debug("%r ", gpuTable[:])
        

        
        #KeepRun = Value('i', 1)
        #lock = Lock()

        total_jobs = 3 # Note: Flag to terminate simulation

        jobID= -1

        #----------------------------------------------------------------------
        # keep listening to the clients
        #----------------------------------------------------------------------
        while True:
            target_gpu = 0
            conn, address = self.socket.accept()
            jobID = jobID + 1
            #self.logger.debug("Got connection : %r at %r ( job %r )", conn, address, jobID)
            self.logger.debug("Got connection : %r ( job %r )", address, jobID)

            #-----------------------------------------
            # select gpu to run
            #-----------------------------------------
            target_gpu = self.monitor(jobTimingTable, jobID, scheme='rr')
            self.logger.debug("Target GPU-%r ", target_gpu)

            #print gpuTable[target_gpu, :]

            #-----------------------------------------
            # Update gpu job table 
            # 5 columns:
            #    jobid      gpu     status      starT       endT 
            #-----------------------------------------
            GpuJobTable[jobID, 0] = jobID
            GpuJobTable[jobID, 1] = target_gpu 
            GpuJobTable[jobID, 2] = 0 


            #-----------------------------------------
            # update gpu status table 
            #-----------------------------------------

            ### add job num
            ##gpuStatusTable[target_gpu, 0] = gpuStatusTable[target_gpu, 0] + 1
            ##self.logger.debug("%r ", gpuStatusTable[:])

            #-----------------------------------------
            # schedule the workload to the target GPU 
            #-----------------------------------------
            process = mp.Process(target=self.handleWorkload, 
                    args=(conn, address,
                        jobID, 
                        GpuJobTable,
                        jobTimingTable,
                        target_gpu))

            process.daemon = False 
            process.start()
            self.logger.debug("Started process %r", process)


            if jobID == total_jobs - 1: # jobID starts from 0
                process.join() # make sure the last process ends
                self.logger.debug("\n\nEnd Simulation\n\n")
                if maxJobHist < total_jobs:
                    self.logger.debug("\n\nError! The total_jobs exceeds the limit!\n\n")

                self.PrintGpuJobTable(GpuJobTable, total_jobs)

            #if KeepRun.value == 0:
            #    print("\n=> (End Simulation)\n")

            #with lock:
            #    if KeepRun.value == 0:
            #        print("\n=> (End Simulation)\n")
                    #self.logger.debug("End Simulation")

            
            #-----------------------------------------
            # check status
            #-----------------------------------------
            #self.logger.debug("%r ", GpuJobTable[:5,:])


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
