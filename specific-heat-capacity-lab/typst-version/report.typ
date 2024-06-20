#import "template.typ": template
#show: doc => template(
  title: [Specific Heat Capacity Lab],
  authors: ([Vincent Edwards], [Ali Mortada], [Andrew Bringas]),
  date: datetime(year: 2023, month: 3, day: 8),
  college: [Mt. San Antonio College],
  course: [Phsics 4B],
  crn: 42240,
  citations: "citations.yml",
  doc
)

= Purpose

The goal of the experiment was to determine the specific heat capacities of various substances based on measurements of mass, temperature, power, and/or time.
For parts 1 and 2 the material was known, so the calculated specific heat capacities could be compared to the accepted values.
For part 3 the material was unknown, so its identity was guessed based on the calculated specific heat capacity.

= Results

In part 1 of the experiment, a sample of DI water stored in a foam calorimeter was heated using an immersion heater for about 2 minutes, causing the temperature of the water to increase.
@tab-part-1-measurements contains the measured values.
$m_c$ is the mass of the dry calorimeter.
$m_(c+w)$ is the combined mass of the water and calorimeter.
$T_i$ is the initial temperature of the water.
$T_f$ is the final temperature of the water.
$H$ is the heat current delivered by the immersion heater, measured using a Watt meter.
$t$ is the time the immersion heater was on, measured using a stopwatch.

#figure(
  table(
    columns: 2,
    [Quantity],[Value],
    $m_c$     ,[$33.02 plus.minus 0.01$ g],
    $m_(c+w)$ ,[$439.19 plus.minus 0.01$ g],
    $T_i$     ,[$20.2 plus.minus 0.4$ #sym.degree.c],
    $T_f$     ,[$38.5 plus.minus 0.4$ #sym.degree.c],
    $H$       ,[$293 plus.minus 1$ W],
    $t$       ,[$120.2 plus.minus 0.2$ s],
  ),
  caption: [Part 1 Measurements],
) <tab-part-1-measurements>

@tab-material-key contains a material key.
A number was given to each material for which the specific heat capacity was calculated.
In addition, the table notes the lab part where the substance was examined.
These numbers are used to index @tab-part-2-and-3-measurements and @tab-specific-heat.

#figure(
  table(
    columns: 3,
    [Key],[Lab Part],[Material],
    [1]  ,[1]       ,[Water],
    [2]  ,[2]       ,[Aluminum (1 piece)],
    [3]  ,[2]       ,[Lead],
    [4]  ,[2]       ,[Aluminum (2 pieces)],
    [5]  ,[3]       ,[Unknown green rock (letter D)],
  ),
  caption: [Material Key],
) <tab-material-key>

In parts 2 and 3 of the experiment, samples of various materials were submerged in boiling water for about 2 minutes to heat them up to a high temperature (the boiling point of water).
One at a time, these samples were transferred to a foam calorimeter containing room temperature DI water.
This caused the sample temperature to decrease and the water temperature to increase until they reached thermal equilibrium.
Table @tab-part-2-and-3-measurements contains the measured values.
$m_c$ is the mass of the dry calorimeter.
$m_(c+w)$ is the combined mass of the water and calorimeter.
$m_m$ is the mass of the sample material.
$T_(i w)$ is the initial temperature of the water.
$T_(i m)$ is the initial temperature of the sample material.
$T_f$ is the final temperature of the water and sample material.

