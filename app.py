def get_greeting(name: str) -> str:
	cleaned_name = name.strip() if name else "Guest"
	return f'hi "{name}"'

if __name__ == "__main__":
	user_name = input("Enter your name - ")
	print(get_greeting(user_name))
