# Unitymedia Invoice Downloader
## Introduction
This scripts allows business customers of the German cable TV/internet provider Unitymedia to automatically download their invoices in PDF format as automatic PDF delivery via email is not supported by Unitymedia for busines customers. This means you will still have to receive your regular paper invoice in the mail, but you will also have the PDF version (clearly labelled as a duplicate by Unitymedia) in a folder of your choosing.

## Usage
Place a file called login.txt containing your login credentials into the same directory as the script as follows:

USERNAME  
PASSWORD

Then the script will automatically read the login credentials from the file and use the python requests module for making the HTTP requests neccessary to download the latest invoice and save it in a file called YYYY-MM.pdf

## Caution

This script could break anytime as it is simply scraping the website of the customer support center.

