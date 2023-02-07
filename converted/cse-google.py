# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# Import dependencies
import requests
import json
import pandas as pd
import timeß


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4, ensure_ascii=False)
    print(text)


# +
# get the API KEY here: https://developers.google.com/custom-search/v1/overview
API_KEY = "APIKEY"

# get your Search Engine ID on your CSE control panel
SEARCH_ENGINE_ID = "CSEID"

COUNT = 0
# -

# # Check Requests

print('COUNT', COUNT, '/100')

# ## Test API

# +
# the search query you want
query = "ทันตแพทย์"

# using the first page
page = 1

# constructing the URL
# doc: https://developers.google.com/custom-search/v1/using_rest
# calculating start, (page=2) => (start=11), (page=3) => (start=21)
start = (page - 1) * 10 + 1
url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"

# -

# make the API request
data = requests.get(url).json()
COUNT = COUNT + 1

# +
# get the result items
search_items = data.get("items")

# iterate over 10 results found
for i, search_item in enumerate(search_items, start=1):
    
    # get the page title
    cse_title = search_item.get("title")
    
    # page snippet
    cse_description = search_item.get("snippet")
    
    # extract the page url
    cse_url = search_item.get("link")
    
    if 'cse_image' in search_item.get("pagemap"):
        cse_image = search_item.get("pagemap").get("cse_image")[0].get("src")
    else:
        cse_image = ''

    meta_title = search_item.get("pagemap").get("metatags")[0].get("og:title", "")

    meta_description = search_item.get("pagemap").get("metatags")[0].get("og:description", "")

    meta_url = search_item.get("pagemap").get("metatags")[0].get("og:url", "")
    
    meta_image = search_item.get("pagemap").get("metatags")[0].get("og:image", "")
    
    meta_site_name = search_item.get("pagemap").get("metatags")[0].get("og:site_name", "")
    
    meta_type = search_item.get("pagemap").get("metatags")[0].get("og:type", "")
    
    udemy_category = search_item.get("pagemap").get("metatags")[0].get("udemy_com:category", "")
    
    udemy_instructor = search_item.get("pagemap").get("metatags")[0].get("udemy_com:instructor", "")
    
    udemy_price = search_item.get("pagemap").get("metatags")[0].get("udemy_com:price", "")
        
    # print the results
    print("="*10, f"Result #{i+start-1}", "="*10)
    print("cse_title:", cse_title)
    print("cse_description:", cse_description)
    print("cse_url:", cse_url)
    print("cse_image:", cse_image)
    
    print("meta_title:", meta_title)
    print("meta_description:", meta_description)
    print("meta_url:", meta_url)
    print("meta_image:", meta_image)
    print("meta_site_name:", meta_site_name)
    print("meta_type:", meta_type)
    print("udemy_category:", udemy_category)
    print("udemy_instructor:", udemy_instructor)
    print("udemy_price:", udemy_price, "\n")
# -

# ---

# ## init keywords

# +
skill_keywords = [
"Reading Comprehension",
"Active Listening",
"Writing",
"Speaking",
"Mathematics",
"Science",
"Critical Thinking",
"Active Learning",
"Learning Strategies",
"Monitoring",
"Social Perceptiveness",
"Coordination",
"Persuasion",
"Negotiation",
"Instructing",
"Service Orientation",
"Complex Problem Solving",
"Operations Analysis",
"Technology Design",
"Equipment Selection",
"Installation",
"Programming",
"Operation Monitoring",
"Operation and Control",
"Equipment Maintenance",
"Troubleshooting",
"Repairing",
"Quality Control Analysis",
"Judgment and Decision Making",
"Systems Analysis",
"Systems Evaluation",
"Time Management",
"Management of Financial Resources",
"Management of Material Resources",
"Management of Personnel Resources"
]

