from bokeh.plotting import figure, output_file, show

if __name__ == "__main__":
    output_file("simple_graphing.html")
    fig = figure()

    total_vals = int(input("¿How many values do you want to graph?: "))
    x_values = list(range(total_vals))
    y_values = []

    for x in x_values:
        val = int(input(f'Y Value for {x}: '))
        y_values.append(val)

    fig.line(x_values, y_values, line_width=2)
    show(fig)