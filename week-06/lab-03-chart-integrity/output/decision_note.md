# Decision note for clinic operations briefing

One completed patient visit is the row grain in `data/clinic_waits.csv`. Each record represents one visit at a clinic site, and there are no missing values in the analysis fields (`site` and `wait_minutes`). The site summary shows that North had the longest average wait time at 38.0 minutes, compared with South at 28.7 minutes and Central at 22.2 minutes. The median wait times follow the same pattern, which suggests the difference is not driven by a single outlier visit.

The most practical next step is to review patient-flow processes at the North site, starting with a short audit of check-in, rooming, and provider-start delays by appointment type and day. That review should be targeted to the specific points where delay is building, rather than assuming the site itself is the source of the issue. This will help distinguish operational bottlenecks from normal variation.

One limitation is that the dataset covers only one month and the appointment mix differs across sites. North has more specialist visits and a larger share of senior patients than Central, so the observed gap may reflect case mix and scheduling patterns as well as clinic operations. The data is therefore useful for comparison and prioritization, but it is not enough to assign cause.
