import requests

class hotsapi:
    def __init__(self):
        self.status_code = 503
        return

    def return_json(self, r):
        self.status_code = r.status_code
        if r.status_code == 200:
            return r.json()
        else:
            return None

    def get_replay_list(self, min_id = None, existing = False, with_players = False):
        payload = {'min_id': min_id, 'existing': existing, 'with_players': with_players}
        r = requests.get("https://hotsapi.net/api/v1/replays", params = payload)
        return self.return_json(r)

    def upload_replay(self, file):
        file = {"file": open(file, "rb")}
        r = requests.post("https://hotsapi.net/api/v1/replays", files = file)
        return self.return_json(r)

    def get_parsed_replay_list(self, min_parsed_id = None, with_players = False):
        payload = {'min_parsed_id': min_parsed_id, 'with_players': with_players}
        r = requests.get("https://hotsapi.net/api/v1/replays/parsed", params = payload)
        return self.return_json(r)
    
    def get_replay(self, id):
        r = requests.get("https://hotsapi.net/api/v1/replays/" + str(id))
        return self.return_json(r)

    def get_hero_list(self):
        r = requests.get("https://hotsapi.net/api/v1/heroes")
        return self.return_json(r)

    def get_hero(self, hero):
        r = requests.get("https://hotsapi.net/api/v1/heroes/" + str(hero))
        return self.return_json(r)

    def get_hero_ability(self, hero, hotkey):
        r = requests.get("https://hotsapi.net/api/v1/heroes/" + str(hero) + "/abilities/" + str(hotkey))
        return self.return_json(r)
    
    def get_talent(self, talent):
        r = requests.get("https://hotsapi.net/api/v1/talents/" + str(talent))
        return self.return_json(r)

    def get_map_list(self):
        r = requests.get("https://hotsapi.net/api/v1/maps")
        return self.return_json(r)

    def get_map(self, map):
        r = requests.get("https://hotsapi.net/api/v1/maps/" + str(map))
