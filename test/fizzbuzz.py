def main():
    for number in range(1, 100 + 1):
        output = ""
        if number % 3 == 0:
            output = "FIZZ"

        if number % 5 == 0:
            output = "FIZZ"

        if output == "":
            output = number

        print(output)
        pass


if __name__ == "__main__":
    main()
    pass
