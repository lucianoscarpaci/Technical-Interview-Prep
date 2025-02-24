# artist is a string
# festival_schedule is a dictionary
def get_artist_info(artist, festival_schedule):
     # map each artist names to dictionaries containing their day, time, and stage
    artist_info = festival_schedule.get(artist)
    if artist_info == None:
        error_dict = {'message': 'Artist not found'}
        return error_dict
    return artist_info    

festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawerence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule))
print(get_artist_info("Taylor Swift", festival_schedule))