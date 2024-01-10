from plotter import Plotter
import pandas as pd


if __name__ == "__main__":
    json_file_path = "deviation.json"
    # Read JSON file as a pandas DataFrame
    df = pd.read_json(json_file_path)

    # Columns to compare (for example)
    columns_to_compare = ['mean', 'ceiling_mean']

    # Create a Plotter instance
    plotter = Plotter()

    # Draw plots for a maximum of 3 rooms
    max_rooms = 3
    plot_paths = plotter.plot_histograms(df, columns_to_compare, max_rooms)
