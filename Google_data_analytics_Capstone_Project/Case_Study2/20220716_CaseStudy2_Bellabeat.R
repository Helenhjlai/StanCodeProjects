##load data
activity <- read.csv('dailyActivity_merged.csv')
hourlycalories <- read.csv('hourlyCalories_merged.csv')
hourlyintensities <- read.csv('hourlyintensities_merged.csv')
sleep <- read.csv('sleepDay_merged.csv')
weight <- read.csv('weightLogInfo_merged.csv')
heart_rate <- read.csv('heartrate_seconds_merged.csv')

## library
library(lubridate)
library(dplyr)
library(tidyverse)
library(ggplot2)

##cleaning data
# activity dataset
activity <- activity[,-c(5:6)]

activity$ActivityDate <- as.Date(activity$ActivityDate, format = '%m/%e/%Y')

colnames(activity)[2] <- "date"

#hourlycalories
str(hourlycalories)
hourlycalories$ActivityHour <- as.POSIXct(hourlycalories$ActivityHour,
                                          format = '%m/%e/%Y %I:%M:%S %p')

hourlycalories$hTime <- format(hourlycalories$ActivityHour, "%Y-%m-%d %H")

# hourlyintensities
hourlyintensities$ActivityHour <- as.POSIXct(hourlyintensities$ActivityHour,
                                             format = '%m/%e/%Y %I:%M:%S %p')

hourlyintensities$hTime <- format(hourlyintensities$ActivityHour, "%Y-%m-%d %H")

# sleep
sleep$SleepDay <- as.Date(as.POSIXct(sleep$SleepDay, 
                                     format = '%m/%e/%Y %I:%M:%S %p'))
colnames(sleep)[2] <- "date"

# weight
weight <- weight[,-c(2,5,7,8)]

# heart_rate
heart_rate$Time <- as.POSIXct(heart_rate$Time, 
                              format = '%m/%e/%Y %I:%M:%S %p')
heart_rate$dTime <- format(heart_rate$Time,  "%Y-%m-%d")
heart_rate$hTime <- format(heart_rate$Time,  "%Y-%m-%d %H")

heart_rate_day <- heart_rate %>% 
  group_by(Id, dTime) %>%
  summarise(mean_d_value = round(mean(Value),2))
colnames(heart_rate_day)[2] <- 'date'
str(heart_rate_day)
heart_rate_day$date <- as.Date(heart_rate_day$date, format = '%Y-%m-%d')
  
heart_rate_hour <- heart_rate %>% 
  group_by(Id, hTime) %>%
  summarise(mean_h_value = round(mean(Value),2)) 

### merge activity with sleep

s_a_merged <- right_join(activity, sleep,
                    by = c('Id', 'date'))
s_a_merged <- s_a_merged[!(s_a_merged$date == '2016-04-11'),]



### merge heart_rate_hour with hourlycalories and hourlyintensities
h_c_merged <- left_join(heart_rate_hour, hourlycalories,
                        by = c('Id','hTime'))


h_c_merged <- left_join(h_c_merged, hourlyintensities,
                        by = c('Id','hTime'))

h_c_merged <- h_c_merged[,-c(4,6)]

str(h_c_merged)
h_c_merged$hTime <- as.POSIXct(h_c_merged$hTime, format = '%Y-%m-%d %H')

### merge heart_rate_day with activity and filter heart_rate is not NA
a_h_merged <- left_join(activity, heart_rate_day,
                        by = c('Id', 'date'))
a_h_merged <- a_h_merged %>% 
  filter(mean_d_value != 'NA')
colnames(a_h_merged)[14] <- 'daily_heart_rate'

### merge hourlycalories with hourlyintensities
cal_in_merged <- left_join(hourlycalories, hourlyintensities,
                           by = c('Id', 'hTime'))
cal_in_merged <- cal_in_merged[, -c(4,5)]
colnames(cal_in_merged)[2] <- 'date'

### exploratory data analysis
## insights --
## average steps = 7638
## average distance = 5.49 miles
## average sleep records = 1.115 (slightly low)
## average calories consumed = 2304
## Too long sedentary minutes 991.2
## those who records heart rate tends to have lower avg hourly heart rate value
## than those who doesn't. Moreover, having more calories consumed and higher intensity of activities
## weight performance -- average weight (KG) = 72.04, BMI = 25.19
## who will wear smart devices: heavier weight, higher BMI, wanna lose their weights.

s_a_merged %>% 
  select(TotalSteps,TotalDistance,TotalSleepRecords,
         VeryActiveMinutes, FairlyActiveMinutes, LightlyActiveMinutes,
         SedentaryMinutes, Calories, TotalMinutesAsleep, TotalTimeInBed) %>% 
  summary()

