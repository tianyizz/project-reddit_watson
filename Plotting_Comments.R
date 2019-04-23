# Description: This program creates a graph of the number of comments over time and 
#              overlays given key events on said graph.

library(dplyr)
library(readr)
library(ggplot2)
library(reshape2)
library(lubridate)
# combine data files

# get all csv file paths
#CHANGE TO CORRECT CSV PATH
path <- "C:/Desktop/largeResult.csv" 
# df <- read.csv(path,
#                quote = "", 
#                row.names = NULL, 
#                stringsAsFactors = FALSE)
df <- readr::read_csv(path)
# df_copy <- df

# convert to standard datetime
df <-
  df %>%
  mutate(
    time = as.POSIXct(time, origin='1970-01-01')
  )

# plot stuff

# plotting trends through time
min(df$time)
max(df$time)

# April 5th, 2016: Vive released
# January 6th, 2017: First Vive Summit announced
# November 2017: Tetherless Vive upgrade kit announced
# June 2017: New Finger-Tracking Controllers announced
# December 12th, 2017: Fallout 4 VR packaged with any purchase of an HTC Vive
# May 4th, 2018: HTC Vive Ecosystem conference date set for May 25th, 2018

# To add more events, simply insert the date (yyy-mm-dd) in dates
# and match it to the event name in label in chronological order
dates <- c('2016-04-05', '2017-01-06','2017-11-1','2017-06-01','2017-12-12','2018-05-04')
label <- c('Vive Released','First Vive Summit\nAnnounced', 'Tetherless Vive Upgrade\nKit Announced', 'New Finger-Tracking\nControllers Announced', 'Promotion with Fallout 4 VR', 'HTC Vive Ecosystem\nConferenced Announced')
height <- c(75000,25000,22000,20000,15000,14000)

df_events <- data.frame(date = ymd(dates),
                        label = label) %>%
  mutate(
    year = year(date),
    week = week(date)
  ) %>%
  dplyr::select(-date)

#df_plot <- merge(df %>% mutate(date=as.Date(time)) %>% View(), df_events, by.x = )

df %>%
  mutate(
    year = year(time),
    month = month(time),
    day = day(time),
    week = week(time)
  ) %>% 
  dplyr::group_by(year,week) %>%
  dplyr::summarize(
    num_comments = n()
  ) %>% 
  merge(df_events, by = c('year', 'week'), all.x=T, all.y=F) %>%
  mutate(
    # time = ymd(paste0(year, '-', month, '-', day))
    time = date_decimal(year + (week-1)/52)
  ) %>%
  ggplot(aes(x=time,y=num_comments)) + 
  geom_line() +
  labs(x = 'Time', y = 'Number of Comments', title = 'Number of Comments Over Time') +
  geom_text(aes(y=num_comments+10000, label=label), check_overlap=T )
  





