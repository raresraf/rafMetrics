import mock

from rComplexity.plotting.constants import pool_plotting_points_symbols
from rComplexity.plotting.plot_points import plot_points_from_file


def test_pool_plotting_points_symbols():
    if next(pool_plotting_points_symbols) != "o":
        raise AssertionError
    if next(pool_plotting_points_symbols) != "x":
        raise AssertionError
    if next(pool_plotting_points_symbols) != "o":
        raise AssertionError
    if next(pool_plotting_points_symbols) != "x":
        raise AssertionError
    if next(pool_plotting_points_symbols) != "o":
        raise AssertionError


@mock.patch("matplotlib.pyplot.show")
@mock.patch("matplotlib.pyplot.legend")
@mock.patch("matplotlib.pyplot.plot")
def test_plot_points_from_file(plt_mock_plot, plt_mock_legend, plt_mock_show):
    plot_points_from_file("rComplexity/plotting/tests/result_file_testing.txt",
                          5)

    if plt_mock_plot.call_count != 5:
        raise AssertionError
    plt_mock_legend.assert_called_once_with()
    plt_mock_show.assert_called_once_with()
