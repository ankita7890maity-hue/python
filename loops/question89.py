'''
Question 3: Write a program to check tram service status based on weather and time.
'''
def tram_status():
	weather = input("Weather (string/clear/stormy/rain): ").strip().lower()
	try:
		hour = int(input("Hour (0-23): ").strip())
	except :
		print("Invalid hour")
		return

	if weather == "snowy":
		print("service suspended")
		return

	
	if weather in ("stormy", "snowy"):
		print("Tram service suspended due to severe weather")
	elif 5 <= hour <= 23:
		print("Tram service is running")
	else:
		print("No trams - outside service hours")


if __name__ == '__main__':
	tram_status()