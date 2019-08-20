import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from scipy.stats import norm
plt.style.use("ggplot")


def normalise_to_upper_value(list_to_adjust, value):
    return [element / max(list_to_adjust) * value for element in list_to_adjust]


def duplicate_list_values(list_to_duplicate):
    return [element for element in list_to_duplicate for _ in (0, 1)]

"""
preparation
"""

upper_point_of_patch, x_upper_lim = 0.95, 50.0
data_arrays = {}
age_progression_graph = plt.figure()
age_max = [1.0, 1.0, 1.0, 1.0, 10.0, 5.0, "", "", "", 1.5, "", "", ""]
average_ages = {}
efficacies = [81, 70, 88, 37, 85, 60, -25, 8, 89, 78, 31, -5, "", "", ""]
followups = [15.0, 10.0, 7.0, 2.5, 6.0, 5.0, 3.0, 50.0, 3.0, 20.0, 6.3, 15.0, 21.0, 3.6, 7.0]
age_patch_colour = "grey"
age_edge_colour = "black"

"""
data collation
"""

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
data_arrays["haiti"] = np.zeros((len(haiti_age_numbers), 2))
data_arrays["haiti"][:, 0] = haiti_age_brackets
data_arrays["haiti"][:, 1] = normalise_to_upper_value(haiti_age_numbers, upper_point_of_patch)

# create data structures for aronson age bracket arrays (from aronson 1948)
aronson_cohort_sizes = \
    [0] + duplicate_list_values(normalise_to_upper_value([433 + 413, 659 + 624, 387 + 351, 72 + 69],
                                                         upper_point_of_patch)) + [0]
data_arrays["aronson"] = np.zeros((len(aronson_cohort_sizes), 2))
data_arrays["aronson"][:, 0] = duplicate_list_values(list(range(0, 25, 5)))
data_arrays["aronson"][:, 1] = aronson_cohort_sizes

# georgia schools
georgia_schools_brackets = [6.0, 6.0, 17.0, 17.0]
georgia_schools_numbers = [0.0, upper_point_of_patch, 0.0833333333 * upper_point_of_patch, 0.0]
data_arrays["georgia_schools"] = np.zeros((len(georgia_schools_brackets), 2))
data_arrays["georgia_schools"][:, 0] = georgia_schools_brackets
data_arrays["georgia_schools"][:, 1] = georgia_schools_numbers

# puerto rico
puerto_rico_age_numbers = \
    [0.0, 2.5850363644096674, 3.020930801292959, 3.500606073494385, 3.5854563627084026, 3.3195814903028236,
     5.158934799251448, 5.858072473630486, 9.758873128615175, 11.15962061925825, 11.288331490302822,
     10.934655707723714, 9.74762887036407, 8.16593654304185, 7.22046189179993, 5.4413171997278,
     3.706152709254848, 2.453494492174208, 1.749053674719292]
puerto_rico_age_brackets = [0] + duplicate_list_values(list(range(1, 20)))
data_arrays["puerto_rico"] = np.zeros((len(puerto_rico_age_brackets), 2))
data_arrays["puerto_rico"][:, 0] = puerto_rico_age_brackets
data_arrays["puerto_rico"][:, 1] = duplicate_list_values(
    normalise_to_upper_value(puerto_rico_age_numbers, upper_point_of_patch)) + [0.0]
average_ages["puerto_rico"] = sum([i * j / sum(puerto_rico_age_numbers) for i, j in zip(puerto_rico_age_numbers, range(19))])

# chengalpattu
chengalpattu_male_numbers = [16199.0, 38369.0, 21289.0, 19519.0, 15700.0, 12238.0, 7739.0, 3959.0]
chengalpattu_female_numbers = [16136.0, 36093.0, 19988.0, 20259.0, 16336.0, 12088.0, 6749.0, 2511.0]
chengalpattu_male_tstpos_props = [4.9, 23.5, 62.0, 81.8, 85.2, 85.5, 82.6, 79.9]
chengalpattu_female_tstpos_props = [5.3, 21.3, 48.4, 64.0, 71.6, 73.7, 72.4, 72.8]
chengalpattu_numbers \
    = normalise_to_upper_value([males * (1.0 - male_props / 1e2) + females * (1.0 - female_props / 1e2)
       for males, females, male_props, female_props in
       zip(chengalpattu_male_numbers, chengalpattu_female_numbers,
           chengalpattu_male_tstpos_props, chengalpattu_female_tstpos_props)], upper_point_of_patch)
data_arrays["chengalpattu"] = np.zeros((len(chengalpattu_numbers) * 2, 2))
data_arrays["chengalpattu"][:, 0] = [0] + duplicate_list_values(list(range(5, 75, 10))) + [0]
data_arrays["chengalpattu"][:, 1] = duplicate_list_values(chengalpattu_numbers)

