import requests
import lxml.html
import pandas as pd

def deal_with_independents(counter, elements):
    if elements[counter].text_content().strip() == "Angus King":
        return counter+4
    elif elements[counter].text_content().strip() == "Bernie Sanders":
        return counter+4
    elif elements[counter].text_content().strip() == "Gregorio Kilili Camacho Sablan":
        return counter+4
    elif elements[counter].text_content().strip() == "Jennifer Gonzalez Colon":
        return counter+2
    else:
        return counter
    
response = requests.get("https://ballotpedia.org/List_of_current_members_of_the_U.S._Congress")
html = lxml.html.fromstring(response.text)
elements = html.xpath("//td/p")
counter = 0
members = []
add = True
while counter < len(elements):
    tmp = {}
    counter = deal_with_independents(counter, elements)
    for i in range(4):
        if i == 0:
            tmp["name"] = elements[i+counter].text_content().strip()
        elif i == 1:
            tmp["office_title"] = elements[i+counter].text_content().strip()
        elif i == 2:
            if "party" not in elements[i+counter].text_content().lower(): 
                tmp["date_assumed_office"] = elements[i+counter].text_content().strip()
            else:
                tmp["party"] = elements[i+counter].text_content().strip()
                counter += 3
                add = False
                break
        else:
            tmp["party"] = elements[i+counter].text_content().strip()
    members.append(tmp)
    if add:
        counter += 4
    else:
        add = True

df = pd.DataFrame()
for member in members:
    df = df.append(member, ignore_index=True)

df.to_csv("party_affiliation.csv", index=False)
