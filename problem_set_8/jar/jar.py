class Jar:

	def __init__(self, capacity=12):
		self.capacity = capacity
		self.cookies_now = 0
		
	def __str__(self):
		return "".join("🍪" for _ in range(self.cookies_now))	


	def deposit(self, n):
		if n + self.cookies_now > self.capacity:
			raise ValueError("Jar cant take this much cookies")
		self.cookies_now += n

	def withdraw(self, n):
		if self.cookies_now - n < 0:
			raise ValueError("Not enough cookies")
		self.cookies_now -= n

	@property
	def capacity(self):
		return self._capacity
	
	@capacity.setter
	def capacity(self, value):
		if value >= 0:
			self._capacity = value
		else:
			raise ValueError("Capacity must be a non-negative value")

	@property
	def size(self):
		return self.cookies_now
	
	@size.setter
	def size(self):
		return self.cookies_now
