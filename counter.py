def main():
    
    initial_value=int(input("enter the intial value :"))
    my_counter = counter(initial_value)
    print(f"initial value : {my_counter.value}")
    
    my_counter.increment()
    print(f"increment value : {my_counter.value}")
    
    my_counter.decrement()
    print(f"decrement value : {my_counter.value}")
    
    my_counter.reset()
    print(f"reset value : {my_counter.value}")

class counter:
    def __init__(self,initial_value):
        self.value = initial_value
    def increment(self):
        self.value += 2 
    def decrement(self):
        self.value -= 1
    def reset(self):
        self.value = 0

if __name__ == '__main__':
    main()       
              

