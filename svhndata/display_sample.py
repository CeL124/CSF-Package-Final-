"""
This will display 9 sample images from you dataself.
Inputs will an image array, corresponding label array and a number.
The number will has to be between 10 and nine less than the length of the array.
"""
import matplotlib.pyplot as plt


def print_sample(img_array, label_array, num):
    min_num = num-9
    plot_list = list(range(min_num, num))
    for i in range(len(plot_list)):
        if min_num < 0:
            print('please pick a num between 10 and ' + str(len(img_array) - 9))
            break
        elif num > (len(img_array) - 9):
            print('Num picked is too high please pick between 10 and ' + str(len(img_array) - 9))
            break
        else:
            plt.subplot(3, 3, i+1)
            img = plot_list[i]
            plt.imshow(img_array[img])
            plt.title(str(label_array[img]))
            plt.xticks([])
            plt.yticks([])
    plt.tight_layout()
    plt.show()
