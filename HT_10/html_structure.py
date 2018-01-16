import re

# Generate html code with titles from DB
class Parser(object):
    def generate_html_code(*args):
        with open('html_structure.html', 'r') as file:
            html_file = file.read().replace('\n', '')

        found_variables = re.findall(r"{{(.*?)}}", html_file)               # find all variables in html code

        attr_counter = 0
        for variable in found_variables:                                    # replace found variables to received *args
            html_file = re.sub(r"{{%s}}" % variable, args[attr_counter], html_file)
            attr_counter += 1

        return html_file