skill_keywords_thai = [
"การอ่านทำความเข้าใจ",
"การฟังอย่างตั้งใจ",
"การเขียน",
"การพูด",
"คณิตศาสตร์",
"วิทยาศาสตร์",
"การคิดแบบมีเหตุมีผล",
"การเรียนรู้เชิงรุก",
"กลยุทธ์การเรียนรู้",
"การติดตามผล",
"การรับรู้ข้อมูลทางสังคม",
"การประสานงาน",
"การโน้มน้าว/ชักชวน",
"การเจรจาต่อรอง",
"การให้คำแนะนำ",
"การคิดเชิงบริการ",
"การแก้ปัญหาที่ซับซ้อน",
"การวิเคราะห์การดำเนินงาน",
"การออกแบบเทคโนโลยี",
"การเลือกอุปกรณ์",
"การติดตั้ง",
"การเขียนโปรแกรม",
"การตรวจสอบการทำงาน",
"การควบคุมการทำงานของเครื่องมือหรือระบบ",
"การบำรุงรักษาเครื่องมือหรืออุปกรณ์",
"การแก้ไขปัญหา",
"การซ่อม",
"การวิเคราะห์ควบคุมคุณภาพ",
"การใช้วิจารณญาณและการตัดสินใจ",
"การวิเคราะห์ระบบ",
"การประเมินระบบ",
"การบริหารเวลา",
"การบริหารทรัพยากรทางการเงิน",
"การบริหารจัดการทรัพยากรและวัสดุ",
"การบริหารจัดการทรัพยากรด้านบุคลากร"
]

career_keywords_thai = [
"ทนายความ",
"วิศวกรโยธา ก่อสร้าง",
"โฟร์แมน",
"สถาปนิก",
"บริหารแบรนด์สินค้า ตราสินค้า ผลิตภัณฑ์",
"การตลาดดิจิทัล",
"การตลาดทั่วไป",
"บริหารการตลาด",
"การตลาดทางตรง",
"งานอีเวนท์",
"ประชาสัมพันธ์ทั่วไป",
"พัฒนาธุรกิจ",
"สื่อสารการตลาด",
"พยาบาล",
"เภสัชกร",
"เทคนิคการแพทย์",
"สัตวแพทย์",
"แพทย์ ศัลยแพทย์",
"ทันตแพทย์",
"ครู",
"ส่งออก นำเข้า",
"Shipping",
"ขับรถส่งเอกสาร ส่งผลิตภัณฑ์",
"ขับรถผู้บริหาร",
"พนักงานขาย",  
"ประสานงานขาย",
"บริการลูกค้า ลูกค้าสัมพันธ์",
"พนักงานขายทางโทรศัพท์",
"พนักงานแนะนำสินค้า (PC)",
"วิศวกรขาย",
"งานล่าม งานแปลภาษา",
"เชฟ พ่อครัว",
"พนักงานเสิร์ฟ",
"บาริสต้า",
"จัดซื้อ จัดหา",
"ช่างซ่อมบำรุง",
"ช่างไฟฟ้า อิเลคโทรนิค",
"ช่างเทคนิค",
"ช่างยนต์ ช่างกลโรงงาน",
"ช่าง CNC Mold กลึง เจียระไน",
"พนักงานฝ่ายบุคคล (HR)",
"ฝึกอบรม",
"บริหารค่าจ้าง บริหารผลตอบแทน",
"สรรหาบุคลากร",
"แรงงานสัมพันธ์", 
"วิเคราะห์ธุรกิจ วิเคราะห์ข้อมูล",
"ที่ปรึกษาทางธุรกิจ",
"การเงิน",
"ธุรการ การจัดการทั่วไป",
"ประสานงานทั่วไป",
"พนักงานทำความสะอาด แม่บ้าน",
"บริหารอสังหาริมทรัพย์",
"บัญชี",
"ธุรการบัญชี",
"ภาษี",
"ตรวจสอบบัญชี",
"Call Center",
"ตรวจสอบคุณภาพ",
"วางแผนการผลิต งานควบคุมการผลิต",
"ผลิตทั่วไป",
"บริหารการผลิต",
"พัฒนาสินค้า",
"เลขานุการ เลขานุการผู้บริหาร",
"วิจัยและพัฒนาผลิตภัณฑ์",
"นักเคมี",
"เจ้าหน้าที่ห้องปฎิบัติการ (Lab)",
"นักวิทยาศาสตร์การอาหาร",
"วิศวกรไฟฟ้า อิเล็กทรอนิกส์",
"วิศวกรการผลิต วิศวกรโรงงาน",
"วิศวกรเครื่องกล",
"วิศวกรสิ่งแวดล้อม และ จป",
"วิศวกรรมอุตสาหการ",
"วิศวกรโครงการ",
"วิศวกรซ่อมบำรุง",
"วิศวกรรมเคมี",
"กราฟิกดีไซน์",
"ครีเอทีฟ",
"ออกแบบกราฟิก",
"วางกลยุทธ์การโฆษณา",
"เขียนแบบ Drawing AutoCad",
"ช่างภาพ ตัดต่อ",
"โปรแกรมเมอร์",
"Software Engineer",
"ดูแลระบบ Network",
"IT Project Manager",
"IT Support Help Desk",
"Software Tester",
"ที่ปรึกษาไอที",
"Database Administration",
"IT Security",
"System Analyst",
"นักวิทยาศาสตร์ข้อมูล",
"ดูแลเว็บไซต์ และ SEO",
"นักออกแบบ UX/UI",
"Business Analyst (BA)",
"Data Engineer",
"Front End Developer",
"Back End Developer",
"DevOps Engineer",
"IT Product Manager",
"iOS Developer",
"Android Developer",
"Scrum Master"
]

