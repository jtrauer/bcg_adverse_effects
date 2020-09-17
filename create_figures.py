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
rosenthal_vaccinated = [0] * 5 + [2, 2, 3, 1, 2, 2, 2, 0, 0, 1] + [0] * 16 + [1, 0]
rosenthal_unvaccinated = [0, 3, 5, 1, 4, 4, 6, 5, 5, 6, 7, 1, 4, 2, 2, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1] + [0] * 8
rosenthal_times = np.linspace(0.0, 16.0, 33)

# chicago nursing data
chicago_nursing_vaccinated = [3 + 4 / 12, 2 + 4 / 12]
chicago_nursing_unvaccinated = [3 + 4 / 12, 2 + 9 / 12, 2 + 11 / 12, 1 + 3 / 12, 3]
chicago_nursing_assumed_age = 18.0

# mrc uk data
english_cities_vaccinated = [14, 13, 13, 9, 2, 5, 3, 3]
english_cities_unvaccinated = [68, 92, 41, 26, 11, 5, 2, 3]
english_cities_times = np.linspace(1.25, 18.75, 8)
english_cities_assumed_age = 14.7 + 1.25

# plotting
plt.style.use("ggplot")
x_limit = 21.
y_limit = 70.
xlabel_fontsize = 9.
title_fontsize = 9.

# bettag plot
reactivation_graph = plt.figure()
vaccinated_colour = "red"
unvaccinated_colour = "blue"
bettag_axis = reactivation_graph.add_subplot(234, xlim=(0, x_limit), ylim=(0, y_limit))
bettag_axis.scatter(bettag_durations_years[:12], bettag_ages[:12], marker='o', linewidth=0.0, alpha=0.5,
                    color=vaccinated_colour, s=1e2)
bettag_axis.scatter(bettag_durations_years[12:], bettag_ages[12:], marker='o', linewidth=0.0, alpha=0.5,
                    color=unvaccinated_colour, s=1e2)
bettag_axis.set_title("Lincoln state school", fontsize=title_fontsize)
bettag_axis.set_xlabel("Years from vaccination", fontsize=xlabel_fontsize)
bettag_axis.set_ylabel("Age", fontsize=xlabel_fontsize)

# madanapalle
frimodt_axis = reactivation_graph.add_subplot(235, title="Madanapalle", xlim=(0, x_limit), ylim=(0, y_limit))
marker_enlargement = 1e2
for age_group in average_starting_ages:
    frimodt_axis.scatter(frimodt_cases.index.values, frimodt_cases.index.values + age_group, marker="o",
                         s=marker_enlargement * frimodt_cases[age_group],
                         color=vaccinated_colour, alpha=0.5)
    frimodt_axis.scatter(frimodt_unvaccinated_cases.index.values, frimodt_unvaccinated_cases.index.values + age_group,
                         marker="o",
                         s=marker_enlargement * frimodt_unvaccinated_cases[age_group],
                         color=unvaccinated_colour, alpha=0.5)
frimodt_axis.axes.get_yaxis().set_ticklabels([])
frimodt_axis.set_title("Madanapalle", fontsize=title_fontsize)
frimodt_axis.set_xlabel("Years from vaccination", fontsize=xlabel_fontsize)

# ferguson plot
ferguson_axis = reactivation_graph.add_subplot(241, xlim=(0, x_limit), ylim=(0, y_limit))
ferguson_axis.scatter(ferguson_times, ferguson_times, s=[marker_enlargement * i for i in ferguson_vaccinated],
                      color=vaccinated_colour, alpha=0.5)
ferguson_axis.scatter(ferguson_times, ferguson_times, s=[marker_enlargement * i for i in ferguson_unvaccinated],
                      color=unvaccinated_colour, alpha=0.5)
ferguson_axis.axes.get_xaxis().set_ticklabels([])
ferguson_axis.set_title("Saskatchewan", fontsize=title_fontsize)
ferguson_axis.set_ylabel("Age", fontsize=xlabel_fontsize)
ferguson_axis.axes.set_xticks(range(0, 30, 10))

# rosenthal plot
rosenthal_axis = reactivation_graph.add_subplot(242, xlim=(0, x_limit), ylim=(0, y_limit))
rosenthal_axis.scatter(rosenthal_times, rosenthal_times, s=[marker_enlargement * i for i in rosenthal_vaccinated],
                       color=vaccinated_colour, alpha=0.5)
rosenthal_axis.scatter(rosenthal_times, rosenthal_times, s=[marker_enlargement * i for i in rosenthal_unvaccinated],
                       color=unvaccinated_colour, alpha=0.5)