activity %>% 
  select(TotalSteps,TotalDistance,
         VeryActiveMinutes, FairlyActiveMinutes, LightlyActiveMinutes,
         SedentaryMinutes, Calories) %>% 
  summary()

h_c_merged %>% 
  select(mean_h_value, Calories, TotalIntensity) %>% 
  summary()

cal_in_merged %>% 
  select(Calories, TotalIntensity) %>% 
  summary()

weight %>% 
  select(WeightKg, BMI) %>% 
  summary()

### analysis(visualization)

## hourly calories consumed -- max: 17~19

hcc <- ggplot(cal_in_merged, aes(hour(date), Calories)) + 
  geom_bar(stat = 'identity')
hcc

## hourly intensity
hic <- ggplot(cal_in_merged, aes(hour(date), TotalIntensity)) + 
  geom_bar(stat = 'identity')
hic

install.packages('patchwork')
library(patchwork)
hcc + hic


### those who have heart rate record don't have different calories or intensity
### consumed pattern

## hourly calories consumed heart rate record
hcc_hr <- ggplot(h_c_merged, aes(hour(hTime), Calories)) + 
  geom_bar(stat = 'identity')
hcc_hr

## hourly intensity heart rate record
hic_hr <- ggplot(h_c_merged, aes(hour(hTime), TotalIntensity)) +
  geom_bar(stat = 'identity')
hic_hr


## group analysis

## very + fair minutes(exercise time) -- 31.91 mins/day per person
activity %>% 
  summarise(total_exercise = sum(VeryActiveMinutes, FairlyActiveMinutes), 
            mean_exercise = ((total_exercise/31)/33))

## fairly very light sedentary grouping -- sedentary > lightly > very > fairly

activity$sedentaryYN <- case_when(
  activity$SedentaryMinutes >= mean(activity$SedentaryMinutes) ~ 1,
  TRUE ~ 0
)
# if very active minutes > average exercise minutes, 
# then the user type will be very active.
activity$user_type <- case_when(
  activity$VeryActiveMinutes >= 32 & 
    activity$VeryActiveMinutes > activity$FairlyActiveMinutes~ 'very active',
  
  activity$FairlyActiveMinutes >= 32 &
    activity$FairlyActiveMinutes > activity$VeryActiveMinutes ~ 'fairly active',
  
  activity$sedentaryYN == 0 ~ 'lightly active',
  
  TRUE ~ 'sedentary'
  )

##  fairly very light activity sedentary vs calories 
# -- very > fairly > lightly > sedentary

user_type_num <- activity %>% 
  group_by(user_type) %>% 
  summarise(count = n())

type_num <- ggplot(user_type_num, aes(reorder(user_type, count), count)) + 
  geom_bar(stat = 'identity') + 
  geom_text(aes(label = count), vjust = -0.3) + 
  scale_x_discrete(limits = rev)
type_num

type_cal <- ggplot(activity, aes(user_type, Calories)) + 
  geom_boxplot()
type_cal

sedentary <- ggplot(activity, aes(factor(sedentaryYN))) +
  geom_bar()
sedentary

## longer sedentary minutes lower sleep records? -- No
sed_sl <- ggplot(s_a_merged, aes(factor(TotalSleepRecords)
                                        , SedentaryMinutes)) + 
  geom_boxplot() + 
  geom_point()
sed_sl

sed_sl2 <- ggplot(s_a_merged, aes(TotalMinutesAsleep, SedentaryMinutes)) + 
  geom_point() + 
  geom_smooth()
sed_sl2
  

## step | distance vs calories -- positive related

step_cal <- ggplot(activity, aes(TotalSteps, Calories)) + 
  geom_point() +
  geom_smooth() + 
  geom_hline(aes(yintercept = mean(Calories)), linetype = 5, col = "red") +
  geom_vline(aes(xintercept = mean(TotalSteps)), linetype = 5, col = 'red')
step_cal

activity$TotalDistancekm <- activity$TotalDistance * 1.6

## distance vs step to calories consumed
# --- distance affect more on calories consumed, that means 
# --- instead of steps, recording distance can be a metric to push user consumes
# --- more calories.

quantile(activity$TotalSteps)
quantile(activity$TotalDistancekm)

# step: < 7000, 7000<s<10000, >10000
# distance km: <8Km, 8Km <d<12Km, > 12Km
activity %>% 
  summarise(
    distance = factor(case_when(
      activity$TotalDistancekm > 12 ~ '>12km',
      activity$TotalDistancekm <= 12 & activity$TotalDistancekm > 8 
      ~ '>8km & <=12km',
      activity$TotalDistancekm <= 8 ~ '<=8km'
    ), levels = c('<=8km', '>8km & <=12km', '>12km')),
    step = factor(case_when(
      activity$TotalSteps > 10000 ~ '>10k',
      activity$TotalSteps >7000 & activity$TotalSteps <=10000 
      ~ '>7k & <=10k',
      activity$TotalSteps <= 7000 ~'<=7k'
    ), levels = c('>10k', '>7k & <=10k', '<=7k')),
    Calories
  ) %>% 
  ggplot(aes(step, Calories, fill = step)) + 
  geom_boxplot() + facet_wrap(~distance) + 
  labs(title='Calories Consumed by Steps and Distance') +
  theme(legend.position="none", text = element_text(size = 10),
        plot.title = element_text(hjust = 0.5))

