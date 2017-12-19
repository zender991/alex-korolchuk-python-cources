from bs4 import BeautifulSoup
import requests
import csv
import json
import os
import xlsxwriter


try:
    directory = ("/python-cources/HT_8/reports/1")  # set path to reports directory
    if not os.path.exists(directory):
        os.makedirs(directory)  # create directory if it doesn't exist
except Exception as e:
    print(e)


def find_full_info():

    next_page_url = ''
    has_next = True     # value by deafult for loop start
    while has_next:     # check flag
        url = "http://quotes.toscrape.com" + next_page_url      # add to initial url part for the next page
        page = requests.get(url)                                # get data from url
        soup = BeautifulSoup(page.content, 'html5lib')          # transfer data to bs
        result = []

        for a in soup.find_all("div", {"itemtype": "http://schema.org/CreativeWork"}):  # find all blocks with info
            quote = a.contents[1].text                          # store quote text

            author_name = a.contents[3].find("small", {"itemprop":"author"}).text   # store author name
            author_url = a.contents[3].find("a").get("href")            # get href value from a tag
            author_id = author_url.split("/")[-1].lower()               # create id for author
            author_full_url = url + author_url                          # create full url for author page

            author_details = requests.get(author_full_url)              # get info for external page
            author_soup = BeautifulSoup(author_details.content, 'html5lib')     # transfer data to bs

            for item in author_soup.find_all("div", {"class": "author-details"}):   # find all blovks with info
                author_born_date = item.contents[3].find("span", {"class": "author-born-date"}).text    # store data
                author_location = item.contents[3].find("span", {"class": "author-born-location"}).text
                author_description = item.find("div", {"class": "author-description"}).text

            dict = {"text": quote[1:-1]}    # write text without quotemarks into dictionary
            dict["author"] = {              # write author details into dictionary
                "url": author_full_url,
                "author-title": author_name,
                "born_date": author_born_date,
                "born_place": author_location[3:],  # skip first 3 empty chars
                "author_description": author_description[:100].lstrip(),  # write first 100 chars
                "author_id": author_id
            }

            tags_list = []
            for tag in a.contents[5].find_all("a", {"class": "tag"}):   # find all blocks with tag info
                tags_list.append({                                      # write tag info into a dictionary
                    "tag_name": tag.text,
                    "tag_url": "http://quotes.toscrape.com" + tag.get("href")
                })

            dict["tags"] = tags_list

            result.append(dict)                         # collect all info and add to list
        write_to_csv_full_info(result)                  # write to 4 files after parse each page
        write_to_json_file(result, "full_results")
        write_to_txt_file(result, "full_results")
        write_to_xls_full_info(result)

        try:
            next_page_url = soup.select('ul.pager')[0].select('li.next a')[0].get('href')   # find next page url
        except:
            has_next = False                        # end loop if hasn't next page url


def find_all_authors():
    next_page_url = ''
    has_next = True         # value by deafult for loop start
    authors_list = []
    while has_next:         # check flag
        url = "http://quotes.toscrape.com" + next_page_url      # add to initial url part for the next page
        page = requests.get(url)                                # get data from url
        soup = BeautifulSoup(page.content, 'html5lib')          # transfer data to bs


        for i in soup.find_all("div", {"itemtype": "http://schema.org/CreativeWork"}):  # find all blocks with info
            result = []
            author_name = i.contents[3].find("small", {"itemprop": "author"}).text      # find author block
            if author_name not in authors_list:                     # check if author already in a list
                author_url = i.contents[3].find("a").get("href")    # if no, store info about this author
                author_full_url = url + author_url

                author_details = requests.get(author_full_url)      # get data from external page
                author_soup = BeautifulSoup(author_details.content, 'html5lib')     # tranfer data to bs

                for item in author_soup.find_all("div", {"class": "author-details"}):   # store author info
                    author_born_date = item.contents[3].find("span", {"class": "author-born-date"}).text
                    author_location = item.contents[3].find("span", {"class": "author-born-location"}).text
                    author_description = item.find("div", {"class": "author-description"}).text

                dict = {}
                dict["author"] = {      # write author info into a dictionary
                    "url": author_full_url,
                    "author-title": author_name,
                    "born_date": author_born_date,
                    "born_place": author_location[3:],
                    "author_description": author_description[:100].lstrip()
                }
                authors_list.append(author_name)    # add author to unique authors list
                result.append(dict)                 # add dictionary to a result list
                write_to_json_file(result, "authors_details")   # write to 4 files after parse each page
                write_to_txt_file(result, "authors_details")
                write_to_csv_all_authors(result)
                write_to_xls_all_authors(result)
            else:
                pass                                            # skip  iteration if author already in a list

        try:
            next_page_url = soup.select('ul.pager')[0].select('li.next a')[0].get('href')   # find next page url
        except:
            has_next = False                # finish loop if page hasn't next page url


