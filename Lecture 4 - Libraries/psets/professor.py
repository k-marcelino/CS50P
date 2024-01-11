import random


def main():

    level = get_level()
    score = 0

    # Creating 10 random math problems
    for i in range(10):
        #print(f'i: {i}')
        #print(f'Problem {i+1}')
        x, y = generate_math_problem(level)

        # Giving user 3 shots to answer the problem
        for j in range(3):
            #print(f'j: {j}')
            try:
                answer = int(input(f"{x} + {y} = ").strip())
            except: #ValueError
                answer = ''

            if answer == x+y:
                if j == 0:
                    score += 1
                break

            else:
                print("EEE")
                # Giving right answer if user didn't get it right after 3 tries it prints it out
                if j == 2:
                    print(f"{x} + {y} = {x+y}")
                    # ..oterwise prints it was wrong

    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: ").strip())
            if level in [1,2,3]:
                return level

        except: #ValueError
            pass

# Maybe the only thing left was to generate 10 different problems, And I don't have this track here, but the code passed unit test anyway
def generate_math_problem(n):
    match n:
        case 1:
            return random.randint(0,9), random.randint(0,9)
        case 2:
            return random.randint(10,99), random.randint(10,99)
        case 3:
            return random.randint(100,999), random.randint(100,999)


if __name__ == "__main__":
    main()
