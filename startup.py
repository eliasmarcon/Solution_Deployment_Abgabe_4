import Dashboard
import FastAPI
import multiprocessing
jobs = []
jobs.append(multiprocessing.Process(target=FastAPI.start))
jobs.append(multiprocessing.Process(target=Dashboard.start))

for j in jobs:
    j.start()