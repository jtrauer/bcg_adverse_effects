import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
plt.style.use("ggplot")


def normalise_to_upper_value(list_to_adjust, value):
    return [element / max(list_to_adjust) * value for element in list_to_adjust]


def duplicate_list_values(list_to_duplicate):
    return [element for element in list_to_duplicate for _ in (0, 1)]


upper_point_of_patch = 0.95

# getting haiti data, obtained through webplotdigitiser
haiti_age_brackets = [0.0, 2.5, 7.5, 12.5, 17.5, 22.5, 30.0, 75.0]
haiti_age_numbers = \
    [0.0,
     16.084033613445378 - 2.4465786314525806,
     18.151260504201684 - 4.084033613445381,
     16.18487394957983 - 4.3361344537815185,
     9.57983193277311 - 4.184873949579835,
     1.260504201680675 - 1.008403361344545,
     0.5546218487395009 - 0.2521008403361371,
     0.0]
haiti_array = np.zeros((len(haiti_age_numbers), 2))
haiti_array[:, 0] = haiti_age_brackets
haiti_array[:, 1] = normalise_to_upper_value(haiti_age_numbers, upper_point_of_patch)

age_progression_graph = plt.figure()

titles = ["Saskatchewan", "Chicago, hospital", "Chicago, contact",
          "Mumbai", "Chicago, housing project", "Agra", "Georgia schools", "Native Americans", "Haiti",
          "English cities", "Puerto Rico", "Chengalpattu", "Madanapalle"]
age_max = [1.0, 1.0, 1.0, 1.0, 10.0, 5.0, "", "", "", 1.5, ""]
efficacies = [81, 70, 88, 37, 85, 60, -25, 8, 89, 78, 31, -5, ""]
followups = [15.0, 10.0, 7.0, 2.5, 6.0, 5.0, 3.0, 50.0, 3.0, 20.0, 6.3, 15.0, 21.0]

# create data structures for aronson age bracket arrays (from aronson 1948)
aronson_cohort_sizes = \
    [0] + duplicate_list_values(normalise_to_upper_value([433 + 413, 659 + 624, 387 + 351, 72 + 69],
                                                         upper_point_of_patch)) + [0]
aronson_array = np.zeros((len(aronson_cohort_sizes), 2))
aronson_array[:, 0] = duplicate_list_values(list(range(0, 25, 5)))
aronson_array[:, 1] = aronson_cohort_sizes

# georgia schools
georgia_schools_brackets = [6.0, 6.0, 17.0, 17.0]
georgia_schools_array = np.zeros((len(georgia_schools_brackets), 2))
georgia_schools_numbers = [0.0, upper_point_of_patch, 0.075, 0.0]
georgia_schools_array[:, 0] = georgia_schools_brackets
georgia_schools_array[:, 1] = georgia_schools_numbers

# puerto rico
puerto_rico_age_numbers = \
    [0.0, 2.5850363644096674, 3.020930801292959, 3.500606073494385, 3.5854563627084026, 3.3195814903028236,
     5.158934799251448, 5.858072473630486, 9.758873128615175, 11.15962061925825, 11.288331490302822,
     10.934655707723714, 9.74762887036407, 8.16593654304185, 7.22046189179993, 5.4413171997278,
     3.706152709254848, 2.453494492174208, 1.749053674719292]
puerto_rico_age_brackets = [0] + duplicate_list_values(list(range(1, 20)))
puerto_rico_array = np.zeros((len(puerto_rico_age_brackets), 2))
puerto_rico_array[:, 0] = puerto_rico_age_brackets
puerto_rico_array[:, 1] = duplicate_list_values(
    normalise_to_upper_value(puerto_rico_age_numbers, upper_point_of_patch)) + [0.0]
puerto_rico_average = sum([i * j / sum(puerto_rico_age_numbers) for i, j in zip(puerto_rico_age_numbers, range(19))])

# chengalpattu
chengalpattu_male_numbers = [16199, 38369, 21289, 19519, 15700, 12238, 7739, 3959]
chengalpattu_female_numbers = [16136, 36093, 19988, 20259, 16336, 12088, 6749, 2511]
chengalpattu_male_tstpos_props = [4.9, 23.5, 62.0, 81.8, 85.2, 85.5, 82.6, 79.9]
chengalpattu_female_tstpos_props = [5.3, 21.3, 48.4, 64.0, 71.6, 73.7, 72.4, 72.8]
chengalpattu_numbers \
    = normalise_to_upper_value([males * (1.0 - male_props / 1e2) + females * (1.0 - female_props / 1e2)
       for males, females, male_props, female_props in
       zip(chengalpattu_male_numbers, chengalpattu_female_numbers,
           chengalpattu_male_tstpos_props, chengalpattu_female_tstpos_props)], upper_point_of_patch)