# madanapalle
madanapalle_vaccinated_numbers = [1812.0, 1791.0, 645.0, 415.0, 366.0]
madanapalle_unvaccinated_numbers = [2079.0, 1972.0, 678.0, 513.0, 566.0]
madanapalle_numbers = normalise_to_upper_value(
    [i + j for i, j in zip(madanapalle_vaccinated_numbers, madanapalle_unvaccinated_numbers)], upper_point_of_patch)
madanapalle_ages = duplicate_list_values([0] + list(range(5, 55, 10)))
data_arrays["madanapalle"] = np.zeros((len(madanapalle_ages), 2))
data_arrays["madanapalle"][:, 0] = madanapalle_ages
data_arrays["madanapalle"][:, 1] = [0] + duplicate_list_values(madanapalle_numbers) + [0]

# rand mines
rand_ages = np.linspace(0.0, 100.0, 1e2)
data_arrays["rand"] = np.zeros((len(rand_ages), 2))
data_arrays["rand"][:, 0] = rand_ages
data_arrays["rand"][:, 1] = rand_values = normalise_to_upper_value(norm.pdf(rand_ages, 30.3, 10.3), upper_point_of_patch)

# muscogee-russell trial
muscogee_russell_age_numbers = [0.0] + duplicate_list_values(
    [0.2468241835849856, 9.354591859539967, 7.280231716147719, 3.7621154826078804, 2.8368957903111927,
     2.751361064177864, 2.3271202653292953, 1.8439849456021342, 1.3459740213300453, 0.965930932138999,
     0.4088824523292338, 0.3381518134112902, 0.10529138841956076, 0.1377244973672731]) + [0.0]
muscogee_russell_age_brackets = duplicate_list_values(np.linspace(0.0, 70.0, 15))
data_arrays["muscogee-russell"] = np.zeros((len(muscogee_russell_age_numbers), 2))
data_arrays["muscogee-russell"][:, 0] = muscogee_russell_age_brackets
data_arrays["muscogee-russell"][:, 1] = normalise_to_upper_value(muscogee_russell_age_numbers, upper_point_of_patch)
muscogee_russell_average = \
    sum([i * j / sum(muscogee_russell_age_numbers) for
         i, j in zip(muscogee_russell_age_numbers, muscogee_russell_age_brackets)])

titles = ["saskatchewan", "chicago, hospital", "chicago, contact",
          "mumbai", "chicago, housing project", "agra", "georgia_schools", "aronson", "haiti",
          "english cities", "puerto_rico", "chengalpattu", "madanapalle", "rand", "muscogee-russell"]

for n_name, name in enumerate(titles):
    current_axis = age_progression_graph.add_subplot(3, 5, n_name + 1, xlim=[-0.8, x_upper_lim], yticks=[],
                                                     xticks=list(np.linspace(0.0, 50.0, 6)))
    current_axis.set_title(titles[n_name], fontsize=8)
    if n_name < 6:
        average_age = age_max[n_name] / 2.0
    elif n_name == 6:
        average_age = 12.0
    elif n_name == 7:
        average_age = sum([age * weight / sum(aronson_cohort_sizes)
                           for age, weight in zip(data_arrays["aronson"][:, 0], aronson_cohort_sizes)])
    elif n_name == 8:
        average_age = 9.0
    elif n_name == 9:
        average_age = 14.75
    elif n_name == 10:
        average_age = average_ages["puerto_rico"]
    elif n_name == 13:
        average_age = 30.3
    elif n_name == 14:
        average_age = muscogee_russell_average

    # use the pre-defined patch array if available
    if name in data_arrays:
        cohort = patches.Polygon(data_arrays[name], facecolor=age_patch_colour, edgecolor=age_edge_colour)

    # otherwise plot a rectangle
    else:
        age_min = 14.0 if n_name == 9 else 0.0
        cohort = patches.Rectangle((age_min, 0.0), age_max[n_name], upper_point_of_patch, facecolor=age_patch_colour,
                                   edgecolor=age_edge_colour)

    # adding and subtracting 0.5 seems to be needed because arrows come out a bit smaller than they should
    followup = patches.FancyArrowPatch(
        (average_age - 0.5, upper_point_of_patch / 2.0),
        (followups[n_name] + average_age + 0.5, upper_point_of_patch / 2.0),
        mutation_scale=10, edgecolor="black", facecolor="darkred")

    current_axis.add_patch(cohort)
    current_axis.add_patch(followup)
    current_axis.axes.get_xaxis().set_ticklabels([])

age_progression_graph.savefig("age_progression.png")


# little scratch pad for estimating parameters to trapezoidal patch to approximate ages of georgia school study
# georgia_ages = list(range(6, 18))
# georgia_proportions = np.linspace(1., 0.075, 12)
# normalised_y_values = [value / sum(georgia_proportions) for value in georgia_proportions]
# print("average age is %s" % sum([x * y for x, y in zip(georgia_ages, normalised_y_values)]))
# print("proportion under 12 is %s" % sum(normalised_y_values[: georgia_ages.index(12)]))

