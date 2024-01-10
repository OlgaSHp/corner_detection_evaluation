import os
import matplotlib.pyplot as plt


class Plotter:
    def __init__(self, output_folder="plots"):
        self.output_folder = output_folder
        os.makedirs(self.output_folder, exist_ok=True)

    def plot_histograms(self, df, columns_to_compare, max_rooms=None):
        plot_paths = []

        # Get unique room names
        room_names = df['name'].unique()

        # If max_rooms is specified,
        # limit the number of rooms to show
        if max_rooms is not None:
            room_names = room_names[:max_rooms]

        # Iterate through each room and create
        # a histogram for the specified columns
        for room_name in room_names:
            # Extract data for the current room
            room_data = df[df['name'] == room_name].iloc[0]

            # Create a figure and axis
            plt.figure(figsize=(10, 6))
            ax = plt.subplot()

            # Plot the histogram for each column
            for column in columns_to_compare:
                ax.hist(room_data[column], bins=20, alpha=0.5, label=column)

            # Add labels and title
            plt.xlabel('Deviation (degrees)')
            plt.ylabel('Frequency')
            plt.title(
                f'Distribution of {", ".join(columns_to_compare)} -'
                f'{room_name}'
            )

            # Add legend
            plt.legend()

            # Replace invalid characters in the filename
            safe_room_name = room_name.replace('/', '_')

            # Save the plot to the output folder
            plot_path = os.path.join(
                self.output_folder, f'{safe_room_name}_histogram.png'
                )
            plt.savefig(plot_path)

            plt.close()

            print(f'Plot saved: {plot_path}')
            plot_paths.append(plot_path)

        print(f'Plots saved in folder: {self.output_folder}')
        return plot_paths
