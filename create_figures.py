import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

filepath = os.path.abspath(__file__)
separator = "\\" if "\\" in filepath else "/"
BASE_PATH = separator.join(filepath.split(separator)[:-1])
folder_name = "figures"
figure_folder = os.path.join(BASE_PATH, folder_name)

"""
input data from trial reports
"""

# Saskatchewan data, from Table IV of Ferguson 1949
saskatchewan_vaccinated = [2, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1]
saskatchewan_unvaccinated = [3, 3, 0, 6, 4, 1, 5, 4, 0, 0, 0]
saskatchewan_times = [i + 0.5 for i in range(11)]

# **** rosenthal data ****
rosenthal_vaccinated = [0] * 5 + [2, 2, 3, 1, 2, 2, 2, 0, 0, 1] + [0] * 16 + [1, 0]
rosenthal_unvaccinated = [0, 3, 5, 1, 4, 4, 6, 5, 5, 6, 7, 1, 4, 2, 2, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1] + [0] * 8
rosenthal_times = np.linspace(0.0, 16.0, 33)

# English cities data, Table 3 of Medical Research Council 1972
english_cities_vaccinated = [14, 13, 13, 9, 2, 5, 3, 3]
english_cities_unvaccinated = [68, 92, 41, 26, 11, 5, 2, 3]
english_cities_times = np.linspace(1.25, 18.75, 8)
english_cities_assumed_age = 14.7 + 1.25

# Chicago nursing data, Table 3 of Rosenthal et al 1963
chicago_nursing_vaccinated = [3 + 4 / 12, 2 + 4 / 12]
chicago_nursing_unvaccinated = [3 + 4 / 12, 2 + 9 / 12, 2 + 11 / 12, 1 + 3 / 12, 3]
chicago_nursing_assumed_age = 18.0

# Lincoln State School, USA, Tables 1 and 2 of Bettag 1964
lincoln_starting_ages = [19, 17, 44, 16, 30, 14, 18, 17, 15, 17, 17, 24, 13, 16, 31, 14, 8, 18, 17, 11]
lincoln_durations_months = \
    [2 * 12 - 3, 3 * 12 - 1, 4 * 12 - 11, 4 * 12 - 9, 4 * 12 - 6, 6 * 12 - 9, 6 * 12 - 8, 8 * 12 - 8, 8 * 12 - 1,
     9 * 12 - 0, 11 * 12 - 1, 11 * 12 - 6, 1 * 12 - 8, 2 * 12 - 3, 9 * 12 - 0, 4 * 12 - 2, 4 * 12 - 2, 6 * 12 - 6,
     6 * 12 - 6, 11 * 12 - 1]
lincoln_durations_years = [i / 12.0 for i in lincoln_durations_months]
# assuming that the data on ages presented is the age at vaccination
lincoln_ages = \
    [i + j for i, j in zip(lincoln_starting_ages, lincoln_durations_years)]

# Madanapalle trial, Table 5 of Frimodt-Moller 1973
madanapalle_vaccinated = \
    [0] * 10 + [1, 0, 0, 0, 1, 1, 2, 2] + [0] * 3 + \
    [0] * 11 + [1, 3, 1, 1, 1, 0, 1, 0, 2, 0] + \
    [1] + [0] * 9 + [1] + [0] * 4 + [1, 0, 1, 0, 1, 0] + \
    [0] * 9 + [1] * 4 + [0, 0, 1, 0, 0, 1, 0, 0] + \
    [0, 1] + [0] * 9 + [1, 1, 2] + [0] * 7
madanapalle = \
    [0] * 12 + [2, 0, 1, 0, 1] + [0] * 4 + \
    [0] * 6 + [1, 0, 0, 1, 0, 1, 3, 0, 1, 2, 2, 0, 1, 1, 0] + \
    [0] * 4 + [1, 0, 1] + [0] * 6 + [1, 1, 0, 1, 2] + [0] * 3 + \
    [0] * 6 + [2, 1, 0, 0] + [1] * 3 + [4, 1] + [0] * 6 + \
    [1, 0, 0, 2, 1, 0, 2, 1] + [0] * 3 + [2, 2, 1] + [0] * 7
madanapalle_array = np.array(madanapalle_vaccinated)
madanapalle_array.shape = (21, 5)
average_starting_ages = [2, 10, 20, 30, 40]
madanapalle_cases = \
    pd.DataFrame(madanapalle_array, columns=average_starting_ages, index=list(range(1, 22)))
madanapalle_array = np.array(madanapalle)
madanapalle_array.shape = (21, 5)
madanapalle_unvaccinated_cases = \
    pd.DataFrame(madanapalle_array, columns=average_starting_ages, index=list(range(1, 22)))

# Chengalpattu data, loaded from data provided from collaborators in India
chengalpattu_data = pd.read_excel("data/chengalpattu_data.xlsx", header=1)
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

"""
plotting
"""

# plotting parameters
plt.style.use("ggplot")
x_limit = 21.
y_limit = 70.
xlabel_fontsize = 9.
title_fontsize = 9.
reactivation_graph = plt.figure()
marker_enlargement = 1e2
vaccinated_colour = "red"
unvaccinated_colour = "blue"

