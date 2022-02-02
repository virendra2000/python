lotterycode = "hello coders"
code = input("Enter Correct Character of the word",lotterycode," to win the prize")
if code == lotterycode[0].lower() or code == lotterycode[1].lower() or code == lotterycode[4].lower() or code == lotterycode[6].lower() or code == lotterycode[8].lower():
    print("congratulation and Celebration, You are Lottery Winner of the Day")
else:
    print("Oops ! Bad to Feel , You didn't win Lottery")
