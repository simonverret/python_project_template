import numpy as np

from projectNameGoesHere import plotter


def test_plotter(mocker):#mock_ax_plot, mock_pause):
    x = np.linspace(1,10)
    y = np.sin(x)

    mocker.patch('projectNameGoesHere.plotter.plt.pause')
    mocker.patch.object(plotter.plt.Line2D, 'set_data')
    plot = plotter.Plotter()
    plot.update(x,y)

    plotter.plt.Line2D.set_data.assert_called_with(x,y)
    assert plotter.plt.pause.call_count == 2
