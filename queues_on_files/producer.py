import csv
import time

def add_job(job_id, job_description):
    with open("jobs.txt", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([job_id, job_description, "pending"])

if __name__ == "__main__":
    job_id = 1
    job_description = "Rozmowa telefoniczna z klientem"
    add_job(job_id, job_description)
    print(f"Dodano pracę: {job_description} (ID: {job_id})")