rosenthal_axis.set_title("Chicago, hospital", fontsize=title_fontsize)
rosenthal_axis.axes.get_yaxis().set_ticklabels([])
rosenthal_axis.axes.get_xaxis().set_ticklabels([])
rosenthal_axis.axes.set_xticks(range(0, 30, 10))

# chicago nursing plot
chicago_nursing_axis = reactivation_graph.add_subplot(244, xlim=(0, x_limit), ylim=(0, y_limit))
chicago_nursing_axis.scatter(chicago_nursing_vaccinated, [i + chicago_nursing_assumed_age for i in chicago_nursing_vaccinated],
                             color=vaccinated_colour, alpha=0.5, s=1e2)
chicago_nursing_axis.scatter(chicago_nursing_unvaccinated, [i + chicago_nursing_assumed_age for i in chicago_nursing_unvaccinated],
                             color=unvaccinated_colour, alpha=0.5, s=1e2)
chicago_nursing_axis.set_title("Chicago, nursing", fontsize=title_fontsize)
chicago_nursing_axis.axes.get_yaxis().set_ticklabels([])
chicago_nursing_axis.axes.get_xaxis().set_ticklabels([])
chicago_nursing_axis.axes.set_xticks(range(0, 30, 10))

# english cities plot
marker_enlargement = 20.0
english_cities_axis = reactivation_graph.add_subplot(243, xlim=(0, x_limit), ylim=(0, y_limit))
english_cities_axis.scatter(english_cities_times, [i + english_cities_assumed_age for i in english_cities_times],
                            color=vaccinated_colour, alpha=0.5,
                            s=[marker_enlargement * i for i in english_cities_vaccinated])
english_cities_axis.scatter(english_cities_times, [i + english_cities_assumed_age for i in english_cities_times],
                            color=unvaccinated_colour, alpha=0.5,
                            s=[marker_enlargement * i for i in english_cities_unvaccinated])
english_cities_axis.axes.get_yaxis().set_ticklabels([])
english_cities_axis.axes.get_xaxis().set_ticklabels([])
english_cities_axis.set_title("English cities", fontsize=title_fontsize)
english_cities_axis.axes.set_xticks(range(0, 30, 10))

# chengalpattu data
chengalpattu_data = pd.read_excel("chengalpattu_data.xlsx", header=1)
chengalpattu_data.columns = chengalpattu_data.columns.astype(str)
chengalpattu_data = chengalpattu_data.drop([13, 14])
chengalpattu_age_groups = [float(age.split(" ")[0]) + 2.5 for age in list(chengalpattu_data.iloc[:, 0])]
chengalpattu_data = \
    chengalpattu_data.loc[:,
    ("Unnamed" not in col and "Age" not in col for col in chengalpattu_data.columns)
    ]
follow_up_times = []
for col in chengalpattu_data.columns:
    if ".1" in col:
        follow_up = col.replace(".1", "")
        follow_up_times.append(float(follow_up) - 1.25)
        chengalpattu_data.loc[:, col] += chengalpattu_data.loc[:, follow_up]
        chengalpattu_data.loc[:, col] /= 2.
chengalpattu_data = \
    chengalpattu_data.loc[:,
    (".1" in col or ".2" in col for col in chengalpattu_data.columns)
    ]
new_col_names = [col.replace(".1", "_bcg") if ".1" in col else col for col in chengalpattu_data.columns]
chengalpattu_data.columns = [col.replace(".2", "_control") if ".2" in col else col for col in new_col_names]

# chengalpattu plotting
marker_enlargement = 3.5
chengalpattu_age_groups[-1] = 65.  # arbitrary y-position for the last age group on the vertical axis, who are aged 60+
chengalpattu_axis = reactivation_graph.add_subplot(236, xlim=(0, x_limit), ylim=(0, y_limit))
for i_age in range(len(chengalpattu_data)):
    chengalpattu_axis.scatter(
        follow_up_times,
        [chengalpattu_age_groups[i_age]] * len(follow_up_times),
        s=[marker_enlargement * i for
           i in  chengalpattu_data.iloc[i_age, :len(follow_up_times)]],
        color=vaccinated_colour,
        alpha=0.5
    )
    chengalpattu_axis.scatter(
        follow_up_times,
        [chengalpattu_age_groups[i_age]] * len(follow_up_times),
        s=[marker_enlargement * i for
           i in chengalpattu_data.iloc[i_age, len(follow_up_times): len(follow_up_times) * 2]],
        color=unvaccinated_colour,
        alpha=0.5
    )
chengalpattu_axis.axes.get_yaxis().set_ticklabels([])
chengalpattu_axis.set_title("Chengalpattu", fontsize=title_fontsize)
chengalpattu_axis.set_xlabel("Years from vaccination", fontsize=xlabel_fontsize)

# plt.show()
reactivation_graph.savefig("reactivation.jpg", dpi=500, bbox_inches="tight")
