## loading data and merge multiple data set
mypath <- "C:/Users/HELEN/Desktop/GitHub/Google_data_analytics_Capstone_Project/Case_Study1/trips_data"

library(tidyverse)

multimerge <- function(mypath){
  filenames = list.files(path = mypath, pattern = '.csv', full.names = TRUE)
  datalist = lapply(filenames, function(x){read.csv(file = x)})
  Reduce(function(x, y) {rbind(x, y)}, datalist)
}

df_one_year <- multimerge(mypath)
head(df_one_year)
str(df_one_year)

## drop start and end station name and id columns
#df_one_year <- df_one_year[,-c(5:8)]

## ride length refers to (start_lat, end_lat) and (start_lng, end_lng)
lat_long <- round(abs(df_one_year$end_lat - df_one_year$start_lat) * 85,2)
lng_long <- round(abs(df_one_year$end_lng - df_one_year$start_lng) * 110,2)
df_one_year$ride_length <- lat_long+lng_long
#df_one_year <- df_one_year[,-14]

## day_of_week
library(lubridate)
df_one_year$started_at <- ymd_hms(df_one_year$started_at)
df_one_year$ended_at <- ymd_hms(df_one_year$ended_at)
df_one_year$day_of_week <- weekdays(df_one_year$started_at, abbreviate = TRUE)

## ride_time(mins)
df_one_year$ride_time <- unclass(df_one_year$ended_at - df_one_year$started_at)
df_one_year$ride_time <- round(df_one_year$ride_time / 60, 2)


## write csv for tableau use
write.csv(df_one_year, 
          file = 'D:/Coursera/Google data analytics certificate/Capstone_Project/Case_Study1/trips_data/divvy_tripdata_2022.csv',
          row.names = FALSE)


## analysis (member vs casual)
#1 time v
#2 length v
#3 location
#4 month v
#5 day of week v
#6 hour v
#7 bike type v
#8 trips percentage v


### the percentage of trips by different type of member -->
### member's trips > casual's trips, however, the percentage of two type of riders are really close.
### 0.56 vs 0.44

install.packages('formattable')
library(formattable)
library(dplyr)
total_trip <- df_one_year %>% 
  select(ride_id, member_casual) %>% 
  summarize(n = n())

member_trip <- df_one_year %>% 
  select(ride_id, member_casual) %>% 
  filter(member_casual == "member") %>% 
  summarize(n = n())

member_percetage <- round(member_trip/total_trip, 2)
casual_percetage <- round((total_trip - member_trip) / total_trip, 2)
percentage <- cbind(member_percetage, casual_percetage)
colnames(percentage) <- c('member', 'casual')
percentage

### bike type overview --> casual -- docked;
### classic > electronic > docked

bike_by_member <- df_one_year %>% 
  select(rideable_type, member_casual) %>% 
  group_by(rideable_type) %>% 
  summarise(count = table(member_casual), 
            p = prop.table(table(member_casual)),
            membership = names(p))

bike_type <- ggplot(bike_by_member, aes(reorder(rideable_type, count), 
                                        count, fill = membership)) +
  geom_bar(stat = 'identity', width = 0.5) + coord_flip() + 
  geom_text(aes(label = count), size = 3.5, vjust = 2, 
            position = position_stack()) + 
  labs(title = 'Rideable Tpye Count',
       subtitle = 'By Membership Distribution',
       x = 'Type') +
  scale_y_continuous(breaks = c(0, 500000, 1000000, 1500000, 2000000, 
                                25000000, 3000000,3500000, 4000000, 
                                4500000, 5000000),
                     labels = c('0','500K','1M','1.5M','2M','2.5M',
                                '3M', '3.5M','4M','4.5M','5M'))

bike_type
  

### ride time overview by member_casual -- casual > member!!
### casual riders' time of ride nearly as three times as member riders'

ride_time <- df_one_year %>% 
  select(ride_time, member_casual) %>% 
  group_by(member_casual) %>% 
  summarise(mean_ride_time_mins = round(mean(ride_time),2))
ride_time

### ride length overview by member_casual --> member = casual(almost equal)

rlength <- df_one_year %>% 
  select(ride_length, member_casual) %>% 
  group_by(member_casual) %>% 
  summarise(mean_km = round(mean(ride_length, na.rm = TRUE),2))
rlength

###different months of trips count --> casual -- 6~8

library(ggplot2)
month <- as.character(month(df_one_year$started_at),format = '%b')
df_one_year$month <- factor(month, levels = c('1','2','3','4','5','6','7','8','9','10','11','12'))

p_month <- ggplot(df_one_year) + 
  geom_bar(mapping = aes(month, fill = member_casual), 
           position = position_fill()) + 
  geom_hline(yintercept=0.5,linetype="twodash",colour="#0000ff",size = 1)
p_month

# label my p_month plot
member_by_m <- df_one_year %>% 
  select(month, member_casual) %>% 
  group_by(month) %>% 
  summarize(count = table(member_casual), p = prop.table(table(member_casual)), 
            membership = names(p))

