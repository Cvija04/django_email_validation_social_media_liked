import requests

class EmailChecker:
    
    def __init__(self, email):
        self.email = email
        self.data = {}
        self.check_linked("Twitter")
        self.check_linked("Instagram")
        self.check_linked("Snapchat")
        self.send_data()


    def check_linked(self, service):
        self.service = service
        s = requests.Session()
        if service == "Twitter":
            url = f"https://api.twitter.com/i/users/email_available.json?email={self.email}"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
                "Host": "api.twitter.com",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            }
            response = s.get(url, headers=headers).json()
            if response.get("valid") == False:
                self.linked()
            else:
                self.unlinked()
        elif service == "Instagram":
            url = "https://www.instagram.com/accounts/account_recovery_send_ajax/"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
                "X-CSRFToken": "missing",
            }
            data = {"email_or_username": self.email}
            response = s.post(url, headers=headers, data=data).text
            if "We sent an email to" in response or "password" in response or "sent" in response:
                self.linked()
            else:
                self.unlinked()
        elif service == "Snapchat":
            url = "https://accounts.snapchat.com/accounts/merlin/login"
            headers = {
                "Host": "accounts.snapchat.com",
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br",
                "X-XSRF-TOKEN": "missing",
                "Content-Type": "application/json",
                "Origin": "https://accounts.snapchat.com",
                "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
                "Connection": "keep-alive",
                "Referer": "https://accounts.snapchat.com/accounts/merlin/login",
            }
            cookies = {"xsrf_token": "missing"}
            data = {"email": self.email, "app": "BITMOJI_APP"}
            response = s.post(url, headers=headers, cookies=cookies, json=data).text
            if "hasSnapchat" in response:
                self.linked()
            else:
                self.unlinked()

    def linked(self):
        data = {self.service : {"email": self.email, "status": "Linked"}}
        self.data.update(data)
        
    def unlinked(self):
        data = {self.service : {"email": self.email, "status": "Unlinked"}}
        self.data.update(data)
        
        
    def send_data(self):
        print(self.data)
        return (self.data)




