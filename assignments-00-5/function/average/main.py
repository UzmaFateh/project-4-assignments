# Write a function that takes two numbers and finds the average between the two.

def average(num1, num2):
    return (num1 + num2) / 2

def main():
    avg_1 = average(20, 30)
    avg_2 = average(45, 67)
    
    final = average(avg_1, avg_2)
    print("avg_1", avg_1)
    print("avg_2", avg_2)
    print("final", final)
    

if __name__ == '__main__':
    main()