# nmit_hack
# Team: Alpha_Queue
Repository for maintaining code of NMIT hackathon
# Description of Idea:
There are many events going on everywhere but on most occasions even the interested people are not able to attend
the event due to lack of information. We are proposing a solution to this problem so that people are notified about
other related events.
We will use a web crawler which will crawl throughout the web and search for such events and will feed that data as
an input to the Neural Network. The neural network will be trained in such a way that only relevant data is stored in
database. The user will be provided with a user interface in the form of web app in which they can filter out the
events based on their preference. A notification API will notify the user about the events based on their preference.

# WORKING
# clone this repo

# Crawler
Working:
A web crawler is used to crawl the web and collect event related data from websites. For this hackathon we have limited ourselves to Indian websites. A specific set of keywords is used to fetch only relevant data.

1. Environment setup
First of all you will need to download latest executable geckodriver to run latest firefox using selenium: https://github.com/mozilla/geckodriver/releases
The Selenium client bindings tries to locate the geckodriver executable from the system PATH. You will need to add the directory containing the executable to the system path.

2. Running the crawler
Open terminal --> Go to the directoty backend_crawler --> execute: python3 crawl.py
This will save all the event (only hackathons for now) into a csv file links.csv

**Crawled Links:**
![Alt text](/screenshots/total_links.png?raw=true "Crawled Links")

# Finding the word level relationship using a deep learning model:

The crawler basically gives us data in unstructured format. The main idea of using a NLP model is to find out the context of the words and their relation. For this we make use of AllenNLP, a open source project by Allen Institute for Artificial Intelligence.

  # Setup AllenNLP on your local system:

   1. Download and install Conda. link: https://conda.io/docs/download.html

   2. Create a Conda environment with Python 3.6

        conda create -n allennlp python=3.6

   3. Activate the Conda environment. You will need to activate the Conda environment in each terminal in which you want to use AllenNLP.

        source activate allennlp
        
   4. Installing the library and dependencies is simple using pip.

        pip install allennlp
   
 Now open terminal and go to directory "finding_word_tokens_using_deep_learning" --> now execute: python3 trying.py
 You can also edit the 'sentence' inside trying.py (currently "Did Uriah honestly think he could beat the game in under three hours?") to anything you'd like
 
 **Filtered Links:**
 ![Alt text](/screenshots/filtered_links.png?raw=true "Filtered Links")
 
# Website
The website can be accessed by opening the index.html file inside the website directory. The website can be used to search for the specific content and one can enable push notification, so that if there is anything new added into that category the user can be notified.

**Website with push notification:**
![Alt text](/screenshots/push_notification.png?raw=true "Push Notification")

# Remaining Part
The current prototype only lists hackathons from India, we intend to extend this prototype to any kind of event specified by the user.
