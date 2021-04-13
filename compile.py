import json
import re

def page_from(content, template):
    output = template
    for key, value in content.items():
        if type(value) is dict:
            item_template = value["template"]
            result_list = []
            if value["items"]:
                # value["items"].reverse()
                for item in value["items"]:
                    result_list.append(
                        page_from(item, item_template)
                    )
            output = output.replace("{{" + key.upper() + "}}", "\n".join(result_list))
        else:
            output = output.replace("{{" + key.upper() + "}}", value)
    return output

def main():
    with open("./template.html") as page_template_file:
        page_template = page_template_file.read()
        with open("./main.json") as content_file:
            content = json.load(content_file)
            for page in content:
                new_page = page_from(page, page_template)
                with open("./" + page["page"] + ".html", "w") as output_file:
                    output_file.write(new_page)

main()