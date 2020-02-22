import requests
from pyquery import PyQuery
import re


def scrape(url):
    HEADERS = {
        'User-Agent'		: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
        'Accept'			: 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding'	: 'gzip,deflate,sdch',
        'Accept-Language'	: 'zh-CN,zh;q=0.8'
    }

    r = requests.get(url, headers=HEADERS)
    assert r.status_code == 200

    data = PyQuery(r.content)
    items = data('div.Box-row')
    items = items.map(lambda i, e: PyQuery(e).outerHtml())

    links = data('a.btn.btn-outline.BtnGroup-item')
    links = dict(links.map(lambda i, e: (PyQuery(e).text(),PyQuery(e).attr("href"))))

    return (items, links)

path = 'https://github.com/react-spring/react-use-gesture/network/dependents'
filename = path.split('/')[4] + '__' + path.split('/')[-1].replace('dependents?dependent_type=', '') + '.html'
items, links = scrape(path)
page_no = 0
data = []

while 'Next' in links.keys():
    print (page_no, ' ---> ', path)
    data.append('\n'.join(items))
    path = links['Next']
    items, links = scrape(path)
    page_no = page_no + 1

data = '\n'.join(data)
data = PyQuery(data)
items = data('div.Box-row')
items = items.map(lambda i, e: PyQuery(e).remove('small'))
items = list(items.map(lambda i, e: PyQuery(e).text()))
items = [re.split('\n| / ', item) for item in items]
items = [i for i in items if len(i)==4]
[i.insert(0, 'https://github.com/'+i[0]+'/'+i[1]) for i in items]

htmlHead = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script src="https://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js"></script>
  <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.20/css/jquery.dataTables.css">
  <script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.10.20/js/jquery.dataTables.js"></script>
  
  <title>Document</title>
  <script>
    $(document).ready( function () {
        $('#table_id').DataTable();
    } );
  </script>
</head>
<body>
  <table id="table_id" class="display">
'''

htmlButton = '''
</table> 
</body>
</html>
'''

title = ['Link', 'User', 'repository', 'star', 'fork']
thead = '<thead>' + '\n'.join(map(lambda i: "<th>{}</th>".format(i),title)) + '</thead>'
tbody = []
for item in items:
    item[0] = '<a href="{}">Link</a>'.format(item[0])
    td = '<tr>' + '\n'.join(map(lambda i: "<td>{}</td>".format(i),item)) + '</tr>'
    tbody.append(td)
tbody = '<tbody>' + '\n'.join(tbody) + '</tbody>'
html = htmlHead + thead + tbody + htmlButton
with open(filename, 'w', encoding='utf-8') as f:
    f.write(html)
