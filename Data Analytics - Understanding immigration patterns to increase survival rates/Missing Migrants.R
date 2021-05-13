setwd("C:\\Users\\aua\\Documents\\IST707 Final Project")
library(readxl)

MissingMigrants <- read_xlsx("MissingMigrants-Global.xlsx", col_names = TRUE) 

# Convert to data frame
MissingMigrantsDF <- as.data.frame(MissingMigrants)
# Remove web id column
MissingMigrantsDF <- MissingMigrantsDF[,-1]
# Remove first row
MissingMigrantsDF <- MissingMigrantsDF[-1,]
# Remove excess coloumns
MissingMigrantsDF <- MissingMigrantsDF[,-13:-19]

# Fix variable types
#str(MissingMigrantsDF)
MissingMigrantsDF[is.na(MissingMigrantsDF)] <- 0
# Fix column names
NamesOfColumns <- c("Region_of_Incident", "Reported_Date", "Reported_Year", "Reported_Month", "Number_Dead", "Min_Est_Num_Missing",
                    "Total_Dead_Missing", "Num_of_Survivors", "Num_of_Females", "Num_of_Males", "Num_of_Children", "Cause_of_Death")
MissingMigrantsDF <- setNames(MissingMigrantsDF, NamesOfColumns)
MissingMigrantsDF$Reported_Month <- as.factor(MissingMigrantsDF$Reported_Month)
MissingMigrantsDF$Region_of_Incident <- as.factor(MissingMigrantsDF$Region_of_Incident)
MissingMigrantsDF[,5] <- as.numeric(MissingMigrantsDF[,5])
MissingMigrantsDF[,6] <- as.numeric(MissingMigrantsDF[,6])
MissingMigrantsDF[,7] <- as.numeric(MissingMigrantsDF[,7])
MissingMigrantsDF[,8] <- as.numeric(MissingMigrantsDF[,8])
MissingMigrantsDF[,9] <- as.numeric(MissingMigrantsDF[,9])
MissingMigrantsDF[,10] <- as.numeric(MissingMigrantsDF[,10])
MissingMigrantsDF[,11] <- as.numeric(MissingMigrantsDF[,11])
MissingMigrantsDF[,12] <- tolower(MissingMigrantsDF[,12])
#table(MissingMigrantsDF$Cause_of_Death)

# Assign categories to cause of death
MissingMigrantsDF$CoD_Category <- 0

# Assign causes of death to categories
library(dplyr)
library(data.table)
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "unknown"] <- "unknown")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "mixed"] <- "unknown")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "exhaustion"] <- "illness")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "accident"] <- "accident")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "crushed"] <- "accident")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "plane"] <- "accident")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "exposure"] <- "envirnoment")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "rockslide"] <- "envirnoment")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "weather"] <- "envirnoment")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "skeletal"] <- "envirnoment")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "mummified"] <- "envirnoment")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "hyperthermia"] <- "envirnoment")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "hypothermia"] <- "envirnoment")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "envenomation"] <- "envirnoment")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "electrocution"] <- "accident")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "fire"] <- "accident")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "fall"] <- "accident")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "gassed"] <- "envirnoment")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "suffocation"] <- "accident")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "sickness"] <- "illness")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "coronary"] <- "illness")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "stroke"] <- "illness")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "organ"] <- "illness")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "pneumonia"] <- "illness")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "post-partum"] <- "illness")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "hypoglycemia"] <- "illness")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "burned"] <- "accident")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "burns"] <- "accident")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "asphyxiation"] <- "accident")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "vehicle"] <- "vehicle")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "cancer"] <- "illness")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "cardiac"] <- "illness")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "exhaustion"] <- "illness")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "illness"] <- "illness")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "edema"] <- "illness")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "harsh"] <- "envirnoment")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "apache"] <- "violence")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "violence"] <- "violence")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "injuries"] <- "violence")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "abuse"] <- "violence")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "killed"] <- "violence")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "hanging"] <- "violence")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "sexual"] <- "sexual_abuse")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "rape"] <- "sexual_abuse")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "vehicle"] <- "vehicle")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "car"] <- "vehicle")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "truck"] <- "vehicle")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "train"] <- "train")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "railway"] <- "train")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "drowning"] <- "drowning")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "murdered"] <- "violence")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "stabbed"] <- "violence")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "shot"] <- "violence")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "starvation"] <- "dehydration_starvation")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "dehydradtion"] <- "dehydration_starvation")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "dehydration"] <- "dehydration_starvation")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "malnutrition"] <- "dehydration_starvation")
MissingMigrantsDF <- within(MissingMigrantsDF, CoD_Category[Cause_of_Death %like% "suicide"] <- "suicide")


# Turn character data to factor
MissingMigrantsDF <- MissingMigrantsDF %>% 
  mutate_if(is.character, funs(as.factor))

# Create data frame for ARM
MissingMigrantsARM <- as.data.frame(MissingMigrantsDF) %>% 
  select(-Reported_Date) %>% 
  mutate_if(is.character, funs(as.factor))
# Remove columns as other column is the sum of these two columns
MissingMigrantsARM <- MissingMigrantsARM[,-4:-5]
# Take out column of cause of dealth not categorized
MissingMigrantsARM <- MissingMigrantsARM[,-9]

# Discretize data 
MissingMigrantsARM$Total_Dead_Missing <- 
  cut(MissingMigrantsARM$Total_Dead_Missing, breaks=c(-Inf, 5, 10, 50, Inf), 
      labels=c("Low", "Med","High", "Very_High"))