pp_month <- ggplot(member_by_m, aes(month, p, fill = membership)) +
  geom_bar(stat = "identity") + 
  geom_text(mapping = aes(label = paste0(round(p*100, 2), "%")),
            size = 5, colour = 'black', 
            vjust = 2, hjust = .5, position = position_stack()) + 
  labs(title = "Monthly Membership Percentage",
       subtitle = "A Stack bar plot to show the percentage of member and casual riders each month",
       y = "percentage") + 
  theme(axis.text.x = element_text(face = 'bold',
                                   size=20,angle=360,color="#333333")) + 
  theme(axis.text.y = element_text(face="bold",size=15,color="#333333")) + 
  scale_y_continuous(breaks = c(0,0.25,0.5,0.75,1) ,
                     labels =c("0%","25%","50%","75%","100%"))
pp_month

pp_month_c <- ggplot(member_by_m, aes(month, count, fill = membership))+
  geom_bar(stat = "identity") + 
  geom_text(aes(label = count),
            size = 3, colour = 'black', 
            vjust = 2, hjust = .5, position = position_stack()) + 
  labs(title = "Monthly Membership Count",
       subtitle = "A Stack bar plot to show the counts of member and casual riders each month") + 
  theme(axis.text.x = element_text(face = 'bold',
                                   size=20,angle=360,color="#333333")) + 
  theme(axis.text.y = element_text(face="bold",size=15,color="#333333"))

pp_month_c


## different hour of day of trips count --> 
## casual -- 0~3 / 22-23 > member; member -- community hour and off work hour
hour <- as.character(hour(df_one_year$started_at),format = '%H')
df_one_year$hour <- hour
df_one_year$hour <- factor(df_one_year$hour, levels = c('0','1','2','3','4','5','6',
                                    '7','8','9','10','11','12',
                                    '13','14','15','16','17','18',
                                    '19','20','21','22','23'))
# str(df_one_year)

hour_member <- df_one_year %>% 
  select(member_casual, hour) %>% 
  group_by(hour) %>% 
  summarise(count = table(member_casual),
            p = prop.table(table(member_casual)),
            membership = names(p))
# hour_member <- as.data.frame(hour_member)

hour_pl <- ggplot(hour_member, aes(hour, count, fill = membership)) + 
  geom_bar(stat = 'identity', width = 0.5, position = position_dodge()) +
  scale_y_continuous(breaks = c(0, 100000, 200000,300000,400000,
                                500000,600000),
                     labels = c('0','100K','200K','300K','400K','500K','600K')) +
  labs(title = 'Hour Trips',
       subtitle = 'By Membership')
hour_pl

### day of week --> casual: weekend; member: weekday

df_one_year$day_of_week <- factor(df_one_year$day_of_week,
                                  levels = c('Mon','Tue','Wed','Thu',
                                             'Fri','Sat','Sun'))
day_pl <- ggplot(df_one_year, aes(day_of_week, fill = member_casual)) + 
  geom_bar(width = .5, position = position_dodge()) +
  labs(title = 'Day of Week',
       subtitle = 'By Membership', x = 'day', y = 'trips') + 
  scale_y_continuous(breaks = c(0, 100000, 200000,300000,400000,
                                500000,600000),
                     labels = c('0','100K','200K','300K','400K','500K','600K')) + 
  scale_fill_discrete(name = 'membership')
day_pl


### start and end location --> casual -- restore place; member -- work place

location_start <- df_one_year %>% 
  select(member_casual, start_station_name) %>% 
  na.omit(start_station_name) %>% 
  group_by(start_station_name) %>% 
  summarise(count = table(member_casual), member = names(count))

location_start <- location_start[-(1:2),]
location_start <- location_start[location_start$count > 22000,]


location_s <- ggplot(location_start, aes(reorder(start_station_name, count)
                                         ,count,fill = member)) +
  geom_bar(stat = 'identity',width = .5, position = position_dodge())+
  geom_text(aes(label = count), size = 3, vjust = 2, 
            position = position_stack()) +
  labs(title = 'Most Popular Start Station',
       subtitle = 'By Membership', x = 'station name', y='trips') + 
  theme(axis.text.x = element_text(angle = 75,
                                   hjust = .9)) + 
  scale_x_discrete(limits = rev)
location_s

location_end <- df_one_year %>% 
  select(member_casual, end_station_name) %>% 
  na.omit(end_station_name) %>% 
  group_by(end_station_name) %>% 
  summarise(count = table(member_casual), member = names(count))

location_end <- location_end[-(1:2),]
location_end <- location_end[location_end$count > 22330,]

location_e <- ggplot(location_end, aes(reorder(end_station_name, count)
                                         ,count,fill = member)) +
  geom_bar(stat = 'identity',width = .5, position = position_dodge())+
  geom_text(aes(label = count), size = 3, vjust = 2, 
            position = position_stack()) +
  labs(title = 'Most Popular End Station',
       subtitle = 'By Membership', x = 'station name', y='trips') + 
  theme(axis.text.x = element_text(angle = 75,
                                   hjust = .9)) + 
  scale_x_discrete(limits = rev)
location_e