career_keywords = [
"Lawyer",
"Civil Engineer",
"Foreman",
"Architect",
"Brand and Product Management",
"Digital Marketing",
"General Marketing",
"Marketing Manager",
"Direct Marketing",
"Event Staff",
"Public Relations",
"Business Development",
"Marketing Communications",
"Nurse",
"Pharmacist",
"Medical Technology",
"Veterinary",
"Physician / Surgeon",
"Dentist",
"Teacher",
"Import Export",
"Shipping",
"Messenger",
"Executive Chauffeur",
"Salesperson",
"Sales Support",
"Customer Service",
"Telesales",
"Sales (PC)",
"Sales Engineer",
"Interpreter",
"Chef",
"Waitress",
"Batista",
"Procurement",
"Maintenance Technician",
"Electrician",
"Technician",
"Mechanical Technician",
"CNC Mold Cutting Lathe",
"HR Executive",
"Training and Deveopment",
"Compensation Management",
"Recruitment",
"Employee Relations",
"Business Analyst",
"Business and Management Consultant",
"Finance",
"Admin Staff",
"Coordinator",
"Housekeeper",
"Property Manager",
"Accounting",
"Accounting Admin",
"Tax",
"Auditor",
"Call Center",
"Quality Control",
"Production Planning and Control",
"General Production",
"Production Management",
"Product Development",
"Executive Secretary",
"Research and Development",
"Chemist",
"Laboratory Staff",
"Food Scientist",
"Electrical Engineer, Electronics",
"Manufacturing Engineer",
"Mechanical Engineer",
"Environment and Safety Engineer",
"Industrial Engineer",
"Engineering Project Manager",
"Maintenance Engineer",
"Chemical Engineer",
"Graphic Design",
"Creative",
"Graphic Design",
"Strategic Media Planning",
"AutoCad Drawings",
"Photography Editing",
"Programmer",
"Software Engineer",
"Network Administrator",
"IT Project Manager",
"Support Help Desk",
"Software Tester",
"IT Consulting",
"Database Administration",
"IT Security",
"System Analyst",
"Data Scientist",
"Web Administrator and SEO",
"UX/UI Designer",
'Business Analyst (BA)',
"Data Engineer",
"Front End Web Developer",
"Back End Developer",
"DevOps Engineer",
"Product Manager",
"iOS Developer",
"Android Developer",
"Scrum Master"
]

