import random
import time

def run_test():
    # 1. SETUP VARIABLES
    num_questions = 10
    correct_count = 0
    wrong_questions = []  # To store details of questions the user misses
    
    print("\n--- Starting the Math Test! ---")
    print("Press ENTER without typing to skip a question.")
    
    # Start the timer
    start_time = time.time()

    # 2. THE MAIN QUESTION LOOP
    for i in range(1, num_questions + 1):
        # Generate random amount of operators (3 to 5)
        num_ops = random.randint(3, 5)
        
        # Generate the first number
        numbers = [random.randint(0, 100)]
        operators = []
        
        # Build the rest of the equation
        for _ in range(num_ops):
            numbers.append(random.randint(0, 100))
            operators.append(random.choice(['+', '-', '*', '/']))

        # CALCULATE THE ANSWER (Left-to-Right Logic)
        # We start with the first number and apply each operator one by one
        result = numbers[0]
        expression_str = str(numbers[0])
        
        for j in range(num_ops):
            op = operators[j]
            next_val = numbers[j+1]
            
            # Update the string we show the user
            expression_str += f"{op}{next_val}"
            
            # Calculate the result based on the operator
            if op == '+':
                result += next_val
            elif op == '-':
                result -= next_val
            elif op == '*':
                result *= next_val
            elif op == '/':
                # Avoid dividing by zero
                if next_val != 0:
                    result /= next_val
        
        # Format the final answer to a whole number for comparison
        final_answer = int(round(result))

        # 3. INTERACT WITH THE USER
        print(f"\nQuestion {i}: {expression_str}")
        user_input = input("Your answer: ").strip()

        # Check if input is empty (User just pressed Enter)
        if user_input == "":
            print("Skipped!")
            wrong_questions.append(f"{expression_str} = {final_answer}")
        else:
            try:
                # Convert user input to an integer to compare
                if int(user_input) == final_answer:
                    print("Thanks!")
                    correct_count += 1
                else:
                    print("Thanks!")
                    wrong_questions.append(f"{expression_str} = {final_answer}")
            except ValueError:
                # If they typed letters instead of numbers
                print("Invalid input! Marked as wrong.")
                wrong_questions.append(f"{expression_str} = {final_answer}")

    # 4. SHOW RESULTS
    end_time = time.time()
    total_time = int(end_time - start_time)

    print("\n" + "="*30)
    print(f"Total time: {total_time} seconds")
    print(f"The number of correct answers: {correct_count}")
    
    if wrong_questions:
        print("\nThe following are the right answers of the questions you got wrong:")
        for item in wrong_questions:
            print(item)
    print("="*30)

# 5. PROGRAM ENTRY POINT
if __name__ == "__main__":
    while True:
        run_test()
        
        print("\nWhether to proceed to the next round of testing?")
        print("1. proceed")
        print("2. exit")
        choice = input("Please input: ")
        
        if choice != "1":
            print("Goodbye!")
            break