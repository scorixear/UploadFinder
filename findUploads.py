import os, sys, getopt

def main(argv):
  # Execute pip3 install for TorCrawl.py

  # Parse Arguments
  url = ""
  depth = ""
  wait = ""

  try:
    opts, args = getopt.getopt(argv, "u:d:p:", [])
  except getopt.GetoptError:
    print('findUploads.py -u <url> -d <depth> -p <wait_time>')
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-u':
      url = arg
    elif opt == '-d':
      depth = arg
    elif opt == '-p':
      wait = arg
  
  # clear links folder
  for f in os.listdir('Links'):
    os.remove(os.path.join('Links', f))

  # print(f'python3 ./TorCrawl.py/torcrawl.py -v -u {url} -c -f ../Links/ -d {depth} -p {wait}')
  # Execute TorCrawl.py
  os.system(f'python3 ./TorCrawl.py/torcrawl.py -v -u {url} -c -f Links -d {depth} -p {wait}')

  # filter links
  
  knownHosts = open('knownUploadHosts.txt', 'r').readlines()
  links = open('Links/links.txt', 'r').readlines()
  print(f'################### Found {len(links)} Links, filtering now ##################################')
  filteredLinks = []
  for link in links:
    found = False
    for host in knownHosts:
      if link.startswith(host):
        found = True
        break
    if found:
      filteredLinks.append(link)
  print(f'################# {len(filteredLinks)} Upload Links found ####################################')
  uploadLinks = open('uploadLinks.txt', 'w')
  uploadLinks.writelines(filteredLinks)


if __name__ == "__main__":
  main(sys.argv[1:])

