data = read.csv('/Users/arunkrishnavajjala/Documents/GMU/URA/aqs/csndat2010-2019-nocor.csv')

data[8:14] <- list(NULL)
data[4:5] <- list(NULL)

data$Date.Local <- as.Date(data$Date.Local, format = "%Y-%m-%d")


data <- data %>% distinct(data$Date.Local, .keep_all = TRUE)

long_unite <- unite(data, State.Code, County.Code, Site.Number, sep = ".")

final_df <- as.data.frame(t(data))


cor(df$Sample.Measurement, data$Sample.Measurement, use = "pair") 

