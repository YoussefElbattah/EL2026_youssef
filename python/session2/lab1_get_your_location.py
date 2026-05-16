"""Write a Python program to get info about your location."""

import requests

def get_info_location():
    """Write your solution here. Don't forget to return the result at the end."""
    r = requests.get("https://ipinfo.io/92.184.116.198/geo", timeout=100)
    loc_info:list = r.json()
    return loc_info

if __name__ == "__main__":
    location_info = get_info_location()
    assert "ip" in location_info, "Test case failed"
    assert "city" in location_info, "Test case failed"
    assert "region" in location_info, "Test case failed"
    assert "country" in location_info, "Test case failed"
    assert "loc" in location_info, "Test case failed"
    assert "org" in location_info, "Test case failed"
