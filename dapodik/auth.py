from requests import Session
from dapodik.config import BASE_URL
from dapodik.sekolah import BaseSekolah


class Auth(Session):
    _url: str = BASE_URL
    _semester_id: str = '20201'

    def login(self, username: str, password: str, rememberme=True, semester_id='20201'):
        data = {
            'username': username,
            'password': password,
            'semester_id': semester_id
        }
        if rememberme == True or rememberme == 'on':
            data['rememberme'] = 'on'
        res0 = self.get(self._url)
        if not res0.ok:
            return False
        res1 = self.post(self._url+'login', data=data)
        # handle redirect
        url = res1.url if res1.is_redirect else ''
        res2 = self.get(self._url+url)
        return 'Memuat Aplikasi' in res2.text

    def logout(self):
        res = self.get(self._url+'destauth')
        return res.status_code == 302
