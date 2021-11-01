import matplotlib.pyplot as plt

def main():
    nb = int(input("Donner un nombre \n>>> "))

    grid = [i for i in range(1, nb+1)]

    for i in grid: #X
        print(i)
        for j in grid: #Y

            if i > j:
                if i % j == 0:
                    plt.scatter(str(j), str(i), color="red")
            elif i < j:
                if j % i == 0:
                    plt.scatter(str(j), str(i), color="blue")
            elif i == j:
                plt.scatter(str(j), str(i), color="gray")

    plt.show()

if __name__ == "__main__":
    main()