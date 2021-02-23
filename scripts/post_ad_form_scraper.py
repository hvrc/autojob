from _imports import *

def get_form(session, url, id=None):
    res = session.get(url)
    # res.html.render()
    print("From get form")
    print(res.text)
    soup = BeautifulSoup(res.html.html, "html.parser")
    form = soup.find("form") if not id else soup.find("form", {"id": id})
    #print(form.text)

    return form

def get_form_details(form):
    inputs, details = [], {}
    print("From get form details")
    print(str(form))
    action, method = form.attrs.get("action").lower(), form.attrs.get("method", "get").lower()

    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        input_value = input_tag.attrs.get("value", "")
        inputs.append({"type": input_type, "name": input_name, "value": input_value})

    details["action"], details["method"], details["inputs"] = action, method, inputs
    print(details)
    
    return details
