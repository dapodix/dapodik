from requests import Session

BASE_URL = "http://localhost:5774/"


class Dapodik(Session):
    def __init__(self, url=BASE_URL, semester_id='20201'):
        self._semester_id = semester_id
        self._url = url
        self.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'
        })

    def login(self, username: str, password: str, rememberme=True, semester_id='20201'):
        data = {
            'username': username,
            'password': password,
        }
        if rememberme == True or rememberme == 'on':
            data['rememberme'] = 'on'
        res1 = self.post(self._url+'login', data)
        # handle redirect
        url = res1.url if res1.is_redirect else ''
        res2 = self.get(self._url+url)
        return 'Memuat Aplikasi' in res2.text

    def logout(self):
        res = self.get(self._url+'destauth')
        return res.status_code == 302
