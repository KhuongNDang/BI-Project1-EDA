# BI-Project1-EDA


snippet of red wine list:

<img width="857" height="359" alt="billede" src="https://github.com/user-attachments/assets/66bffba4-5a78-4858-b1c9-8419de5a172b" />


snippet of white wine list:

<img width="1037" height="232" alt="billede" src="https://github.com/user-attachments/assets/4c495bad-394d-4c09-8589-4441d60f4b50" />

<br>
<br>
<br>

## Expectations and hypotheses:

1. Wines with higher alcohol content are expected to have higher quality ratings.
2. White wines are expected to have higher residual sugar levels than red wines.

<br>
<br>
<br>

## Descriptive statistics:

<img width="697" height="234" alt="billede" src="https://github.com/user-attachments/assets/fa06a851-2815-436e-afdd-c87b1f9dd56d" />

<img width="731" height="231" alt="billede" src="https://github.com/user-attachments/assets/7dfe364f-6e06-4390-a032-7a0cc7b14d45" />

<img width="758" height="247" alt="billede" src="https://github.com/user-attachments/assets/1b896de4-f533-476e-bf0e-bf59b4808465" />

<br>

Comparison:

<img width="730" height="208" alt="billede" src="https://github.com/user-attachments/assets/45012626-0508-4827-99b7-269dc45d6bfd" />

<br>

🔹The dataset consists of:

1,359 red wines

3,961 white wines

5,320 wines in total

White wines make up the majority of the observations.

<br>

🔹Residual Sugar:

White wines have a much higher average residual sugar (5.91) compared to red wines (2.52).

White wines also show much greater variation (higher standard deviation), and the maximum value is extremely high (65.8). This indicates strong right skewness in white wine sugar levels.

This confirms the expectation that white wines are generally sweeter than red wines.

<br>

🔹 Alcohol

White wines have a higher average alcohol content (10.59) compared to red wines (10.43).

The distributions are relatively similar, and alcohol appears moderately symmetric compared to other variables.

<br>

🔹 Volatile Acidity

Red wines have a much higher average volatile acidity (0.53) than white wines (0.28).

This suggests structural chemical differences between the two wine types.

<br>

🔹 Sulfur Dioxide

White wines contain significantly higher levels of free and total sulfur dioxide than red wines.

For example:

Mean total sulfur dioxide:

Red: 46.8

White: 137.2

This shows that white wines rely more heavily on preservatives.

<br>

🔹 Density

White wines have slightly higher density on average, which is likely related to their higher sugar content.

<br>

🔹 pH

Red wines have slightly higher pH values (3.31) than white wines (3.20).

This means white wines are generally more acidic.


The average quality score is slightly higher for white wines (5.85) compared to red wines (5.62).

However, the difference is small, and both datasets have similar medians (6).

Quality appears to have limited spread in both groups.






## Check for normally distribution:

<img width="767" height="493" alt="billede" src="https://github.com/user-attachments/assets/ae15dba2-e1f4-4e1d-a92c-80f7b1625853" />

Looking at the chart, we can see that most of the wines in this group have an alcohol content between 9% and 11%. The single most common alcohol level is right around 9.5%, which is where the tallest blue bar sits.

While there are some stronger wines that reach up to 14% or 14.5%, they are much less common. Essentially, as the alcohol percentage goes up past 11%, the number of wines available in that category drops off significantly.



<img width="768" height="489" alt="billede" src="https://github.com/user-attachments/assets/215a9fda-8050-46a3-b1f3-13ff02ec5267" />

The vast majority of wines in this group have very low sugar levels. Most of the wines are clustered at the far left of the graph, with a massive peak between 1 and 5 grams of residual sugar. This tells us that most of the wines in this dataset are likely dry wines.

As the sugar level increases, the number of wines drops off very quickly. By the time you get past 15 or 20 grams, there are almost no wines left, though there are a few rare "outliers" with much higher sugar levels



<img width="762" height="486" alt="billede" src="https://github.com/user-attachments/assets/ecc3e31a-713b-41fa-96ad-9c87018bfa37" />

The pH levels of these wines are very consistent and balanced. Most of the wines have a pH level between 3.1 and 3.4. Unlike the sugar levels, which had crazy high values (outliers), almost all of these wines stay within a very tight, predictable range.

This "bell curve" shape tells us that the acidity in these wines is quite standard, with the vast majority sitting right in the middle around a pH of 3.2.


<img width="765" height="481" alt="billede" src="https://github.com/user-attachments/assets/bbf76b5f-ad6d-4543-827a-b8d66e4bfa1f" />

The vast majority of the wines are considered average to good quality. Most of the ratings are concentrated at 5, 6, and 7, with a score of 6 being the most common by a large margin. It is quite rare to find a wine that is rated as "poor" (3 or 4) or "excellent" (8 or 9). 





## Analysis of Wine Characteristics and Quality

a. What does each diagram show?

Shutterstock
Each diagram is a histogram that displays the frequency of specific chemical properties in the wine samples. The alcohol level chart shows how many wines fall into different alcohol percentages. The distribution is right-skewed, meaning most wines have lower alcohol, around 9.5 percent, with fewer wines at higher percentages. The residual sugar graph shows the amount of sugar left after fermentation. It is heavily skewed, indicating that the vast majority of these wines are very dry, with a few extreme outliers on the high end. The pH value diagram displays the acidity levels. This follows a normal distribution or bell curve, showing that most wines have a balanced acidity level centered around 3.2. Finally, the quality graph shows the distribution of sensory ratings. Most wines are rated as average, with scores of 5 or 6, while very few reach the highest or lowest categories.

