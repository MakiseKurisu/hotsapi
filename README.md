# hotsapi
A simple Python package to interact with [hotsapi](http://hotsapi.net)

## Requirement
[Python 3](https://www.python.org/downloads/) with [requests](http://docs.python-requests.org/en/master/user/install/) package

## Docs
Check [official site](http://hotsapi.net/docs) for latest API usage.

Functions all return json when success, or None for failure. Check hotsapi.status_code for the http status code of last request.

hotsapi.get_hero_list() and hotsapi.get_map_list() use [HotsLogs](https://www.hotslogs.com/info/api) data for now.

    class hotsapi:
        status_code
        get_replay_list(min_id = None, existing = False, with_players = False)
        upload_replay(file)
	get_parsed_replay_list(min_parsed_id = None, with_players = False)
        get_replay(id)
        get_hero_list()
        get_hero(hero)
        get_hero_ability(hero, hotkey)
	get_talent(talent)
        get_map_list()
        get_map(map)

## Example
    def test():
        h = hotsapi()
        try:
            r = h.get_replay_list()
            r = h.get_replay(r[0]["id"])
            print(r)
        except TypeError:
            print("Error when request data, last error code:" + str(h.status_code))
