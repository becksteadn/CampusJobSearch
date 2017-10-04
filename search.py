#!/usr/bin/python

from bs4 import BeautifulSoup
import requests
import smtplib

#jobURL = "https://www.rit.edu/emcs/seo/students/oncampus/ct"
jobs_begin = "https://www.rit.edu/emcs/seo/students/oncampus/"
jobs_ends = ["ac", "at", "cl", "cs", "ct", "fs", "mt", "mc", "sv"]
jobs_names = ["Academic", "Atheltic", "Clerical", "Community Service", "Computer / Technical", "Food Service", "Maintenance", "Miscellaneous", "Services"]
#mail_to = "dest@example.com"
mail_to = "sender@example.com"
mail_from = "Job Search Bot"
mail_subject = "Campus Job Search"
mail_server = "smtp.gmail.com"


def category(url, name):
    print
    print
    head_len = len(name + "      " + url)
    head = head_len * "-"
    print(head)
    #print(str(name).upper().rjust((head_len / 2) - len(name)))
    print(str(name).upper() + "     " + str(url))
    #print(url)
    print(head)
    getJobs(url)

def sendText(body):
    msg = MimeText("Job found!\n" + body)
    msg['Subject'] = mail_subject
    msg['From'] = mail_from
    msg['To'] = mail_to
    try:
        s = smtplib.SMTP(mail_server)
        s.starttls()
        s.login("EMAIL-HERE", "LOGIN-HERE")
        s.sendmail(mail_from, [mail_to], msg.as_string())
        s.quit()
        print("Email sent")
    except Exception:
        print("Error: Text failed to send")

def getJobs(jobURL):
    r = requests.get(jobURL)
    soup = BeautifulSoup(r.content, 'html.parser')

    for job in soup.find_all("div", {"class":"container-fluid job"}):
        title = job.contents[1].text
        print("[*] " + title)
#        try:
#            with open("jobs.txt", "ab+") as f:
#                if title not in f.read():
#                    #f.write(title + "\n")
#                    #sendText(title)
#                    print("[*] " + title)
#        except IOError:
#            with open("jobs.txt", "a") as f:
#                #f.write(title + "\n")
#                #sendText(title)
#                print("[*] " + title)

for n in range(len(jobs_names)):
    category(jobs_begin + jobs_ends[n], jobs_names[n])
