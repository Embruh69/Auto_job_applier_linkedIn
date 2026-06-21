'''
Author:     Sai Vignesh Golla
LinkedIn:   https://www.linkedin.com/in/saivigneshgolla/

Copyright (C) 2024 Sai Vignesh Golla

License:    GNU Affero General Public License
            https://www.gnu.org/licenses/agpl-3.0.en.html
            
GitHub:     https://github.com/GodsScion/Auto_job_applier_linkedIn

Support me: https://github.com/sponsors/GodsScion

version:    26.01.20.5.08
'''


###################################################### APPLICATION INPUTS ######################################################


# >>>>>>>>>>> Easy Apply Questions & Inputs <<<<<<<<<<<

# Give an relative path of your default resume to be uploaded. If file in not found, will continue using your previously uploaded resume in LinkedIn.
default_resume_path = "A:\importantstuffs\Leonard Aldo Suhendri-resume-3.pdf"      # (In Development)

# What do you want to answer for questions that ask about years of experience you have, this is different from current_experience? 
years_of_experience = "0"          # A number in quotes Eg: "0","1","2","3","4", etc.

# Do you need visa sponsorship now or in future?
require_visa = "Yes"               # "Yes" or "No"

# What is the link to your portfolio website, leave it empty as "", if you want to leave this question unanswered
website = "https://github.com/Embruh69/datavizpersonalprojects"   # "www.example.bio" or "" and so on....

# Please provide the link to your LinkedIn profile.
linkedIn = "https://www.linkedin.com/in/leonard-aldosuhendri-248341238"       # "https://www.linkedin.com/in/example" or "" and so on...

# What is the status of your citizenship? # If left empty as "", tool will not answer the question. However, note that some companies make it compulsory to be answered
# Valid options are: "U.S. Citizen/Permanent Resident", "Non-citizen allowed to work for any employer", "Non-citizen allowed to work for current employer", "Non-citizen seeking work authorization", "Canadian Citizen/Permanent Resident" or "Other"
us_citizenship = "Other"



## SOME ANNOYING QUESTIONS BY COMPANIES 🫠 ##

# What to enter in your desired salary question (American and European), What is your expected CTC (South Asian and others)?, only enter in numbers as some companies only allow numbers,
desired_salary = 2000000          # 80000, 90000, 100000 or 120000 and so on... Do NOT use quotes
'''
Note: If question has the word "lakhs" in it (Example: What is your expected CTC in lakhs), 
then it will add '.' before last 5 digits and answer. Examples: 
* 2400000 will be answered as "24.00"
* 850000 will be answered as "8.50"
And if asked in months, then it will divide by 12 and answer. Examples:
* 2400000 will be answered as "200000"
* 850000 will be answered as "70833"
'''

# What is your current CTC? Some companies make it compulsory to be answered in numbers...
current_ctc = 0            # 800000, 900000, 1000000 or 1200000 and so on... Do NOT use quotes
'''
Note: If question has the word "lakhs" in it (Example: What is your current CTC in lakhs), 
then it will add '.' before last 5 digits and answer. Examples: 
* 2400000 will be answered as "24.00"
* 850000 will be answered as "8.50"
# And if asked in months, then it will divide by 12 and answer. Examples:
# * 2400000 will be answered as "200000"
# * 850000 will be answered as "70833"
'''

# (In Development) # Currency of salaries you mentioned. Companies that allow string inputs will add this tag to the end of numbers. Eg: 
# currency = "IDR"                 # "USD", "INR", "EUR", etc.

# What is your notice period in days?
notice_period = 0                   # Any number >= 0 without quotes. Eg: 0, 7, 15, 30, 45, etc.
'''
Note: If question has 'month' or 'week' in it (Example: What is your notice period in months), 
then it will divide by 30 or 7 and answer respectively. Examples:
* For notice_period = 66:
  - "66" OR "2" if asked in months OR "9" if asked in weeks
* For notice_period = 15:"
  - "15" OR "0" if asked in months OR "2" if asked in weeks
* For notice_period = 0:
  - "0" OR "0" if asked in months OR "0" if asked in weeks
'''

# Your LinkedIn headline in quotes Eg: "Software Engineer @ Google, Masters in Computer Science", "Recent Grad Student @ MIT, Computer Science"
linkedin_headline = "Information Systems Undergraduate | Aspiring Data Analyst/Data Scientist | Python, SQL, Power BI" # "Headline" or "" to leave this question unanswered

# Your summary in quotes, use \n to add line breaks if using single quotes "Summary".You can skip \n if using triple quotes """Summary"""
linkedin_summary = """
Active 5th semester undergraduate student of Information Systems at Universitas Multimedia Nusantara and a freelance worker looking to find an entry level job in data analytics or data science.
Fluent in English and Python for processing data, able to manage databases in SQL, and a perceptive person with strong analytical skills.
Looking for a new experience while challenging myself into data related work, open to learning new skills and skills related towards the job.
"""

'''
Note: If left empty as "", the tool will not answer the question. However, note that some companies make it compulsory to be answered. Use \n to add line breaks.
''' 

