# UploadFinder

This project uses Python3 to crawl through TOR and Normal websites searching for Links to UploadHosts such as mediafire or solidfiles.
It uses the TorCrawl Project developed by James04gr which can be found (here)[https://github.com/james04gr/TorCrawl.py]

## Setup
1. Install Python3 and Pip3
2. Install Tor
3. Navigate to the TorCrawl.py folder and execute `pip3 install -r requirements.txt`
4. Start the Tor Service with `sudo service tor start`

## Usage
The `findUploads.py` generates a `uploadLinks.txt` file which will contain all found links.
To start the programm, use command arguments to set it the url to crawl and other settings.

| Argument  | Description | Example |
|-----------|-------------|---------|
| -u | Sets the URL to crawl from. Can also end on *.onion | `-u https://github.com` |
| -d | Sets the depth to crawl (the clicks to take)        | `-d 2`                  |
| -p | Set the time to wait between each click in seconds  | `-p 2`                  |

## Adding new Uploads
For temporal use you can update the `knownUploadHosts.txt` with additional links.
Please consider creating a PR in this repository to update the list globaly aswell.
