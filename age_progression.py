import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
plt.style.use("ggplot")


def normalise_to_upper_value(list_to_adjust, value):
    return [element / max(list_to_adjust) * value for element in list_to_adjust]


def duplicate_list_values(list_to_duplicate):
    return [element for element in list_to_duplicate for _ in (0, 1)]


upper_point_of_patch = 0.9

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
          "Mumbai", "Chicago, housing project", "Agra", "Georgia schools", "Muscogee-Russell", "Haiti",
          "English cities"]
age_max = [1.0, 1.0, 1.0, 1.0, 10.0, 5.0, "", "", "", 1.5]
efficacies = [81, 70, 88, 37, 85, 60, "?", "", 89, 78]
followups = [15.0, 10.0, 7.0, 2.5, 6.0, 5.0, 3.0, "?", 3.0, 20.0]

# create data structures for aronson age bracket arrays
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

age_patch_colour = "grey"

for n_plot in range(10):
    current_axis = age_progression_graph.add_subplot(3, 4, n_plot + 1, xlim=[0.0, 50.], yticks=[],
                                                     xticks=list(np.linspace(0.0, 50.0, 6)))
    current_axis.set_title(titles[n_plot], fontsize=8)
    if n_plot < 6:
        average_age = age_max[n_plot] / 2.0
    elif n_plot == 6:
        average_age = sum([age * prop / sum(georgia_schools_numbers) for
                           age, prop in zip(georgia_schools_brackets, georgia_schools_numbers)])
    elif n_plot == 8:
        average_age = \
            sum([age * prop / sum(haiti_age_numbers) for age, prop in zip(haiti_age_brackets, haiti_age_numbers)])
    elif n_plot == 9:
        average_age = 14.75

    if n_plot < 6 or n_plot == 9:
        age_min = 14.0 if n_plot == 9 else 0.0
        cohort = patches.Rectangle((age_min, 0.0), age_max[n_plot], upper_point_of_patch, color=age_patch_colour)
    elif n_plot == 6:
        cohort = patches.Polygon(georgia_schools_array, color=age_patch_colour)
    elif n_plot == 7:
        cohort = patches.Polygon(aronson_array, color=age_patch_colour)
    elif n_plot == 8:
        cohort = patches.Polygon(haiti_array, color=age_patch_colour)

    if n_plot < 7 or n_plot == 8 or n_plot == 9:

        # adding and subtracting 0.5 seems to be needed because arrows come out a bit smaller than they should
        followup = patches.FancyArrowPatch(
            (average_age - 0.5, upper_point_of_patch / 2.0),
            (followups[n_plot] + average_age + 0.5, upper_point_of_patch / 2.0),
            mutation_scale=16, edgecolor="darkred", facecolor="darkred")

    current_axis.add_patch(cohort)
    current_axis.text(25.0, 0.7, "%s%% efficacy" % efficacies[n_plot], fontsize=7)

    if n_plot < 7 or n_plot == 8 or n_plot == 9:
        current_axis.add_patch(followup)
        current_axis.axes.get_xaxis().set_ticklabels([])

age_progression_graph.savefig("age_progression.png")

# little scratch pad for estimating parameters to trapezoidal patch to approximate ages of georgia school study
# georgia_ages = list(range(6, 18))
# georgia_proportions = np.linspace(1., 0.075, 12)
# normalised_y_values = [value / sum(georgia_proportions) for value in georgia_proportions]
# print("average age is %s" % sum([x * y for x, y in zip(georgia_ages, normalised_y_values)]))
# print("proportion under 12 is %s" % sum(normalised_y_values[: georgia_ages.index(12)]))

