from bs4 import BeautifulSoup
import requests
import csv
import json
import os
import xlsxwriter


try:
    directory = ("/python-cources/HT_8/reports")  # set path to reports directory
    if not os.path.exists(directory):
        os.makedirs(directory)  # create directory if it doesn't exist
except Exception as e:
    print(e)


def find_full_info():

    next_page_url = ''
    has_next = True
    while has_next:
        url = "http://quotes.toscrape.com" + next_page_url
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html5lib')
        result = []

        for a in soup.find_all("div", {"itemtype": "http://schema.org/CreativeWork"}):
            quote = a.contents[1].text

            author_name = a.contents[3].find("small", {"itemprop":"author"}).text
            author_url = a.contents[3].find("a").get("href")
            author_id = author_url.split("/")[-1].lower()
            author_full_url = url + author_url

            author_details = requests.get(author_full_url)
            author_soup = BeautifulSoup(author_details.content, 'html5lib')

            for item in author_soup.find_all("div", {"class": "author-details"}):
                author_born_date = item.contents[3].find("span", {"class": "author-born-date"}).text
                author_location = item.contents[3].find("span", {"class": "author-born-location"}).text
                author_description = item.find("div", {"class": "author-description"}).text

            dict = {"text": quote[1:-1]}
            dict["author"] = {
                "url": author_full_url,
                "author-title": author_name,
                "born_date": author_born_date,
                "born_place": author_location[3:],
                "author_description": author_description[:100].lstrip(),
                "author_id": author_id
            }

            tags_list = []
            for tag in a.contents[5].find_all("a", {"class": "tag"}):
                tags_list.append({
                    "tag_name": tag.text,
                    "tag_url": "http://quotes.toscrape.com" + tag.get("href")
                })

            dict["tags"] = tags_list

            result.append(dict)
        write_to_csv_full_info(result)
        write_to_json_file(result, "full_results")
        write_to_txt_file(result, "full_results")
        write_to_xls_full_info(result)

        try:
            next_page_url = soup.select('ul.pager')[0].select('li.next a')[0].get('href')
        except:
            has_next = False


def find_all_authors():
    next_page_url = ''
    has_next = True
    authors_list = []
    while has_next:
        url = "http://quotes.toscrape.com" + next_page_url
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html5lib')


        for i in soup.find_all("div", {"itemtype": "http://schema.org/CreativeWork"}):
            result = []
            author_name = i.contents[3].find("small", {"itemprop": "author"}).text
            if author_name not in authors_list:
                author_url = i.contents[3].find("a").get("href")
                author_full_url = url + author_url

                author_details = requests.get(author_full_url)
                author_soup = BeautifulSoup(author_details.content, 'html5lib')

                for item in author_soup.find_all("div", {"class": "author-details"}):
                    author_born_date = item.contents[3].find("span", {"class": "author-born-date"}).text
                    author_location = item.contents[3].find("span", {"class": "author-born-location"}).text
                    author_description = item.find("div", {"class": "author-description"}).text

                dict = {}
                dict["author"] = {
                    "url": author_full_url,
                    "author-title": author_name,
                    "born_date": author_born_date,
                    "born_place": author_location[3:],
                    "author_description": author_description[:100].lstrip()
                }
                authors_list.append(author_name)
                result.append(dict)
                write_to_json_file(result, "authors_details")
                write_to_txt_file(result, "authors_details")
                write_to_csv_all_authors(result)
                write_to_xls_all_authors(result)
            else:
                pass

        try:
            next_page_url = soup.select('ul.pager')[0].select('li.next a')[0].get('href')
        except:
            has_next = False


def find_all_tags():
    next_page_url = ''
    has_next = True
    tags_list = []

    while has_next:
        url = "http://quotes.toscrape.com" + next_page_url
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html5lib')

        for item in soup.find_all("div", {"class": "tags"}):
            tags = item.find_all("a", {"class": "tag"})
            for tag in tags:
                if tag.text not in tags_list:
                    tags_list.append(tag.text)

                else:
                    pass

            try:
                next_page_url = soup.select('ul.pager')[0].select('li.next a')[0].get('href')
            except:
                has_next = False

    write_to_json_file(tags_list, "all_tags")
    write_to_txt_file(tags_list, "all_tags")
    write_tags_to_xls(tags_list)
    write_tags_to_csv(tags_list)


def find_author(json_object, *search_queries):
   found_authors_list = []
   for query in search_queries:
      for i in json_object:
         current_author = i['author']['author_id']
         if current_author == query:
            found_author = {
               "author_name": i['author']['author-title'],
               "author_url": i['author']['url'],
               "author_born_date": i['author']['born_date'],
               "author_born_place": i['author']['born_place'],
               "author_description": i['author']['author_description']
            }

      found_authors_list.append(found_author)

   return found_authors_list

# ---- For full info ----------

def write_to_csv_full_info(result):
    csv_file = open('reports/full_results.csv', 'a')
    csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

    for i in result:
        csv_writer.writerow("##")
        quote_csv = "Quote", i["text"]
        csv_writer.writerow(quote_csv)
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
        csv_writer.writerow("")


def write_to_xls_full_info(result):
    workbook = xlsxwriter.Workbook('reports/full_results.xls')
    worksheet = workbook.add_worksheet()

    row = 0
    col = 0
    for i in result:
        worksheet.write(row, col, "##")
        row += 1
        worksheet.write(row, col, "Quote")
        worksheet.write(row, col + 1, i["text"])
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
        worksheet.write(row, col, "")
        row += 1

# ---- End for full info ---------

# ----- For all authors ----------

def write_to_csv_all_authors(result):
    csv_file = open('reports/authors_details.csv', 'a')
    csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

    for i in result:
        csv_writer.writerow("##")
        author_url_csv = "Author url", i["author"]["url"]
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
    workbook = xlsxwriter.Workbook('reports/authors_details.xls')
    worksheet = workbook.add_worksheet()

    row = 0
    col = 0
    for i in result:
        worksheet.write(row, col, "##")
        row += 1
        worksheet.write(row, col, "Author url")
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
    csv_file = open('reports/all_tags.csv', 'a')
    csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

    for i in result:
        csv_writer.writerow([i])


def write_tags_to_xls(result):
    workbook = xlsxwriter.Workbook('reports/all_tags.xls')
    worksheet = workbook.add_worksheet()

    row = 0
    col = 0

    for i in result:
        worksheet.write(row, col, i)
        row += 1

# ------- End for all tags ---------

def write_to_json_file(result, file_name):
    with open('reports/%s.json' %file_name, 'a') as fp:
        json.dump(result, fp)

def write_to_txt_file(result, file_name):
    with open('reports/%s.txt' % file_name, 'a') as fp:
        fp.write(str(result))



#find_full_info()
#find_all_authors()
find_all_tags()

with open('reports/test_results.json') as data_file:
    data = json.load(data_file)

#print(find_author(data, "j-k-rowling", "albert-einstein"))