#figure(
  table(
    columns: 7,
    [Key],[$m_c$ (g)],[$m_(c+w)$ (g)],[$m_m$ (g)],[$T_(i w)$ (#sym.degree.c)],[$T_(i m)$ (#sym.degree.c)],[$T_f$ (#sym.degree.c)],
    [2]  ,$31.85 plus.minus 0.01$,$531.6 plus.minus 0.1$,$88.26 plus.minus 0.01$,$21.5 plus.minus 0.4$,$99.1 plus.minus 0.4$,$24.4 plus.minus 0.4$,
    [3]  ,$31.85 plus.minus 0.01$,$531.3 plus.minus 0.1$,$370.26 plus.minus 0.01$,$24.2 plus.minus 0.4$,$99.1 plus.minus 0.4$,$26.0 plus.minus 0.4$,
    [4]  ,$31.85 plus.minus 0.01$,$530.3 plus.minus 0.1$,$175.42 plus.minus 0.01$,$25.9 plus.minus 0.4$,$99.1 plus.minus 0.4$,$30.9 plus.minus 0.4$,
    [5]  ,$31.85 plus.minus 0.01$,$529.9 plus.minus 0.1$,$161.14 plus.minus 0.01$,$30.0 plus.minus 0.4$,$99.1 plus.minus 0.4$,$33.3 plus.minus 0.4$,
  ),
  caption: [Material Key],
) <tab-part-2-and-3-measurements>

@tab-specific-heat contains the calculated specific heat capacity ($c$) for each material examined in the experiment.
In addition, it contains the accepted, true specific heat capacity for those materials ($c_"true"$) and how far off the experimental values were from the true values ($c - c_"true"$).

#figure(
  table(
    columns: 4,
    [Key],[$c$ (J/(kg K))],[$c_"true"$ (J/(kg K))],[$c - c_"true"$ (J/(kg K))],
    [1]  ,$4740 plus.minus 150$,$4186$,$550  plus.minus 150$,
    [2]  ,$920  plus.minus 180$,$910 $,$10   plus.minus 180$,
    [3]  ,$140  plus.minus  40$,$130 $,$10   plus.minus 40 $,
    [4]  ,$870  plus.minus 100$,$910 $,$-40  plus.minus 100$,
    [5]  ,$650  plus.minus 110$,$750 $,$-100 plus.minus 110$,
  ),
  caption: [Specific Heat Capacity Values],
) <tab-specific-heat>

= Uncertainty

All the mass measurements in the experiment were made using a digital balance.
The uncertainty was taken to be the smallest increment of measure, since that is the precision of the equipment.
A full increment of measure was used rather than a half increment because the school balance is likely worn out after lots of use.

All three parts of the experiment involved a calculation of the mass of a sample of DI water ($m_w$).
In the experiment, $m_(c+w)$ (the combined mass of the water and the foam calorimeter it was it) and $m_c$ (the mass of the dry calorimeter) were measured.
Thus, $m_w$ could be calculated using @eq-water-mass.
$
m_w = m_(c+w) - m_c
$ <eq-water-mass>
The uncertainty of $m_w$ is given by @eq-water-mass-uncertainty.
$
Delta m_w &= sqrt( ((partial m_w) / (partial m_c) Delta m_c)^2 +
                   ((partial m_w) / (partial m_(c+w)) Delta m_(c+w))^2 
                 ) \
          &= sqrt( (Delta m_c)^2 + (Delta m_(c+w))^2 )
$ <eq-water-mass-uncertainty>

All the temperature measurements were made using a temperature probe.
In order to get an idea of the uncertainty present in readings with the temperature probe, a special set of ``uncertainty trials'' were performed.
A beaker of DI water was boiled on a hot plate.
To measure the temperature, the probe was placed in the boiling water, the reading was allowed to stabilize, that stable temperature was recorded, and the temperature probe was removed from the water.
This process was repeated 25 times, and the measured values are shown in @tab-uncertainty-trials.
Since the water was at its boiling point, its temperature would remain constant.
Thus, any variation in the measured temperature of the water could be attributed to the uncertainty of the temperature probe.
Care was taken to make sure that the probe did not make contact with the glass beaker, as that could have been at a slightly different temperature than the water.
The uncertainty in the temperature measurements was taken to be the max absolute deviation from the mean, as that gives an upper bound for how much the temperature readings tend to fluctuate.
That value came out to be 0.4 #sym.degree.c.

