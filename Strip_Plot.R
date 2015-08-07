source("http://www.staff.uni-marburg.de/~appelhat/r_stuff/strip.R")

year <- substr(as.character(totalxhour$hour), 1, 4)

## PLOT STRIP FOR HOURLY ACTIVITY
strip(x = totalxhour$count, 
      date = totalxhour$hour,
      cond = year,
      arrange = "wide",
      main = "trips")