# +
tech_keywords = []
df_tech_keywords = pd.read_excel('exports/Tech-Keywords.xlsx', index_col=0).reset_index()

for index in df_tech_keywords.index:
    if pd.isnull(df_tech_keywords['other_keywords'][index]):
        tech_keywords.append(df_tech_keywords['keyword'][index])
        
    else:
        tech_keywords.append(df_tech_keywords['keyword'][index]+ " OR " + df_tech_keywords['other_keywords'][index].replace(', ', ' OR '))
# -

# tech_keywords = tech_keywords[90:]
tech_keywords

skill_keywords_merge = []
for i in range(len(skill_keywords)):
    skill_keywords_merge.append(skill_keywords_thai[i] + " OR " + skill_keywords[i])

career_keywords_merge = []
for i in range(len(career_keywords)):
    career_keywords_merge.append(career_keywords_thai[i] + " OR " + career_keywords[i])

career_keywords_thai = career_keywords_thai[0:100]
career_keywords_thai

# # google cse request

df_cse = pd.DataFrame(columns = [
                        'keyword',
                        'cse_title', 
                        'cse_description', 
                        'cse_url', 
                        'cse_image', 
                        'meta_title',
                        'meta_description',
                        'meta_url',
                        'meta_image',
#                         'meta_article_published_time',
#                         'meta_article_author',
#                         'meta_author',
#                         'meta_section',
#                         'meta_tag',
                        'meta_site_name',
                        'meta_type',
                        'udemy_category',
                        'udemy_instructor',
                        'udemy_price'
                      ])

df_cse_en = pd.DataFrame(columns = [
                        'keyword',
                        'cse_title', 
                        'cse_description', 
                        'cse_url', 
                        'cse_image', 
                        'meta_title',
                        'meta_description',
                        'meta_url',
                        'meta_image',
#                         'meta_article_published_time',
#                         'meta_article_author',
#                         'meta_author',
#                         'meta_section',
#                         'meta_tag',
                        'meta_site_name',
                        'meta_type',
                        'udemy_category',
                        'udemy_instructor',
                        'udemy_price'
                      ])

# +
for keyword in tech_keywords:
    
    query = keyword
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}"
    data = requests.get(url).json()
    COUNT = COUNT + 1

    search_items = data.get("items")
    if search_items:
        for i, search_item in enumerate(search_items, start=1):
            
            ### CSE SECTION
            cse_title = search_item.get("title")
            cse_description = search_item.get("snippet")
            cse_url = search_item.get("link")
            if 'cse_image' in search_item.get("pagemap"):
                cse_image = search_item.get("pagemap").get("cse_image")[0].get("src")
            else:
                cse_image = ''
            
            ### META SECTION
            meta_title = search_item.get("pagemap").get("metatags")[0].get("og:title", "")
            meta_description = search_item.get("pagemap").get("metatags")[0].get("og:description", "")
            meta_url = search_item.get("pagemap").get("metatags")[0].get("og:url", "")
            meta_image = search_item.get("pagemap").get("metatags")[0].get("og:image", "")
            
#             meta_article_published_time = search_item.get("pagemap").get("metatags")[0].get("article:published_time", "")
#             meta_article_author = search_item.get("pagemap").get("metatags")[0].get("article:author", "")
#             meta_author = search_item.get("pagemap").get("metatags")[0].get("author", "")
#             meta_section = search_item.get("pagemap").get("metatags")[0].get("article:section", "")
#             meta_tag = search_item.get("pagemap").get("metatags")[0].get("article:tag", "")

            meta_site_name = search_item.get("pagemap").get("metatags")[0].get("og:site_name", "")
            meta_type = search_item.get("pagemap").get("metatags")[0].get("og:type", "")
            
            udemy_category = search_item.get("pagemap").get("metatags")[0].get("udemy_com:category", "")
            udemy_instructor = search_item.get("pagemap").get("metatags")[0].get("udemy_com:instructor", "")
            udemy_price = search_item.get("pagemap").get("metatags")[0].get("udemy_com:price", "")
            