def find_all_tags():
    next_page_url = ''
    has_next = True                          # value by deafult for loop start
    tags_list = []

    while has_next:                          # check flag
        url = "http://quotes.toscrape.com" + next_page_url      # add to initial url part for the next page
        page = requests.get(url)                                # get data from url
        soup = BeautifulSoup(page.content, 'html5lib')          # transfer data to bs

        for item in soup.find_all("div", {"class": "tags"}):    # find all block with tags
            tags = item.find_all("a", {"class": "tag"})         # find all tags inside each block
            for tag in tags:
                if tag.text not in tags_list:
                    tags_list.append(tag.text)                  # write unique tags in a list
                else:
                    pass

            try:
                next_page_url = soup.select('ul.pager')[0].select('li.next a')[0].get('href')
            except:
                has_next = False                                # skip  iteration if author already in a list

    write_to_json_file(tags_list, "all_tags")                   # write to 4 files after parse each page
    write_to_txt_file(tags_list, "all_tags")
    write_tags_to_xls(tags_list)
    write_tags_to_csv(tags_list)


def find_author(*search_queries):                               # func can obtain multiple value
   found_authors_list = []
   for query in search_queries:                                 # select each search query
      for i in read_from_json_file():                           # read each line in json file
          for item in i:
              current_author = item['author']['author_id']      # find author in each record inside current item
              if current_author == query:                       # compare found author with search query
                  found_author = {                              # write data about searched author
                      "author_name": item['author']['author-title'],
                      "author_url": item['author']['url'],
                      "author_born_date": item['author']['born_date'],
                      "author_born_place": item['author']['born_place'],
                      "author_description": item['author']['author_description']
                  }

          found_authors_list.append(found_author)               # add to list info about searched authors
          break                                                 # don't need to continue loop if author found

   return found_authors_list


def read_from_json_file():
    data = []
    with open('reports/full_results.json') as f:                # read data from json file according to it format
        for line in f:
            data.append(json.loads(line))

    return data

# ---- For full info ----------

def write_to_csv_full_info(result):
    csv_file = open('reports/1/full_results.csv', 'a')          # add ability to write to the file end
    csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)    # initiate writer

    for i in result:
        csv_writer.writerow("##")                               # add separator for records
        quote_csv = "Quote", i["text"]
        csv_writer.writerow(quote_csv)                          # write each value to the columns. Below the same
        csv_writer.writerow(["Author"])
        author_url_csv = "", "Author url", i["author"]["url"]
        csv_writer.writerow(author_url_csv)
        author_title_csv = "", "Author name", i["author"]["author-title"]
        csv_writer.writerow(author_title_csv)
        author_born_csv = "", "Author birth date", i["author"]["born_date"]
        csv_writer.writerow(author_born_csv)
        author_born_place_csv = "", "Author birth place", i["author"]["born_place"]
        csv_writer.writerow(author_born_place_csv)
        author_description_csv = "", "Author description", i["author"]["author_description"]
        csv_writer.writerow(author_description_csv)
        author_id_csv = "", "Author id", i["author"]["author_id"]
        csv_writer.writerow(author_id_csv)
        tags_csv = "Tags", i["tags"]
        csv_writer.writerow(tags_csv)
        csv_writer.writerow("")                                 # add empty string


