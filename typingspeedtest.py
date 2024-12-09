import time

def calculate_typing_speed(text, time_taken):
    words = text.split()
    num_words = len(words)
    typing_speed = num_words / time_taken
    return typing_speed

def main():
    text = "The quick brown fox jumps over the lazy dog."
    print("Type the following text:")
    print(text)
    print("Press Enter when you're done.")

    input("Press Enter to start...")

    start_time = time.time()
    user_text = input()
    end_time = time.time()

    time_taken = end_time - start_time
    typing_speed = calculate_typing_speed(user_text, time_taken)

    print(f"\nTime taken: {time_taken:.2f} seconds")
    print(f"Typing speed: {typing_speed:.2f} words per second")

if __name__ == "__main__":
    main()


