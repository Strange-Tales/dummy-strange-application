import requests

def get_quote_of_the_day():
    url = 'https://quotes.rest/qod?category=management'
    api_token = "eT1F9wcWgxIW7WSCm3GK17fDgzL1F7JG6oKo1FP0"
    headers = {'content-type': 'application/json',
	   'X-TheySaidSo-Api-Secret': format(api_token)}
    response = requests.get(url, headers=headers)
    data = response.json()
    if "contents" in data and "quotes" in data["contents"]:
        quote = data["contents"]["quotes"][0]["quote"]
        author = data["contents"]["quotes"][0]["author"]
        return f'"{quote}" - {author}'
    else:
        return "Failed to fetch a quote of the day."

if __name__ == "__main__":
    quote = get_quote_of_the_day()
    print("Quote of the Day:")
    print(quote)