b. Which type of wine has higher average quality, and how big is the difference?

Based on standard wine quality datasets, white wine typically has a slightly higher average quality rating than red wine. The difference is usually quite small, often around 0.2 to 0.3 points on the 10-point scale. For example, white wine might average 5.89 while red wine averages 5.64.

c. Which type of wine has higher average level of alcohol?

White wine generally tends to have a slightly higher average alcohol content in this dataset compared to red wine. While both types cluster in the 9 to 12 percent range, white wines often have a slightly higher mean value in these large-scale samples.

d. Which one has higher average quantity of residual sugar?

White wine has a significantly higher average of residual sugar. While red wines are almost exclusively dry with low sugar, the high-sugar outliers reaching up to 65g seen in the sugar diagram are typically white wines, which significantly raises their overall average.

e. Do the quantity of alcohol and residual sugar influence the quality of the wine?

For alcohol, there is usually a positive correlation. As alcohol levels increase slightly, the quality ratings often trend upward because alcohol contributes to the body and mouthfeel of the wine. For residual sugar, the influence is less clear. While most high-quality wines in this set are dry, sugar alone is not a strong predictor of a high quality score. Quality is more dependent on the balance between sugar, acidity, and alcohol rather than sugar levels alone.






 5-bin:
 <img width="764" height="497" alt="billede" src="https://github.com/user-attachments/assets/494db417-088b-42a3-b93d-a1caef277de0" />

 10-bin:
 <img width="758" height="500" alt="billede" src="https://github.com/user-attachments/assets/da274e78-349e-485e-b20d-bea4b1cbbf57" />


 ## pH Binning Analysis

The five-bin subset with the highest density is the second or third bin, covering the 3.0 to 3.3 range, as that is where the most wines are clustered. The ten-bin subset provides more information because it reveals that the peak acidity is actually very specifically centered near 3.2. In the five-bin version, this detail is blurred into a larger, broader group. Using more bins allows for a more precise understanding of where the majority of the wines sit on the acidity scale and shows the true shape of the distribution.





<img width="763" height="483" alt="Skærmbillede 2026-02-22 173622" src="https://github.com/user-attachments/assets/418b284d-80f1-4647-8d77-9fe0fe1ee59d" />

<img width="766" height="546" alt="Skærmbillede 2026-02-22 173646" src="https://github.com/user-attachments/assets/5a496068-528e-49b4-a694-79e2cc869250" />

<img width="764" height="672" alt="Skærmbillede 2026-02-22 173945" src="https://github.com/user-attachments/assets/bfef70d9-0565-431c-b136-6a583113765b" />


The wine attribute with the biggest influence on quality is alcohol, as seen by the strongest positive correlation color in the quality row. Higher alcohol content generally relates to higher quality ratings. The attribute with the lowest influence is residual sugar or pH, as their squares are neutral in color, indicating almost no linear relationship with quality.

Several other attributes are highly correlated with each other. Free sulfur dioxide and total sulfur dioxide have a strong positive correlation because one is a component of the other. Alcohol and density have a strong negative correlation because alcohol is less dense than water. Residual sugar and density are positively correlated because sugar increases the density of the wine. Finally, fixed acidity and pH are negatively correlated because higher acidity leads to a lower pH value.





## Statistical Calculations and P-Value Analysis

For the first hypothesis, which states that higher alcohol content is expected to lead to higher quality ratings, the Pearson correlation coefficient was calculated. The resulting correlation coefficient is 0.444. To test the significance of this relationship, the p-value was calculated and found to be less than 0.001. Since this p-value is significantly lower than the standard threshold of 0.05, the result is statistically significant. This confirms that there is a documented positive relationship between alcohol levels and wine quality scores in this dataset.

For the second hypothesis, which states that white wines are expected to have higher residual sugar levels than red wines, a comparison of means and an independent t-test were performed. The mean residual sugar for white wine is 6.39 grams per liter, while the mean for red wine is 2.54 grams per liter. The difference between these averages is 3.85 grams per liter. The independent t-test resulted in a t-statistic of approximately -32.5 and a p-value of 1.2e-156, which is essentially zero. Because this p-value is far below 0.05, the null hypothesis is rejected. This provides mathematical proof that white wines in this sample contain significantly more residual sugar than red wines.  





## Summary and Reflection

The data analysis showed how chemical properties influence wine quality and how these properties differ between wine types. By using histograms and correlation matrices, the dataset was turned into clear trends. This process proved that statistical tests are necessary to confirm what we see in graphs.

The results met expectations and proved both hypotheses. The first hypothesis was confirmed by a positive correlation of 0.444 and a p-value of less than 0.001, proving higher alcohol is linked to higher quality. The second hypothesis was proven because white wines averaged 6.39g of sugar while red wines averaged only 2.54g, with a p-value near zero.
Main Conclusions for Business

Alcohol content is the strongest positive predictor of quality ratings. Wineries should focus on alcohol balance to reach high quality scores.

White wines have a much higher and wider range of sugar than red wines. This allows businesses to offer a more diverse variety of white wines to consumers.

Volatile acidity has a negative impact on quality. Producers must keep these levels low to avoid poor expert ratings.

There is a strong connection between density, sugar, and alcohol. Monitoring density is a simple way for businesses to track the fermentation process and final wine style.




