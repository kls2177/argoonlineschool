#!/usr/bin/env python
# coding: utf-8

# #  The Argo General Data Stream

# **[ANIMATION Video 202-01]**

# The data flow is a representation to understand how the information moves through the system, from the early stages of data collection by the floats to their final disposal to the scientific community, operational services, and the general public. It is organized at different levels to guarantee its integrity and quality. Each level houses different centers that supervise the processes, contributing to the correct flow of data. Such is the case with the Argo Information Center (AIC), the National Data Acquisition Centers (DACs), the Global Data Acquisition Centers (GDAC), the Argo Regional Centers (ARC) and the different research centers. Do not worry about the acronyms! We are about to look at it carefully. Just imagine that these are necessary pieces in a gear system.

# **The basis of the Argo Data System**
# 
# As explained in the videos of Lesson 2, when an Argo float surfaces, the data are received by one of the *Data Assembly Centers* (DAC). At the DACs, they are subjected to initial scrutiny using a set of real-time quality control tests where erroneous data are flagged or corrected, then the data are passed to one of the two Argo *Global Data Assembly Center* (GDAC), the Coriolis GDAC (Brest, France, Europe) or the US-Godae GDAC (Monterey, California, USA). 
# 
# The GDACs are the first stage at which the freely available data can be obtained via the internet. The GDACs synchronize their data to ensure consistent data is available on both sites. The target is for these *real-time* data to be available within 12-24 hours of their transmission from the float.

# **[IMAGE]: “Fig_Euro_ARGO_16_35” from the EURO-ARGO Activity Report 2014-2018 BOTTOM TO TOP DIAGRAM**

#    a. The Argo floats network: With a network of approximately 4000 active floats at any one time, it is possible to efficiently collect data from? the main physical variables that define the state of seawater, in addition to the complementary collection of other biogeochemical variables. During the operating cycle of the floats, continuous monitoring is carried out by the Argo Information Center (AIC) that also facilitates international collaboration.
# 
#    Before the Argo float is deployed in the ocean, its owner institution communicates to the Argo Information Center the information from each of the Argo floats, including its technical specifications and the foreseeable launching dates. Once deployed and after a regular work cycle, the floats will transmit the data collected from the ocean surface through the different satellite communication systems (ARGOS or IRIDIUM), which will have one of the 11 different National Data Acquisition Centers (DACs) spread worldwide as their final recipient.
# 
#    b. Data Assembly Centers (DACs): The different DACs are the places where the raw data observed by Argo floats is processed and decoded into a well-defined data format. The data also undergoes a first quality control in real-time (Real-Time Quality Control) through initial scrutiny based on a certain number of tests, which allow its classification, making necessary corrections and discarding possible anomalous data.  Delivering the data within 12 to 24 hours of the transmission from the float is a basic requirement. In this way, the data is fully available to the scientific community and the general public at this stage. More information about quality control procedures will be provided in the following lessons.
# 
#    c. Global Data Acquisition Centers (GDACs):  Within 12 to 24 hours of the transmission from the float the data has undergone the different quality controls in the DACs and it is delivered to one of the two Global Data Acquisition Centers (GDACs). The two GDACs are located in Brest (France) and California (USA). Once in the GDACs the data is made publicly available and can be obtained in netCDF format, free of charge through the internet. GDACs are also responsible for synchronizing with each other, to ensure the consistency and availability of the data on both sites. The data is also delivered, within the same 12 to 24 hours target, to the oceanic and climatic forecast operational centers via a different route, the Global Telecommunication System (GTS).  In this case, this data is in a format called BUFR, but it doesn’t require our attention in this lesson. Given the size of Argo data sets, there are other ways to access Argo data in addition to the GDACs mentioned above. 
#     
#    There are different data viewers which have been developed to observe the Argo network data set. Through different actions, the user can make specific analyses of the Argo data available. Be patient, more information about getting access to data, analysis, and data viewers will be provided in the following lessons.
# 
#    d. Delayed Mode (DM) data stream: The next stage of the data flow only begins to operate about one year (1) after data is observed.  In this state, the intervention of expert scientific personnel is required to give a definitive boost in terms of the quality of the Argo data. There are numerous reasons why data can be reported abnormally during the Argo float's operating cycles. Studying the data, sometimes it is possible to discern between the natural variability of the area where the float is located and a possible sensor malfunction. Once the anomalous data and its causes have been determined, they can be corrected. We'll look further into Delayed Mode quality control in section 7.
# 
#    e. Argo Regional Centers (ARC):  An additional phase of regional Argo data management is carried out at Argo Regional Centers (ARC), which enables the accumulation of consistent regional datasets. These permit to generate regional-specific analyses and, among other tasks, to help the assessment in the Delayed Mode quality control. Once the data goes through the DM quality control, it means that it has been inspected through a total of two exhaustive quality controls, guaranteeing the best quality and integrity of the data for the scientific community and the general public. Therefore, the databases of the AIC, DACs, GDACs, and ARCs will be updated a year later with the new data. The final repository for Argo data is found at the US National Environmental Information Center (NCEI).
# 

# **[VIDEO 202-02] or/and [ANIMATION Video 201-02] The Final Data Pool**
