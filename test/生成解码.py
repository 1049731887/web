def main():
    input_str = input("请输入要解码的：")
    initial_password = eval(input_str)

    # Get the original positions of the elements in the initial password
    original_positions = [initial_password.index(i) for i in range(len(initial_password))]

    # Print the recovered order
    print("Recovered Order:", original_positions)

if __name__ == "__main__":
    main()
