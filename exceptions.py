while True:
	try:
		number = int(input("What's your favorite number?\n"))
		print(18/number)
		# break out of the loop
		break
	except ValueError:
		print("Make shure and enter a number.")
	except ZeroDivisionError:
		print("Don't pick zero")
	# general exception
	except:
		break
	# prints no matter what happens
	finally:
		print("loop complete")