def write_to_xls_full_info(result):
    workbook = xlsxwriter.Workbook('reports/1/full_results.xls')
    worksheet = workbook.add_worksheet()                            # initiate worksheet

    row = 0
    col = 0
    for i in result:
        worksheet.write(row, col, "##")                             # add separator for records
        row += 1                                                    # increase row number
        worksheet.write(row, col, "Quote")
        worksheet.write(row, col + 1, i["text"])                    # write each value to the columns. Below the same
        row += 1
        worksheet.write(row, col, "Author")
        row += 1
        worksheet.write(row, col + 1, "Author url")
        worksheet.write(row, col + 2, i["author"]["url"])
        row += 1
        worksheet.write(row, col + 1, "Author name")
        worksheet.write(row, col + 2, i["author"]["author-title"])
        row += 1
        worksheet.write(row, col + 1, "Author birth date")
        worksheet.write(row, col + 2, i["author"]["born_date"])
        row += 1
        worksheet.write(row, col + 1, "Author birth place")
        worksheet.write(row, col + 2, i["author"]["born_place"])
        row += 1
        worksheet.write(row, col + 1, "Author description")
        worksheet.write(row, col + 2, i["author"]["author_description"])
        row += 1
        worksheet.write(row, col, "")                               # add empty string
        row += 1

# ---- End for full info ---------

# ----- For all authors ----------

def write_to_csv_all_authors(result):
    csv_file = open('reports/1/authors_details.csv', 'a')       # add ability to write to the file end
    csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)    # initiate writer

    for i in result:
        csv_writer.writerow("##")                               # add separator for records
        author_url_csv = "Author url", i["author"]["url"]       # write each value to the columns. Below the same
        csv_writer.writerow(author_url_csv)
        author_title_csv = "Author name", i["author"]["author-title"]
        csv_writer.writerow(author_title_csv)
        author_born_csv = "Author birth date", i["author"]["born_date"]
        csv_writer.writerow(author_born_csv)
        author_born_place_csv = "Author birth place", i["author"]["born_place"]
        csv_writer.writerow(author_born_place_csv)
        author_description_csv = "Author description", i["author"]["author_description"]
        csv_writer.writerow(author_description_csv)
        csv_writer.writerow("")


def write_to_xls_all_authors(result):
    workbook = xlsxwriter.Workbook('reports/1/authors_details.xls')
    worksheet = workbook.add_worksheet()                                # initiate worksheet

    row = 0
    col = 0
    for i in result:
        worksheet.write(row, col, "##")                                 # add separator for records
        row += 1                                                        # increase row number
        worksheet.write(row, col, "Author url")                       # write each value to the columns. Below the same
        worksheet.write(row, col + 1, i["author"]["url"])
        row += 1
        worksheet.write(row, col, "Author name")
        worksheet.write(row, col + 1, i["author"]["author-title"])
        row += 1
        worksheet.write(row, col, "Author birth date")
        worksheet.write(row, col + 1, i["author"]["born_date"])
        row += 1
        worksheet.write(row, col, "Author birth place")
        worksheet.write(row, col + 1, i["author"]["born_place"])
        row += 1
        worksheet.write(row, col, "Author description")
        worksheet.write(row, col + 1, i["author"]["author_description"])
        row += 1
        worksheet.write(row, col, "")
        row += 1

# ------- End for all authors -------

# ------- For all tags -------------

def write_tags_to_csv(result):
    csv_file = open('reports/1/all_tags.csv', 'a')              # add ability to write to the file end
    csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)    # initiate writer

    for i in result:
        csv_writer.writerow([i])                                # write each tag to a file


def write_tags_to_xls(result):
    workbook = xlsxwriter.Workbook('reports/1/all_tags.xls')
    worksheet = workbook.add_worksheet()                        # initiate worksheet

    row = 0
    col = 0

    for i in result:
        worksheet.write(row, col, i)                            # write each tag to a file
        row += 1                                                # increase row number

# ------- End for all tags ---------

def write_to_json_file(result, file_name):
    with open('reports/1/%s.json' %file_name, 'a') as fp:   # add ability to write to the file end
        json.dump(result, fp)                               # write object to a file
        fp.write('\n')                                      # write next value from the new line


def write_to_txt_file(result, file_name):
    with open('reports/1/%s.txt' % file_name, 'a') as fp:   # add ability to write to the file end
        fp.write(str(result))                               # write object to a file
        fp.write('\n')                                      # write next value from the new line



# find_full_info()
# find_all_authors()
# find_all_tags()

print(find_author("j-k-rowling", "albert-einstein"))
