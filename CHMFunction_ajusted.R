require(devtools)
install_github('makeR', 'jbryer')
library(makeR)
calendarHeat(total$day, total$count, ncolors = 99, color = "r2b",
             varname = "Trips per day")

source("https://raw.githubusercontent.com/iascchen/VisHealth/master/R/calendarHeat.R")
#copy
calendarHeat2<-calendarHeat

#insert line to calulate day number
bl<-as.list(body(calendarHeat2))
body(calendarHeat2) <- as.call(c(
  bl[1:14], 
  quote(caldat$dom <- as.numeric(format(caldat$date.seq, "%d"))),
  bl[-(1:14)]
))

#change call to level plot
lp<-as.list(body(calendarHeat2)[[c(32,2,3)]])
lp$dom <- quote(caldat$dom)
lp$panel <- quote(function(x,y,subscripts,dom,...) {
  str(list(...))
  panel.levelplot(x,y,subscripts=subscripts,...)
  panel.text(x[subscripts],y[subscripts],labels=dom[subscripts])
})
body(calendarHeat2)[[c(32,2,3)]]<-as.call(lp)

# Appliying the funtion to TLC data
calendarHeat2(total$day, total$count, ncolors = 99, color = "r2b",
              varname = "Trips per day")

read()