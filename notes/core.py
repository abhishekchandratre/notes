from notes.params import *
import argparse

def parse_and_return_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--domain", help="domain of notes;" +
            " if domain is empty then print all domains")
    parser.add_argument("-n", "--notebook", help="notebook within domain;" +
            " if notebook is empty then show all notebooks of given domain")
    parser.add_argument("-p", "--page", help="page within notebook;" +
            " if page is empty then show all pages of given notebook")
    args = parser.parse_args()
    domain = args.domain; notebook = args.notebook; page = args.page
    return (domain, notebook, page)


def handle_main():
    print ("notes path:", NOTES_PATH)
    (domain_name, notebook_name, page_name) = parse_and_return_arguments()