# Your cover letter in quotes, use \n to add line breaks if using single quotes "Cover Letter".You can skip \n if using triple quotes """Cover Letter""" (This question makes sense though)
cover_letter = """
Dear Hiring Manager,

I am Leonard Aldo Suhendri, an active 5th semester undergraduate student of Information Systems at Universitas Multimedia Nusantara, currently maintaining a GPA of 3.55/3.75. I am writing to express my interest in an entry level role in data analytics or data science.

I am fluent in Python for data processing, comfortable managing databases in SQL, and have hands-on experience with Power BI, Tableau, and Google Cloud Platform through coursework in Big Data Analysis, Data Modelling, Machine Learning, Deep Learning, Data Warehousing, and Data Visualization. I hold certifications in Data Visualization (CISDV), Data Analysis (MySkill), and TOEIC English.

Beyond academics, I have organized events and led teams in organizational settings, strengthening my communication and critical thinking skills. I am eager to bring my analytical mindset and willingness to learn to your team.

Thank you for considering my application.

Best regards,
Leonard Aldo Suhendri
"""
##> ------ Dheeraj Deshwal : dheeraj9811 Email:dheeraj20194@iiitd.ac.in/dheerajdeshwal9811@gmail.com - Feature ------

# Your user_information_all letter in quotes, use \n to add line breaks if using single quotes "user_information_all".You can skip \n if using triple quotes """user_information_all""" (This question makes sense though)
# We use this to pass to AI to generate answer from information , Assuing Information contians eg: resume  all the information like name, experience, skills, Country, any illness etc. 
user_information_all ="""
Name: Leonard Aldo Suhendri
Phone: 081311208478
Email: leonard.aldo123@gmail.com
LinkedIn: https://www.linkedin.com/in/leonard-aldosuhendri-248341238
GitHub: https://github.com/Embruh69/datavizpersonalprojects
Location: Duri Kosambi, West Jakarta, Indonesia

Summary: Active 5th semester undergraduate student of Information Systems at Universitas Multimedia Nusantara and a freelance worker looking to find an entry level job in data analytics or data science. Fluent in English and Python for processing data, able to manage databases in SQL, a perceptive person in analytical skill looking for a new experience while also challenging myself into data related work. Open to learning new skills related towards the job.

Education:
Universitas Multimedia Nusantara - Tangerang, Indonesia, Jun 2024 - Jun 2027 (Expected)
Diploma in Information Systems, GPA 3.55/3.75
Relevant coursework: Big Data Analysis, Data Modelling, Machine Learning, Deep Learning, Data Warehouse, Data Visualization, Data Engineering.

Organisational Experience:
DnD Jakarta (Online), Member, Jan 2018 - Present - Organize events and set up small team work games for members, increasing teamwork and cohesion.
Seminary Class - Indonesia, Event Organizer - Set up events and oversaw continuity of events in AI education seminary classes; 90% satisfaction rate.
Introduction to AI: A Practical Guide to Everyone - Seminar, Indonesia - Learned the basis of AI in modern real use cases and fundamentals of AI in Big Data context.
Pekantara 2025 - Tangerang Selatan, Indonesia, Dec 2025 - Present, LO Peserta.

Skills:
Hard Skills: Python, English, SQL, PowerBI, Google Cloud Platform, Tableau, Machine Learning, Data Analytics
Soft Skills: Analytical Skills, Presenting, Critical Thinking

Certifications:
CISDV Data Visualization (2024)
TOEIC English (2024)
MySkill Data Analysis (2023)
"""
##<
'''
Note: If left empty as "", the tool will not answer the question. However, note that some companies make it compulsory to be answered. Use \n to add line breaks.
''' 

# Name of your most recent employer
recent_employer = "Upwork" # "", "Lala Company", "Google", "Snowflake", "Databricks"

# Example question: "On a scale of 1-10 how much experience do you have building web or mobile applications? 1 being very little or only in school, 10 being that you have built and launched applications to real users"
confidence_level = "5"             # Any number between "1" to "10" including 1 and 10, put it in quotes ""
##



# >>>>>>>>>>> RELATED SETTINGS <<<<<<<<<<<

## Allow Manual Inputs
# Should the tool pause before every submit application during easy apply to let you check the information?
pause_before_submit = True         # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''

# Should the tool pause if it needs help in answering questions during easy apply?
# Note: If set as False will answer randomly...
pause_at_failed_question = True    # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''
##

# Do you want to overwrite previous answers?
overwrite_previous_answers = False # True or False, Note: True or False are case-sensitive







############################################################################################################
'''
THANK YOU for using my tool 😊! Wishing you the best in your job hunt 🙌🏻!

Sharing is caring! If you found this tool helpful, please share it with your peers 🥺. Your support keeps this project alive.

Support my work on <PATREON_LINK>. Together, we can help more job seekers.

As an independent developer, I pour my heart and soul into creating tools like this, driven by the genuine desire to make a positive impact.

Your support, whether through donations big or small or simply spreading the word, means the world to me and helps keep this project alive and thriving.

Gratefully yours 🙏🏻,
Sai Vignesh Golla
'''
############################################################################################################
