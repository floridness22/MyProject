import random

def main():
    secret = random.randint(1, 100)
    attempts = 0
    print("歡迎來到猜數字遊戲！我已選好一個 1-100 的整數。")
    print("提示：輸入一個整數，看看它是太大、太小，或是恰好。")
    while True:
        user_input = input("請輸入你的猜測（或輸入 q 退出）：").strip()
        if user_input.lower() in ('q', 'quit', 'exit'):
            print(f"遊戲結束。正確答案是 {secret}。再見！")
            break
        try:
            guess = int(user_input)
        except ValueError:
            print("請輸入整數數字。")
            continue
        attempts += 1
        if guess < secret:
            print("太小了。")
        elif guess > secret:
            print("太大了。")
        else:
            print(f"恭喜！你猜對了，答案就是 {secret}。共猜了 {attempts} 次。")
            break

if __name__ == "__main__":
    main()