## sleep quality vs activity -- sleep record of 3 only happened if 
## user type is very active

s_a_merged$sedentaryYN <- case_when(
  s_a_merged$SedentaryMinutes >= mean(s_a_merged$SedentaryMinutes) ~ 1,
  TRUE ~ 0
)

s_a_merged$user_type <- case_when(
  s_a_merged$VeryActiveMinutes >= 32 & 
    s_a_merged$VeryActiveMinutes > s_a_merged$FairlyActiveMinutes~ 'very active',
  
  s_a_merged$FairlyActiveMinutes >= 32 &
    s_a_merged$FairlyActiveMinutes > s_a_merged$VeryActiveMinutes ~ 'fairly active',
  
  s_a_merged$sedentaryYN == 0 ~ 'lightly active',
  
  TRUE ~ 'sedentary'
)

activity_sleep <- s_a_merged %>% 
  select(user_type, TotalSleepRecords) %>% 
  group_by(user_type) %>% 
  summarise(count = table(TotalSleepRecords),
            p = prop.table(table(TotalSleepRecords)),
            activity = factor(names(p), levels = c('3','2','1')))
activity_sleep$user_type <- factor(activity_sleep$user_type, 
                                   levels = c('sedentary',
                                              'lightly active',
                                              'fairly active',
                                              'very active'))
# stack bar plot #
activity_sleep_q <- ggplot(activity_sleep,aes(user_type, p,
                                              fill = activity))+
  geom_bar(stat = 'identity') + 
  scale_fill_brewer(palette = 'Set2') + 
  geom_text(mapping = aes(label = paste0(round(p*100, 2), "%")),
            size = 3.5, colour = 'black', 
            vjust = 2, hjust = .5, position = position_stack()) + 
  labs(title = "sleep quality by different user type",
       subtitle = "A Stack bar plot to show the percentage of different user type's sleep quality",
       y = "percentage") + 
  theme(axis.text.x = element_text(face = 'bold',
                                   size=10,angle=360,color="#333333")) + 
  theme(axis.text.y = element_text(face="bold",size=10,color="#333333")) + 
  scale_y_continuous(breaks = c(0,0.25,0.5,0.75,1) ,
                     labels =c("0%","25%","50%","75%","100%"))
activity_sleep_q

# sleep record 1: in bed hour--7.5; asleep hour--6.9
# sleep record 2: in bed hour--8.4; asleep hour--7.6
# sleep record 3: in bed hour--10.6; asleep hour--9.8

s_a_merged %>% 
  group_by(TotalSleepRecords) %>% 
  summarise(mean_bed = mean(TotalTimeInBed/60),
            mean_asleep = mean(TotalMinutesAsleep/60))

## sleep time VS activity
quantile(s_a_merged$TotalTimeInBed/60)
quantile(s_a_merged$TotalMinutesAsleep/60)
# > 8hr -- over sleep
# > 6hr & <=8hr -- normal sleep
# <= 6hr -- lack of sleep

sleep_type_df <- s_a_merged %>% 
  select(user_type,TotalTimeInBed) %>% 
  group_by(user_type) %>% 
  summarise(sleep_type = factor(case_when(
    TotalTimeInBed/60 > 8 ~ 'over sleep',
    TotalTimeInBed/60 <= 8 & TotalTimeInBed/60 >6 ~ 'normal sleep',
    TotalTimeInBed/60 <= 6 ~ 'lack of sleep'), 
    c('lack of sleep',  'normal sleep', 'over sleep'))) %>% 
  summarise(p = prop.table(table(sleep_type)),
            sleep = names(p))
sleep_type_df$user_type <- factor(sleep_type_df$user_type,
                                  levels = c('sedentary', 'lightly active',
                                             'fairly active', 'very active'))
activity_sleep_time <- ggplot(sleep_type_df, aes(user_type, p, fill = sleep)) + 
  geom_bar(position = position_dodge(), stat = 'identity') + 
  geom_text(aes(label = paste0(round(p*100, 2), "%")),
            size = 3.5, colour = 'black', 
            vjust = 2, hjust = .5, position = position_dodge(0.9)) + 
  scale_y_continuous(labels = scales::percent) +
  labs(x = NULL, fill="Sleep type") + 
  theme(legend.position="bottom",text = element_text(size = 10))
activity_sleep_time





