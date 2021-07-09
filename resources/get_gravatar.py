import json
import requests

from libgravatar import Gravatar, sanitize_email

def list2dict(list_data):
    return list_data[0]

def replace_keys(dictonary):
    replacements = {
        "id": "id",
        "hash": "email_hash",
        "profileUrl": "url",
        "preferredUsername": "alias",
        "thumbnailUrl": "thumb",
        "photos": "photos",
        "currentLocation": "location",
        "emails": "emails",
        "accounts": "accounts",
        "urls": "urls"}

    for i in replacements:
        if i in dictonary:
            dictonary[replacements[i]] = dictonary.pop(i)

    name1 = dictonary.get("name",{})
    if "formatted" in name1:
        dictonary["person"] = name1.pop("formatted")
    return dictonary


def get_gravatar(email):
    email = sanitize_email(email)
    g = Gravatar(email)  # must be the main email for the account
    url = g.get_profile(data_format='.json')
    content = requests.get(url).content
    try:
        json_data = json.loads(content)["entry"]
    except:
        print("requst parsing error")
        return {"message": "content", "error": "request error"}
    json_data=list2dict(json_data)
    json_data=replace_keys(json_data)
    return json_data


