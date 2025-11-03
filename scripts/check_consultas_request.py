import urllib.request
import urllib.error

url = 'http://127.0.0.1:5000/consultas'
try:
    with urllib.request.urlopen(url, timeout=5) as r:
        code = r.getcode()
        body = r.read(800).decode('utf-8', errors='replace')
        print('STATUS', code)
        print('--- BODY START ---')
        print(body)
        print('--- BODY END ---')
except urllib.error.HTTPError as e:
    print('HTTPError', e.code)
    try:
        print(e.read().decode('utf-8', errors='replace'))
    except Exception:
        pass
except Exception as e:
    print('ERROR', e)