#             'keyword_en':keyword.split(' OR ')[1], 
#             'keyword_th':keyword.split(' OR ')[0],
            new_row = {'keyword':keyword, 
                        'cse_title':cse_title, 
                        'cse_description':cse_description, 
                        'cse_url':cse_url, 
                        'cse_image':cse_image, 
                        'meta_title':meta_title,
                        'meta_description':meta_description,
                        'meta_url':meta_url,
                        'meta_image':meta_image,
#                         'meta_article_published_time':meta_article_published_time,
#                         'meta_article_author':meta_article_author,
#                         'meta_author':meta_author,
#                         'meta_section':meta_section,
#                         'meta_tag':meta_tag,
                        'meta_site_name':meta_site_name,
                        'meta_type':meta_type,
                        'udemy_category':udemy_category,
                        'udemy_instructor':udemy_instructor,
                        'udemy_price':udemy_price
                      }
            df_cse_en = df_cse_en.append(new_row, ignore_index=True)
    elif not search_items:
            new_row = {'keyword':keyword, 
                        'cse_title':'', 
                        'cse_description':'', 
                        'cse_url':'', 
                        'cse_image':'', 
                        'meta_title':'',
                        'meta_description':'',
                        'meta_url':'',
                        'meta_image':'',
#                         'meta_article_published_time':'',
#                         'meta_article_author':'',
#                         'meta_author':'',
#                         'meta_section':'',
#                         'meta_tag':'',
                        'meta_site_name':'',
                        'meta_type':'',
                        'udemy_category':'',
                        'udemy_instructor':'',
                        'udemy_price':''
                      }
            df_cse_en = df_cse_en.append(new_row, ignore_index=True)
    time.sleep(1)
    
df_cse_en.to_excel('exports/cse-keywords-en.xlsx', index=False)

# +
for keyword in tech_keywords:
    
    query = keyword
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&cr=countryTH&q={query}"
    data = requests.get(url).json()
    COUNT = COUNT + 1

    search_items = data.get("items")
    if search_items:
        for i, search_item in enumerate(search_items, start=1):
            
            ### CSE SECTION
            cse_title = search_item.get("title")
            cse_description = search_item.get("snippet")
            cse_url = search_item.get("link")
            if 'cse_image' in search_item.get("pagemap"):
                cse_image = search_item.get("pagemap").get("cse_image")[0].get("src")
            else:
                cse_image = ''
            
            ### META SECTION
            meta_title = search_item.get("pagemap").get("metatags")[0].get("og:title", "")
            meta_description = search_item.get("pagemap").get("metatags")[0].get("og:description", "")
            meta_url = search_item.get("pagemap").get("metatags")[0].get("og:url", "")
            meta_image = search_item.get("pagemap").get("metatags")[0].get("og:image", "")
            
#             meta_article_published_time = search_item.get("pagemap").get("metatags")[0].get("article:published_time", "")
#             meta_article_author = search_item.get("pagemap").get("metatags")[0].get("article:author", "")
#             meta_author = search_item.get("pagemap").get("metatags")[0].get("author", "")
#             meta_section = search_item.get("pagemap").get("metatags")[0].get("article:section", "")
#             meta_tag = search_item.get("pagemap").get("metatags")[0].get("article:tag", "")

            meta_site_name = search_item.get("pagemap").get("metatags")[0].get("og:site_name", "")
            meta_type = search_item.get("pagemap").get("metatags")[0].get("og:type", "")
            
            udemy_category = search_item.get("pagemap").get("metatags")[0].get("udemy_com:category", "")
            udemy_instructor = search_item.get("pagemap").get("metatags")[0].get("udemy_com:instructor", "")
            udemy_price = search_item.get("pagemap").get("metatags")[0].get("udemy_com:price", "")
            
