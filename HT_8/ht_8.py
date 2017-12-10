from bs4 import BeautifulSoup
import requests
import csv
import json


def find_full_info():
    url = "http://quotes.toscrape.com/"
    page = requests.get(url)

    soup = BeautifulSoup(page.content)
    result = []
    for a in soup.find_all("div", {"itemtype": "http://schema.org/CreativeWork"}):
        quote = a.contents[1].text

        author_name = a.contents[3].find("small", {"itemprop":"author"}).text
        author_url = a.contents[3].find("a").get("href")
        author_full_url = "http://quotes.toscrape.com/" + author_url

        author_details = requests.get(author_full_url)
        author_soup = BeautifulSoup(author_details.content)

        for item in author_soup.find_all("div", {"class": "author-details"}):
            author_born_date = item.contents[3].find("span", {"class": "author-born-date"}).text
            author_location = item.contents[3].find("span", {"class": "author-born-location"}).text
            author_description = item.find("div", {"class": "author-description"}).text

        dict = {"text": quote}
        dict["author"] = {
            "url": author_full_url,
            "author-title": author_name,
            "born_date": author_born_date,
            "born_place": author_location,
            "author_description": author_description[:100].lstrip()
        }

        result.append(dict)
    return result


def find_all_authors():
    url = "http://quotes.toscrape.com/"
    page = requests.get(url)

    soup = BeautifulSoup(page.content)
    result = []
    authors_list = []

    for i in soup.find_all("div", {"itemtype": "http://schema.org/CreativeWork"}):
        author_name = i.contents[3].find("small", {"itemprop": "author"}).text
        if author_name not in authors_list:
            author_url = i.contents[3].find("a").get("href")
            author_full_url = "http://quotes.toscrape.com/" + author_url

            author_details = requests.get(author_full_url)
            author_soup = BeautifulSoup(author_details.content)

            for item in author_soup.find_all("div", {"class": "author-details"}):
                author_born_date = item.contents[3].find("span", {"class": "author-born-date"}).text
                author_location = item.contents[3].find("span", {"class": "author-born-location"}).text
                author_description = item.find("div", {"class": "author-description"}).text

            dict = {}
            dict["author"] = {
                "url": author_full_url,
                "author-title": author_name,
                "born_date": author_born_date,
                "born_place": author_location,
                "author_description": author_description[:100].lstrip()
            }
            authors_list.append(author_name)
            result.append(dict)
        else:
            pass

    return result


def find_all_tags():
    url = "http://quotes.toscrape.com/"
    page = requests.get(url)

    soup = BeautifulSoup(page.content)

    tags_list = []
    for item in soup.find_all("div", {"class": "tags"}):
        tags = item.find_all("a", {"class": "tag"})
        for tag in tags:
            if tag.text not in tags_list:
                tags_list.append(tag.text)
            else:
                pass

    return tags_list


def write_to_csv_all_authors(result):
    csv_file = open('authors_details.csv', 'w')
    csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

    counter = 1
    for i in result:
        csv_writer.writerow(["Recond %i" % counter])
        author_url_csv = "Author url", i["author"]["url"]
        csv_writer.writerow(author_url_csv)
        author_title_csv = "Author name", i["author"]["author-title"]
        csv_writer.writerow(author_title_csv)
        author_born_csv = "Author birth date", i["author"]["born_date"]
        csv_writer.writerow(author_born_csv)
        author_born_place_csv = "Author birth place", i["author"]["born_place"]
        csv_writer.writerow(author_born_place_csv)
        author_description_csv = "", "Author description", i["author"]["author_description"]
        csv_writer.writerow(author_description_csv)
        csv_writer.writerow("")

        counter += 1

def write_to_csv_full_info(result):
    csv_file = open('full_results.csv', 'w')
    csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

    counter = 1
    for i in result:
        csv_writer.writerow(["Recond %i" %counter])
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
        csv_writer.writerow("")

        counter += 1


def write_tags_to_csv(result):
    csv_file = open('all_tags.csv', 'w')
    csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

    for i in result:
        csv_writer.writerow([i])


write_to_csv_full_info(find_full_info())
write_to_csv_all_authors(find_all_authors())
write_tags_to_csv(find_all_tags())