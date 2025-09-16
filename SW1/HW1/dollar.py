def convert_dollar(usd):
    indian = usd * 88.27
    british = usd * 0.81
    chinese = usd * 7.12
    return indian, british, chinese

while True:
    user_input = input("Enter dollar ($) (* to exit): ")

    if user_input == "*":
        print ("Bye")
        break

    print(f"\n{'Dollar ($)':<15}{'Indian (R)':<20}{'British (Pound)':<20}{'Chinese (Yuan)':<20}")
    for x in user_input.split("@"):
        usd = int(x)
        indian, british, chinese = convert_dollar(usd)
        print(f"{usd:<15}{indian:<20.2f}{british:<20.2f}{chinese:<20.2f}")



    