#figure(
  table(
    columns: 2,
    [Run],[$T$ (#sym.degree.c)],
    [1] ,[99.0],
    [2] ,[99.1],
    [3] ,[98.8],
    [4] ,[98.7],
    [5] ,[98.6],
    [6] ,[99.0],
    [7] ,[99.1],
    [8] ,[99.1],
    [9] ,[99.0],
    [10],[98.9],
    [11],[98.8],
    [12],[98.8],
    [13],[99.1],
    [14],[99.2],
    [15],[99.1],
    [16],[99.2],
    [17],[99.1],
    [18],[99.1],
    [19],[99.2],
    [20],[99.1],
    [21],[99.0],
    [22],[99.1],
    [23],[99.3],
    [24],[99.0],
    [25],[98.8],
  ),
  caption: [Specific Heat Capacity Values],
) <tab-uncertainty-trials>

In part 1, measurements of $H$ and $t$ were made.
The reading for $H$ given by the Watt meter fluctuated.
Thus, the uncertainty in the measurement was taken to be size of the fluctuations, as that gives an upper bound for how much the value could have varied.
The uncertainty in $t$ was taken to be human reaction time (0.2 s).
The stopwatch uncertainty was negligible compared to the much larger uncertainty in starting/stopping the stopwatch.

The experimental specific heat capacity for part 1 was calculated using @eq-c-part-1.
$
c = (H t) / (m_w (T_f - T_i))
$ <eq-c-part-1>
The uncertainty of $c$ for part 1 is given by @eq-c-part-1-uncertainty.
$
Delta c &= [ ((partial c) / (partial H) Delta H)^2 +
             ((partial c) / (partial t) Delta t)^2 +
             ((partial c) / (partial m_w) Delta m_w)^2 +
             ((partial c) / (partial T_i) Delta T_i)^2 +
             ((partial c) / (partial T_f) Delta T_f)^2
           ]^(1/2) \
        &= (H t)/(m_w (T_f - T_i)) [ ((Delta H)/(H))^2 +
                                     ((Delta t)/(t))^2 +
                                     ((Delta m_w)/(m_w))^2 +
                                     ((Delta T_i)/(T_f - T_i))^2 +
                                     ((Delta T_f)/(T_f - T_i))^2
                                   ]^(1/2)
$ <eq-c-part-1-uncertainty>

The experimental specific heat capacities for parts 2 and 3 were calculated using @eq-c-part-2-and-3.
$
c = (m_w c_w (T_f - T_(i w))) / (m_m (T_(i m) - T_f))
$ <eq-c-part-2-and-3>
The uncertainty of $c$ for parts 2 and 3 is given by @eq-c-part-2-and-3-uncertainty.
$
Delta c &= [ ((partial c) / (partial m_w) Delta m_w)^2 +
             ((partial c) / (partial m_m) Delta m_m)^2 +
             ((partial c) / (partial T_(i w)) Delta T_(i w))^2 +
             ((partial c) / (partial T_(i m)) Delta T_(i m))^2 +
             ((partial c) / (partial T_f) Delta T_f)^2
           ]^(1/2) \
        &= (m_w c_w (T_f - T_(i w))) / (m_m (T_(i m) - T_f)) [ ((Delta m_w)/(m_w))^2 +
                                                               ((Delta m_m)/(m_m))^2 +
                                                               ((Delta T_(i w))/(T_f - T_(i w)))^2 +
                                                               ((Delta T_(i m))/(T_(i m) - T_f))^2 +
                                                               ((1 / (T_f - T_(i w)) + 1 / (T_(i m) - T_f))Delta T_f)^2
                                                             ]^(1/2)
$ <eq-c-part-2-and-3-uncertainty>

= Conclusion

The goal of the experiment was to determine the specific heat capacities of various substances based on measurements of mass, temperature, power, and/or time.
For parts 1 and 2 the material was known, so the calculated specific heat capacities could be compared to the accepted values.
For part 3 the material was unknown, so its identity was guessed based on the calculated specific heat capacity and its visual appearance.
Since specific heat capacity is an intensive property, the masses of the samples (the materials and/or the water) should not have mattered, so long as the masses used in the experiment were properly measured.
As such, the exact same amount of water did not need to be used in all the trials.
The results for materials 2 and 4 support this notion.
Both trials used the same material, aluminum, but in different amounts.
The trial for material 2 used $88.26 plus.minus 0.01$ g of aluminum, and had a specific heat capacity of $920 plus.minus 180$ J/(kg K).
The trial for material 4 used $175.42 plus.minus 0.01$ g of aluminum, and had a specific heat capacity of $870 plus.minus 100$ J/(kg K).
These $c$ values are within each other's uncertainty, thereby supporting the idea that specific heat capacity does not depend on the mass of the sample.

It might be noticed that the initial temperature of the water ($T_(i w)$) was different in each trial for parts 2 and 3.
However, even if the initial temperature of the water had been noticeably different, it would not have impacted the results for specific heat capacity.
Specific heat capacity is a property of the material that does not depend on the situation it is put into.
Looking at @eq-c-part-2-and-3, even if $T_(i w)$ were to increase/decrease, $T_f$ would also increase/decrease in such a way to keep the calculated $c$ value the same.

The calculated specific heat capacity for each trial is shown in @tab-specific-heat, as well as how they compare to the theoretical values.
Materials 1, 2, and 3 had a higher measured specific heat capacity than their true, accepted value, while material 4 and 5 had a lower value.
The experimental values were not consistently higher or lower that the expected values; they were all over.
This seems to suggest that multiple factors were at play, some that would cause the measured specific heat capacity to be higher than expected and some that would cause it to be lower than expected.
Material 1's specific heat capacity did not match the accepted value within uncertainty, while for all the other trials the measured specific heat capacities did match the accepted value within uncertainty.
This seems to suggest that the method used in part 1 to determine specific heat capacity is more error prone than the method used in parts 2 and 3.

The identity of material 5, the unknown green rock, was guessed to be malachite based on its measured specific heat capacity and its greenish appearance.
The experimental specific heat capacity was $650 plus.minus 110$ J/(kg K).
Assuming the true value lied within that uncertainty, then the true value could fall between 540 J/(kg K) and 760 J/(kg K).
Malachite, with a specific heat capacity of 750 J/(kg K), was one possible material.
While other materials in the list of possibilities had closer specific heat capacities, malachite was the only material in range that had the distinctive green color of the sample.
Thus, it was concluded that the unknown material was malachite.
Though, it should be noted that the uncertainty in the specific heat capacity for material 5 had to be rounded to two significant figures in order for the range of possible values to include the true value for malachite.
Since the first digit of the uncertainty in the measurement is 1, rounding to two significant figures prevents a significant reduction in uncertainty.
In addition, while carrying out the trial a small piece broke off the unknown sample and was left in the beaker.
Thus, the sample mass recorded was slightly larger than the actual mass present in the calorimeter.
This higher mass would have caused the calculated specific heat capacity to be lower than expected.

Focusing on the result for part 1, the calculated specific heat capacity for water (material 1) was $4740 plus.minus 150$ J/(kg K).
This result is much higher than the accepted value of 4186 J/(kg K).
The difference between them, 550 J/(kg K), is more than the magnitude of the propagated uncertainty.
Thus, this result is not consistent with what theory predicts.
The calculations assumed that all the heat generated by the immersion was transferred into the water, and that the water transferred no heat to the environment.
However, that assumption may not have been reasonable for this part of the experiment.
Perhaps some of the electrical energy transferred into the immersion heater was converted into thermal energy in the cord rather than the thermal energy in the main heating element.
This would have resulted in less power being put into the water than what the Watt meter suggested.
Or, perhaps the water sample transferred some heat to the environment.
This would include any heat transferred to the walls of the calorimeter, transferred to the air above the water, or radiated away (the water would be expected to radiate more heat than it absorbed since it was at a higher temperature than the surrounding environment).
The latter two heat transfers, transfer to the nearby air and radiation, were made more pronounced due to the lid of the foam calorimeter not being used.
Having the lid on would have better insulated the water from the environment (though it also would impede stirring).
In essence, all these effects would have caused water to not receive the full amount of heat generated by the immersion heater.
Thus, $H t$, the amount of heat used for the calculation, is likely higher than the actual amount of heat transferred to the water.
As a result, this would cause the calculated specific heat capacity to also be higher than expected.

Turning to the results of parts 2 and 3, some of the specific heat capacity values were higher than the accepted values, while some were lower.
The single piece of aluminum (material 2) had a specific heat capacity of $920 plus.minus 180$ J/(kg K), 10 J/(kg K) higher than the true value (910 J/(kg K)).
The lead (material 3) had a specific heat capacity of $140 plus.minus 40$ J/(kg K), 10 J/(kg K) higher than the true value (130 J/(kg K)).
The two pieces of aluminum (material 4) had a specific heat capacity of $870 plus.minus 100$ J/(kg K), 40 J/(kg K) lower than the true value (910 J/(kg K)).
The unknown rock (material 5) had a specific heat capacity of $650 plus.minus 110$ J/(kg K), 100 J/(kg K) lower than what the true value is guessed to be (750 J/(kg K)).
For each of these materials, the deviations from the accepted value were not larger than the propagated uncertainty.
Thus, these results are consistent with what theory predicts.
The calculations assumed that all the heat transferred out of the material was transferred into the water, and that no heat was exchanged with the environment.
While it seems like that assumption was reasonable for this part of the experiment, it likely wasn't perfect.
For instance, when transferring the samples from the boiling water to the calorimeter, some water tended to cling to the sample surfaces.
This extra hot water would have added thermal energy to the material, cold water system.
As a result, the final temperature would be increased, thereby causing the experimental specific heat capacity to be higher than expected.
Another possibility is that some heat was transferred to the environment (perhaps into the walls of the calorimeter, the air above the water, or radiated away).
This loss of thermal energy would have decreased the final temperature of the system, thereby causing the experimental specific heat capacity to be lower than expected.
It's possible that both these effects (heat being added to the system and heat being removed) did occur to some extent.
This would have helped keep deviations from the expected value small, though some trials may have randomly had more heat gained or lost.
With that line of reasoning, the trials for materials 2 and 3 would have gained heat overall, while the trials for materials 4 and 5 would have lost heat overall.
