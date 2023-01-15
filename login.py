

def login(self):
    client = login.Client()
    jingdong = client.jingdong(reload_history=True)
    infos_return, session = jingdong.login(self.username, '微信公众号: Charles的皮卡丘', 'scanqr')
    return session