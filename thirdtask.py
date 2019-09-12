import requests


class Car:
	def __init__(self,name,price,currency):
		self.name = name.lower().strip()
		self.price = price.strip()
		self.currency = currency.upper().strip()
	
		
	def get_usd(self):
		if self.currency == 'USD':
			return self.price

		url = 'https://api.exchangeratesapi.io/latest?base=USD'
		response = requests.get(url).json()
		exchange_value = response['rates'][self.currency]
		try:
			usd = int(self.price) / exchange_value
			return str(usd) + ' USD'
		except:
			return 'invalid input, try again'



def ask_user_car_name():
	car_name = input('Enter your car\'s name: ')
	return car_name


def create_file():
	try:
		file = open('carsfile.txt')
		file.close()
	except:
		new_file = open('carsfile.txt','w')
		new_file.close()
	

def find_car(car_name):
	create_file()
	with open('carsfile.txt') as file:
		try:
			all_cars = file.readlines()#[]
			for car in all_cars:
				name = car.split(',')[0]

				if name == car_name:
					price = car.split(',')[1]
					currency = car.split(',')[2]
					user_car = Car(name,price,currency)

			return user_car
		except:
			return None
	


def write_in_file(car):
	with open('carsfile.txt','a') as file:
		file.write(car.name +','+ str(car.price)+ ',' + car.currency + '\n')

def validation_check(user_car):
	if user_car.currency in ['USD','EUR','GBP']:
		try:
			int(user_car.price)
			return True
		except:
			return False


def main():
	car_name = ask_user_car_name()
	user_car = find_car(car_name)
	if user_car:
		print(user_car.get_usd())
	else:
		print('Car wasn\'t found,please enter price and currency for your car')
		car_price = input('Enter price: ')
		car_currency = input('Enter currency(USD,EUR,GBP)')
		new_car = Car(car_name,car_price,car_currency)
		if validation_check(new_car):
			write_in_file(new_car)
			print('\n')
			print('car is successfully saved!')
			print('\n')
		else:
			print('\n')
			print('Invalid input')
			print('\n')
			main()



if __name__ == '__main__':
	main()