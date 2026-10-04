# Dispatch Difficulty and Technician Time

**To:** Operations Manager  
**Subject:** Exploratory review of service dispatches

Each row represents one completed field-service dispatch; the dataset contains 36 dispatches. There are no missing values in job difficulty, technician hours, or service region. The scatter plot shows a clear positive, roughly linear pattern: dispatches with higher difficulty scores generally require more technician hours. This upward pattern is visible across Central, North, and South, so region does not appear to reverse the relationship. The regional summaries do show different overall time levels: Central averages 7.98 hours (median 6.9), South averages 7.17 (median 6.7), and North averages 6.34 (median 6.3), with 12 dispatches per region.

One unusual observation is FD-035 in North: its difficulty score is 5, but it required 11.8 hours, substantially more than other dispatches around that score. Operations should review this dispatch record and its work details, then continue tracking difficulty, hours, region, and job type to see whether these patterns persist in a larger sample. This dataset is small, and job type or other factors may influence technician time; the regional comparisons do not control for those factors. This exploratory analysis identifies associations only and does not establish that difficulty causes longer service time.
