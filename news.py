import requests
class newsDaily:
    base_url = "http:newsapi.org/v2/everything"
    api_key = "843212a55bfa47623e4490069ebee18c"

    def __init__(self, interest, from_data, to_data, language = 'en'):
        self.interest = interest
        self.from_data = from_data
        self.to_data = to_data
        self.language = language

    def get(self):
        url = f"{self.base_url}"\
              f"qInTitle={self.interest}&"\
              f"to={self.from_date}"\
              f"to={self.to_date}"\
              f"language={self.language}"\
              f"apikey{self.api_key}"
        response = requests.get(url)
        content = response.json()
        articles = content['articles']

        email_body = ''
        for a in articles:
            email_body = email_body + a['title']+"\n"+a['url']+"\n\n"

        return email_body
if __name__ == '__main__':
    dailyNews = dailyNews(interest={interest}, from_date={from_date}, to_date={to_date}, language={language})
    print(dailyNews.get())

            

