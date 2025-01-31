import csv
import time

def read_jobs():
    jobs = []
    with open("jobs.txt", mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            jobs.append(row)
    return jobs

def update_job_status(job_id, new_status):
    jobs = read_jobs()
    with open("jobs.txt", mode="w", newline="") as file:
        writer = csv.writer(file)
        for job in jobs:
            if job[0] == job_id:
                job[2] = new_status
            writer.writerow(job)

def perform_job(job_id, job_description):
    print(f"Rozpoczęto pracę: {job_description} (ID: {job_id})")
    time.sleep(30)
    print(f"Zakończono pracę: {job_description} (ID: {job_id})")

if __name__ == "__main__":
    while True:
        jobs = read_jobs()
        for job in jobs:
            job_id, job_description, status = job
            if status == "pending":
                update_job_status(job_id, "in_progress")
                perform_job(job_id, job_description)
                update_job_status(job_id, "done")
        time.sleep(5)