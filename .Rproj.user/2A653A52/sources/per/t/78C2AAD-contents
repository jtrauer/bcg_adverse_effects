
library(ggplot2)

# get data from bettag paper
bettag_starting_ages <- 
  c(19, 17, 44, 16, 30, 14, 18, 17, 15, 17, 17, 24,
    13, 16, 31, 14, 8, 18, 17, 11)
bettag_durations_months <- 
  c(2 * 12 - 3,
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
    11 * 12 - 1)
bettag_vaccinated <- 
  c(rep(1, 12), rep(0, 8))
bettag_durations_years <- bettag_durations_months / 12

# if we assume the data on ages presented is the age at vaccination
bettag_starting_ages <- bettag_starting_ages + bettag_durations_years

# frimodt_moller study - got to end of first row only
frimodt_cases <- data.frame(matrix(
  c(rep(0, 10), 1, 0, 0, 0, 1, 1, 2, 2, rep(0, 3),
    rep(0, 11), 1, 3, 1, 1, 1, 0, 1, 0, 2, 0,
    1, rep(0, 9), 1, rep(0, 4), 1, 0, 1, 0, 1, 0,
    rep(0, 9), rep(1, 4), 0, 0, 1, 0, 0, 1, 0, 0,
    0, 1, rep(0, 9), 1, 1, 2, rep(0, 7),
    rep(0, 12), 2, 0, 1, 0, 1, rep(0, 4),
    rep(0, 6), 1, 0, 0, 1, 0, 1, 3, 0, 1, 2, 2, 0, 1, 1, 0,
    rep(0, 4), 1, 0, 1, rep(0, 6), 1, 1, 0, 1, 2, rep(0, 3),
    rep(0, 6), 2, 1, 0, 0, rep(1, 3), 4, 1, rep(0, 6),
    1, 0, 0, 2, 1, 0, 2, 1, rep(0, 3), 2, 2, 1, rep(0, 7)), 
  ncol=10))
colnames(frimodt_cases) <- c(0, seq(5, 35, 10), 0, seq(5, 35, 10))


# bettag plot
marker = 16
bettag_vaccinated_colour = "red"
unbettag_vaccinated_colour = "blue"
plot(bettag_durations_years[bettag_vaccinated == 1], bettag_starting_ages[bettag_vaccinated == 1], 
     col=bettag_vaccinated_colour, pch=marker, xlab="Time from vaccination", ylab="Age", xlim=c(0, 11), ylim=c(0, 48))
points(bettag_durations_years[bettag_vaccinated == 0], bettag_starting_ages[bettag_vaccinated == 0], col=unbettag_vaccinated_colour, pch=marker)
legend(5, 45, legend=c("Vaccinated", "Unvaccinated"), col=c(bettag_vaccinated_colour, unbettag_vaccinated_colour), pch=marker)


qplot(bettag_durations_years[bettag_vaccinated == 1], bettag_starting_ages[bettag_vaccinated == 1])
