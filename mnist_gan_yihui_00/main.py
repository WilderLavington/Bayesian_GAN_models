from mnist_gan_yihui_00.load import *
from mnist_gan_yihui_00.train import run_yihui_model


def yihui_gan():
    run_yihui_model()



def main():
    print('Running . . . ')
    yihui_gan()
    print('end')


if __name__ == "__main__":
    main()