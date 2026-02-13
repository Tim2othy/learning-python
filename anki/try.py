def fun():
    print("first")
    try:
        print("second")
        print(1 / 0)
    except:  # noqa: E722
        print("end")


fun()

# Yes, "end" is only printed if the 1/0 error producing term is included
