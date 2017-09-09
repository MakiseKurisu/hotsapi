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
        get_replay_list(start_date = None, end_date = None, game_map = None, game_type = None, player = None, min_id = None)
        get_replay(id)
        upload_replay(file)
        get_hero_list()
        get_map_list()

## Example
    def test():
        h = hotsapi()
        try:
            r = h.get_replay_list()
            r = h.get_replay(r[0]["id"])
            print(r)
        except TypeError:
            print("Error when request data, last error code:" + str(h.status_code))