#             'keyword_en':keyword.split(' OR ')[1], 
#             'keyword_th':keyword.split(' OR ')[0],
            new_row = {'keyword':keyword, 
                        'cse_title':cse_title, 
                        'cse_description':cse_description, 
                        'cse_url':cse_url, 
                        'cse_image':cse_image, 
                        'meta_title':meta_title,
                        'meta_description':meta_description,
                        'meta_url':meta_url,
                        'meta_image':meta_image,
#                         'meta_article_published_time':meta_article_published_time,
#                         'meta_article_author':meta_article_author,
#                         'meta_author':meta_author,
#                         'meta_section':meta_section,
#                         'meta_tag':meta_tag,
                        'meta_site_name':meta_site_name,
                        'meta_type':meta_type,
                        'udemy_category':udemy_category,
                        'udemy_instructor':udemy_instructor,
                        'udemy_price':udemy_price
                      }
            df_cse = df_cse.append(new_row, ignore_index=True)
    elif not search_items:
            new_row = {'keyword':keyword, 
                        'cse_title':'', 
                        'cse_description':'', 
                        'cse_url':'', 
                        'cse_image':'', 
                        'meta_title':'',
                        'meta_description':'',
                        'meta_url':'',
                        'meta_image':'',
#                         'meta_article_published_time':'',
#                         'meta_article_author':'',
#                         'meta_author':'',
#                         'meta_section':'',
#                         'meta_tag':'',
                        'meta_site_name':'',
                        'meta_type':'',
                        'udemy_category':'',
                        'udemy_instructor':'',
                        'udemy_price':''
                      }
            df_cse = df_cse.append(new_row, ignore_index=True)
    time.sleep(1)
    
df_cse.to_excel('exports/cse-keywords.xlsx', index=False)
# -

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    display(df_cse)

# +
# res = {} 
# for key in keywords: 
#     for value in keywords_thai: 
#         res[key] = value 
#         keywords_thai.remove(value) 
#         break  
        
# df_thai = pd.DataFrame(res.items(), columns=['keyword_eng', 'keyword'])

# df_new = pd.merge(df_cse, df_thai, on='keyword')

# +
# df_new.to_excel('exports/cse-keywords-thai.xlsx', index=False)
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#     display(df_new)
# -

# ---

# # udemy api request

from requests.auth import HTTPBasicAuth
auth = HTTPBasicAuth("csRUo422lFAc78bHOPlbKsvK4mv4Lqar0vATRo0Z", "Cz2Zkw6vgQSPgQxxBtxT7QZuSy26s6VjNB1wRXiCsFIGcrKq5SbJl0kPXk5SxxXGYQLsmI4CHUOrea5aFl7tB7yNUKFOXdT0y009K2Dicju47BsqCIKiSD1qUv2fkWk9")

df_udemy = pd.DataFrame(columns = ['keyword', 'title', 'url', 'headline', 'price', 'img_url'])

# +
for keyword in keywords:
    query = keyword
    url_ude = f"https://www.udemy.com/api-2.0/courses?page=1&page_size=5&search={query}"
    data_ude = requests.get(url_ude, auth=auth).json()

    response_items = data_ude.get("results")

    for i, response_item in enumerate(response_items, start=1):
        if i > 10: 
            break
            
        new_row = {'keyword':query, 
                   'title':response_item.get("title"), 
                   'url':"https://udemy.com" + response_item.get("url"), 
                   'headline':response_item.get("headline"),
                   'price':response_item.get("price"), 
                   'img_url':response_item.get("image_480x270")}
        df_udemy = df_udemy.append(new_row, ignore_index=True)

    time.sleep(1)

df_udemy.to_excel('exports/udemy-keywords.xlsx', index=False)
# -

df_merge = pd.concat([df_cse, df_cse_en], ignore_index=True)

df_merge = df_merge.drop_duplicates(subset=['cse_url'])

df_merge.to_excel('exports/cse-keywords.xlsx', index=False)