MissingMigrantsARM$Num_of_Survivors <- 
  cut(MissingMigrantsARM$Num_of_Survivors, breaks=c(-Inf, 5, 10, 50, Inf), 
      labels=c("Low", "Med","High", "Very_High"))
MissingMigrantsARM$Num_of_Females <- 
  cut(MissingMigrantsARM$Num_of_Females, breaks=c(-Inf, 0, 5, 10, 50, Inf), 
      labels=c("Zero", "Low", "Med","High", "Very_High"))
MissingMigrantsARM$Num_of_Males <- 
  cut(MissingMigrantsARM$Num_of_Males, breaks=c(-Inf, 0, 5, 10, 50, Inf), 
      labels=c("Zero", "Low", "Med","High", "Very_High"))
MissingMigrantsARM$Num_of_Children <- 
  cut(MissingMigrantsARM$Num_of_Children, breaks=c(-Inf, 0, 5, 10, 50, Inf), 
      labels=c("Zero", "Low", "Med","High", "Very_High"))
#str(MissingMigrantsARM)

MissingMigrantsARM1 <- subset.data.frame(MissingMigrantsARM, Total_Dead_Missing == "Very_High")


# Generate rules 
Highest_Totals <- apriori(data = MissingMigrantsARM1, parameter = list(supp=0.025, conf=1.0, minlen=4),
                          appearance = list(default="lhs", rhs="Total_Dead_Missing=Very_High"),
                          control = list(verbose=F))
Highest_Totals <- sort(Highest_Totals, decreasing = TRUE, by="confidence")
inspect(Highest_Totals[1:10])

# Decision Tree
# Create data frame for Decision Tree removing reported date and cause of dealth
MissingMigrantsDT <- as.data.frame(MissingMigrantsDF[-c(2,12)]) 


# Take samples for training and testing
set.seed(123)
nrows <- nrow(MissingMigrantsDT)
sample_size <- round(0.8*nrows)
training_index <- sample(1:nrows, size = sample_size, replace = FALSE)
DT_train <- MissingMigrantsDT[training_index, ]
DT_test <- MissingMigrantsDT[-training_index, ]
# Remove labels of testing data frame
DT_Test_Labels <- DT_test$CoD_Category
DT_test <- DT_test[,-11]
TestLabels <- DT_Test_Labels


# Train the data with a decision tree
library(rpart)
library(rpart.plot)
library(RColorBrewer)
library(rattle)
Treefit <- rpart(DT_train$CoD_Category ~., data = DT_train, method = "class")
#summary(Treefit)
fancyRpartPlot(Treefit)

predicted = predict(Treefit, DT_test, type = "class")
(Results <- data.frame(Predicted=predicted, Actual=TestLabels))

# Create confusion matrix
library(caret)
library(e1071)
confusionMatrix(predicted, TestLabels )


# Add minisplit to tree model
Treefit2 <- rpart(DT_train$CoD_Category ~., data = DT_train, method = "class", 
                  control = rpart.control(minsplit = 3, cp=0))
summary(Treefit2)
fancyRpartPlot(Treefit2)

# Test decision tree on test data
predicted1 = predict(Treefit2, DT_test, type = "class")
(Results <- data.frame(Predicted=predicted1, Actual=TestLabels))


confusionMatrix(predicted1, TestLabels )

library(randomForest)
MissingMigrantsRF <- randomForest(CoD_Category ~ ., data = DT_train)
print(MissingMigrantsRF)
"
#library(reprtree)
#plot.getTree(MissingMigrantsRF, labelVar=TRUE)"

# Prediction
pred_RF <- predict(MissingMigrantsRF, DT_test)
# Check classification accuracy
confusionMatrix(pred_RF, TestLabels)



g <- MissingMigrantsDF %>% group_by(Region_of_Incident, CoD_Category) %>% summarise(sum(Total_Dead_Missing))
h <- MissingMigrantsDF %>% group_by(Region_of_Incident, CoD_Category) %>% tally()
i <- MissingMigrantsDF %>% group_by(Region_of_Incident) %>% summarise(sum(Num_of_Children))
j <- MissingMigrantsDF %>% group_by(CoD_Category) %>% summarise(sum(Num_of_Children)) 
k <- MissingMigrantsDF %>% group_by(CoD_Category) %>% summarise(sum(Num_of_Females))
l <- MissingMigrantsDF %>% group_by(CoD_Category) %>% summarise(sum(Num_of_Males))

g$total<-g$`sum(Total_Dead_Missing)`
g

# Plot y = # dead / missing
library(ggplot2)
m <- ggplot(data = g) + geom_bar(mapping = aes(x=Region_of_Incident, y=total, fill = CoD_Category))
m <- m + theme(axis.text.x = 
                 element_text(angle = 90, hjust = 1))
m

m2 <- ggplot(g) + geom_bar(mapping=aes(x=reorder(Region_of_Incident, total), y=total, fill=CoD_Category), stat="identity") + ggtitle("Number of missing or dead migrants between 2014-2019") + ylab("Total Dead or Missing") + xlab("Geography of Incident")
m2 <- m2 + theme(axis.text.x = element_text(angle = 90, hjust = 1))
m2

MissingMigrantsDF$CoD_Category



## select females & children where dead or missing = >1
## keep: region of incident & CoD Category
#g$category <- MissingMigrantsDF$CoD_Category
