# A script that will gather data from a website online
# Connect this to a recommendation app

# https://realpython.com/beautiful-soup-web-scraper-python/

import requests    # user friendly way to fetch static html from the internet
from bs4 import BeautifulSoup     # used to extract relevant information from the hml

URL = "https://realpython.github.io/fake-jobs/"   # The url you are interested in
page = requests.get(URL)                          # this basically tells the program to pull results form this url

soup = BeautifulSoup(page.content, "html.parser")    # creates a Beautifulsoup object that takes page.content as its input
                                                     # html.parser makes sure you use the correct parser for HTML content

results= soup.find(id="ResultsContainer")            # Every item in dev-tools has an id, and soup can find that object by its ID

#print(results.prettify())                         # a function that prettifies the printed results to make for easier reading

# job_elements = results.find_all("div", class_ = "card_content")  # here we run find.all on a specific BS object
                                                                 # returns an iterable with all the HTML for all listings on the page

# for job_element in job_elements:
#    title_element = job_element.find("h2", class_="title")           # here we can id specific info elements we are interested in
#    company_element = job_element.find("h3", class_="company")       # and it will find and print them
#    location_element = job_element.find("p", class_="location")
#    print(title_element.text.strip())                                              # this prints the element, however if we add .text
#    print(company_element.text.strip())                                            # it prints the info as plain text
#    print(location_element.text.strip())                                           # adding .strip() removes the white highlight
#    print()

# python_jobs = results.find_all("h2", string="Python") # filters out all h2 objects with python in them 

python_jobs = results.find_all("h2", string=lambda text: "python" in text.lower())  # filters all h2 objects with keyword python in them

python_job_elements = [h2_element.parent.parent.parent for h2_element in python_jobs] 
# reaches up into the "card content" to extract the term python through all information given in the job post rather than just the title h2

print(len(python_jobs))

for job_element in python_job_elements:
    title_element = job_element.find("h2", class_="title")           # here we can id specific info elements we are interested in
    company_element = job_element.find("h3", class_="company")       # and it will find and print them
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())                                              # this prints the element, however if we add .text
    print(company_element.text.strip())                                            # it prints the info as plain text
    print(location_element.text.strip())                                           # adding .strip() removes the white highlight
    print()










    # -- snip --
    links= job_element.find_all("a")                    # what we do her eis first fetch links from all the filtered job postings
    for link in links:                                  # then we extract the href attribute, which is the application link for 
        link_url= link["href"]                          # the positions and print it in our console
        print(f"Apply here:{link_url}\n")

