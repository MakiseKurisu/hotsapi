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

    def get_replay_list(self, start_date = None, end_date = None, game_map = None, game_type = None, player = None, min_id = None):
        payload = {'start_date': start_date, 'end_date': end_date, 'game_map': game_map, 'game_type': game_type, 'player': player, 'min_id': min_id}
        r = requests.get("https://hotsapi.net/api/v1/replays/", params = payload)
        return self.return_json(r)
    
    def get_paged_replay_list(self, page = None, start_date = None, end_date = None, game_map = None, game_type = None, player = None, min_id = None):
        payload = {'page': page, 'start_date': start_date, 'end_date': end_date, 'game_map': game_map, 'game_type': game_type, 'player': player, 'min_id': min_id}
        r = requests.get("https://hotsapi.net/api/v1/replays/paged", params = payload)
        return self.return_json(r)

    def get_replay(self, id):
        r = requests.get("https://hotsapi.net/api/v1/replays/" + str(id))
        return self.return_json(r)

    def upload_replay(self, file):
        file = {"file": open(file, "rb")}
        r = requests.post("https://hotsapi.net/api/v1/replays/", files = file)
        return self.return_json(r)

    def get_hero_list(self):
        r = requests.get("https://hotsapi.net/api/v1/heroes/translations")
        return self.return_json(r)

    def get_map_list(self):
        r = requests.get("https://hotsapi.net/api/v1/maps/translations")
        return self.return_json(r)