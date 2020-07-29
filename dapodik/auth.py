from requests import Session
from dapodik.config import BASE_URL, SEMESTER_ID
from dapodik.sekolah import BaseSekolah


class Auth(object):
    _url: str = BASE_URL
    _semester_id: str = SEMESTER_ID
    session: Session = None

    def login(self, username: str, password: str, rememberme: bool = True, semester_id: str = SEMESTER_ID):
        data = {
            'username': username,
            'password': password,
            'semester_id': semester_id
        }
        if rememberme == True or rememberme == 'on':
            data['rememberme'] = 'on'
        res0 = self.session.get(self._url)
        if not res0.ok:
            return False
        res1 = self.session.post(self._url+'login', data=data)
        # handle redirect
        url = res1.url if res1.is_redirect else ''
        res2 = self.session.get(self._url+url)
        return 'Memuat Aplikasi' in res2.text

    def logout(self):
        res = self.session.get(self._url+'destauth')
        return res.status_code == 302
