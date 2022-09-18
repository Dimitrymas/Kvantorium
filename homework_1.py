bananas = 100
max = 100

goril_bananas = 3
shimpanze_bananas = 2
lemur_bananas = 0.5


def main():
    for goril in range(bananas//goril_bananas):
        for shimpanze in range(bananas//shimpanze_bananas):
            for lemur in range(bananas//int(2*lemur_bananas)):
                if goril + shimpanze + lemur == max and goril * goril_bananas + shimpanze * shimpanze_bananas + lemur * lemur_bananas == 100:
                    print(f"Горил:{goril}, шимпанзе:{shimpanze}, лемуров:{lemur}")

if __name__ == '__main__':
    main()
