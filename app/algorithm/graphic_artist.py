import matplotlib.pyplot as plt

from algorithm import Algorithm


def main(**kwargs) -> None:
    number_of_cells_per_side = kwargs["number_of_cells_per_side"]
    product_storage = kwargs["product_storage"]
    number_of_iterations = kwargs["number_of_iterations"]
    percentage_of_consumers = kwargs["percentage_of_consumers"]
    percentage_of_advertising = kwargs["percentage_of_advertising"]

    algorithm = Algorithm(number_of_cells_per_side=number_of_cells_per_side,
                          product_storage=product_storage,
                          number_of_iterations=number_of_iterations,
                          percentage_of_consumers=percentage_of_consumers,
                          percentage_of_advertising=percentage_of_advertising)
    buyers = []
    potential_buyers = []
    days = []

    fig, ax = plt.subplots()

    for buyers_y, potential_buyers_y, day_x in algorithm.number_users_and_day():
        buyers.append(buyers_y)
        potential_buyers.append(potential_buyers_y)
        days.append(day_x)

    ax.stackplot(days, potential_buyers, buyers, alpha=0.8, labels=['Потенциальный покупатель', 'Купивший'])

    ax.set_title("Популяция агентов")
    ax.legend(loc='lower right')
    ax.set_xlabel("Дни")
    ax.set_ylabel("Пользователи")

    ax.set_xlim(xmin=days[0], xmax=days[-1])
    fig.tight_layout()

    plt.show()


if __name__ == '__main__':
    main(number_of_cells_per_side=50,
         product_storage=2,
         number_of_iterations=31,
         percentage_of_consumers=15,
         percentage_of_advertising=2)
