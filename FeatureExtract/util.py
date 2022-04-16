import matplotlib.pyplot as plt
import seaborn as sns


class Util:
    def __init__(self):
        pass

    def generate_feature_heatmap(self, input) -> None:
        plt.figure()
        sns.heatmap(input, annot=True, cmap='Greys')
        plt.xlabel("To")
        plt.ylabel("From")
        plt.show()
        plt.close('all')
