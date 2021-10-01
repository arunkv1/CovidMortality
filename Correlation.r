library(ggplot2)
library(hrbrthemes)

# getting data
data = read.csv('/Users/arunkrishnavajjala/Documents/GMU/URA/project/USCovidPM.csv')

# sorting into their own vecots
pm <- c()
pm <- data$pm

mortality <- c()
mortality <- data$Mortality

# plotting using that data
ggplot(data, aes(x=pm, y=mortality)) +
  geom_point() +
  geom_smooth(method=lm , color="red", fill="#69b3a2", se=TRUE, ) +
  theme_ipsum()
