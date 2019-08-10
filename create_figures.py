import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# get data from bettag paper
bettag_starting_ages = [19, 17, 44, 16, 30, 14, 18, 17, 15, 17, 17, 24, 13, 16, 31, 14, 8, 18, 17, 11]
bettag_durations_months = \
    [2 * 12 - 3,
     3 * 12 - 1,
     4 * 12 - 11,
     4 * 12 - 9,
     4 * 12 - 6,
     6 * 12 - 9,
     6 * 12 - 8,
     8 * 12 - 8,
     8 * 12 - 1,
     9 * 12 - 0,
     11 * 12 - 1,
     11 * 12 - 6,
     1 * 12 - 8,
     2 * 12 - 3,
     9 * 12 - 0,
     4 * 12 - 2,
     4 * 12 - 2,
     6 * 12 - 6,
     6 * 12 - 6,
     11 * 12 - 1]
bettag_durations_years = [i / 12.0 for i in bettag_durations_months]

# if we assume the data on ages presented is the age at vaccination
bettag_ages = [i + j for i, j in zip(bettag_starting_ages, bettag_durations_years)]

# frimodt_moller study
frimodt_vaccinated\
    = [0] * 10 + [1, 0, 0, 0, 1, 1, 2, 2] + [0] * 3 + \
      [0] * 11 + [1, 3, 1, 1, 1, 0, 1, 0, 2, 0] + \
      [1] + [0] * 9 + [1] + [0] * 4 + [1, 0, 1, 0, 1, 0] + \
      [0] * 9 + [1] * 4 + [0, 0, 1, 0, 0, 1, 0, 0] + \
      [0, 1] + [0] * 9 + [1, 1, 2] + [0] * 7
frimodt_unvaccinated = \
    [0] * 12 + [2, 0, 1, 0, 1] + [0] * 4 + \
    [0] * 6 + [1, 0, 0, 1, 0, 1, 3, 0, 1, 2, 2, 0, 1, 1, 0] + \
    [0] * 4 + [1, 0, 1] + [0] * 6 + [1, 1, 0, 1, 2] + [0] * 3 + \
    [0] * 6 + [2, 1, 0, 0] + [1] * 3 + [4, 1] + [0] * 6 + \
    [1, 0, 0, 2, 1, 0, 2, 1] + [0] * 3 + [2, 2, 1] + [0] * 7
frimodt_array = np.array(frimodt_vaccinated)
frimodt_array.shape = (21, 5)
average_starting_ages = [2, 10, 20, 30, 40]
frimodt_cases = pd.DataFrame(frimodt_array,
                             columns=average_starting_ages,
                             index=list(range(1, 22)))

frimodt_array = np.array(frimodt_unvaccinated)
frimodt_array.shape = (21, 5)
frimodt_unvaccinated_cases = pd.DataFrame(frimodt_array,
                                          columns=average_starting_ages,
                                          index=list(range(1, 22)))

# ferguson data
ferguson_vaccinated = [2, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1]
ferguson_unvaccinated = [3, 3, 0, 6, 4, 1, 5, 4, 0, 0, 0]
ferguson_times = [i + 0.5 for i in range(11)]

# rosenthal data
rosenthal_vaccinated = [0, 0, 0, 0, 2, 0, 2, 2, 1, 1, 1, 1, 0, 0, 1, 0, 0]
rosenthal_unvaccinated = [0, 5, 1, 3, 2, 5, 4, 4, 2, 5, 3, 3, 0, 0, 1, 0, 1]
rosenthal_times = np.linspace(0.0, 8.0, 17)

# plotting
plt.style.use("ggplot")
x_limit = 21.
y_limit = 60.

# bettag plot
reactivation_graph = plt.figure()
vaccinated_colour = "red"
unvaccinated_colour = "blue"
bettag_axis = reactivation_graph.add_subplot(221, title="Lincoln state school", xlim=(0, x_limit), ylim=(0, y_limit),
                                             ylabel="Age")
bettag_axis.scatter(bettag_durations_years[:12], bettag_ages[:12], marker='o', linewidth=0.0, alpha=0.5,
                    color=vaccinated_colour, s=1e2)
bettag_axis.scatter(bettag_durations_years[12:], bettag_ages[12:], marker='o', linewidth=0.0, alpha=0.5,
                    color=unvaccinated_colour, s=1e2)
bettag_axis.axes.get_xaxis().set_ticklabels([])

# madanapalle
frimodt_axis = reactivation_graph.add_subplot(222, title="Madanapalle", xlim=(0, x_limit), ylim=(0, y_limit))
marker_enlargement = 1e2
for age_group in average_starting_ages:
    frimodt_axis.scatter(frimodt_cases.index.values, frimodt_cases.index.values + age_group, marker="o",
                         s=marker_enlargement * frimodt_cases[age_group],
                         color=vaccinated_colour, alpha=0.5)
    frimodt_axis.scatter(frimodt_unvaccinated_cases.index.values, frimodt_unvaccinated_cases.index.values + age_group,
                         marker="o",
                         s=marker_enlargement * frimodt_unvaccinated_cases[age_group],
                         color=unvaccinated_colour, alpha=0.5)
frimodt_axis.axes.get_xaxis().set_ticklabels([])

# ferguson plot
ferguson_axis = reactivation_graph.add_subplot(223, title="Saskatchewan", xlim=(0, x_limit), ylim=(0, y_limit),
                                               xlabel="Time from vaccination")
ferguson_axis.scatter(ferguson_times, ferguson_times, s=[marker_enlargement * i for i in ferguson_vaccinated],
                      color=vaccinated_colour, alpha=0.5)
ferguson_axis.scatter(ferguson_times, ferguson_times, s=[marker_enlargement * i for i in ferguson_unvaccinated],
                      color=unvaccinated_colour, alpha=0.5)

# rosenthal plot
rosenthal_axis = reactivation_graph.add_subplot(224, title="Chicago", xlim=(0, x_limit), ylim=(0, y_limit),
                                                xlabel="Time from vaccination")
rosenthal_axis.scatter(rosenthal_times, rosenthal_times, s=[marker_enlargement * i for i in rosenthal_vaccinated],
                       color=vaccinated_colour, alpha=0.5)
rosenthal_axis.scatter(rosenthal_times, rosenthal_times, s=[marker_enlargement * i for i in rosenthal_unvaccinated],
                       color=unvaccinated_colour, alpha=0.5)

plt.show()
reactivation_graph.savefig("reactivation.png")
