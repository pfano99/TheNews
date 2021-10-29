from Apis.secrets_info import API_KEY
import requests

class TheGuardian:
    def latest_news(self,):
        url='https://content.guardianapis.com/search?api-key={}&show-fields=thumbnail'.format(API_KEY)
        
        return self._make_request(url)
        
    def search_by_topic(self, topic:str):

        query_strings = topic.split(' ')
        url=None
        query = ''
        if len(query_strings) == 1:
            query=query_strings[0]
            url = 'https://content.guardianapis.com/search?q={}&api-key={}&show-fields=thumbnail'.format(query, API_KEY)

        else:
            for index, string in enumerate(query_strings):
                if index != len(query_strings)-1:
                    query += string + '%20'
                else:
                    query += string

            url = 'https://content.guardianapis.com/search?q={}&api-key={}&show-fields=thumbnail'.format(query, API_KEY)

        return self._make_request(url)


    def _make_request(self, url):
        re = requests.get(url)
        if re.status_code == 200:
            return re.json()
        else:
            return None


# tg = TheGuardian()
# # print(tg.latest_news())
# print(tg.search_by_topic('south'))