# Saskatchewan plot
saskatchewan_axis = reactivation_graph.add_subplot(241, xlim=(0, x_limit), ylim=(0, y_limit))
saskatchewan_axis.scatter(
    saskatchewan_times, saskatchewan_times, s=[marker_enlargement * i for i in saskatchewan_vaccinated],
    color=vaccinated_colour, alpha=0.5
)
saskatchewan_axis.scatter(
    saskatchewan_times, saskatchewan_times, s=[marker_enlargement * i for i in saskatchewan_unvaccinated],
    color=unvaccinated_colour, alpha=0.5
)
saskatchewan_axis.axes.get_xaxis().set_ticklabels([])
saskatchewan_axis.set_title("Saskatchewan", fontsize=title_fontsize)
saskatchewan_axis.set_ylabel("Age", fontsize=xlabel_fontsize)
saskatchewan_axis.axes.set_xticks(range(0, 30, 10))

# Chicago hospital-delivered infants plot
rosenthal_axis = reactivation_graph.add_subplot(242, xlim=(0, x_limit), ylim=(0, y_limit))
rosenthal_axis.scatter(rosenthal_times, rosenthal_times, s=[marker_enlargement * i for i in rosenthal_vaccinated],
                       color=vaccinated_colour, alpha=0.5)
rosenthal_axis.scatter(rosenthal_times, rosenthal_times, s=[marker_enlargement * i for i in rosenthal_unvaccinated],
                       color=unvaccinated_colour, alpha=0.5)
rosenthal_axis.set_title("Chicago, hospital", fontsize=title_fontsize)
rosenthal_axis.axes.get_yaxis().set_ticklabels([])
rosenthal_axis.axes.get_xaxis().set_ticklabels([])
rosenthal_axis.axes.set_xticks(range(0, 30, 10))

# English cities plot
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

# Chicago nursing students plot
chicago_nursing_axis = reactivation_graph.add_subplot(244, xlim=(0, x_limit), ylim=(0, y_limit))
chicago_nursing_axis.scatter(
    chicago_nursing_vaccinated, [i + chicago_nursing_assumed_age for i in chicago_nursing_vaccinated],
    color=vaccinated_colour, alpha=0.5, s=1e2
)
chicago_nursing_axis.scatter(
    chicago_nursing_unvaccinated, [i + chicago_nursing_assumed_age for i in chicago_nursing_unvaccinated],
    color=unvaccinated_colour, alpha=0.5, s=1e2
)
chicago_nursing_axis.set_title("Chicago, nursing", fontsize=title_fontsize)
chicago_nursing_axis.axes.get_yaxis().set_ticklabels([])
chicago_nursing_axis.axes.get_xaxis().set_ticklabels([])
chicago_nursing_axis.axes.set_xticks(range(0, 30, 10))

# Lincoln State School plot
lincoln_axis = reactivation_graph.add_subplot(234, xlim=(0, x_limit), ylim=(0, y_limit))
lincoln_axis.scatter(lincoln_durations_years[:12], lincoln_ages[:12], marker='o', linewidth=0.0, alpha=0.5,
                     color=vaccinated_colour, s=1e2)
lincoln_axis.scatter(lincoln_durations_years[12:], lincoln_ages[12:], marker='o', linewidth=0.0, alpha=0.5,
                     color=unvaccinated_colour, s=1e2)
lincoln_axis.set_title("Lincoln state school", fontsize=title_fontsize)
lincoln_axis.set_xlabel("Years from vaccination", fontsize=xlabel_fontsize)
lincoln_axis.set_ylabel("Age", fontsize=xlabel_fontsize)

# Madanapalle plot
madanapalle_axis = reactivation_graph.add_subplot(235, title="Madanapalle", xlim=(0, x_limit), ylim=(0, y_limit))
for age_group in average_starting_ages:
    madanapalle_axis.scatter(madanapalle_cases.index.values, madanapalle_cases.index.values + age_group, marker="o",
                             s=marker_enlargement * madanapalle_cases[age_group],
                             color=vaccinated_colour, alpha=0.5)
    madanapalle_axis.scatter(madanapalle_unvaccinated_cases.index.values, madanapalle_unvaccinated_cases.index.values + age_group,
                             marker="o",
                             s=marker_enlargement * madanapalle_unvaccinated_cases[age_group],
                             color=unvaccinated_colour, alpha=0.5)
madanapalle_axis.axes.get_yaxis().set_ticklabels([])
madanapalle_axis.set_title("Madanapalle", fontsize=title_fontsize)
madanapalle_axis.set_xlabel("Years from vaccination", fontsize=xlabel_fontsize)

# Chengalpattu plot
marker_enlargement = 3.5
chengalpattu_age_groups[-1] = 65.  # arbitrary y-position for the last age group on the vertical axis, who are aged 60+
chengalpattu_axis = reactivation_graph.add_subplot(236, xlim=(0, x_limit), ylim=(0, y_limit))
for i_age in range(len(chengalpattu_data)):
    chengalpattu_axis.scatter(
        follow_up_times,
        [chengalpattu_age_groups[i_age]] * len(follow_up_times),
        s=[marker_enlargement * i for
           i in chengalpattu_data.iloc[i_age, :len(follow_up_times)]],
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

# save multi-panel plot
file_name = os.path.join(figure_folder, "reactivation.jpg")
reactivation_graph.savefig(file_name, dpi=500, bbox_inches="tight")