chengalpattu_array = np.zeros((len(chengalpattu_numbers) * 2, 2))
chengalpattu_array[:, 0] = [0] + duplicate_list_values(list(range(5, 75, 10))) + [0]
chengalpattu_array[:, 1] = duplicate_list_values(chengalpattu_numbers)

# madanapalle
madanapalle_vaccinated_numbers = [1812, 1791, 645, 415, 366]
madanapalle_unvaccinated_numbers = [2079, 1972, 678, 513, 566]
madanapalle_numbers = normalise_to_upper_value(
    [i + j for i, j in zip(madanapalle_vaccinated_numbers, madanapalle_unvaccinated_numbers)], upper_point_of_patch)
madanapalle_ages = duplicate_list_values([0] + list(range(5, 45, 10)) + [50])
madanapalle_array = np.zeros((len(madanapalle_ages), 2))
madanapalle_array[:, 0] = madanapalle_ages
madanapalle_array[:, 1] = [0] + duplicate_list_values(madanapalle_numbers) + [0]

age_patch_colour = "grey"
age_edge_colour = "black"

for n_plot in range(13):
    current_axis = age_progression_graph.add_subplot(3, 5, n_plot + 1, xlim=[-0.8, 50.], yticks=[],
                                                     xticks=list(np.linspace(0.0, 50.0, 6)))
    current_axis.set_title(titles[n_plot], fontsize=8)
    if n_plot < 6:
        average_age = age_max[n_plot] / 2.0
    elif n_plot == 6:
        average_age = 12.0
    elif n_plot == 7:
        average_age = sum([age * weight / sum(aronson_cohort_sizes)
                           for age, weight in zip(aronson_array[:, 0], aronson_cohort_sizes)])
    elif n_plot == 8:
        average_age = 9.0
    elif n_plot == 9:
        average_age = 14.75
    elif n_plot == 10:
        average_age = puerto_rico_average

    if n_plot < 6 or n_plot == 9:
        age_min = 14.0 if n_plot == 9 else 0.0
        cohort = patches.Rectangle((age_min, 0.0), age_max[n_plot], upper_point_of_patch, facecolor=age_patch_colour,
                                   edgecolor=age_edge_colour)
    elif n_plot == 6:
        cohort = patches.Polygon(georgia_schools_array, facecolor=age_patch_colour, edgecolor=age_edge_colour)
    elif n_plot == 7:
        cohort = patches.Polygon(aronson_array, facecolor=age_patch_colour, edgecolor=age_edge_colour)
    elif n_plot == 8:
        cohort = patches.Polygon(haiti_array, facecolor=age_patch_colour, edgecolor=age_edge_colour)
    elif n_plot == 10:
        cohort = patches.Polygon(puerto_rico_array, facecolor=age_patch_colour, edgecolor=age_edge_colour)
    elif n_plot == 11:
        cohort = patches.Polygon(chengalpattu_array, facecolor=age_patch_colour, edgecolor=age_edge_colour)
    elif n_plot == 12:
        cohort = patches.Polygon(madanapalle_array, facecolor=age_patch_colour, edgecolor=age_edge_colour)

    # adding and subtracting 0.5 seems to be needed because arrows come out a bit smaller than they should
    followup = patches.FancyArrowPatch(
        (average_age - 0.5, upper_point_of_patch / 2.0),
        (followups[n_plot] + average_age + 0.5, upper_point_of_patch / 2.0),
        mutation_scale=10, edgecolor="black", facecolor="darkred")

    current_axis.add_patch(cohort)
    current_axis.text(25.0, 0.7, "%s%% efficacy" % efficacies[n_plot], fontsize=7)

    # if n_plot < 7 or n_plot == 8 or n_plot == 9:
    current_axis.add_patch(followup)
    current_axis.axes.get_xaxis().set_ticklabels([])

age_progression_graph.savefig("age_progression.png")

# little scratch pad for estimating parameters to trapezoidal patch to approximate ages of georgia school study
# georgia_ages = list(range(6, 18))
# georgia_proportions = np.linspace(1., 0.075, 12)
# normalised_y_values = [value / sum(georgia_proportions) for value in georgia_proportions]
# print("average age is %s" % sum([x * y for x, y in zip(georgia_ages, normalised_y_values)]))
# print("proportion under 12 is %s" % sum(normalised_y_values[: georgia_ages.index(12)]))

